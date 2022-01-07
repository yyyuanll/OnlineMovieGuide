from django.shortcuts import HttpResponse
import json
import os
from django.db import connection
import math
import pandas as pd

def to_tuple(result):
    if isinstance(result[0],tuple):
        t = []
        for i in result:
            t.append(i[0])
        return tuple(t)
    else:
        return result

def search_title(title: str):
    title = title.lower()
    df = pd.read_excel('film.xlsx', usecols=['Title', 'imdbID','Poster'])
    titles, imdbIDs, Posters = df['Title'].values, df['imdbID'].values, df['Poster'].values
    ids = []
    for i, t in enumerate(titles):
        t = str(t)
        if title in t.lower():
            image_url = Posters[i]
            if image_url != "N/A":
                image_url = os.path.join('http://127.0.0.1:8000/', 'images/'+imdbIDs[i]+'.jpg')
            else:
                image_url = 'http://127.0.0.1:8000/images/none.jpg'
            tmp = {
                "imdbid": imdbIDs[i],
                "title": titles[i],
                "img": image_url,
            }
            ids.append(tmp)
    return ids

def search(request):
    title = request.GET.get('value', None)
    data = search_title(title)

    return HttpResponse(json.dumps(data), content_type='application/json')

def allmovie(request): 
        data = []
        # 如果前端发起了post请求
        if request.method == 'GET':
            # 纪录数据
            page = request.GET.get('index', None)
            genre_choice = request.GET.get('Genre', None)
            country_choice = request.GET.get('Country', None)
            language_choice = request.GET.get('Language', None)
            rating = request.GET.get('IMDBRating', None)
            released_choice = request.GET.get('Released', None)
            rated_choice = request.GET.get('Rated', None)
        else:
            # 如果不是，返回一个空json
            return HttpResponse(json.dumps(data), content_type='application/json')
        
        #下面这些元组用来纪录用户的可选选项
        genre_list = ('Drama','Action','Comedy','Romance','Crime', 'Thriller', 'Adventure', 'Horror',
                   'Documenntary', 'Fantasy','Biography','Mystery','Sci-fi','Music','Animatinon','History',
                   'Sport','War')
        country_list = ('China','USA','UK','Hong Kong','France','Germany','Japan','South Korea','Italy',
                        'Australia','Russia','Spain','India','Canada','South Adrica','Mexico')
        language_list = ('English','Spanish','French','Hindi','German','Italian','Russian','Japanese',
                        'Mandarin','Arabic','Portuguese','Cantonese','Korean','Lation','Hebrew','Urdu',
                        'Greek','Chinese')
        rated_list = ('R','PG-13','PG','G','NC-17','UR/NR')
        page = int(page)
        from_id = (page - 1)*28
        to_id = page*28
        # 获得能操作mysql数据库的光标
        cursor=connection.cursor()

        # 处理类别选择
        if genre_choice != 'All':
            # 如果用户选择了其他
            # 查询剔除可选列表中的字段，并纪录结果
            if genre_choice not in genre_list:
                sql = f"select imdbid from genre where genre not in {genre_list}"
                cursor.execute(sql)
                result1 = cursor.fetchall()
            else:
                # 如果用户的选择在我们的可选列表中，直接查询该字段
                sql = f"select imdbid from genre where genre = '{genre_choice}'"
                cursor.execute(sql)
                result1 = cursor.fetchall()
        else:
            # 如果用户选择了全部
            # 因为是第一次查询，所以需要将获得所有imdb
            sql = r"select imdbid from genre"
            cursor.execute(sql)
            result1 = cursor.fetchall()
        # 这一步将得到的数据转换成标准元组
        result1 = to_tuple(result1)
        
        if country_choice != 'All':
            # 如果用户选择了其他
            # 在上一次的查询结果中查询，提高查询效率
            # 查询剔除可选列表中的字段，并纪录结果
            if country_choice not in country_list:
                sql = f"select imdbid from country where imdbid in {result1} and imdb_country not in {country_list}"
                cursor.execute(sql)
                result2 = cursor.fetchall()
            else:
                # 如果用户的选择在我们的可选列表中，直接查询该字段
                # 在上一次的查询结果中查询，提高查询效率
                sql = f"select imdbid from country where imdbid in {result1} and imdb_country = '{country_choice}'"
                cursor.execute(sql)
                result2 = cursor.fetchall()
        else:
            # 如果用户选择了全部
            # 不查询，这一次查询的结果直接等于上一次查询结果
            result2 = result1
        # 这一步将得到的数据转换成标准元组
        result2 = to_tuple(result2)

        # 这一步的逻辑和上一步一样，不再重复注释
        if language_choice != "All":
            if language_choice not in language_list:
                sql = f"select imdbid from language where imdbid in {result2} and language not in {language_list}"
                cursor.execute(sql)
                result3 = cursor.fetchall()
            else:
                sql = f"select imdbid from language where imdbid in {result2} and language = '{language_choice}'"
                cursor.execute(sql)
                result3 = cursor.fetchall()
        else:
            result3 = result2
        result3 = to_tuple(result3)

        # 如果用户选择不是全部，纪录评分区间 [from_star, to_star]
        if rating != 'All':
            from_star = rating.split('--')[0]
            to_star = rating.split('--')[1]
            # 查询在用户选择的评分区间内的电影
            sql = f"select imdbid from film where imdbid in {result3} and imdbrating >= {from_star} and imdbrating <= {to_star}"
            cursor.execute(sql)
            result4 = cursor.fetchall()
        else:
            # 如果用户选择了全部
            # 不查询，这一次查询的结果直接等于上一次查询结果
            result4 = result3
        # 这一步将得到的数据转换成标准元组
        result4 = to_tuple(result4)

        # 如果用户选择不是全部，纪录年份区间 [from_year, to_year]
        if released_choice != 'All':
            from_year = released_choice.split('--')[0]
            to_year = released_choice.split('--')[1]
            # 查询在用户选择的年份区间内的电影
            sql = f"select imdbid from film where imdbid in {result4} and _year >= {from_year} and _year <= {to_year}"
            cursor.execute(sql)
            result5 = cursor.fetchall()
        else:
            # 如果用户选择了全部
            # 不查询，这一次查询的结果直接等于上一次查询结果
            result5 = result4
        # 这一步将得到的数据转换成标准元组
        result5 = to_tuple(result5)
        
        # 处理最后一次查询
        # 因为是最后一次查询，需要返回电影的imdbid, Title, Poster三个信息
        if rated_choice != 'All':
            # 如果用户选择了其他
            # 在上一次的查询结果中查询，提高查询效率
            # 查询剔除可选列表中的字段，并纪录结果
            if rated_choice not in rated_list:
                sql = f"select count(imdbid) from film where imdbid in {result5} and Rated not in {rated_list}"
                cursor.execute(sql)
                r = cursor.fetchall()
                page_number = r[0][0]
                sql = f"select imdbid, Title, Poster from film where imdbid in {result5} and Rated not in {rated_list} limit {from_id},{to_id}"
                cursor.execute(sql)
                result6 = cursor.fetchall()
            else:
                # 如果用户的选择在我们的可选列表中，直接查询该字段
                # 在上一次的查询结果中查询，提高查询效率
                sql = f"select count(imdbid) from film where imdbid in {result5} and Rated = {rated_list}"
                cursor.execute(sql)
                r = cursor.fetchall()
                page_number = r[0][0]
                sql = f"select imdbid, Title, Poster from film where imdbid in {result5} and Rated = '{rated_choice}' limit {from_id},{to_id}"
                cursor.execute(sql)
                result6 = cursor.fetchall()
        else:
            # 如果用户选择了全部
            page_number = len(result5)
            sql = f"select imdbid, Title, Poster from film where imdbid in {result5} limit {from_id},{to_id}"
            cursor.execute(sql)
            result6 = cursor.fetchall()

        connection.commit()
        cursor.close()
        connection.close()

        tmp = {
            "page_number": math.ceil(page_number/28),
        }
        data.append(tmp)

        for i in result6:
            # 处理封面链接
            image_url = i[2]
            if image_url != "N/A":
                image_url = os.path.join('http://127.0.0.1:8000/', 'images/'+str(i[0])+'.jpg')
            else:
                image_url = 'http://127.0.0.1:8000/images/none.jpg'
            # 每一个tmp包含了查询结果中的 一个 电影的imdbid、名字和封面链接
            tmp = {
                "imdbid": i[0],
                "title": i[1],
                "img": image_url,
            }
            data.append(tmp)
        # 向前端返回查询结果，以json的形式
        return HttpResponse(json.dumps(data), content_type='application/json')
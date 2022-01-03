from django.db import connection
import os
from django.shortcuts import HttpResponse
import json

# Create your views here.
def to_tuple(result):
    if isinstance(result[0],tuple):
        t = []
        for i in result:
            t.append(i[0])
        return tuple(t)
    else:
        return result

def command(request):
    data = []
    if request.method == 'POST':
        # 纪录数据
        page = request.POST.get('index', None)
        genre_choice = request.POST.get('Genre', None)
        country_choice = request.POST.get('Country', None)
        rating = request.POST.get('IMDBRating', None)

        genre_list = ('Drama','Action','Comedy','Romance','Crime', 'Thriller', 'Adventure', 'Horror',
                   'Documenntary', 'Fantasy','Biography','Mystery','Sci-fi','Music','Animatinon','History',
                   'Sport','War')
        country_list = ('China','USA','UK','Hong Kong','France','Germany','Japan','South Korea','Italy',
                        'Australia','Russia','Spain','India','Canada','South Adrica','Mexico')
        page = int(page)
        from_id = (page - 1)*28
        to_id = page*28-1
        cursor = connection.cursor()
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

        # 如果用户选择不是全部，纪录评分区间 [from_star, to_star]
        if rating != 'All':
            from_star = rating.split('--')[0]
            to_star = rating.split('--')[1]
            # 查询在用户选择的评分区间内的电影
            sql = f"select imdbid from film where imdbid in {result2} and imdbrating >= {from_star} and imdbrating <= {to_star}"
            cursor.execute(sql)
            result3 = cursor.fetchall()
        else:
            # 如果用户选择了全部
            # 不查询，这一次查询的结果直接等于上一次查询结果
            result3 = result2
        # 这一步将得到的数据转换成标准元组
        result3 = to_tuple(result3)

        sql = f"select imdbid, Title, Poster from film where imdbid in {result3} order by imdbVotes, _year desc limit {from_id},{to_id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            # 处理封面链接
            image_url = i[2]
            if image_url != "N/A":
                image_url = os.path.join('http://127.0.0.1:8000/', 'images/'+str(i[0])+'.jpg')
            # 每一个tmp包含了查询结果中的 一个 电影的imdbid、名字和封面链接
            tmp = {
                "imdbid": i[0],
                "title": i[1],
                "img": image_url,
            }
            data.append(tmp)

        connection.commit()
        cursor.close()
        connection.close()
        # 向前端返回查询结果，以json的形式
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json')
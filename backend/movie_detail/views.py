from django.shortcuts import HttpResponse
from numpy import add
from sqlalchemy import true
from . import models 
import json
import os
from django.db import connection

def add_his(user, id):
    if models.History.objects.filter(username = user, imdbid = id):
        return False
    else:
        his_size = models.History.objects.values("field_id").count()
        try:
            new_his = models.History.objects.create(field_id=his_size+2,username=user,imdbid=id)
            return True
        except Exception as e:
            print(e)
            return False

def detail(request): 
    if request.method == 'GET':
        _id = request.GET.get('imdbid')
        username = request.GET.get('username')
        add_his(username, _id)
    with open('Recommend_dictionary.json', 'r', encoding='utf-8') as f:
        movie_dics = json.load(f)
    filmobject = models.Film.objects.filter(imdbid=_id)
    data = []

    for f in filmobject:
        image_url = f.poster
        title = f.title
        # 处理封面链接
        if image_url != "N/A":
            image_url = os.path.join('http://127.0.0.1:8000/', 'images/'+str(f.imdbid)+'.jpg')
        else:
            image_url = 'http://127.0.0.1:8000/images/none.jpg'
        # 加入数据
        p_tmp = {
            "title": title,
            "image": image_url,
            "imdbrating": f.imdbrating,
            "imdbid": f.imdbid,
            "metascore": f.metascore,
            "day": f.field_day,
            "month": f.field_month,
            "year": f.field_year,
            "runtime": f.runtime,
            "rated": f.rated,
            "award": f.awards,
            "director": f.director,
            "writer": f.writer,
        }
        data.append(p_tmp)
        # 获取电影所有的genre
        genres = models.Genre.objects.filter(imdbid=_id)
        tmp = {}
        i = 1
        for g in genres:
            tmp[f"genre{i}"] = g.genre
            i += 1
        data.append(tmp)

        # 获取电影所有的语言
        languages = models.Language.objects.filter(imdbid=_id)
        tmp = {}
        i = 1
        for l in languages:
            tmp[f"language{i}"] = l.language
            i += 1
        data.append(tmp)
        
        # 获取电影所有的国家
        countries = models.Country.objects.filter(imdbid=_id)
        tmp = {}
        i = 1
        for c in countries:
            tmp[f"country{i}"] = c.imdb_country
            i += 1
        data.append(tmp)
        
        # 获取电影所有的演员
        actors = models.Actor.objects.filter(imdbid=_id)
        tmp = {}
        i = 1
        for a in actors:
            tmp[f"actor{i}"] = a.actor
            tmp[f"actor_link{i}"] = a.link
            i += 1
        data.append(tmp)
        
        # 获取电影所有的评论
        comments = models.Review.objects.filter(imdbid=_id)     
        i = 1
        tmp = {}
        for c in comments:
            user = c.username
            profile = models.Username.objects.filter(username=user)
            for p in profile:
                p_link = p.head_portrait
            tmp[f"user{i}"] = user
            tmp[f"profile{i}"] = p_link
            tmp[f"review{i}"] = c.review
            tmp[f"star{i}"] = c.star/5*10
            i += 1
        data.append(tmp)

    recommend_list = tuple(movie_dics[_id])
    print(recommend_list)
    cursor = connection.cursor()
    sql = f"select imdbid, Title, Poster from film where imdbid in {recommend_list}"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
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

    connection.commit()
    cursor.close()
    connection.close()
    return HttpResponse(json.dumps(data), content_type='application/json')
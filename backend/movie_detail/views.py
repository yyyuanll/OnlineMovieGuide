from django.shortcuts import render,HttpResponse
from matplotlib.pyplot import title
from . import models 
import json
import os
from django.core import serializers

def detail(request): 
    _id = request.GET.get('imdbid')
    #_id = 'tt0080684'
    filmobject = models.Film.objects.filter(imdbid=_id)
    data = []

    for f in filmobject:
        image_url = f.poster
        title = f.title
        # 处理封面链接
        if image_url != "N/A":
            image_url = os.path.join('http://127.0.0.1:8000/', 'images/'+str(f.imdbid)+'.jpg')
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

    # NOTE:推荐电影待完成
        
    return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(data)
    print(data)
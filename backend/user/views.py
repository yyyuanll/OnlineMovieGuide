from django.shortcuts import HttpResponse
from . import models 
import json
import os

def user(request): 
    genre_list = {"Drama":0, "Action":0, "Comedy":0, "Romance":0,
                  "Crime":0, "Thriller":0, "Adventure":0, "Horror":0,
                   "Documenntary":0, "Fantasy":0,"Biography":0,"Mystery":0,
                   "Sci-fi":0,"Music":0,"Animatinon":0,"History":0,
                   "Sport":0,"War":0,"Others":0}
    user_name = request.GET.get('value', None)
    #user_name = "Louis Robertson"
    user_info = models.Username.objects.filter(username=user_name)
    fav = models.Favorite.objects.filter(username=user_name)
    his = models.History.objects.filter(username=user_name)
    comment = models.Review.objects.filter(username=user_name)
    
    data = []
    # 找到用户最喜欢的电影的类别，并计数
    for f in fav:
        genres = models.Genre.objects.filter(imdbid=f.imdbid)
        for i in genres:
            if i.genre in genre_list:
                genre_list[i.genre] += 1
            else:
                genre_list["Others"] += 1
    data.append(genre_list)
    
    for i in user_info:
        print(i.username)
        tmp = {
            "username": i.username,
            "useravatar": i.head_portrait,
        }
        data.append(tmp)
    
    for i in his:
        poster = models.Film.objects.filter(title=i.imdbid)
        for j in poster:
            image_url = j.poster
            if image_url != "N/A":
                image_url = os.path.join('http://127.0.0.1:8000/', 'images/'+str(j.imdbid)+'.jpg')
            p_tmp = {
                "type": "history",
                "title": j.title,
                "image": image_url,
            }
            data.append(p_tmp)
    
    for m in fav:
        poster = models.Film.objects.filter(title=m.imdbid)
        for j in poster:
            print(j.title)
            image_url = j.poster
            if image_url != "N/A":
                image_url = os.path.join('http://127.0.0.1:8000/', 'images/'+str(j.imdbid)+'.jpg')
            p_tmp = {
                "type": "favorites",
                "title": j.title,
                "image": image_url,
            }
            data.append(p_tmp)
    
    for i in comment:
        tmp = {
            "type": "review",
            "movie": i.movie,
            "review": i.review,
            "star": i.star/5*10,
        }
        data.append(tmp)
    
    return HttpResponse(json.dumps(data), content_type='application/json')

def add_comment(request):
    data = []
    if request.method == "POST":
        user = request.POST.get('username', None)
        movie_id= request.POST.get('imdbid', None)
        review_txt = request.POST.get('review', None)

        his_size = models.History.objects.values("field_id").count()
        rev_size = models.Review.objects.values("field_id").count()
        
        try:
            new_his = models.History.objects.create(field_id=his_size+2,username=user,imdbid=movie_id)
            new_review = models.Review.objects.create(field_id=rev_size+2,username=user,imdbid=movie_id,review=review_txt)
        except Exception as e:
            tmp = {
                'status': 404,
                'error': str(e),
            }
            data.append(tmp)
            print(data)
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    tmp = {
        'status': 200,
        'error': None,
    }
    data.append(tmp)
    return HttpResponse(json.dumps(data), content_type='application/json')

def add_star(request):
    data = []
    if request.method == "POST":
        user = request.POST.get('username', None)
        movie_id= request.POST.get('imdbid', None)
        rating = request.POST.get('star', None)

        his_size = models.History.objects.values("field_id").count()
        rev_size = models.Review.objects.values("field_id").count()

        try:
            new_his = models.History.objects.create(field_id=his_size+2,username=user,imdbid=movie_id)
            new_star = models.Review.objects.create(field_id=rev_size+2,username=user,imdbid=movie_id,star=int(rating))
        except Exception as e:
            tmp = {
                'status': 404,
                'error': str(e),
            }
            data.append(tmp)
            print(data)
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    tmp = {
        'status': 200,
        'error': None,
    }
    data.append(tmp)
    return HttpResponse(json.dumps(data), content_type='application/json')
            


def add_fav(request):
    data = []
    if request.method == "POST":
        user = request.POST.get('username', None)
        movie_id= request.POST.get('imdbid', None)

        his_size = models.History.objects.values("field_id").count()
        fav_size = models.Favorite.objects.values("field_id").count()

        try:
            new_his = models.History.objects.create(field_id=his_size+2,username=user,imdbid=movie_id)
            new_fav = models.Favorite.objects.create(field_id=fav_size+2,username=user,imdbid=movie_id)
        except Exception as e:
            tmp = {
                'status': 404,
                'error': str(e),
            }
            data.append(tmp)
            print(data)
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    tmp = {
        'status': 200,
        'error': None,
    }
    data.append(tmp)
    print(data)
    return HttpResponse(json.dumps(data), content_type='application/json')
        

def remove_fav(request):
    data = []
    if request.method == "POST":
        user = request.POST.get('username', None)
        movie_id= request.POST.get('imdbid', None)
        
        try:
            dele = models.Favorite.objects.filter(username=user,imdbid=movie_id)
            dele.delete()
        except Exception as e:
            tmp = {
                'status': 404,
                'error': str(e),
            }
            data.append(tmp)
            print(data)
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    tmp = {
        'status': 200,
        'error': None,
    }
    data.append(tmp)
    return HttpResponse(json.dumps(data), content_type='application/json')
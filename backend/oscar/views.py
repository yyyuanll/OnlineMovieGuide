from django.shortcuts import HttpResponse
from . import models 
import json

def oscar(request): 
    data = []
    if request.method == "POST":
        c_year = request.POST.get('value', None)
        c_year = int(c_year)
        data = []
        best_actor = models.BestActor.objects.filter(year=c_year)
        best_actress = models.BestActress.objects.filter(year=c_year)
        best_sactor = models.BestSupportingActor.objects.filter(year=c_year)
        best_sactress = models.BestSupportingActress.objects.filter(year=c_year)
        best_picture = models.BestPicture.objects.filter(year=c_year)
        
        for i in best_actor:
            tmp = {
                "award": "BestActor",
                "name": i.name,
                "introduction": i.introduction,
                "representitive": i.representitive,
                "movie_name": i.movie_name,
                "character_name": i.character_name,
                "url": i.profile,
            }
            data.append(tmp)
        for i in best_actress:
            tmp = {
                "award": "BestActress",
                "name": i.name,
                "introduction": i.introduction,
                "representitive": i.representitive,
                "movie_name": i.movie_name,
                "character_name": i.character_name,
                "url": i.profile,
            }
            data.append(tmp)
        for i in best_sactor:
            tmp = {
                "award": "BestSupportingActress",
                "name": i.name,
                "introduction": i.introduction,
                "representitive": i.representitive,
                "movie_name": i.movie_name,
                "character_name": i.character_name,
                "url": i.profile,
            }
            data.append(tmp)
        for i in best_sactress:
            tmp = {
                "award": "BestSupportingActress",
                "name": i.name,
                "introduction": i.introduction,
                "representitive": i.representitive,
                "movie_name": i.movie_name,
                "character_name": i.character_name,
                "url": i.profile,
            }
            data.append(tmp)
        for i in best_picture:
            tmp = {
                "award": "BestPicture",
                "title": i.name,
                "introduction": i.introduction,
                "director": i.director,
                "actors": i.star1+','+i.star2+','+i.star3+','+i.star4,
                "genre": i.genre1+','+i.genre2+','+i.genre3,
                "url": i.cover,
            }
            data.append(tmp)

        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json')

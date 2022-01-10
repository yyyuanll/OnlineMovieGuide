from django.shortcuts import HttpResponse
from . import models 
import json
import os
import hashlib
import datetime
from django.db import connection
from random import Random  # 用于生成随机码
from django.core.mail import send_mail  # 发送邮件模块
from django.conf import settings    # setting.py添加的的配置信息

def profile(request):
    data = []
    user_name = request.GET.get('username', None)
    user_info = models.Username.objects.filter(username=user_name)
    #print(user_name)

    for i in user_info:
        print(i.username)
        tmp = {
            "useravatar": i.head_portrait,
        }
        data.append(tmp)
    return HttpResponse(json.dumps(data), content_type='application/json')

def history(request):
    data = []
    user_name = request.GET.get('username', None)
    his = models.History.objects.filter(username=user_name)
    
    for i in his:
        poster = models.Film.objects.filter(imdbid=i.imdbid)
        for j in poster:
            image_url = j.poster
            print(j.poster)
            if image_url != "N/A":
                image_url = os.path.join('http://127.0.0.1:8000/', 'images/'+str(j.imdbid)+'.jpg')
            else:
                image_url = 'http://127.0.0.1:8000/images/none.jpg'
            p_tmp = {
                "title": j.title,
                "image": image_url,
            }
            data.append(p_tmp)

    return HttpResponse(json.dumps(data), content_type='application/json')

def favorite(request):
    data = []
    user_name = request.GET.get('username', None)
    fav = models.Favorite.objects.filter(username=user_name)

    for m in fav:
        poster = models.Film.objects.filter(imdbid=m.imdbid)
        for j in poster:
            image_url = j.poster
            if image_url != "N/A":
                image_url = os.path.join('http://127.0.0.1:8000/', 'images/'+str(j.imdbid)+'.jpg')
            else:
                image_url = 'http://127.0.0.1:8000/images/none.jpg'
            p_tmp = {
                "type": "favorites",
                "title": j.title,
                "image": image_url,
            }
            data.append(p_tmp)
    return HttpResponse(json.dumps(data), content_type='application/json')

def review(request):
    data = []
    user_name = request.GET.get('value', None)
    
    comment = models.Review.objects.filter(username=user_name)

    for i in comment:
        tmp = {
            "type": "review",
            "movie": i.movie,
            "review": i.review,
            "star": i.star/5*10,
        }
        data.append(tmp)
    
    return HttpResponse(json.dumps(data), content_type='application/json')

def user_genre(request):
    genre_list = {"Drama":0, "Action":0, "Comedy":0, "Romance":0,
                  "Crime":0, "Thriller":0, "Adventure":0, "Horror":0,
                   "Documenntary":0, "Fantasy":0,"Biography":0,"Mystery":0,
                   "Sci-fi":0,"Music":0,"Animatinon":0,"History":0,
                   "Sport":0,"War":0,"Others":0}
    user_name = request.GET.get('username', None)
    
    data = []
    fav = models.Favorite.objects.filter(username=user_name)
    # 找到用户最喜欢的电影的类别，并计数
    for f in fav:
        genres = models.Genre.objects.filter(imdbid=f.imdbid)
        for i in genres:
            print(i.genre)
            if i.genre in genre_list:
                genre_list[i.genre] += 1
            else:
                genre_list["Others"] += 1

    for i in genre_list:
        tmp = {
            'value': genre_list[i],
            'name': i,
        }
        data.append(tmp)

    return HttpResponse(json.dumps(data), content_type='application/json')

def user(request): 
    genre_list = {"Drama":0, "Action":0, "Comedy":0, "Romance":0,
                  "Crime":0, "Thriller":0, "Adventure":0, "Horror":0,
                   "Documenntary":0, "Fantasy":0,"Biography":0,"Mystery":0,
                   "Sci-fi":0,"Music":0,"Animatinon":0,"History":0,
                   "Sport":0,"War":0,"Others":0}
    user_name = request.GET.get('value', None)
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
            else:
                image_url = 'http://127.0.0.1:8000/images/none.jpg'
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
            else:
                image_url = 'http://127.0.0.1:8000/images/none.jpg'
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

        rev_size = models.Review.objects.values("field_id").count()
        
        try:
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

        rev_size = models.Review.objects.values("field_id").count()

        try:
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

        if models.Favorite.objects.filter(username = user, imdbid = id):
            tmp = {
                'status': 200,
                'error': "The movie is already in the favorite!",
            }
            data.append(tmp)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            fav_size = models.Favorite.objects.values("field_id").count()
            try:
                new_fav = models.Favorite.objects.create(field_id=fav_size+2,username=user,imdbid=movie_id)
                tmp = {
                'status': 200,
                'error': None,
                }
            except Exception as e:
                tmp = {
                    'status': 404,
                    'error': str(e),
                    }
            data.append(tmp)
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    tmp = {
        'status': 200,
        'error': None,
    }
    data.append(tmp)
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

# 加盐
def md5(psword):
    _obj = hashlib.md5()
    _obj.update((psword + psword).encode('utf-8'))  # 加盐
    ret = _obj.hexdigest()
    return ret

def register(request):
    data = []
    if request.method == "POST":
        code = request.POST.get('code', None)
        user = request.POST.get('username', None)
        psword = request.POST.get('password', None)
        user_email = request.POST.get('mail', None)
        profile = request.FILES.get("file", None)
        
        stored = models.UserEmailverifyrecord.objects.filter(email = user_email).order_by('-send_time').first()
        #stored = models.EmailVerifyRecord.objects.filter(email = user_email).order_by('-send_time').first()

        sent = stored.send_time.replace(tzinfo=None)
        if (datetime.datetime.now()-sent).seconds > 300:
            tmp = {
                'status': 404,
                'error': "Your verification code is outdated.",
                }
            data.append(tmp)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            if code != stored.code:
                tmp = {
                'status': 404,
                'error': "Your verification code is wrong.",
                }
                data.append(tmp)
                return HttpResponse(json.dumps(data), content_type='application/json')


        if models.Username.objects.filter(username=user):
            tmp = {
                'status': 404,
                'error': "The account has been created before.",
                }
            data.append(tmp)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            # 将用户输入的密码哈希
            hashed_psword = md5(psword)
            # 修改头像图片名称，保证每一个头像的图片名称都是唯一的
            profile.name = user + profile.name
            if profile != None:
                if not os.path.exists('images'):
                    os.mkdir('images')
                with open(os.path.join(os.getcwd(), 'images', profile.name), 'wb') as fw:
                    # 分块读取
                    for ck in profile.chunks():
                        fw.write(ck)
                profile_link = os.path.join('http://127.0.0.1:8000/', 'images/'+ profile.name)
                
                models.Username.objects.create(username=user,password=hashed_psword,mail=user_email,head_portrait=profile_link)
                tmp = {
                    'status': 200,
                    'error': None,
                    }
                data.append(tmp)
                return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json') 

def login(request):
    data = []
    if request.method == "POST":
        user = request.POST.get('username', None)
        psword = request.POST.get('password', None)
        print("user",user)
        print("password",psword)

        try:
            cursor=connection.cursor()
            sql = f"select password from username where username = '{user}'"
            cursor.execute(sql)
            stored_psw = cursor.fetchall()
            connection.commit()
            cursor.close()
            connection.close()
            if md5(psword) == stored_psw[0][0]:
                tmp = {
                'status': 200,
                'error': None,
            }
            else:
                tmp = {
                    'status': 404,
                    'error': 'Wrong Password',
                }
            data.append(tmp)
            print(data)
            return HttpResponse(json.dumps(data), content_type='application/json')
        except Exception as e:
            tmp = {
                'status': 404,
                'error': str(e),
            }
            data.append(tmp)
            print(data)
            return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json')

def sendEmailCode(request):
    data = []
    if request.method == "POST":
        email = request.POST.get('mail', None)
        print(email)
        if send_code_email(email):
            tmp = {
                'status': 200,
                'error': None,
            }
        else:
            tmp = {
                    'status': 404,
                    'error': '验证码发送失败',
                }
        data.append(tmp)
        print(data)
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json')


# 生成随机字符串
def random_str(randomlength=6):
    """
    随机字符串
    :param randomlength: 字符串长度
    :return: String 类型字符串
    """
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

# 发送电子邮件
def send_code_email(email):
    """
    发送电子邮件
    :param email: 要发送的邮箱
    :param send_type: 邮箱类型
    :return: True/False
    """
    email_record = models.UserEmailverifyrecord()
    #email_record = models.EmailVerifyRecord()
    # 将给用户发的信息保存在数据库中
    code = random_str()
    email_record.code = code
    email_record.email = email
    email_record.send_time = datetime.datetime.now()
    email_record.save()
    # 初始化为空
    email_title = ""
    email_body = ""
    # 如果为注册类型
    email_title = "Online Movie Guide"
    email_body = f"Hi, welcome to Online Movie Guide:)\nHere is your 6-character code to verify your email address: {code}.\nPlease note that you will only have FIVE minutes to verify your email."
    email_body += '\n \n \n \n \n'
    email_body += 'The email was sent by Online Movie Guide, an online movie information website built by SUFE bachelor students.\n'
    email_body += '——————————————————————————\n'
    email_body += r"Online Movie Guide is a is an online system that enables users to search and browse movie information, including ratings, genres, actors, awards and so on. Here, users can freely score and comment on movies, tv shows and put them into their private links. OMG will smartly learn from user's behavior and recommend suitable shows according to their preference."
    # 发送邮件
    send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
    if not send_status:
        return False
    return True
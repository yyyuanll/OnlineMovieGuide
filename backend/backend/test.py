import pandas as pd
from numpy import delete
import pymysql
import os
from sshtunnel import SSHTunnelForwarder

ssh_host = "47.103.210.229"  # 堡垒机ip地址或主机名
ssh_port = 22  # 堡垒机连接mysql服务器的端口号，一般都是22，必须是数字
ssh_user = "root"  # 这是你在堡垒机上的用户名
ssh_password = r"sufeOMG666"  # 这是你在堡垒机上的用户密码
mysql_host = "localhost"  # 这是你mysql服务器的主机名或ip地址
mysql_port = 3306  # 这是你mysql服务器上的端口，3306，mysql就是3306，必须是数字
mysql_user = "root"  # 这是你mysql数据库上的用户名
mysql_password = "12345678"  # 这是你mysql数据库的密码
mysql_db = "u2019111089"  # mysql服务器上的数据库名
 
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

with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        remote_bind_address=(mysql_host, mysql_port)) as server:
    conn = pymysql.connect(host=mysql_host,
                           port=server.local_bind_port,
                           user=mysql_user,
                           passwd=mysql_password,
                           db=mysql_db)
 
    cursor = conn.cursor()
    root_path = r'C:/Users/14472/Desktop/collection/Database/final project/OnlineMovieGuide/backend/images'
    df = pd.read_excel('film.xlsx', usecols=['Title', 'imdbID','Poster'])
    titles, imdbIDs, Posters = df['Title'].values, df['imdbID'].values, df['Poster'].values
    
    for i, t in enumerate(imdbIDs):
        t = str(t)
        target = t + '.jpg'
        for root,dirs,files in os.walk(root_path):
            if target not in files:
                sql = f"update film set poster = 'N/A' where imdbid = '{t}'"
                cursor.execute(sql)
                '''
                sql = f"select imdbid, poster from film where imdbid = '{t}'"
                cursor.execute(sql)
                print(cursor.fetchall())
                '''
   
    conn.commit()
    cursor.close()
    conn.close()
    
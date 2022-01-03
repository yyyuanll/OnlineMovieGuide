import json
from unittest import result
from numpy import delete
import pymysql
import os
from sshtunnel import SSHTunnelForwarder

ssh_host = "sandbox.bundit-lae.me"  # 堡垒机ip地址或主机名
ssh_port = 22  # 堡垒机连接mysql服务器的端口号，一般都是22，必须是数字
ssh_user = "u2019111089"  # 这是你在堡垒机上的用户名
ssh_password = r"MINISTER%telephone%326%MIGHTY"  # 这是你在堡垒机上的用户密码
mysql_host = "localhost"  # 这是你mysql服务器的主机名或ip地址
mysql_port = 3306  # 这是你mysql服务器上的端口，3306，mysql就是3306，必须是数字
mysql_user = "u2019111089"  # 这是你mysql数据库上的用户名
mysql_password = "PIN-PROTECT-111-CAPABLE"  # 这是你mysql数据库的密码
mysql_db = "u2019111089"  # mysql服务器上的数据库名
 
def to_tuple(result):
    if isinstance(result[0],tuple):
        t = []
        for i in result:
            t.append(i[0])
        return tuple(t)
    else:
        return result

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

    deleted = []
    root_path = r'C:/Users/14472/Desktop/collection/Database/final project/OnlineMovieGuide/backend/images'
    with open('Recommend_dictionary.json', 'r', encoding='utf-8') as f:
        movie_dics = json.load(f)

    for root,dirs,files in os.walk(root_path):
        for key in movie_dics:
            s = key+'.jpg'
            if s not in files:
                deleted.append(key)
                sql = f"UPDATE film SET Poster = 'N/A' WHERE imdbid = '{key}'"
                cursor.execute(sql)

    print(deleted)
    
    conn.commit()
    cursor.close()
    conn.close()
    
import json
from unittest import result
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
    data = []
    _id = 'tt0080455'
    with open('Recommend_dictionary.json', 'r', encoding='utf-8') as f:
        movie_dics = json.load(f)

    recommend_list = tuple(movie_dics[_id])
    print(recommend_list)
    sql = f"select imdbid, Title, Poster from film where imdbid in {recommend_list}"
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
    print(data)

    conn.commit()
    cursor.close()
    conn.close()

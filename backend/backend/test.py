
from unittest import result
import pymysql

from sshtunnel import SSHTunnelForwarder
import sys

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
    '''
    s = '2'
    sql = f"select imdbid, Title, Poster from film where _year < 2010"
    cursor.execute(sql)
    result = cursor.fetchall()
    '''

    genre_choice = 'Action'
    sql = f"select imdbid from genre where genre = '{genre_choice}'"
    cursor.execute(sql)
    result1 = cursor.fetchall()
    print(result1)
    
    conn.commit()
    cursor.close()
    conn.close()

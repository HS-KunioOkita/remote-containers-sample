import pymysql.cursors

connection = pymysql.connect(host='mysql',
                             user='user',
                             password='password',
                             database='testdb')

print(connection)

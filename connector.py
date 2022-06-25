import pymysql
from sys import argv

query = str(input("mysql> "))
host,port,user,passwd,db = argv[1],argv[2],argv[3],argv[4],argv[5]
conn = pymysql.connect(host=host,port=int(port),user=user,passwd=passwd,db=db)
_cursor = conn.cursor()

try:
    while True:

        _cursor.execute(query)

        print(_cursor.description)
        print()

        for row in _cursor:
            print(row)
            print("===============================")
       
        
except pymysql.err.ProgrammingError:
    print()


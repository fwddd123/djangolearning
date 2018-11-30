import pymysql
def get_list(sql,args):
    conn = pymysql.connect(user='root', password='123456', db='test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 创建user表:
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute(sql,args)

    result= cursor.fetchall()

    cursor.close()

    conn.close()
    return result
def get_one(sql,args):
    conn = pymysql.connect(user='root', password='123456', db='test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 创建user表:
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute(sql,args)

    result= cursor.fetchone()

    cursor.close()

    conn.close()
    return result
def modify(sql,args):
    conn = pymysql.connect(user='root', password='123456', db='test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 创建user表:
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute(sql, args)
    conn.commit()

    cursor.close()

    conn.close()


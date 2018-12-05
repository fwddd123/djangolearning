from django.shortcuts import render
import requests

from django.shortcuts import HttpResponse,render,redirect
import requests
import json
import pymysql
from utils import sqlhelper
def classes(request):


    conn = pymysql.connect(user='root', password='123456', db='test')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 创建user表:
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute('select id,title from test.classes1')

    classes_list = cursor.fetchall()

    cursor.close()

    conn.close()
    return render(request, 'classes.html',{'classes_list':classes_list})
def login(request):
    #return HttpResponse('login.html')
    #print(request.method)
    if request.method=='GET':

        return render(request,'login.html')
    else:
        u= request.POST.get('user')
        p= request.POST.get('pwd')
        print(u,p)
        if u=='root' and p=='123456':
            return redirect('/index/')
        else:
            return render(request,'login.html',{'msg':'123456'})
def index(request):
    return render(
        request,'index.html',
        {
            'name':'alex',
            'users':['123','123'],
            'user_dict':{'k1':'123','k2':'123'},
        }
    )

def new(request):
    if request.method=='GET':
        return render(request,'new.html')
    else:
        v=request.POST.get('title')

        conn = pymysql.connect(user='root', password='123456', db='test')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 创建user表:
        # 插入一行记录，注意MySQL的占位符是%s:
        cursor.execute('insert into classes1(title) value(%s)',[v,])
        conn.commit()

        cursor.close()
        conn.close()
        return redirect('/classes/')
def del_class(request):
        nid = request.GET.get('nid')
        conn = pymysql.connect(user='root', password='123456', db='test')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 创建user表:
        # 插入一行记录，注意MySQL的占位符是%s:
        cursor.execute('delete from test.classes1 where id=%s',[nid,])
        conn.commit()

        cursor.close()
        conn.close()
        return redirect('/classes/')
def edit_class(request):
    if request.method =='GET':
        nid =request.GET.get('nid')
        conn = pymysql.connect(user='root', password='123456', db='test')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 创建user表:
        # 插入一行记录，注意MySQL的占位符是%s:
        cursor.execute('select id,title from test.classes1 where id=%s',[nid,])
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        return render(request,'edit_class.html',{'result':result})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        conn = pymysql.connect(user='root', password='123456', db='test')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 创建user表:
        # 插入一行记录，注意MySQL的占位符是%s:
        cursor.execute('update test.classes1 set title=%s where id = %s',[title,nid,])
        conn.commit()

        cursor.close()
        conn.close()
        return redirect('/classes/')
def student(request):
        conn = pymysql.connect(user='root', password='123456', db='test')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 创建user表:
        # 插入一行记录，注意MySQL的占位符是%s:
        cursor.execute('select * from test.student left join test.classes1 on student.class = classes1.id')

        student_list = cursor.fetchall()

        cursor.close()

        conn.close()
        return render(request,'student.html',{'student_list':student_list})
def new_student(request):
        if request.method=='GET':
            conn = pymysql.connect(user='root', password='123456', db='test')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 创建user表:
            # 插入一行记录，注意MySQL的占位符是%s:
            cursor.execute('select id,title from test.classes1')

            classes_list = cursor.fetchall()

            cursor.close()

            conn.close()
            return render(request,'new_student.html',{'classes_list':classes_list})
        else:
            name =request.POST.get("name")
            if len(name)>0:
                classid = request.POST.get('class')
                conn = pymysql.connect(user='root', password='123456', db='test')
                cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
                # 创建user表:
                # 插入一行记录，注意MySQL的占位符是%s:
                cursor.execute('insert into student(name,class) value(%s,%s)', [name,classid,])
                conn.commit()
                cursor.close()
                conn.close()
                return redirect('/student/')
            else:
                return render(request,'new_student.html',{'msg':'bukeuyi'})


def edit_student(request):
    if request.method=='GET':
        nid = request.GET.get('nid')
        class_list=sqlhelper.get_list('select id,title from test.classes1',[])
        current_student_info=sqlhelper.get_one('select * from student where id=%s',[nid,])
        return render(request,'edit_student.html',{'class_list':class_list,'current_student_info':current_student_info})
    else:
        nid = request.GET.get('nid')
        name =request.POST.get('name')
        classid= request.POST.get('class')
        sqlhelper.modify('update student set name=%s ,class =%s where id=%s',[name,classid,nid,])
        return redirect('/student/')
##############################对话框
def modal_add_class(request):
    title= request.POST.get('title')
    if len(title)>0:
        sqlhelper.modify('insert into test.classes1(title) value(%s)', [title,])
        return HttpResponse('ok')
    else:
        return HttpResponse('buok')
def modal_edit_class(request):
    ret ={'status':True,'message':None}
    try:
        nid = request.POST.get('nid')
        content = request.POST.get('content')

        sqlhelper.modify('update test.classes1 set title=%s where id=%s',[content,nid,])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))

def modal_new_student(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('title')


        sqlhelper.modify('insert into student(name,class) value(%s,%s)', [name,classid,])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))
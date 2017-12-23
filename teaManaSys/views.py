# -*- coding: utf-8 -*-
import StringIO
import csv
import datetime

from django.db  import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from teaManaSys import models
import json
from django.db.models import Q
from form import UserForm

def model(req):

    return render_to_response('model.html')
@csrf_exempt
def signIn(req):
        # 用户登录
    if req.method == "GET":
        return render_to_response('login/sign-in.html')
    if req.method == "POST":
        # req.setCharactorEcoding("utf-8")
        try:
            userid = req.POST['userid']
            password = req.POST['password']
        except Exception as e:
            result={
                'status':0,
                'message':"用户密码错误"
            }
            return HttpResponse(json.dumps(result))
        else:
                if models.User.objects.filter(Q(userId=userid)):
                    user = models.User.objects.get(userId=userid)
                    if user.password == password:
                        result = {
                            'status': 1,
                            'message': "登录成功!请稍等..."
                        }
                        return HttpResponse(json.dumps(result))
                    elif user.password != password:
                        result = {
                            'status': 0,
                            'message': "用户密码错误"
                        }
                        return HttpResponse(json.dumps(result))
                else:
                    result = {
                        'status': 0,
                        'message': "用户不存在"
                    }
                    return HttpResponse(json.dumps(result))

def signup(req):
    if req.method == 'GET':
        return render_to_response('login/sign-up.html')
    if req.method == "POST":
        try:
            userid = req.POST['userid']
            username = req.POST['UserName']
            password = req.POST['Passwd']
        except:
            result['status'] = 0
            result['message'] = '获取信息失败'
            return HttpResponse(json.dumps(result))
        else:
            if not (varidate_char(username) and varidate_emial(email)):
                result['message'] = '输入非法字符'
                result['status'] = 0
                return HttpResponse(json.dumps(result))
            elif models.User.objects.filter(Email=email):
                result['status'] = 0
                result['message'] = '邮箱已经被注册'
                return HttpResponse(json.dumps(result))
            elif models.User.objects.filter(UserName=username):
                result['status'] = 0
                result['message'] = '姓名已被注册'
                return HttpResponse(json.dumps(result))
            else:
                try:
                    models.User.objects.create(Email=email, UserName=username, PassWord=password, Uuid=uuid.uuid1())
                    user = models.User.objects.get(Email=email)
                    user.Img = 'photos/2017/09/19/user/default_cdNstvn.jpg'
                    req.session['uuid'] = str(user.Uuid)
                    result['email'] = email
                    result['username'] = username
                    result['message'] = '注册成功，正在调转'
                    result['status'] = 1
                    return HttpResponse(json.dumps(result))
                except Exception as e:
                    print(e)
                    result['status'] = 0
                    result['message'] = '服务器异常!!'
                    return HttpResponse(json.dumps(result))


def grade(req):
    return render_to_response('page/grade.html')

def teacher(req):
    return render_to_response('page/teacher.html')

def student(req):
    return render_to_response('page/student.html')

def classa(req):
    return render_to_response('page/class.html')

def courses(req):
    return render_to_response('page/courses.html')
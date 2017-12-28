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
    '''
    登录页面
    :param req:
    :return:
    '''
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

@csrf_exempt
def signup(req):
    '''
    注册页面
    :param req:
    :return:
    '''
    if req.method == 'GET':
        return render_to_response('login/sign-up.html', context=RequestContext(req))
    if req.method == "POST":
        try:
            userid = req.POST['userid']
            username = req.POST['username']
            password = req.POST['password']
        except:
            result = {
                'status': 0,
                'message': "获取信息失败"
            }
            return HttpResponse(json.dumps(result))
        else:
            if models.User.objects.filter(userid=userid):
                result={
                'status': 0,
                'message': '学号/工号已经注册'
                }
                return HttpResponse(json.dumps(result))
            else:
                try:
                    models.User.objects.create(userId=userid, userName=username, password=password)
                    user = models.User.objects.get(userId=userid)
                    result={
                        'userid' : userid,
                        'username' : username,
                        'message': '注册成功，正在调转',
                        'status': 1
                    }
                    return HttpResponse(json.dumps(result))
                except Exception as e:
                    result={
                        'status': 0,
                        'message': '服务器异常!!'
                    }
                    return HttpResponse(json.dumps(result))


def grade(req):
    if req.method == "GET":
        grade = models.grade.objects.all()
        courses = models.courses.objects.all()
        return render_to_response("page/grade.html", {"grade": grade, "courses": courses})
    if req.method == "POST":
        pass


def teacher(req):
    return render_to_response('page/teacher.html')

def student(req):
    return render_to_response('page/student.html')

def classa(req):
    return render_to_response('page/class.html')

def courses(req):
    return render_to_response('page/courses.html')
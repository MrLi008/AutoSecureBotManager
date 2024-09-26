from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_default_login
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from .form import *
from .models import *
from config_busi.models import *
from appcenter.models import *
from sys_user.func import *

# Create your views here.

"""

登录
注册
修改密码
默认注册为系统用户
模块管理员

"""


def register(request):
    if request.method == "GET":
        context = dict()
        context["registerform"] = RegisterForm()
        context["error_message"] = ""
        return HttpResponse(
            loader.get_template(f"register.html").render(context, request)
        )
    obj = mydict(request.POST)
    registerform = RegisterForm(request.POST)
    if not registerform.is_valid():
        return render(request, "login.html", locals())
    username = registerform.cleaned_data.get("username")
    password1 = registerform.cleaned_data.get("password1")
    password2 = registerform.cleaned_data.get("password2")

    user = User.objects.filter(username=username)
    if user:
        return render(
            request,
            "register.html",
            {"registerform": RegisterForm(), "error_message": "用户名已存在"},
        )
    if password1 != password2:
        return render(
            request,
            "register.html",
            {"registerform": RegisterForm(), "error_message": "密码不一致"},
        )
    user_table_id = obj.get("user_table_id")
    table_user_ins = None

    # 用户信息表

    if str(8137) == user_table_id:
        table_user_ins = mc_userinfo
    # 系统管理员

    if str(8158) == user_table_id:
        table_user_ins = mc_supermanager
    if table_user_ins is None:
        print("登录失败,table_user_ins is None,注意表单提交用户表类型与系统配置不符")
    my_user = table_user_ins.objects.filter(username=username)
    if my_user:
        print("该用户已经注册")
        return render(
            request,
            "register.html",
            {"registerform": RegisterForm(), "error_message": "用户名已存在"},
        )
    # save

    my_user = table_user_ins(username=username)
    my_user.save()

    user = User.objects.create_user(
        username=username,
        password=password1,
        email=registerform.cleaned_data.get("email"),
        is_superuser=True,
    )

    user.set_password(password1)
    user.save()
    return redirect("/")


def logout_view(request):
    logout(request)

    response = redirect("/")
    response.delete_cookie("username")
    response.delete_cookie("user_table_id")
    return response


def admin_logout_view(request):
    logout(request)
    response = redirect("/admin")
    response.delete_cookie("username")
    return response


def login_view(request):
    if request.method == "GET":
        context = dict()
        print("in login.html")
        context["loginform"] = LoginForm()

        # response = HttpResponse(loader.get_template('login_v6.html').render(context, request))

        response = HttpResponse(
            loader.get_template("login.html").render(context, request)
        )
        response.delete_cookie("user_table_id")
        return response
    # post

    obj = mydict(request.POST)
    loginform = LoginForm(request.POST)
    # print(loginform)

    if not loginform.is_valid():
        response = render(request, "login.html", locals())
        response.delete_cookie("user_table_id")
        return response
    username = loginform.cleaned_data.get("username")
    password = loginform.cleaned_data.get("password")
    # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。

    user = authenticate(request, username=username, password=password)

    user_table_id = obj.get("user_table_id")
    table_user_ins = None

    # 用户信息表

    if str(8137) == user_table_id:
        table_user_ins = mc_userinfo
        page = "userinfo"
    # 系统管理员

    if str(8158) == user_table_id:
        table_user_ins = mc_supermanager
        page = "supermanager"
    if table_user_ins is None:
        print("登录失败,table_user_ins is None,注意表单提交用户表类型与系统配置不符")
        error_message = "登录信息失效"
        return redirect("/", locals())
    my_user = table_user_ins.objects.filter(username=username)
    if len(my_user) == 0:
        print("登录失败")
        error_message = "登录信息失效"
        return redirect("/", locals())
    # 验证如果用户不为空

    if user is None:
        # 强制注册功能
        # 返回登录失败信息
        # error_message = 'login faild'
        # response = render(request, 'login.html', locals())
        # response.delete_cookie('user_table_id')
        # return response
        # 默认即注册:

        # save

        my_user = table_user_ins(username=username)
        my_user.save()
        user = User.objects.create_user(
            username=username,
            password=password,
            email="",
            is_superuser=True,
        )

        user.set_password(password)
        user.save()
    # login方法登录

    django_default_login(request, user)
    print("login success")
    response = HttpResponseRedirect("/index", locals())
    response.set_cookie("user_table_id", user_table_id)
    return response


def usercenter(request):
    if request.method == "GET":
        context = dict()
        context["usercenterform"] = UserCenterForm()
        context["error_message"] = ""
    return render(request, "config_user/index.html", locals())


def index(request):

    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    username = request.user.username

    table_user_ins = None

    # 用户信息表

    if str(8137) == user_table_id:
        table_user_ins = mc_userinfo
        page = "userinfo"
    # 系统管理员

    if str(8158) == user_table_id:
        table_user_ins = mc_supermanager
        page = "supermanager"
    if table_user_ins is None:
        print("登录失败,table_user_ins is None,注意表单提交用户表类型与系统配置不符")
        error_message = "登录信息失效"
        return redirect("/", locals())
    my_user = table_user_ins.objects.filter(username=username)
    if len(my_user) == 0:
        print("登录失败")
        error_message = "登录信息失效"
        return redirect("/", locals())
    if request.method == "GET":
        # 主页默认配置信息

        """若需控制访问权限，可在此处加上判断条件，如：
            if not request.user.is_superuser:
                return render(request, 'index.html', locals())

            # 判断表内容对于当前用户的权限:
                1. 若是管理员，则显示所有项目
                2. 若是普通用户，则显示当前用户所属内容

        Returns:
            response: 请求处理
        """

        tab_mc_robotinfo = {
            "params": mc_robotinfo().toParams_zh(),
            "records": mc_robotinfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robotinfo.objects.all()[::-1]],
        }

        tab_mc_productionlkwkwineinfo = {
            "params": mc_productionlkwkwineinfo().toParams_zh(),
            "records": mc_productionlkwkwineinfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_productionlkwkwineinfo.objects.all()[::-1]],
        }

        tab_mc_safetymonitkwkworlog = {
            "params": mc_safetymonitkwkworlog().toParams_zh(),
            "records": mc_safetymonitkwkworlog.objects.all()[::-1],
            "json": [m.toJson() for m in mc_safetymonitkwkworlog.objects.all()[::-1]],
        }

        tab_mc_alarmreckwkword = {
            "params": mc_alarmreckwkword().toParams_zh(),
            "records": mc_alarmreckwkword.objects.all()[::-1],
            "json": [m.toJson() for m in mc_alarmreckwkword.objects.all()[::-1]],
        }

        tab_mc_robotlocation = {
            "params": mc_robotlocation().toParams_zh(),
            "records": mc_robotlocation.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robotlocation.objects.all()[::-1]],
        }

        tab_mc_robotstatus = {
            "params": mc_robotstatus().toParams_zh(),
            "records": mc_robotstatus.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robotstatus.objects.all()[::-1]],
        }

        tab_mc_robottkwkwask = {
            "params": mc_robottkwkwask().toParams_zh(),
            "records": mc_robottkwkwask.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robottkwkwask.objects.all()[::-1]],
        }

        tab_mc_productionlkwkwineconfig = {
            "params": mc_productionlkwkwineconfig().toParams_zh(),
            "records": mc_productionlkwkwineconfig.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_productionlkwkwineconfig.objects.all()[::-1]
            ],
        }

        tab_mc_permkwkwissionmanagement = {
            "params": mc_permkwkwissionmanagement().toParams_zh(),
            "records": mc_permkwkwissionmanagement.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_permkwkwissionmanagement.objects.all()[::-1]
            ],
        }

        tab_mc_userinfo = {
            "params": mc_userinfo().toParams_zh(),
            "records": mc_userinfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_userinfo.objects.all()[::-1]],
        }

        tab_mc_roleinfo = {
            "params": mc_roleinfo().toParams_zh(),
            "records": mc_roleinfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_roleinfo.objects.all()[::-1]],
        }

        tab_mc_userrolerelation = {
            "params": mc_userrolerelation().toParams_zh(),
            "records": mc_userrolerelation.objects.all()[::-1],
            "json": [m.toJson() for m in mc_userrolerelation.objects.all()[::-1]],
        }

        tab_mc_robotfault = {
            "params": mc_robotfault().toParams_zh(),
            "records": mc_robotfault.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robotfault.objects.all()[::-1]],
        }

        tab_mc_makwkwintenancereckwkword = {
            "params": mc_makwkwintenancereckwkword().toParams_zh(),
            "records": mc_makwkwintenancereckwkword.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_makwkwintenancereckwkword.objects.all()[::-1]
            ],
        }

        tab_mc_robotmokwkwdel = {
            "params": mc_robotmokwkwdel().toParams_zh(),
            "records": mc_robotmokwkwdel.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robotmokwkwdel.objects.all()[::-1]],
        }

        tab_mc_senskwkworinfo = {
            "params": mc_senskwkworinfo().toParams_zh(),
            "records": mc_senskwkworinfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_senskwkworinfo.objects.all()[::-1]],
        }

        tab_mc_senskwkwordata = {
            "params": mc_senskwkwordata().toParams_zh(),
            "records": mc_senskwkwordata.objects.all()[::-1],
            "json": [m.toJson() for m in mc_senskwkwordata.objects.all()[::-1]],
        }

        tab_mc_camerainfo = {
            "params": mc_camerainfo().toParams_zh(),
            "records": mc_camerainfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_camerainfo.objects.all()[::-1]],
        }

        tab_mc_videoreckwkword = {
            "params": mc_videoreckwkword().toParams_zh(),
            "records": mc_videoreckwkword.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videoreckwkword.objects.all()[::-1]],
        }

        tab_mc_robotoperationlog = {
            "params": mc_robotoperationlog().toParams_zh(),
            "records": mc_robotoperationlog.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robotoperationlog.objects.all()[::-1]],
        }

        tab_mc_productionlkwkwineefficiency = {
            "params": mc_productionlkwkwineefficiency().toParams_zh(),
            "records": mc_productionlkwkwineefficiency.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_productionlkwkwineefficiency.objects.all()[::-1]
            ],
        }

        tab_mc_robotfirmwareupdate = {
            "params": mc_robotfirmwareupdate().toParams_zh(),
            "records": mc_robotfirmwareupdate.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robotfirmwareupdate.objects.all()[::-1]],
        }

        tab_mc_robotfirmwareversion = {
            "params": mc_robotfirmwareversion().toParams_zh(),
            "records": mc_robotfirmwareversion.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robotfirmwareversion.objects.all()[::-1]],
        }

        tab_mc_productionlkwkwinesafetyrule = {
            "params": mc_productionlkwkwinesafetyrule().toParams_zh(),
            "records": mc_productionlkwkwinesafetyrule.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_productionlkwkwinesafetyrule.objects.all()[::-1]
            ],
        }

        tab_mc_robotsafetyconfig = {
            "params": mc_robotsafetyconfig().toParams_zh(),
            "records": mc_robotsafetyconfig.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robotsafetyconfig.objects.all()[::-1]],
        }

        tab_mc_robotinspectionplan = {
            "params": mc_robotinspectionplan().toParams_zh(),
            "records": mc_robotinspectionplan.objects.all()[::-1],
            "json": [m.toJson() for m in mc_robotinspectionplan.objects.all()[::-1]],
        }

        tab_mc_inspectionresult = {
            "params": mc_inspectionresult().toParams_zh(),
            "records": mc_inspectionresult.objects.all()[::-1],
            "json": [m.toJson() for m in mc_inspectionresult.objects.all()[::-1]],
        }

        tab_mc_robotmakwkwintenancecycle = {
            "params": mc_robotmakwkwintenancecycle().toParams_zh(),
            "records": mc_robotmakwkwintenancecycle.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_robotmakwkwintenancecycle.objects.all()[::-1]
            ],
        }

        tab_mc_productionlkwkwinedowntimereckwkword = {
            "params": mc_productionlkwkwinedowntimereckwkword().toParams_zh(),
            "records": mc_productionlkwkwinedowntimereckwkword.objects.all()[::-1],
            "json": [
                m.toJson()
                for m in mc_productionlkwkwinedowntimereckwkword.objects.all()[::-1]
            ],
        }

        tab_mc_robotpermkwkwissionassignment = {
            "params": mc_robotpermkwkwissionassignment().toParams_zh(),
            "records": mc_robotpermkwkwissionassignment.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_robotpermkwkwissionassignment.objects.all()[::-1]
            ],
        }

        tab_mc_supermanager = {
            "params": mc_supermanager().toParams_zh(),
            "records": mc_supermanager.objects.all()[::-1],
            "json": [m.toJson() for m in mc_supermanager.objects.all()[::-1]],
        }
    __version__ = settings.GLOBAL_VERSION

    if request.method == "GET":

        # 配置不同用户访问的主页不同
        # return render(request, f'index_{page}.html', locals())

        return render(request, f"index{__version__}.html", locals())
    # 处理post请求，一般不建议在这里添加多余功能。

    return render(request, f"index{__version__}.html", locals())

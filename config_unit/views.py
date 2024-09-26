import codecs
import json
import os
from django.http import FileResponse, JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from django.contrib.auth import login as django_default_login
from django.conf import settings
from django.contrib.auth.models import User
from sys_user.form import *
from sys_user.func import *
from config_unit.models import all_tables, gl
from config_unit.form import all_tables_form
from config_unit.captcha_impl import get_refresh_captcha, captcha_image
from appcenter.models import *


# Create your views here.


def index_view(request):
    if request.method == "GET":
        # 默认接口前缀配置

        config_unit = ""
        # config_unit = "/config_unit"
        # 主页默认配置信息

        tables = all_tables

        return render(request, "config_unit/index.html", locals())
    return JsonResponse({"status": "error", "msg": "请求错误"})


def refresh_view(request):
    code = get_refresh_captcha(request)
    return JsonResponse({"code": code, "msg": "验证码刷新成功", "res": "ok"})


def register(request):
    registerform = RegisterForm(request.POST)
    if not registerform.is_valid():
        return JsonResponse({"status": "error", "msg": "表单验证失败"})
    username = registerform.cleaned_data.get("username")
    password1 = registerform.cleaned_data.get("password1")
    password2 = registerform.cleaned_data.get("password2")

    user = User.objects.filter(username=username)
    if user:
        return JsonResponse({"status": "error", "msg": "用户名已存在"})
    if password1 != password2:
        return JsonResponse({"status": "error", "msg": "密码不一致"})
    user = User.objects.create_user(
        username=username,
        password=password1,
        email=registerform.cleaned_data.get("email"),
        is_superuser=True,
    )

    user.set_password(password1)
    user.save()
    return JsonResponse({"res": "OK", "msg": "注册成功"})


def logout_view(request):
    logout(request)

    response = redirect("/")
    response.delete_cookie("username")
    return response


def login_view(request):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    # post

    loginform = LoginForm(json.loads(request.body))
    print(loginform)
    if not loginform.is_valid():
        return JsonResponse({"res": "error", "msg": "表单验证失败"})
    username = loginform.cleaned_data.get("username")
    password = loginform.cleaned_data.get("password")
    # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。

    user = authenticate(request, username=username, password=password)
    # 验证如果用户不为空

    if user is None:
        # 返回登录失败信息

        return JsonResponse({"res": "error", "message": "用户名或密码错误"})
    # login方法登录

    django_default_login(request, user)

    response = JsonResponse(
        {
            "res": "OK",
            "msg": "登录成功",
            "token": 1,
            "userid": request.user.id,
            "username": request.user.username,
        }
    )
    response.set_cookie("username", username)
    response.set_cookie("token", 1)
    response.set_cookie("userid", request.user.id)
    return response


def serve_media(request, path):
    """访问media内文件

    Args:
        request (RequestHandle): 请求
        path (路径): XXX.xxx

    Raises:
        Http404: 未找到文件

    Returns:
        filestream: 文件流
    """
    # 构建文件的绝对路径

    file_path = "media/" + path + ".zip"
    # file_path = os.path.join(settings.MEDIA_ROOT, file_path)

    file_path = file_path.replace("\\", "/")
    print(file_path)

    # 检查文件是否存在

    if os.path.exists(file_path):
        # 在打开文件之前添加安全性检查
        # safe_path = os.path.normpath(file_path).replace('\\', '/')
        # if not os.path.commonprefix((safe_path, settings.MEDIA_ROOT)) == settings.MEDIA_ROOT.replace('\\', '/'):
        #     # 路径不在 MEDIA_ROOT 内，拒绝服务
        #     print('safe_path: ',safe_path)
        #     print(os.path.commonprefix((safe_path, settings.MEDIA_ROOT)))
        #     print('MEDIA_ROOT:', settings.MEDIA_ROOT.replace('\\', '/'))
        #     raise Http404
        # 创建一个响应对象，设置适当的 Content-Disposition 头部

        response = FileResponse(file_path, filename=file_path)
        response["Content-Type"] = "application/octet-stream"
        response["Content-Disposition"] = (
            'attachment; filename="' + os.path.basename(file_path) + '"'
        )
        return response
    # 如果文件不存在，返回 404 错误

    from django.http import Http404

    raise Http404


def config_unit(request, tablename):
    # 检查权限

    has_add = True
    has_upd = True
    has_del = True
    has_view = True

    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    # 对于无参数的post请求此处会报异常
    # obj = mydict(request.POST)

    if len(request.body) == 0:
        return JsonResponse({"res": "Not Allowed", "msg": "optype不存在"})
    obj = json.loads(request.body)
    print(obj.keys())
    if "optype" not in obj:
        return JsonResponse({"res": "Not Allowed", "msg": "optype不存在"})
    optype = obj.get("optype")

    # 根据表名获取数据

    tableins = gl.get(tablename)
    tablemeta = all_tables.get(tablename)
    if tableins is None:
        print(gl.keys())
        return JsonResponse({"res": "Not Allowed", "msg": "表名错误:" + tablename})
    if optype == "add" and has_add:
        ins_table_busi = tableins()
        for field in tablemeta.get("field"):
            if field.name == "id":
                continue
            if field.name not in obj:
                continue
            setattr(ins_table_busi, field.name, obj.get(field.name, ""))
        ins_table_busi.save()
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    if optype == "upd" and has_upd:
        ins_table_busi = tableins.objects.get(id=obj.get("_id_upd"))

        for field in tablemeta.get("field"):
            if field.name == "id":
                continue
            if field.name not in obj:
                continue
            setattr(ins_table_busi, field.name, obj.get(field.name))
        ins_table_busi.save()
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    if optype == "del" and has_del:
        ins_table_busi = tableins.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    if optype == "get" and has_view:
        ins_table_busi = tableins.objects.get(id=obj.get("_id"))
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    if optype == "filter" and has_view:
        condition = {
            param: obj.get(param) for param in tableins().toParams() if param in obj
        }
        ins_table_busis = [m.toJson() for m in tableins.objects.filter(**condition)]
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busis,
        }
    if optype == "view" and has_view:
        ins_table_busi = tableins.objects.get(id=obj.get("recordid"))
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    if optype == "go_add" and has_add:
        ins_table_busi = tableins()
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    if optype == "go_upd" and has_add:
        ins_table_busi = tableins.objects.get(id=obj.get("form").get("id"))
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    return JsonResponse(res)


def table_busi(request):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    ins = dict()

    ins["robotinfo"] = mymeta(mc_robotinfo)

    ins["productionlkwkwineinfo"] = mymeta(mc_productionlkwkwineinfo)

    ins["safetymonitkwkworlog"] = mymeta(mc_safetymonitkwkworlog)

    ins["alarmreckwkword"] = mymeta(mc_alarmreckwkword)

    ins["robotlocation"] = mymeta(mc_robotlocation)

    ins["robotstatus"] = mymeta(mc_robotstatus)

    ins["robottkwkwask"] = mymeta(mc_robottkwkwask)

    ins["productionlkwkwineconfig"] = mymeta(mc_productionlkwkwineconfig)

    ins["permkwkwissionmanagement"] = mymeta(mc_permkwkwissionmanagement)

    ins["userinfo"] = mymeta(mc_userinfo)

    ins["roleinfo"] = mymeta(mc_roleinfo)

    ins["userrolerelation"] = mymeta(mc_userrolerelation)

    ins["robotfault"] = mymeta(mc_robotfault)

    ins["makwkwintenancereckwkword"] = mymeta(mc_makwkwintenancereckwkword)

    ins["robotmokwkwdel"] = mymeta(mc_robotmokwkwdel)

    ins["senskwkworinfo"] = mymeta(mc_senskwkworinfo)

    ins["senskwkwordata"] = mymeta(mc_senskwkwordata)

    ins["camerainfo"] = mymeta(mc_camerainfo)

    ins["videoreckwkword"] = mymeta(mc_videoreckwkword)

    ins["robotoperationlog"] = mymeta(mc_robotoperationlog)

    ins["productionlkwkwineefficiency"] = mymeta(mc_productionlkwkwineefficiency)

    ins["robotfirmwareupdate"] = mymeta(mc_robotfirmwareupdate)

    ins["robotfirmwareversion"] = mymeta(mc_robotfirmwareversion)

    ins["productionlkwkwinesafetyrule"] = mymeta(mc_productionlkwkwinesafetyrule)

    ins["robotsafetyconfig"] = mymeta(mc_robotsafetyconfig)

    ins["robotinspectionplan"] = mymeta(mc_robotinspectionplan)

    ins["inspectionresult"] = mymeta(mc_inspectionresult)

    ins["robotmakwkwintenancecycle"] = mymeta(mc_robotmakwkwintenancecycle)

    ins["productionlkwkwinedowntimereckwkword"] = mymeta(
        mc_productionlkwkwinedowntimereckwkword
    )

    ins["robotpermkwkwissionassignment"] = mymeta(mc_robotpermkwkwissionassignment)

    ins["supermanager"] = mymeta(mc_supermanager)

    res = {"res": "OK", "msg": "success", "obj": {}, "ins": ins}

    return JsonResponse(res)


def table_user(request):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    ins = dict()

    ins["userinfo"] = mymeta(mc_userinfo)

    ins["supermanager"] = mymeta(mc_supermanager)

    res = {"res": "OK", "msg": "success", "obj": {}, "ins": ins}

    return JsonResponse(res)


def auth_table(request):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    ins = dict()

    ins["8128,8137"] = (mymeta(mc_robotinfo), mymeta(mc_userinfo))

    ins["8128,8158"] = (mymeta(mc_robotinfo), mymeta(mc_supermanager))

    ins["8129,8137"] = (mymeta(mc_productionlkwkwineinfo), mymeta(mc_userinfo))

    ins["8129,8158"] = (mymeta(mc_productionlkwkwineinfo), mymeta(mc_supermanager))

    ins["8130,8137"] = (mymeta(mc_safetymonitkwkworlog), mymeta(mc_userinfo))

    ins["8130,8158"] = (mymeta(mc_safetymonitkwkworlog), mymeta(mc_supermanager))

    ins["8131,8137"] = (mymeta(mc_alarmreckwkword), mymeta(mc_userinfo))

    ins["8131,8158"] = (mymeta(mc_alarmreckwkword), mymeta(mc_supermanager))

    ins["8132,8137"] = (mymeta(mc_robotlocation), mymeta(mc_userinfo))

    ins["8132,8158"] = (mymeta(mc_robotlocation), mymeta(mc_supermanager))

    ins["8133,8137"] = (mymeta(mc_robotstatus), mymeta(mc_userinfo))

    ins["8133,8158"] = (mymeta(mc_robotstatus), mymeta(mc_supermanager))

    ins["8134,8137"] = (mymeta(mc_robottkwkwask), mymeta(mc_userinfo))

    ins["8134,8158"] = (mymeta(mc_robottkwkwask), mymeta(mc_supermanager))

    ins["8135,8137"] = (mymeta(mc_productionlkwkwineconfig), mymeta(mc_userinfo))

    ins["8135,8158"] = (mymeta(mc_productionlkwkwineconfig), mymeta(mc_supermanager))

    ins["8136,8137"] = (mymeta(mc_permkwkwissionmanagement), mymeta(mc_userinfo))

    ins["8136,8158"] = (mymeta(mc_permkwkwissionmanagement), mymeta(mc_supermanager))

    ins["8137,8137"] = (mymeta(mc_userinfo), mymeta(mc_userinfo))

    ins["8137,8158"] = (mymeta(mc_userinfo), mymeta(mc_supermanager))

    ins["8138,8137"] = (mymeta(mc_roleinfo), mymeta(mc_userinfo))

    ins["8138,8158"] = (mymeta(mc_roleinfo), mymeta(mc_supermanager))

    ins["8139,8137"] = (mymeta(mc_userrolerelation), mymeta(mc_userinfo))

    ins["8139,8158"] = (mymeta(mc_userrolerelation), mymeta(mc_supermanager))

    ins["8140,8137"] = (mymeta(mc_robotfault), mymeta(mc_userinfo))

    ins["8140,8158"] = (mymeta(mc_robotfault), mymeta(mc_supermanager))

    ins["8141,8137"] = (mymeta(mc_makwkwintenancereckwkword), mymeta(mc_userinfo))

    ins["8141,8158"] = (mymeta(mc_makwkwintenancereckwkword), mymeta(mc_supermanager))

    ins["8142,8137"] = (mymeta(mc_robotmokwkwdel), mymeta(mc_userinfo))

    ins["8142,8158"] = (mymeta(mc_robotmokwkwdel), mymeta(mc_supermanager))

    ins["8143,8137"] = (mymeta(mc_senskwkworinfo), mymeta(mc_userinfo))

    ins["8143,8158"] = (mymeta(mc_senskwkworinfo), mymeta(mc_supermanager))

    ins["8144,8137"] = (mymeta(mc_senskwkwordata), mymeta(mc_userinfo))

    ins["8144,8158"] = (mymeta(mc_senskwkwordata), mymeta(mc_supermanager))

    ins["8145,8137"] = (mymeta(mc_camerainfo), mymeta(mc_userinfo))

    ins["8145,8158"] = (mymeta(mc_camerainfo), mymeta(mc_supermanager))

    ins["8146,8137"] = (mymeta(mc_videoreckwkword), mymeta(mc_userinfo))

    ins["8146,8158"] = (mymeta(mc_videoreckwkword), mymeta(mc_supermanager))

    ins["8147,8137"] = (mymeta(mc_robotoperationlog), mymeta(mc_userinfo))

    ins["8147,8158"] = (mymeta(mc_robotoperationlog), mymeta(mc_supermanager))

    ins["8148,8137"] = (mymeta(mc_productionlkwkwineefficiency), mymeta(mc_userinfo))

    ins["8148,8158"] = (
        mymeta(mc_productionlkwkwineefficiency),
        mymeta(mc_supermanager),
    )

    ins["8149,8137"] = (mymeta(mc_robotfirmwareupdate), mymeta(mc_userinfo))

    ins["8149,8158"] = (mymeta(mc_robotfirmwareupdate), mymeta(mc_supermanager))

    ins["8150,8137"] = (mymeta(mc_robotfirmwareversion), mymeta(mc_userinfo))

    ins["8150,8158"] = (mymeta(mc_robotfirmwareversion), mymeta(mc_supermanager))

    ins["8151,8137"] = (mymeta(mc_productionlkwkwinesafetyrule), mymeta(mc_userinfo))

    ins["8151,8158"] = (
        mymeta(mc_productionlkwkwinesafetyrule),
        mymeta(mc_supermanager),
    )

    ins["8152,8137"] = (mymeta(mc_robotsafetyconfig), mymeta(mc_userinfo))

    ins["8152,8158"] = (mymeta(mc_robotsafetyconfig), mymeta(mc_supermanager))

    ins["8153,8137"] = (mymeta(mc_robotinspectionplan), mymeta(mc_userinfo))

    ins["8153,8158"] = (mymeta(mc_robotinspectionplan), mymeta(mc_supermanager))

    ins["8154,8137"] = (mymeta(mc_inspectionresult), mymeta(mc_userinfo))

    ins["8154,8158"] = (mymeta(mc_inspectionresult), mymeta(mc_supermanager))

    ins["8155,8137"] = (mymeta(mc_robotmakwkwintenancecycle), mymeta(mc_userinfo))

    ins["8155,8158"] = (mymeta(mc_robotmakwkwintenancecycle), mymeta(mc_supermanager))

    ins["8156,8137"] = (
        mymeta(mc_productionlkwkwinedowntimereckwkword),
        mymeta(mc_userinfo),
    )

    ins["8156,8158"] = (
        mymeta(mc_productionlkwkwinedowntimereckwkword),
        mymeta(mc_supermanager),
    )

    ins["8157,8137"] = (mymeta(mc_robotpermkwkwissionassignment), mymeta(mc_userinfo))

    ins["8157,8158"] = (
        mymeta(mc_robotpermkwkwissionassignment),
        mymeta(mc_supermanager),
    )

    ins["8158,8137"] = (mymeta(mc_supermanager), mymeta(mc_userinfo))

    ins["8158,8158"] = (mymeta(mc_supermanager), mymeta(mc_supermanager))

    res = {"res": "OK", "msg": "success", "obj": {}, "ins": ins}

    return JsonResponse(res)


def common_form(request, tablename):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    tableins = gl.get(tablename)
    tablemeta = all_tables.get(tablename)

    obj = json.loads(request.body)

    optype = obj.get("optype")
    if optype == "add":
        formins = all_tables_form.get(tablename)
        res = {"res": "OK", "msg": "success", "obj": {}, "ins": formins().as_p()}
    if optype == "upd":
        formins = all_tables_form.get(tablename)
        myform = formins(tableins.objects.get(id=obj.get("id")))
        res = {"res": "OK", "msg": "success", "obj": {}, "ins": myform.as_p()}
    return JsonResponse(res)


def submit_view(request):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    obj = json.loads(request.body)

    tablename = obj.get("tablename")
    if tablename == "supermanager":
        return JsonResponse({"res": "Not Allowed", "msg": "禁止在此创建系统管理员"})
    tableins = gl.get(tablename)
    tablemeta = all_tables.get(tablename)
    form = obj["form"]
    print(form)
    if "id" not in form or form["id"] is None:
        ins = tableins()
        for k, v in obj.get("form").items():
            if v is None:
                continue
            setattr(ins, k, v)
        ins.save()
        obj["optype"] = "add"
        res = {"res": "OK", "msg": "success", "ins": ins.toJson(), "obj": obj}
    else:
        ins = tableins.objects.get(id=obj.get("form").get("id"))
        for k, v in obj.get("form").items():
            setattr(ins, k, v)
        ins.save()
        obj["optype"] = "upd"
        res = {"res": "OK", "msg": "success", "ins": ins.toJson(), "obj": obj}
    return JsonResponse(res)

from datetime import datetime
import os
import time
import uuid

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from appcenter.models import *
from sys_user.func import *


def resp(res, msg, url=None, **kwargs):
    return {"res": res, "msg": msg, "url": url, **kwargs}


# Create your views here.


def index(request):
    records = [
        {
            "id": 1,
        },
        {"id": 2},
    ]
    return render(request, "config_visual/index.html", locals())


@login_required
def view_robotinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人信息表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人名称

        mcauthfield_robotname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 型号编号

        mcauthfield_mokwkwdelnumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 序列号

        mcauthfield_serialnumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产日期

        mcauthfield_manufacturedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最近维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 运行状态

        mcauthfield_operationalstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人信息表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人名称

        mcauthfield_robotname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 型号编号

        mcauthfield_mokwkwdelnumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 序列号

        mcauthfield_serialnumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产日期

        mcauthfield_manufacturedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最近维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 运行状态

        mcauthfield_operationalstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotinfo.objects.filter(**filter)
        else:
            records = mc_robotinfo.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/robotinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotinfo()

        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 机器人名称

        if mcauthfield_robotname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.robotname = obj.get("robotname")
        # 型号编号

        if mcauthfield_mokwkwdelnumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.mokwkwdelnumber = obj.get("mokwkwdelnumber")
        # 序列号

        if mcauthfield_serialnumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.serialnumber = obj.get("serialnumber")
        # 生产日期

        if mcauthfield_manufacturedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.manufacturedate = obj.get("manufacturedate")
        # 最近维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 运行状态

        if mcauthfield_operationalstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.operationalstatus = obj.get("operationalstatus")
        # 位置

        if mcauthfield_location["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.location = obj.get("location")
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.departmentid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotinfo.objects.get(id=obj.get("_id_upd"))

        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 机器人名称

        if mcauthfield_robotname["mcauthchange"]:

            # CharField

            ins_table_busi.robotname = obj.get("robotname")
        # 型号编号

        if mcauthfield_mokwkwdelnumber["mcauthchange"]:

            # CharField

            ins_table_busi.mokwkwdelnumber = obj.get("mokwkwdelnumber")
        # 序列号

        if mcauthfield_serialnumber["mcauthchange"]:

            # CharField

            ins_table_busi.serialnumber = obj.get("serialnumber")
        # 生产日期

        if mcauthfield_manufacturedate["mcauthchange"]:

            # DateField

            ins_table_busi.manufacturedate = obj.get("manufacturedate")
        # 最近维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 运行状态

        if mcauthfield_operationalstatus["mcauthchange"]:

            # CharField

            ins_table_busi.operationalstatus = obj.get("operationalstatus")
        # 位置

        if mcauthfield_location["mcauthchange"]:

            # CharField

            ins_table_busi.location = obj.get("location")
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.departmentid = str(uuid.uuid4())

            ins_table_busi.departmentid = str(ins_table_busi.departmentid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_productionlkwkwineinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 生产线信息表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 生产线ID

        mcauthfield_productionlkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线名称

        mcauthfield_productionlkwkwinename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_creationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大产能

        mcauthfield_maxcapacity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护周期

        mcauthfield_makwkwintenancecycle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人数量

        mcauthfield_robotcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联工厂ID

        mcauthfield_associatedfactkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 生产线信息表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 生产线ID

        mcauthfield_productionlkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线名称

        mcauthfield_productionlkwkwinename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建日期

        mcauthfield_creationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大产能

        mcauthfield_maxcapacity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护周期

        mcauthfield_makwkwintenancecycle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人数量

        mcauthfield_robotcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联工厂ID

        mcauthfield_associatedfactkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_productionlkwkwineinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_productionlkwkwineinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_productionlkwkwineinfo.objects.filter(**filter)
        else:
            records = mc_productionlkwkwineinfo.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_productionlkwkwineinfo_55559 = []
        for m in mc_productionlkwkwineinfo.objects.all():
            mobj = m.toJson()
            data_mc_productionlkwkwineinfo_55559.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("productionlkwkwinename"),
                }
            )
        return render(request, "config_busi/productionlkwkwineinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_productionlkwkwineinfo()

        # 生产线ID

        if mcauthfield_productionlkwkwineid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.productionlkwkwineid = str(uuid.uuid4())
        # 生产线名称

        if mcauthfield_productionlkwkwinename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.productionlkwkwinename = obj.get("productionlkwkwinename")
        # 生产线位置

        if mcauthfield_location["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.location = obj.get("location")
        # 创建日期

        if mcauthfield_creationdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.creationdate = obj.get("creationdate")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 最大产能

        if mcauthfield_maxcapacity["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.maxcapacity = obj.get("maxcapacity")
        # 维护周期

        if mcauthfield_makwkwintenancecycle["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenancecycle = obj.get("makwkwintenancecycle")
        # 上次维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 机器人数量

        if mcauthfield_robotcount["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.robotcount = obj.get("robotcount")
        # 关联工厂ID

        if mcauthfield_associatedfactkwkworyid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.associatedfactkwkworyid = obj.get("associatedfactkwkworyid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_productionlkwkwineinfo.objects.get(id=obj.get("_id_upd"))

        # 生产线ID

        if mcauthfield_productionlkwkwineid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.productionlkwkwineid = str(uuid.uuid4())

            ins_table_busi.productionlkwkwineid = str(
                ins_table_busi.productionlkwkwineid
            )
        # 生产线名称

        if mcauthfield_productionlkwkwinename["mcauthchange"]:

            # CharField

            ins_table_busi.productionlkwkwinename = obj.get("productionlkwkwinename")
        # 生产线位置

        if mcauthfield_location["mcauthchange"]:

            # CharField

            ins_table_busi.location = obj.get("location")
        # 创建日期

        if mcauthfield_creationdate["mcauthchange"]:

            # DateField

            ins_table_busi.creationdate = obj.get("creationdate")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 最大产能

        if mcauthfield_maxcapacity["mcauthchange"]:

            # CharField

            ins_table_busi.maxcapacity = obj.get("maxcapacity")
        # 维护周期

        if mcauthfield_makwkwintenancecycle["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenancecycle = obj.get("makwkwintenancecycle")
        # 上次维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 机器人数量

        if mcauthfield_robotcount["mcauthchange"]:

            # IntegerField

            ins_table_busi.robotcount = obj.get("robotcount")
        # 关联工厂ID

        if mcauthfield_associatedfactkwkworyid["mcauthchange"]:

            # SelectField

            ins_table_busi.associatedfactkwkworyid = obj.get("associatedfactkwkworyid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_productionlkwkwineinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_productionlkwkwineinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/productionlkwkwineinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_safetymonitkwkworlog(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 安全监控日志表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 日志ID

        mcauthfield_logid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 设备ID

        mcauthfield_deviceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 事件类型

        mcauthfield_eventtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 事件发生时间

        mcauthfield_eventtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 事件描述

        mcauthfield_eventdescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 严重程度

        mcauthfield_severity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 采取的措施

        mcauthfield_actiontaken = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作人员ID

        mcauthfield_operatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 安全监控日志表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 日志ID

        mcauthfield_logid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 设备ID

        mcauthfield_deviceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 事件类型

        mcauthfield_eventtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 事件发生时间

        mcauthfield_eventtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 事件描述

        mcauthfield_eventdescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 严重程度

        mcauthfield_severity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 采取的措施

        mcauthfield_actiontaken = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作人员ID

        mcauthfield_operatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_safetymonitkwkworlog.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_safetymonitkwkworlog().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_safetymonitkwkworlog.objects.filter(**filter)
        else:
            records = mc_safetymonitkwkworlog.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/safetymonitkwkworlog.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_safetymonitkwkworlog()

        # 日志ID

        if mcauthfield_logid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.logid = str(uuid.uuid4())
        # 设备ID

        if mcauthfield_deviceid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.deviceid = str(uuid.uuid4())
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 事件类型

        if mcauthfield_eventtype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.eventtype = obj.get("eventtype")
        # 事件发生时间

        if mcauthfield_eventtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.eventtime = obj.get("eventtime")
        # 事件描述

        if mcauthfield_eventdescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.eventdescription = obj.get("eventdescription")
        # 严重程度

        if mcauthfield_severity["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.severity = obj.get("severity")
        # 采取的措施

        if mcauthfield_actiontaken["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.actiontaken = obj.get("actiontaken")
        # 操作人员ID

        if mcauthfield_operatkwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.operatkwkworid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_safetymonitkwkworlog.objects.get(id=obj.get("_id_upd"))

        # 日志ID

        if mcauthfield_logid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.logid = str(uuid.uuid4())

            ins_table_busi.logid = str(ins_table_busi.logid)
        # 设备ID

        if mcauthfield_deviceid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.deviceid = str(uuid.uuid4())

            ins_table_busi.deviceid = str(ins_table_busi.deviceid)
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 事件类型

        if mcauthfield_eventtype["mcauthchange"]:

            # CharField

            ins_table_busi.eventtype = obj.get("eventtype")
        # 事件发生时间

        if mcauthfield_eventtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.eventtime = obj.get("eventtime")
        # 事件描述

        if mcauthfield_eventdescription["mcauthchange"]:

            # TextField

            ins_table_busi.eventdescription = obj.get("eventdescription")
        # 严重程度

        if mcauthfield_severity["mcauthchange"]:

            # CharField

            ins_table_busi.severity = obj.get("severity")
        # 采取的措施

        if mcauthfield_actiontaken["mcauthchange"]:

            # CharField

            ins_table_busi.actiontaken = obj.get("actiontaken")
        # 操作人员ID

        if mcauthfield_operatkwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.operatkwkworid = str(uuid.uuid4())

            ins_table_busi.operatkwkworid = str(ins_table_busi.operatkwkworid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_safetymonitkwkworlog.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_safetymonitkwkworlog.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/safetymonitkwkworlog")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_alarmreckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 报警记录表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 记录ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警时间

        mcauthfield_alarmtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警类型

        mcauthfield_alarmtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警等级

        mcauthfield_alarmlevel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID关联字段

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已解决

        mcauthfield_resolved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 解决时间

        mcauthfield_resolvedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 报警记录表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 记录ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警时间

        mcauthfield_alarmtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警类型

        mcauthfield_alarmtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警等级

        mcauthfield_alarmlevel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID关联字段

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已解决

        mcauthfield_resolved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 解决时间

        mcauthfield_resolvedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_alarmreckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_alarmreckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_alarmreckwkword.objects.filter(**filter)
        else:
            records = mc_alarmreckwkword.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_robotinfo_55574 = []
        for m in mc_robotinfo.objects.all():
            mobj = m.toJson()
            data_mc_robotinfo_55574.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("mokwkwdelnumber"),
                }
            )
        return render(request, "config_busi/alarmreckwkword.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_alarmreckwkword()

        # 记录ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 报警时间

        if mcauthfield_alarmtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.alarmtime = obj.get("alarmtime")
        # 报警类型

        if mcauthfield_alarmtype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.alarmtype = obj.get("alarmtype")
        # 报警等级

        if mcauthfield_alarmlevel["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.alarmlevel = obj.get("alarmlevel")
        # 报警描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 机器人ID关联字段

        if mcauthfield_robotid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.robotid = obj.get("robotid")
        # 是否已解决

        if mcauthfield_resolved["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.resolved = obj.get("resolved")
        # 解决时间

        if mcauthfield_resolvedtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.resolvedtime = obj.get("resolvedtime")
        # 报警位置

        if mcauthfield_location["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.location = obj.get("location")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_alarmreckwkword.objects.get(id=obj.get("_id_upd"))

        # 记录ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 报警时间

        if mcauthfield_alarmtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.alarmtime = obj.get("alarmtime")
        # 报警类型

        if mcauthfield_alarmtype["mcauthchange"]:

            # CharField

            ins_table_busi.alarmtype = obj.get("alarmtype")
        # 报警等级

        if mcauthfield_alarmlevel["mcauthchange"]:

            # CharField

            ins_table_busi.alarmlevel = obj.get("alarmlevel")
        # 报警描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 机器人ID关联字段

        if mcauthfield_robotid["mcauthchange"]:

            # SelectField

            ins_table_busi.robotid = obj.get("robotid")
        # 是否已解决

        if mcauthfield_resolved["mcauthchange"]:

            # BooleanField

            ins_table_busi.resolved = obj.get("resolved")
        # 解决时间

        if mcauthfield_resolvedtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.resolvedtime = obj.get("resolvedtime")
        # 报警位置

        if mcauthfield_location["mcauthchange"]:

            # CharField

            ins_table_busi.location = obj.get("location")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_alarmreckwkword.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_alarmreckwkword.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/alarmreckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotlocation(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人位置表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 机器人ID唯一标识每一个智能机器人的编号

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 位置编码机器人当前所在位置的唯一编码

        mcauthfield_locationcode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 区域名称机器人所在区域的名称

        mcauthfield_areaname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 坐标机器人在该区域内的X轴坐标

        mcauthfield_xcokwkwordkwkwinatex = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 坐标机器人在该区域内的Y轴坐标

        mcauthfield_ycokwkwordkwkwinatey = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 坐标机器人在该区域内的Z轴坐标如果适用

        mcauthfield_zcokwkwordkwkwinatez = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态机器人的当前状态如“运行中”、“空闲”、“故障”等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后更新时间机器人位置信息最后一次更新的时间

        mcauthfield_lkwkwastupdatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 工作站ID机器人当前所在的工作站的ID关联字段

        mcauthfield_wkwkworkstationid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人位置表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 机器人ID唯一标识每一个智能机器人的编号

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 位置编码机器人当前所在位置的唯一编码

        mcauthfield_locationcode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 区域名称机器人所在区域的名称

        mcauthfield_areaname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 坐标机器人在该区域内的X轴坐标

        mcauthfield_xcokwkwordkwkwinatex = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 坐标机器人在该区域内的Y轴坐标

        mcauthfield_ycokwkwordkwkwinatey = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 坐标机器人在该区域内的Z轴坐标如果适用

        mcauthfield_zcokwkwordkwkwinatez = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态机器人的当前状态如“运行中”、“空闲”、“故障”等

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后更新时间机器人位置信息最后一次更新的时间

        mcauthfield_lkwkwastupdatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 工作站ID机器人当前所在的工作站的ID关联字段

        mcauthfield_wkwkworkstationid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotlocation.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotlocation().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotlocation.objects.filter(**filter)
        else:
            records = mc_robotlocation.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_productionlkwkwineinfo_55586 = []
        for m in mc_productionlkwkwineinfo.objects.all():
            mobj = m.toJson()
            data_mc_productionlkwkwineinfo_55586.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("location"),
                }
            )
        return render(request, "config_busi/robotlocation.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotlocation()

        # 机器人ID唯一标识每一个智能机器人的编号

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 位置编码机器人当前所在位置的唯一编码

        if mcauthfield_locationcode["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.locationcode = obj.get("locationcode")
        # 区域名称机器人所在区域的名称

        if mcauthfield_areaname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.areaname = obj.get("areaname")
        # 坐标机器人在该区域内的X轴坐标

        if mcauthfield_xcokwkwordkwkwinatex["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.xcokwkwordkwkwinatex = obj.get("xcokwkwordkwkwinatex")
        # 坐标机器人在该区域内的Y轴坐标

        if mcauthfield_ycokwkwordkwkwinatey["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.ycokwkwordkwkwinatey = obj.get("ycokwkwordkwkwinatey")
        # 坐标机器人在该区域内的Z轴坐标如果适用

        if mcauthfield_zcokwkwordkwkwinatez["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.zcokwkwordkwkwinatez = obj.get("zcokwkwordkwkwinatez")
        # 状态机器人的当前状态如“运行中”、“空闲”、“故障”等

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 最后更新时间机器人位置信息最后一次更新的时间

        if mcauthfield_lkwkwastupdatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastupdatetime = obj.get("lkwkwastupdatetime")
        # 工作站ID机器人当前所在的工作站的ID关联字段

        if mcauthfield_wkwkworkstationid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.wkwkworkstationid = obj.get("wkwkworkstationid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotlocation.objects.get(id=obj.get("_id_upd"))

        # 机器人ID唯一标识每一个智能机器人的编号

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 位置编码机器人当前所在位置的唯一编码

        if mcauthfield_locationcode["mcauthchange"]:

            # CharField

            ins_table_busi.locationcode = obj.get("locationcode")
        # 区域名称机器人所在区域的名称

        if mcauthfield_areaname["mcauthchange"]:

            # CharField

            ins_table_busi.areaname = obj.get("areaname")
        # 坐标机器人在该区域内的X轴坐标

        if mcauthfield_xcokwkwordkwkwinatex["mcauthchange"]:

            # CharField

            ins_table_busi.xcokwkwordkwkwinatex = obj.get("xcokwkwordkwkwinatex")
        # 坐标机器人在该区域内的Y轴坐标

        if mcauthfield_ycokwkwordkwkwinatey["mcauthchange"]:

            # CharField

            ins_table_busi.ycokwkwordkwkwinatey = obj.get("ycokwkwordkwkwinatey")
        # 坐标机器人在该区域内的Z轴坐标如果适用

        if mcauthfield_zcokwkwordkwkwinatez["mcauthchange"]:

            # CharField

            ins_table_busi.zcokwkwordkwkwinatez = obj.get("zcokwkwordkwkwinatez")
        # 状态机器人的当前状态如“运行中”、“空闲”、“故障”等

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 最后更新时间机器人位置信息最后一次更新的时间

        if mcauthfield_lkwkwastupdatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastupdatetime = obj.get("lkwkwastupdatetime")
        # 工作站ID机器人当前所在的工作站的ID关联字段

        if mcauthfield_wkwkworkstationid["mcauthchange"]:

            # SelectField

            ins_table_busi.wkwkworkstationid = obj.get("wkwkworkstationid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotlocation.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotlocation.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotlocation")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotstatus(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人状态表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 时间戳

        mcauthfield_timestamp = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障代码

        mcauthfield_faultcode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护标志

        mcauthfield_makwkwintenanceflag = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电量水平

        mcauthfield_powerlevel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联工作站ID

        mcauthfield_associatedwkwkworkstationid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人状态表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 时间戳

        mcauthfield_timestamp = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障代码

        mcauthfield_faultcode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护标志

        mcauthfield_makwkwintenanceflag = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电量水平

        mcauthfield_powerlevel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联工作站ID

        mcauthfield_associatedwkwkworkstationid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotstatus.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotstatus().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotstatus.objects.filter(**filter)
        else:
            records = mc_robotstatus.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_productionlkwkwineinfo_55596 = []
        for m in mc_productionlkwkwineinfo.objects.all():
            mobj = m.toJson()
            data_mc_productionlkwkwineinfo_55596.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("productionlkwkwinename"),
                }
            )
        return render(request, "config_busi/robotstatus.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotstatus()

        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 时间戳

        if mcauthfield_timestamp["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.timestamp = obj.get("timestamp")
        # 位置

        if mcauthfield_location["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.location = obj.get("location")
        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.tkwkwaskid = str(uuid.uuid4())
        # 故障代码

        if mcauthfield_faultcode["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.faultcode = obj.get("faultcode")
        # 维护标志

        if mcauthfield_makwkwintenanceflag["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenanceflag = obj.get("makwkwintenanceflag")
        # 电量水平

        if mcauthfield_powerlevel["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.powerlevel = obj.get("powerlevel")
        # 上次维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 关联工作站ID

        if mcauthfield_associatedwkwkworkstationid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.associatedwkwkworkstationid = obj.get(
                "associatedwkwkworkstationid"
            )
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotstatus.objects.get(id=obj.get("_id_upd"))

        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 时间戳

        if mcauthfield_timestamp["mcauthchange"]:

            # DateTimeField

            ins_table_busi.timestamp = obj.get("timestamp")
        # 位置

        if mcauthfield_location["mcauthchange"]:

            # CharField

            ins_table_busi.location = obj.get("location")
        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.tkwkwaskid = str(uuid.uuid4())

            ins_table_busi.tkwkwaskid = str(ins_table_busi.tkwkwaskid)
        # 故障代码

        if mcauthfield_faultcode["mcauthchange"]:

            # CharField

            ins_table_busi.faultcode = obj.get("faultcode")
        # 维护标志

        if mcauthfield_makwkwintenanceflag["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenanceflag = obj.get("makwkwintenanceflag")
        # 电量水平

        if mcauthfield_powerlevel["mcauthchange"]:

            # CharField

            ins_table_busi.powerlevel = obj.get("powerlevel")
        # 上次维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 关联工作站ID

        if mcauthfield_associatedwkwkworkstationid["mcauthchange"]:

            # SelectField

            ins_table_busi.associatedwkwkworkstationid = obj.get(
                "associatedwkwkworkstationid"
            )
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotstatus.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotstatus.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotstatus")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robottkwkwask(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人任务表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务名称

        mcauthfield_tkwkwaskname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 开始时间

        mcauthfield_starttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 结束时间

        mcauthfield_endtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务优先级

        mcauthfield_prikwkwority = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务详情

        mcauthfield_details = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 失败原因

        mcauthfield_failurerekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联流程ID

        mcauthfield_associatedprocessid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人任务表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务名称

        mcauthfield_tkwkwaskname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 开始时间

        mcauthfield_starttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 结束时间

        mcauthfield_endtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务优先级

        mcauthfield_prikwkwority = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 任务详情

        mcauthfield_details = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 失败原因

        mcauthfield_failurerekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联流程ID

        mcauthfield_associatedprocessid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robottkwkwask.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robottkwkwask().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robottkwkwask.objects.filter(**filter)
        else:
            records = mc_robottkwkwask.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_productionlkwkwineinfo_55606 = []
        for m in mc_productionlkwkwineinfo.objects.all():
            mobj = m.toJson()
            data_mc_productionlkwkwineinfo_55606.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("productionlkwkwinename"),
                }
            )
        return render(request, "config_busi/robottkwkwask.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robottkwkwask()

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.tkwkwaskid = str(uuid.uuid4())
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 任务名称

        if mcauthfield_tkwkwaskname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.tkwkwaskname = obj.get("tkwkwaskname")
        # 开始时间

        if mcauthfield_starttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.starttime = obj.get("starttime")
        # 结束时间

        if mcauthfield_endtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.endtime = obj.get("endtime")
        # 任务状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 任务优先级

        if mcauthfield_prikwkwority["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.prikwkwority = obj.get("prikwkwority")
        # 任务详情

        if mcauthfield_details["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.details = obj.get("details")
        # 失败原因

        if mcauthfield_failurerekwkwason["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.failurerekwkwason = obj.get("failurerekwkwason")
        # 关联流程ID

        if mcauthfield_associatedprocessid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.associatedprocessid = obj.get("associatedprocessid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robottkwkwask.objects.get(id=obj.get("_id_upd"))

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.tkwkwaskid = str(uuid.uuid4())

            ins_table_busi.tkwkwaskid = str(ins_table_busi.tkwkwaskid)
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 任务名称

        if mcauthfield_tkwkwaskname["mcauthchange"]:

            # CharField

            ins_table_busi.tkwkwaskname = obj.get("tkwkwaskname")
        # 开始时间

        if mcauthfield_starttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.starttime = obj.get("starttime")
        # 结束时间

        if mcauthfield_endtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.endtime = obj.get("endtime")
        # 任务状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 任务优先级

        if mcauthfield_prikwkwority["mcauthchange"]:

            # CharField

            ins_table_busi.prikwkwority = obj.get("prikwkwority")
        # 任务详情

        if mcauthfield_details["mcauthchange"]:

            # CharField

            ins_table_busi.details = obj.get("details")
        # 失败原因

        if mcauthfield_failurerekwkwason["mcauthchange"]:

            # CharField

            ins_table_busi.failurerekwkwason = obj.get("failurerekwkwason")
        # 关联流程ID

        if mcauthfield_associatedprocessid["mcauthchange"]:

            # SelectField

            ins_table_busi.associatedprocessid = obj.get("associatedprocessid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robottkwkwask.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robottkwkwask.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robottkwkwask")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_productionlkwkwineconfig(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 生产线配置表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 生产线ID

        mcauthfield_lkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线名称

        mcauthfield_lkwkwinename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 产能

        mcauthfield_capacity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_creationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后更新时间

        mcauthfield_lkwkwastupdatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人数量

        mcauthfield_robotcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护周期

        mcauthfield_makwkwintenancecycle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联工厂ID

        mcauthfield_associatedfactkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 生产线配置表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 生产线ID

        mcauthfield_lkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线名称

        mcauthfield_lkwkwinename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 产能

        mcauthfield_capacity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_creationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后更新时间

        mcauthfield_lkwkwastupdatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人数量

        mcauthfield_robotcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护周期

        mcauthfield_makwkwintenancecycle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联工厂ID

        mcauthfield_associatedfactkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_productionlkwkwineconfig.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_productionlkwkwineconfig().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_productionlkwkwineconfig.objects.filter(**filter)
        else:
            records = mc_productionlkwkwineconfig.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_productionlkwkwineinfo_55616 = []
        for m in mc_productionlkwkwineinfo.objects.all():
            mobj = m.toJson()
            data_mc_productionlkwkwineinfo_55616.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("productionlkwkwinename"),
                }
            )
        return render(request, "config_busi/productionlkwkwineconfig.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_productionlkwkwineconfig()

        # 生产线ID

        if mcauthfield_lkwkwineid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.lkwkwineid = str(uuid.uuid4())
        # 生产线名称

        if mcauthfield_lkwkwinename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.lkwkwinename = obj.get("lkwkwinename")
        # 生产线位置

        if mcauthfield_location["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.location = obj.get("location")
        # 产能

        if mcauthfield_capacity["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.capacity = obj.get("capacity")
        # 生产线状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_creationtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.creationtime = obj.get("creationtime")
        # 最后更新时间

        if mcauthfield_lkwkwastupdatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastupdatetime = obj.get("lkwkwastupdatetime")
        # 机器人数量

        if mcauthfield_robotcount["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.robotcount = obj.get("robotcount")
        # 维护周期

        if mcauthfield_makwkwintenancecycle["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenancecycle = obj.get("makwkwintenancecycle")
        # 关联工厂ID

        if mcauthfield_associatedfactkwkworyid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.associatedfactkwkworyid = obj.get("associatedfactkwkworyid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_productionlkwkwineconfig.objects.get(id=obj.get("_id_upd"))

        # 生产线ID

        if mcauthfield_lkwkwineid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.lkwkwineid = str(uuid.uuid4())

            ins_table_busi.lkwkwineid = str(ins_table_busi.lkwkwineid)
        # 生产线名称

        if mcauthfield_lkwkwinename["mcauthchange"]:

            # CharField

            ins_table_busi.lkwkwinename = obj.get("lkwkwinename")
        # 生产线位置

        if mcauthfield_location["mcauthchange"]:

            # CharField

            ins_table_busi.location = obj.get("location")
        # 产能

        if mcauthfield_capacity["mcauthchange"]:

            # CharField

            ins_table_busi.capacity = obj.get("capacity")
        # 生产线状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_creationtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.creationtime = obj.get("creationtime")
        # 最后更新时间

        if mcauthfield_lkwkwastupdatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastupdatetime = obj.get("lkwkwastupdatetime")
        # 机器人数量

        if mcauthfield_robotcount["mcauthchange"]:

            # IntegerField

            ins_table_busi.robotcount = obj.get("robotcount")
        # 维护周期

        if mcauthfield_makwkwintenancecycle["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenancecycle = obj.get("makwkwintenancecycle")
        # 关联工厂ID

        if mcauthfield_associatedfactkwkworyid["mcauthchange"]:

            # SelectField

            ins_table_busi.associatedfactkwkworyid = obj.get("associatedfactkwkworyid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_productionlkwkwineconfig.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_productionlkwkwineconfig.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/productionlkwkwineconfig")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_permkwkwissionmanagement(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 权限管理表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 权限ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限名称

        mcauthfield_permkwkwissionname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如启用禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联用户ID可选用于特定用户权限

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 系统模块如生产监控、设备控制等

        mcauthfield_systemmodule = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 权限管理表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 权限ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限名称

        mcauthfield_permkwkwissionname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如启用禁用

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联用户ID可选用于特定用户权限

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 系统模块如生产监控、设备控制等

        mcauthfield_systemmodule = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_permkwkwissionmanagement.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_permkwkwissionmanagement().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_permkwkwissionmanagement.objects.filter(**filter)
        else:
            records = mc_permkwkwissionmanagement.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_roleinfo_55623 = []
        for m in mc_roleinfo.objects.all():
            mobj = m.toJson()
            data_mc_roleinfo_55623.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("rolename"),
                }
            )
        data_mc_userinfo_55624 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_55624.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/permkwkwissionmanagement.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_permkwkwissionmanagement()

        # 权限ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 权限名称

        if mcauthfield_permkwkwissionname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.permkwkwissionname = obj.get("permkwkwissionname")
        # 权限描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdtime = obj.get("createdtime")
        # 更新时间

        if mcauthfield_updatedtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedtime = obj.get("updatedtime")
        # 状态如启用禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 关联角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.roleid = obj.get("roleid")
        # 关联用户ID可选用于特定用户权限

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 系统模块如生产监控、设备控制等

        if mcauthfield_systemmodule["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.systemmodule = obj.get("systemmodule")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_permkwkwissionmanagement.objects.get(id=obj.get("_id_upd"))

        # 权限ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 权限名称

        if mcauthfield_permkwkwissionname["mcauthchange"]:

            # CharField

            ins_table_busi.permkwkwissionname = obj.get("permkwkwissionname")
        # 权限描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdtime = obj.get("createdtime")
        # 更新时间

        if mcauthfield_updatedtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedtime = obj.get("updatedtime")
        # 状态如启用禁用

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 关联角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # SelectField

            ins_table_busi.roleid = obj.get("roleid")
        # 关联用户ID可选用于特定用户权限

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 系统模块如生产监控、设备控制等

        if mcauthfield_systemmodule["mcauthchange"]:

            # CharField

            ins_table_busi.systemmodule = obj.get("systemmodule")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_permkwkwissionmanagement.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_permkwkwissionmanagement.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/permkwkwissionmanagement")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_userinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户信息表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 密码

        mcauthfield_pkwkwasswkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电子邮箱

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电话号码

        mcauthfield_phonenumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后登录时间

        mcauthfield_lkwkwastlogkwkwintime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 用户信息表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 密码

        mcauthfield_pkwkwasswkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电子邮箱

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 电话号码

        mcauthfield_phonenumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后登录时间

        mcauthfield_lkwkwastlogkwkwintime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_userinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_userinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_userinfo.objects.filter(**filter)
        else:
            records = mc_userinfo.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/userinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_userinfo()

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        # 密码

        if mcauthfield_pkwkwasswkwkword["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.pkwkwasswkwkword = obj.get("pkwkwasswkwkword")
        # 电子邮箱

        if mcauthfield_email["mcauthchange"]:

            # EmailField # 其他情况/待补充

            ins_table_busi.email = obj.get("email")
        # 电话号码

        if mcauthfield_phonenumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.phonenumber = obj.get("phonenumber")
        # 角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.roleid = str(uuid.uuid4())
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 最后登录时间

        if mcauthfield_lkwkwastlogkwkwintime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastlogkwkwintime = obj.get("lkwkwastlogkwkwintime")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.departmentid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_userinfo.objects.get(id=obj.get("_id_upd"))

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        # 密码

        if mcauthfield_pkwkwasswkwkword["mcauthchange"]:

            # CharField

            ins_table_busi.pkwkwasswkwkword = obj.get("pkwkwasswkwkword")
        # 电子邮箱

        if mcauthfield_email["mcauthchange"]:

            # EmailField

            ins_table_busi.email = obj.get("email")
        # 电话号码

        if mcauthfield_phonenumber["mcauthchange"]:

            # CharField

            ins_table_busi.phonenumber = obj.get("phonenumber")
        # 角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.roleid = str(uuid.uuid4())

            ins_table_busi.roleid = str(ins_table_busi.roleid)
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 最后登录时间

        if mcauthfield_lkwkwastlogkwkwintime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastlogkwkwintime = obj.get("lkwkwastlogkwkwintime")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 部门ID

        if mcauthfield_departmentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.departmentid = str(uuid.uuid4())

            ins_table_busi.departmentid = str(ins_table_busi.departmentid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_userinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_userinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/userinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_roleinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 角色信息表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色名称

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色描述

        mcauthfield_roledescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储

        mcauthfield_permkwkwissionids = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID关联字段指向创建该角色的用户ID

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新者ID关联字段指向最后更新该角色的用户ID

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 角色信息表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 角色ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色名称

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色描述

        mcauthfield_roledescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储

        mcauthfield_permkwkwissionids = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID关联字段指向创建该角色的用户ID

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新者ID关联字段指向最后更新该角色的用户ID

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_roleinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_roleinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_roleinfo.objects.filter(**filter)
        else:
            records = mc_roleinfo.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_permkwkwissionmanagement_55642 = []
        for m in mc_permkwkwissionmanagement.objects.all():
            mobj = m.toJson()
            data_mc_permkwkwissionmanagement_55642.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("permkwkwissionname"),
                }
            )
        data_mc_userinfo_55643 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_55643.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_userinfo_55644 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_55644.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/roleinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_roleinfo()

        # 角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.roleid = str(uuid.uuid4())
        # 角色名称

        if mcauthfield_rolename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rolename = obj.get("rolename")
        # 角色描述

        if mcauthfield_roledescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.roledescription = obj.get("roledescription")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储

        if mcauthfield_permkwkwissionids["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.permkwkwissionids = obj.get("permkwkwissionids")
        # 创建者ID关联字段指向创建该角色的用户ID

        if mcauthfield_createdby["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.createdby = obj.get("createdby")
        # 更新者ID关联字段指向最后更新该角色的用户ID

        if mcauthfield_updatedby["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.updatedby = obj.get("updatedby")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_roleinfo.objects.get(id=obj.get("_id_upd"))

        # 角色ID

        if mcauthfield_roleid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.roleid = str(uuid.uuid4())

            ins_table_busi.roleid = str(ins_table_busi.roleid)
        # 角色名称

        if mcauthfield_rolename["mcauthchange"]:

            # CharField

            ins_table_busi.rolename = obj.get("rolename")
        # 角色描述

        if mcauthfield_roledescription["mcauthchange"]:

            # TextField

            ins_table_busi.roledescription = obj.get("roledescription")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储

        if mcauthfield_permkwkwissionids["mcauthchange"]:

            # SelectField

            ins_table_busi.permkwkwissionids = obj.get("permkwkwissionids")
        # 创建者ID关联字段指向创建该角色的用户ID

        if mcauthfield_createdby["mcauthchange"]:

            # SelectField

            ins_table_busi.createdby = obj.get("createdby")
        # 更新者ID关联字段指向最后更新该角色的用户ID

        if mcauthfield_updatedby["mcauthchange"]:

            # SelectField

            ins_table_busi.updatedby = obj.get("updatedby")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_roleinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_roleinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/roleinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_userrolerelation(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户角色关联表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色名

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联ID

        mcauthfield_relationid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制用户角色关系的有效性

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新者ID

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色ID关联到角色的ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 用户角色关联表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色名

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联ID

        mcauthfield_relationid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活用于控制用户角色关系的有效性

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者ID

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新者ID

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 角色ID关联到角色的ID

        mcauthfield_roleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_userrolerelation.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_userrolerelation().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_userrolerelation.objects.filter(**filter)
        else:
            records = mc_userrolerelation.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userrolerelation_55647 = []
        for m in mc_userrolerelation.objects.all():
            mobj = m.toJson()
            data_mc_userrolerelation_55647.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("relationid"),
                }
            )
        data_mc_roleinfo_55653 = []
        for m in mc_roleinfo.objects.all():
            mobj = m.toJson()
            data_mc_roleinfo_55653.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("rolename"),
                }
            )
        return render(request, "config_busi/userrolerelation.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_userrolerelation()

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 角色名

        if mcauthfield_rolename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rolename = obj.get("rolename")
        # 关联ID

        if mcauthfield_relationid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relationid = obj.get("relationid")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活用于控制用户角色关系的有效性

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 创建者ID

        if mcauthfield_createdby["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.createdby = str(uuid.uuid4())
        # 更新者ID

        if mcauthfield_updatedby["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.updatedby = str(uuid.uuid4())
        # 角色ID关联到角色的ID

        if mcauthfield_roleid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.roleid = obj.get("roleid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_userrolerelation.objects.get(id=obj.get("_id_upd"))

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 角色名

        if mcauthfield_rolename["mcauthchange"]:

            # CharField

            ins_table_busi.rolename = obj.get("rolename")
        # 关联ID

        if mcauthfield_relationid["mcauthchange"]:

            # SelectField

            ins_table_busi.relationid = obj.get("relationid")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活用于控制用户角色关系的有效性

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 创建者ID

        if mcauthfield_createdby["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.createdby = str(uuid.uuid4())

            ins_table_busi.createdby = str(ins_table_busi.createdby)
        # 更新者ID

        if mcauthfield_updatedby["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.updatedby = str(uuid.uuid4())

            ins_table_busi.updatedby = str(ins_table_busi.updatedby)
        # 角色ID关联到角色的ID

        if mcauthfield_roleid["mcauthchange"]:

            # SelectField

            ins_table_busi.roleid = obj.get("roleid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_userrolerelation.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_userrolerelation.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/userrolerelation")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotfault(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人故障表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 故障ID

        mcauthfield_faultid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障类型

        mcauthfield_faulttype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障描述

        mcauthfield_faultdescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障时间

        mcauthfield_faulttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修状态

        mcauthfield_repairstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修时间

        mcauthfield_repairtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修人员

        mcauthfield_repairperson = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障严重程度

        mcauthfield_faultseverity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联组件

        mcauthfield_relatedcomponent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人故障表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 故障ID

        mcauthfield_faultid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障类型

        mcauthfield_faulttype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障描述

        mcauthfield_faultdescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障时间

        mcauthfield_faulttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修状态

        mcauthfield_repairstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修时间

        mcauthfield_repairtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修人员

        mcauthfield_repairperson = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障严重程度

        mcauthfield_faultseverity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联组件

        mcauthfield_relatedcomponent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotfault.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotfault().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotfault.objects.filter(**filter)
        else:
            records = mc_robotfault.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_robotfault_55663 = []
        for m in mc_robotfault.objects.all():
            mobj = m.toJson()
            data_mc_robotfault_55663.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("relatedcomponent"),
                }
            )
        return render(request, "config_busi/robotfault.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotfault()

        # 故障ID

        if mcauthfield_faultid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.faultid = str(uuid.uuid4())
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 故障类型

        if mcauthfield_faulttype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.faulttype = obj.get("faulttype")
        # 故障描述

        if mcauthfield_faultdescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.faultdescription = obj.get("faultdescription")
        # 故障时间

        if mcauthfield_faulttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.faulttime = obj.get("faulttime")
        # 维修状态

        if mcauthfield_repairstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repairstatus = obj.get("repairstatus")
        # 维修时间

        if mcauthfield_repairtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.repairtime = obj.get("repairtime")
        # 维修人员

        if mcauthfield_repairperson["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repairperson = obj.get("repairperson")
        # 故障严重程度

        if mcauthfield_faultseverity["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.faultseverity = obj.get("faultseverity")
        # 关联组件

        if mcauthfield_relatedcomponent["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relatedcomponent = obj.get("relatedcomponent")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotfault.objects.get(id=obj.get("_id_upd"))

        # 故障ID

        if mcauthfield_faultid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.faultid = str(uuid.uuid4())

            ins_table_busi.faultid = str(ins_table_busi.faultid)
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 故障类型

        if mcauthfield_faulttype["mcauthchange"]:

            # CharField

            ins_table_busi.faulttype = obj.get("faulttype")
        # 故障描述

        if mcauthfield_faultdescription["mcauthchange"]:

            # TextField

            ins_table_busi.faultdescription = obj.get("faultdescription")
        # 故障时间

        if mcauthfield_faulttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.faulttime = obj.get("faulttime")
        # 维修状态

        if mcauthfield_repairstatus["mcauthchange"]:

            # CharField

            ins_table_busi.repairstatus = obj.get("repairstatus")
        # 维修时间

        if mcauthfield_repairtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.repairtime = obj.get("repairtime")
        # 维修人员

        if mcauthfield_repairperson["mcauthchange"]:

            # CharField

            ins_table_busi.repairperson = obj.get("repairperson")
        # 故障严重程度

        if mcauthfield_faultseverity["mcauthchange"]:

            # CharField

            ins_table_busi.faultseverity = obj.get("faultseverity")
        # 关联组件

        if mcauthfield_relatedcomponent["mcauthchange"]:

            # SelectField

            ins_table_busi.relatedcomponent = obj.get("relatedcomponent")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotfault.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotfault.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotfault")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_makwkwintenancereckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 维修记录表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 记录ID

        mcauthfield_reckwkwordid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修日期

        mcauthfield_makwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修类型

        mcauthfield_makwkwintenancetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 问题描述

        mcauthfield_problemdescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修状态

        mcauthfield_repairstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 技术员ID

        mcauthfield_technicianid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修费用

        mcauthfield_repaircost = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修时长

        mcauthfield_repairduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 相关部件

        mcauthfield_relatedparts = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 维修记录表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 记录ID

        mcauthfield_reckwkwordid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修日期

        mcauthfield_makwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修类型

        mcauthfield_makwkwintenancetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 问题描述

        mcauthfield_problemdescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修状态

        mcauthfield_repairstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 技术员ID

        mcauthfield_technicianid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修费用

        mcauthfield_repaircost = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修时长

        mcauthfield_repairduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 相关部件

        mcauthfield_relatedparts = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_makwkwintenancereckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_makwkwintenancereckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_makwkwintenancereckwkword.objects.filter(**filter)
        else:
            records = mc_makwkwintenancereckwkword.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/makwkwintenancereckwkword.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_makwkwintenancereckwkword()

        # 记录ID

        if mcauthfield_reckwkwordid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.reckwkwordid = str(uuid.uuid4())
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 维修日期

        if mcauthfield_makwkwintenancedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.makwkwintenancedate = obj.get("makwkwintenancedate")
        # 维修类型

        if mcauthfield_makwkwintenancetype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenancetype = obj.get("makwkwintenancetype")
        # 问题描述

        if mcauthfield_problemdescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.problemdescription = obj.get("problemdescription")
        # 维修状态

        if mcauthfield_repairstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repairstatus = obj.get("repairstatus")
        # 技术员ID

        if mcauthfield_technicianid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.technicianid = str(uuid.uuid4())
        # 维修费用

        if mcauthfield_repaircost["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repaircost = obj.get("repaircost")
        # 维修时长

        if mcauthfield_repairduration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repairduration = obj.get("repairduration")
        # 相关部件

        if mcauthfield_relatedparts["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.relatedparts = obj.get("relatedparts")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_makwkwintenancereckwkword.objects.get(id=obj.get("_id_upd"))

        # 记录ID

        if mcauthfield_reckwkwordid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.reckwkwordid = str(uuid.uuid4())

            ins_table_busi.reckwkwordid = str(ins_table_busi.reckwkwordid)
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 维修日期

        if mcauthfield_makwkwintenancedate["mcauthchange"]:

            # DateField

            ins_table_busi.makwkwintenancedate = obj.get("makwkwintenancedate")
        # 维修类型

        if mcauthfield_makwkwintenancetype["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenancetype = obj.get("makwkwintenancetype")
        # 问题描述

        if mcauthfield_problemdescription["mcauthchange"]:

            # TextField

            ins_table_busi.problemdescription = obj.get("problemdescription")
        # 维修状态

        if mcauthfield_repairstatus["mcauthchange"]:

            # CharField

            ins_table_busi.repairstatus = obj.get("repairstatus")
        # 技术员ID

        if mcauthfield_technicianid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.technicianid = str(uuid.uuid4())

            ins_table_busi.technicianid = str(ins_table_busi.technicianid)
        # 维修费用

        if mcauthfield_repaircost["mcauthchange"]:

            # CharField

            ins_table_busi.repaircost = obj.get("repaircost")
        # 维修时长

        if mcauthfield_repairduration["mcauthchange"]:

            # CharField

            ins_table_busi.repairduration = obj.get("repairduration")
        # 相关部件

        if mcauthfield_relatedparts["mcauthchange"]:

            # CharField

            ins_table_busi.relatedparts = obj.get("relatedparts")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_makwkwintenancereckwkword.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_makwkwintenancereckwkword.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/makwkwintenancereckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotmokwkwdel(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人型号表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 机器人型号ID

        mcauthfield_robotmokwkwdelid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人型号名称

        mcauthfield_mokwkwdelname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 制造商

        mcauthfield_manufacturer = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产年份

        mcauthfield_productionyear = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大负载能力

        mcauthfield_maxpayload = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 工作电压

        mcauthfield_operatkwkwingvoltage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 连接类型

        mcauthfield_connectivitytype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 安全认证

        mcauthfield_safetycertkwkwification = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护周期

        mcauthfield_makwkwintenanceinterval = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 相关组件ID关联字段指向其他如组件

        mcauthfield_relatedcomponentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人型号表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 机器人型号ID

        mcauthfield_robotmokwkwdelid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人型号名称

        mcauthfield_mokwkwdelname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 制造商

        mcauthfield_manufacturer = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产年份

        mcauthfield_productionyear = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最大负载能力

        mcauthfield_maxpayload = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 工作电压

        mcauthfield_operatkwkwingvoltage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 连接类型

        mcauthfield_connectivitytype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 安全认证

        mcauthfield_safetycertkwkwification = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护周期

        mcauthfield_makwkwintenanceinterval = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 相关组件ID关联字段指向其他如组件

        mcauthfield_relatedcomponentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotmokwkwdel.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotmokwkwdel().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotmokwkwdel.objects.filter(**filter)
        else:
            records = mc_robotmokwkwdel.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_robotmokwkwdel_55683 = []
        for m in mc_robotmokwkwdel.objects.all():
            mobj = m.toJson()
            data_mc_robotmokwkwdel_55683.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("relatedcomponentid"),
                }
            )
        return render(request, "config_busi/robotmokwkwdel.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotmokwkwdel()

        # 机器人型号ID

        if mcauthfield_robotmokwkwdelid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotmokwkwdelid = str(uuid.uuid4())
        # 机器人型号名称

        if mcauthfield_mokwkwdelname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.mokwkwdelname = obj.get("mokwkwdelname")
        # 制造商

        if mcauthfield_manufacturer["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.manufacturer = obj.get("manufacturer")
        # 生产年份

        if mcauthfield_productionyear["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.productionyear = obj.get("productionyear")
        # 最大负载能力

        if mcauthfield_maxpayload["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.maxpayload = obj.get("maxpayload")
        # 工作电压

        if mcauthfield_operatkwkwingvoltage["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.operatkwkwingvoltage = obj.get("operatkwkwingvoltage")
        # 连接类型

        if mcauthfield_connectivitytype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.connectivitytype = obj.get("connectivitytype")
        # 安全认证

        if mcauthfield_safetycertkwkwification["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.safetycertkwkwification = obj.get("safetycertkwkwification")
        # 维护周期

        if mcauthfield_makwkwintenanceinterval["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenanceinterval = obj.get("makwkwintenanceinterval")
        # 相关组件ID关联字段指向其他如组件

        if mcauthfield_relatedcomponentid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relatedcomponentid = obj.get("relatedcomponentid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotmokwkwdel.objects.get(id=obj.get("_id_upd"))

        # 机器人型号ID

        if mcauthfield_robotmokwkwdelid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotmokwkwdelid = str(uuid.uuid4())

            ins_table_busi.robotmokwkwdelid = str(ins_table_busi.robotmokwkwdelid)
        # 机器人型号名称

        if mcauthfield_mokwkwdelname["mcauthchange"]:

            # CharField

            ins_table_busi.mokwkwdelname = obj.get("mokwkwdelname")
        # 制造商

        if mcauthfield_manufacturer["mcauthchange"]:

            # CharField

            ins_table_busi.manufacturer = obj.get("manufacturer")
        # 生产年份

        if mcauthfield_productionyear["mcauthchange"]:

            # CharField

            ins_table_busi.productionyear = obj.get("productionyear")
        # 最大负载能力

        if mcauthfield_maxpayload["mcauthchange"]:

            # CharField

            ins_table_busi.maxpayload = obj.get("maxpayload")
        # 工作电压

        if mcauthfield_operatkwkwingvoltage["mcauthchange"]:

            # CharField

            ins_table_busi.operatkwkwingvoltage = obj.get("operatkwkwingvoltage")
        # 连接类型

        if mcauthfield_connectivitytype["mcauthchange"]:

            # CharField

            ins_table_busi.connectivitytype = obj.get("connectivitytype")
        # 安全认证

        if mcauthfield_safetycertkwkwification["mcauthchange"]:

            # CharField

            ins_table_busi.safetycertkwkwification = obj.get("safetycertkwkwification")
        # 维护周期

        if mcauthfield_makwkwintenanceinterval["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenanceinterval = obj.get("makwkwintenanceinterval")
        # 相关组件ID关联字段指向其他如组件

        if mcauthfield_relatedcomponentid["mcauthchange"]:

            # SelectField

            ins_table_busi.relatedcomponentid = obj.get("relatedcomponentid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotmokwkwdel.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotmokwkwdel.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotmokwkwdel")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_senskwkworinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 传感器信息表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 传感器ID

        mcauthfield_senskwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 传感器名称

        mcauthfield_senskwkworname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 传感器类型

        mcauthfield_senskwkwortype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后更新时间

        mcauthfield_lkwkwastupdatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 测量值

        mcauthfield_mekwkwasurementvalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 单位

        mcauthfield_unit = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警阈值

        mcauthfield_alarmthreshold = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联机器人ID

        mcauthfield_associatedrobotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 传感器信息表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 传感器ID

        mcauthfield_senskwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 传感器名称

        mcauthfield_senskwkworname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 传感器类型

        mcauthfield_senskwkwortype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后更新时间

        mcauthfield_lkwkwastupdatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 测量值

        mcauthfield_mekwkwasurementvalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 单位

        mcauthfield_unit = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警阈值

        mcauthfield_alarmthreshold = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联机器人ID

        mcauthfield_associatedrobotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_senskwkworinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_senskwkworinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_senskwkworinfo.objects.filter(**filter)
        else:
            records = mc_senskwkworinfo.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_robotinfo_55693 = []
        for m in mc_robotinfo.objects.all():
            mobj = m.toJson()
            data_mc_robotinfo_55693.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("mokwkwdelname"),
                }
            )
        return render(request, "config_busi/senskwkworinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_senskwkworinfo()

        # 传感器ID

        if mcauthfield_senskwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.senskwkworid = str(uuid.uuid4())
        # 传感器名称

        if mcauthfield_senskwkworname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.senskwkworname = obj.get("senskwkworname")
        # 传感器类型

        if mcauthfield_senskwkwortype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.senskwkwortype = obj.get("senskwkwortype")
        # 位置

        if mcauthfield_location["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.location = obj.get("location")
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 最后更新时间

        if mcauthfield_lkwkwastupdatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastupdatetime = obj.get("lkwkwastupdatetime")
        # 测量值

        if mcauthfield_mekwkwasurementvalue["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.mekwkwasurementvalue = obj.get("mekwkwasurementvalue")
        # 单位

        if mcauthfield_unit["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.unit = obj.get("unit")
        # 报警阈值

        if mcauthfield_alarmthreshold["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.alarmthreshold = obj.get("alarmthreshold")
        # 关联机器人ID

        if mcauthfield_associatedrobotid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.associatedrobotid = obj.get("associatedrobotid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_senskwkworinfo.objects.get(id=obj.get("_id_upd"))

        # 传感器ID

        if mcauthfield_senskwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.senskwkworid = str(uuid.uuid4())

            ins_table_busi.senskwkworid = str(ins_table_busi.senskwkworid)
        # 传感器名称

        if mcauthfield_senskwkworname["mcauthchange"]:

            # CharField

            ins_table_busi.senskwkworname = obj.get("senskwkworname")
        # 传感器类型

        if mcauthfield_senskwkwortype["mcauthchange"]:

            # CharField

            ins_table_busi.senskwkwortype = obj.get("senskwkwortype")
        # 位置

        if mcauthfield_location["mcauthchange"]:

            # CharField

            ins_table_busi.location = obj.get("location")
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 最后更新时间

        if mcauthfield_lkwkwastupdatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastupdatetime = obj.get("lkwkwastupdatetime")
        # 测量值

        if mcauthfield_mekwkwasurementvalue["mcauthchange"]:

            # CharField

            ins_table_busi.mekwkwasurementvalue = obj.get("mekwkwasurementvalue")
        # 单位

        if mcauthfield_unit["mcauthchange"]:

            # CharField

            ins_table_busi.unit = obj.get("unit")
        # 报警阈值

        if mcauthfield_alarmthreshold["mcauthchange"]:

            # CharField

            ins_table_busi.alarmthreshold = obj.get("alarmthreshold")
        # 关联机器人ID

        if mcauthfield_associatedrobotid["mcauthchange"]:

            # SelectField

            ins_table_busi.associatedrobotid = obj.get("associatedrobotid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_senskwkworinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_senskwkworinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/senskwkworinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_senskwkwordata(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 传感器数据表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 传感器ID

        mcauthfield_senskwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 时间戳

        mcauthfield_timestamp = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 温度

        mcauthfield_temperature = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 湿度

        mcauthfield_humidity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 压力

        mcauthfield_pressure = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 振动强度

        mcauthfield_vibration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如正常、异常

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 设备ID关联字段指向产生数据的设备

        mcauthfield_deviceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 传感器数据表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 传感器ID

        mcauthfield_senskwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 时间戳

        mcauthfield_timestamp = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 温度

        mcauthfield_temperature = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 湿度

        mcauthfield_humidity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 压力

        mcauthfield_pressure = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 振动强度

        mcauthfield_vibration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如正常、异常

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 设备ID关联字段指向产生数据的设备

        mcauthfield_deviceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_senskwkwordata.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_senskwkwordata().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_senskwkwordata.objects.filter(**filter)
        else:
            records = mc_senskwkwordata.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_senskwkworinfo_55702 = []
        for m in mc_senskwkworinfo.objects.all():
            mobj = m.toJson()
            data_mc_senskwkworinfo_55702.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("senskwkworname"),
                }
            )
        return render(request, "config_busi/senskwkwordata.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_senskwkwordata()

        # 传感器ID

        if mcauthfield_senskwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.senskwkworid = str(uuid.uuid4())
        # 时间戳

        if mcauthfield_timestamp["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.timestamp = obj.get("timestamp")
        # 温度

        if mcauthfield_temperature["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.temperature = obj.get("temperature")
        # 湿度

        if mcauthfield_humidity["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.humidity = obj.get("humidity")
        # 压力

        if mcauthfield_pressure["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.pressure = obj.get("pressure")
        # 振动强度

        if mcauthfield_vibration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.vibration = obj.get("vibration")
        # 状态如正常、异常

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 位置

        if mcauthfield_location["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.location = obj.get("location")
        # 设备ID关联字段指向产生数据的设备

        if mcauthfield_deviceid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.deviceid = obj.get("deviceid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_senskwkwordata.objects.get(id=obj.get("_id_upd"))

        # 传感器ID

        if mcauthfield_senskwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.senskwkworid = str(uuid.uuid4())

            ins_table_busi.senskwkworid = str(ins_table_busi.senskwkworid)
        # 时间戳

        if mcauthfield_timestamp["mcauthchange"]:

            # DateTimeField

            ins_table_busi.timestamp = obj.get("timestamp")
        # 温度

        if mcauthfield_temperature["mcauthchange"]:

            # CharField

            ins_table_busi.temperature = obj.get("temperature")
        # 湿度

        if mcauthfield_humidity["mcauthchange"]:

            # CharField

            ins_table_busi.humidity = obj.get("humidity")
        # 压力

        if mcauthfield_pressure["mcauthchange"]:

            # CharField

            ins_table_busi.pressure = obj.get("pressure")
        # 振动强度

        if mcauthfield_vibration["mcauthchange"]:

            # CharField

            ins_table_busi.vibration = obj.get("vibration")
        # 状态如正常、异常

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 位置

        if mcauthfield_location["mcauthchange"]:

            # CharField

            ins_table_busi.location = obj.get("location")
        # 设备ID关联字段指向产生数据的设备

        if mcauthfield_deviceid["mcauthchange"]:

            # SelectField

            ins_table_busi.deviceid = obj.get("deviceid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_senskwkwordata.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_senskwkwordata.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/senskwkwordata")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_camerainfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 监控摄像头信息表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 摄像头ID

        mcauthfield_cameraid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 摄像头名称

        mcauthfield_cameraname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 安装位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 地址

        mcauthfield_ipaddressip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 端口号

        mcauthfield_pkwkwortnumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 分辨率

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如在线、离线

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后检查时间

        mcauthfield_lkwkwastchecktime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 连接机器人ID关联字段指向机器人信息

        mcauthfield_connectedrobotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 监控摄像头信息表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 摄像头ID

        mcauthfield_cameraid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 摄像头名称

        mcauthfield_cameraname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 安装位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 地址

        mcauthfield_ipaddressip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 端口号

        mcauthfield_pkwkwortnumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 分辨率

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 状态如在线、离线

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后检查时间

        mcauthfield_lkwkwastchecktime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 连接机器人ID关联字段指向机器人信息

        mcauthfield_connectedrobotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_camerainfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_camerainfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_camerainfo.objects.filter(**filter)
        else:
            records = mc_camerainfo.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_robotinfo_55711 = []
        for m in mc_robotinfo.objects.all():
            mobj = m.toJson()
            data_mc_robotinfo_55711.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("robotname"),
                }
            )
        return render(request, "config_busi/camerainfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_camerainfo()

        # 摄像头ID

        if mcauthfield_cameraid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.cameraid = str(uuid.uuid4())
        # 摄像头名称

        if mcauthfield_cameraname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.cameraname = obj.get("cameraname")
        # 安装位置

        if mcauthfield_location["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.location = obj.get("location")
        # 地址

        if mcauthfield_ipaddressip["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.ipaddressip = obj.get("ipaddressip")
        # 端口号

        if mcauthfield_pkwkwortnumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.pkwkwortnumber = obj.get("pkwkwortnumber")
        # 分辨率

        if mcauthfield_resolution["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.resolution = obj.get("resolution")
        # 状态如在线、离线

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 最后检查时间

        if mcauthfield_lkwkwastchecktime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastchecktime = obj.get("lkwkwastchecktime")
        # 连接机器人ID关联字段指向机器人信息

        if mcauthfield_connectedrobotid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.connectedrobotid = obj.get("connectedrobotid")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_camerainfo.objects.get(id=obj.get("_id_upd"))

        # 摄像头ID

        if mcauthfield_cameraid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.cameraid = str(uuid.uuid4())

            ins_table_busi.cameraid = str(ins_table_busi.cameraid)
        # 摄像头名称

        if mcauthfield_cameraname["mcauthchange"]:

            # CharField

            ins_table_busi.cameraname = obj.get("cameraname")
        # 安装位置

        if mcauthfield_location["mcauthchange"]:

            # CharField

            ins_table_busi.location = obj.get("location")
        # 地址

        if mcauthfield_ipaddressip["mcauthchange"]:

            # TextField

            ins_table_busi.ipaddressip = obj.get("ipaddressip")
        # 端口号

        if mcauthfield_pkwkwortnumber["mcauthchange"]:

            # CharField

            ins_table_busi.pkwkwortnumber = obj.get("pkwkwortnumber")
        # 分辨率

        if mcauthfield_resolution["mcauthchange"]:

            # CharField

            ins_table_busi.resolution = obj.get("resolution")
        # 状态如在线、离线

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 最后检查时间

        if mcauthfield_lkwkwastchecktime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastchecktime = obj.get("lkwkwastchecktime")
        # 连接机器人ID关联字段指向机器人信息

        if mcauthfield_connectedrobotid["mcauthchange"]:

            # SelectField

            ins_table_busi.connectedrobotid = obj.get("connectedrobotid")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_camerainfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_camerainfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/camerainfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videoreckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频录像表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 视频文件路径

        mcauthfield_videofilepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 录像开始时间

        mcauthfield_reckwkwordkwkwingstarttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 录像结束时间

        mcauthfield_reckwkwordkwkwingendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 摄像头ID关联摄像头信息

        mcauthfield_cameraid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID关联机器人信息

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 录像状态如正常、异常、删除

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 录像分辨率

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 录像时长秒

        mcauthfield_duration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 视频录像表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 视频文件路径

        mcauthfield_videofilepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 录像开始时间

        mcauthfield_reckwkwordkwkwingstarttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 录像结束时间

        mcauthfield_reckwkwordkwkwingendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 摄像头ID关联摄像头信息

        mcauthfield_cameraid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID关联机器人信息

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 录像状态如正常、异常、删除

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 录像分辨率

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 录像时长秒

        mcauthfield_duration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoreckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoreckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoreckwkword.objects.filter(**filter)
        else:
            records = mc_videoreckwkword.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_camerainfo_55717 = []
        for m in mc_camerainfo.objects.all():
            mobj = m.toJson()
            data_mc_camerainfo_55717.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("location"),
                }
            )
        data_mc_robotinfo_55718 = []
        for m in mc_robotinfo.objects.all():
            mobj = m.toJson()
            data_mc_robotinfo_55718.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("robotname"),
                }
            )
        return render(request, "config_busi/videoreckwkword.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoreckwkword()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 视频文件路径

        if mcauthfield_videofilepath["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "videofilepath" in request.FILES:
                ins_table_busi.videofilepath = request.FILES["videofilepath"]
        # 录像开始时间

        if mcauthfield_reckwkwordkwkwingstarttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.reckwkwordkwkwingstarttime = obj.get(
                "reckwkwordkwkwingstarttime"
            )
        # 录像结束时间

        if mcauthfield_reckwkwordkwkwingendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.reckwkwordkwkwingendtime = obj.get(
                "reckwkwordkwkwingendtime"
            )
        # 摄像头ID关联摄像头信息

        if mcauthfield_cameraid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.cameraid = obj.get("cameraid")
        # 机器人ID关联机器人信息

        if mcauthfield_robotid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.robotid = obj.get("robotid")
        # 录像状态如正常、异常、删除

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 录像分辨率

        if mcauthfield_resolution["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.resolution = obj.get("resolution")
        # 录像时长秒

        if mcauthfield_duration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.duration = obj.get("duration")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoreckwkword.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 视频文件路径

        if mcauthfield_videofilepath["mcauthchange"]:

            # Save File FileField

            if "videofilepath" in request.FILES:
                ins_table_busi.videofilepath = request.FILES["videofilepath"]
        # 录像开始时间

        if mcauthfield_reckwkwordkwkwingstarttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.reckwkwordkwkwingstarttime = obj.get(
                "reckwkwordkwkwingstarttime"
            )
        # 录像结束时间

        if mcauthfield_reckwkwordkwkwingendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.reckwkwordkwkwingendtime = obj.get(
                "reckwkwordkwkwingendtime"
            )
        # 摄像头ID关联摄像头信息

        if mcauthfield_cameraid["mcauthchange"]:

            # SelectField

            ins_table_busi.cameraid = obj.get("cameraid")
        # 机器人ID关联机器人信息

        if mcauthfield_robotid["mcauthchange"]:

            # SelectField

            ins_table_busi.robotid = obj.get("robotid")
        # 录像状态如正常、异常、删除

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 录像分辨率

        if mcauthfield_resolution["mcauthchange"]:

            # CharField

            ins_table_busi.resolution = obj.get("resolution")
        # 录像时长秒

        if mcauthfield_duration["mcauthchange"]:

            # CharField

            ins_table_busi.duration = obj.get("duration")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoreckwkword.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoreckwkword.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoreckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotoperationlog(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人操作日志表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 日志ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作时间

        mcauthfield_operationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作类型

        mcauthfield_operationtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作结果

        mcauthfield_operationresult = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作员ID

        mcauthfield_operatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误代码

        mcauthfield_errkwkworcode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线ID

        mcauthfield_machkwkwinelkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人操作日志表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 日志ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作时间

        mcauthfield_operationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作类型

        mcauthfield_operationtype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作结果

        mcauthfield_operationresult = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作员ID

        mcauthfield_operatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误代码

        mcauthfield_errkwkworcode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 错误信息

        mcauthfield_errkwkwormessage = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线ID

        mcauthfield_machkwkwinelkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotoperationlog.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotoperationlog().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotoperationlog.objects.filter(**filter)
        else:
            records = mc_robotoperationlog.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/robotoperationlog.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotoperationlog()

        # 日志ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 操作时间

        if mcauthfield_operationtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.operationtime = obj.get("operationtime")
        # 操作类型

        if mcauthfield_operationtype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.operationtype = obj.get("operationtype")
        # 操作结果

        if mcauthfield_operationresult["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.operationresult = obj.get("operationresult")
        # 操作员ID

        if mcauthfield_operatkwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.operatkwkworid = str(uuid.uuid4())
        # 错误代码

        if mcauthfield_errkwkworcode["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.errkwkworcode = obj.get("errkwkworcode")
        # 错误信息

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        # 生产线ID

        if mcauthfield_machkwkwinelkwkwineid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.machkwkwinelkwkwineid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotoperationlog.objects.get(id=obj.get("_id_upd"))

        # 日志ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 操作时间

        if mcauthfield_operationtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.operationtime = obj.get("operationtime")
        # 操作类型

        if mcauthfield_operationtype["mcauthchange"]:

            # CharField

            ins_table_busi.operationtype = obj.get("operationtype")
        # 操作结果

        if mcauthfield_operationresult["mcauthchange"]:

            # CharField

            ins_table_busi.operationresult = obj.get("operationresult")
        # 操作员ID

        if mcauthfield_operatkwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.operatkwkworid = str(uuid.uuid4())

            ins_table_busi.operatkwkworid = str(ins_table_busi.operatkwkworid)
        # 错误代码

        if mcauthfield_errkwkworcode["mcauthchange"]:

            # CharField

            ins_table_busi.errkwkworcode = obj.get("errkwkworcode")
        # 错误信息

        if mcauthfield_errkwkwormessage["mcauthchange"]:

            # CharField

            ins_table_busi.errkwkwormessage = obj.get("errkwkwormessage")
        # 生产线ID

        if mcauthfield_machkwkwinelkwkwineid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.machkwkwinelkwkwineid = str(uuid.uuid4())

            ins_table_busi.machkwkwinelkwkwineid = str(
                ins_table_busi.machkwkwinelkwkwineid
            )
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotoperationlog.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotoperationlog.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotoperationlog")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_productionlkwkwineefficiency(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 生产线效率统计表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 生产线ID

        mcauthfield_lkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 效率率

        mcauthfield_efficiencyrate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 日产量

        mcauthfield_dailyoutput = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 停机时间小时

        mcauthfield_downtimehours = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护频率

        mcauthfield_makwkwintenancefrequency = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人数量

        mcauthfield_robotcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作人员数量

        mcauthfield_operatkwkworcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 产品缺陷率

        mcauthfield_productdefectrate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联车间ID

        mcauthfield_kwkwassociatedwkwkworkshopid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 生产线效率统计表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 生产线ID

        mcauthfield_lkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 效率率

        mcauthfield_efficiencyrate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 日产量

        mcauthfield_dailyoutput = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 停机时间小时

        mcauthfield_downtimehours = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护频率

        mcauthfield_makwkwintenancefrequency = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人数量

        mcauthfield_robotcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作人员数量

        mcauthfield_operatkwkworcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 产品缺陷率

        mcauthfield_productdefectrate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联车间ID

        mcauthfield_kwkwassociatedwkwkworkshopid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_productionlkwkwineefficiency.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_productionlkwkwineefficiency().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_productionlkwkwineefficiency.objects.filter(**filter)
        else:
            records = mc_productionlkwkwineefficiency.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_productionlkwkwineinfo_55741 = []
        for m in mc_productionlkwkwineinfo.objects.all():
            mobj = m.toJson()
            data_mc_productionlkwkwineinfo_55741.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("productionlkwkwinename"),
                }
            )
        return render(
            request, "config_busi/productionlkwkwineefficiency.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_productionlkwkwineefficiency()

        # 生产线ID

        if mcauthfield_lkwkwineid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.lkwkwineid = str(uuid.uuid4())
        # 效率率

        if mcauthfield_efficiencyrate["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.efficiencyrate = obj.get("efficiencyrate")
        # 日产量

        if mcauthfield_dailyoutput["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.dailyoutput = obj.get("dailyoutput")
        # 停机时间小时

        if mcauthfield_downtimehours["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.downtimehours = obj.get("downtimehours")
        # 维护频率

        if mcauthfield_makwkwintenancefrequency["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenancefrequency = obj.get(
                "makwkwintenancefrequency"
            )
        # 上次维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 机器人数量

        if mcauthfield_robotcount["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.robotcount = obj.get("robotcount")
        # 操作人员数量

        if mcauthfield_operatkwkworcount["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.operatkwkworcount = obj.get("operatkwkworcount")
        # 产品缺陷率

        if mcauthfield_productdefectrate["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.productdefectrate = obj.get("productdefectrate")
        # 关联车间ID

        if mcauthfield_kwkwassociatedwkwkworkshopid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.kwkwassociatedwkwkworkshopid = obj.get(
                "kwkwassociatedwkwkworkshopid"
            )
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_productionlkwkwineefficiency.objects.get(
            id=obj.get("_id_upd")
        )

        # 生产线ID

        if mcauthfield_lkwkwineid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.lkwkwineid = str(uuid.uuid4())

            ins_table_busi.lkwkwineid = str(ins_table_busi.lkwkwineid)
        # 效率率

        if mcauthfield_efficiencyrate["mcauthchange"]:

            # CharField

            ins_table_busi.efficiencyrate = obj.get("efficiencyrate")
        # 日产量

        if mcauthfield_dailyoutput["mcauthchange"]:

            # CharField

            ins_table_busi.dailyoutput = obj.get("dailyoutput")
        # 停机时间小时

        if mcauthfield_downtimehours["mcauthchange"]:

            # DateTimeField

            ins_table_busi.downtimehours = obj.get("downtimehours")
        # 维护频率

        if mcauthfield_makwkwintenancefrequency["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenancefrequency = obj.get(
                "makwkwintenancefrequency"
            )
        # 上次维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 机器人数量

        if mcauthfield_robotcount["mcauthchange"]:

            # IntegerField

            ins_table_busi.robotcount = obj.get("robotcount")
        # 操作人员数量

        if mcauthfield_operatkwkworcount["mcauthchange"]:

            # IntegerField

            ins_table_busi.operatkwkworcount = obj.get("operatkwkworcount")
        # 产品缺陷率

        if mcauthfield_productdefectrate["mcauthchange"]:

            # CharField

            ins_table_busi.productdefectrate = obj.get("productdefectrate")
        # 关联车间ID

        if mcauthfield_kwkwassociatedwkwkworkshopid["mcauthchange"]:

            # SelectField

            ins_table_busi.kwkwassociatedwkwkworkshopid = obj.get(
                "kwkwassociatedwkwkworkshopid"
            )
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_productionlkwkwineefficiency.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_productionlkwkwineefficiency.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/productionlkwkwineefficiency")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotfirmwareupdate(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人固件更新表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 固件版本号

        mcauthfield_firmwareversion = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新日期

        mcauthfield_updatedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新状态

        mcauthfield_updatestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新描述

        mcauthfield_updatedescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 前固件版本号

        mcauthfield_previousfirmwareversion = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新者

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否成功

        mcauthfield_issuccessful = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 失败原因

        mcauthfield_failurerekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人固件更新表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 固件版本号

        mcauthfield_firmwareversion = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新日期

        mcauthfield_updatedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新状态

        mcauthfield_updatestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新描述

        mcauthfield_updatedescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 前固件版本号

        mcauthfield_previousfirmwareversion = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 更新者

        mcauthfield_updatedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否成功

        mcauthfield_issuccessful = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 失败原因

        mcauthfield_failurerekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotfirmwareupdate.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotfirmwareupdate().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotfirmwareupdate.objects.filter(**filter)
        else:
            records = mc_robotfirmwareupdate.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/robotfirmwareupdate.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotfirmwareupdate()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 固件版本号

        if mcauthfield_firmwareversion["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.firmwareversion = obj.get("firmwareversion")
        # 更新日期

        if mcauthfield_updatedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.updatedate = obj.get("updatedate")
        # 更新状态

        if mcauthfield_updatestatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.updatestatus = obj.get("updatestatus")
        # 更新描述

        if mcauthfield_updatedescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.updatedescription = obj.get("updatedescription")
        # 前固件版本号

        if mcauthfield_previousfirmwareversion["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.previousfirmwareversion = obj.get("previousfirmwareversion")
        # 更新者

        if mcauthfield_updatedby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.updatedby = obj.get("updatedby")
        # 是否成功

        if mcauthfield_issuccessful["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.issuccessful = obj.get("issuccessful")
        # 失败原因

        if mcauthfield_failurerekwkwason["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.failurerekwkwason = obj.get("failurerekwkwason")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotfirmwareupdate.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 固件版本号

        if mcauthfield_firmwareversion["mcauthchange"]:

            # CharField

            ins_table_busi.firmwareversion = obj.get("firmwareversion")
        # 更新日期

        if mcauthfield_updatedate["mcauthchange"]:

            # DateField

            ins_table_busi.updatedate = obj.get("updatedate")
        # 更新状态

        if mcauthfield_updatestatus["mcauthchange"]:

            # CharField

            ins_table_busi.updatestatus = obj.get("updatestatus")
        # 更新描述

        if mcauthfield_updatedescription["mcauthchange"]:

            # TextField

            ins_table_busi.updatedescription = obj.get("updatedescription")
        # 前固件版本号

        if mcauthfield_previousfirmwareversion["mcauthchange"]:

            # CharField

            ins_table_busi.previousfirmwareversion = obj.get("previousfirmwareversion")
        # 更新者

        if mcauthfield_updatedby["mcauthchange"]:

            # CharField

            ins_table_busi.updatedby = obj.get("updatedby")
        # 是否成功

        if mcauthfield_issuccessful["mcauthchange"]:

            # BooleanField

            ins_table_busi.issuccessful = obj.get("issuccessful")
        # 失败原因

        if mcauthfield_failurerekwkwason["mcauthchange"]:

            # CharField

            ins_table_busi.failurerekwkwason = obj.get("failurerekwkwason")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotfirmwareupdate.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotfirmwareupdate.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotfirmwareupdate")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotfirmwareversion(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人固件版本表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 固件ID

        mcauthfield_firmwareid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 固件版本号

        mcauthfield_firmwareversion = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发布日期

        mcauthfield_relekwkwasedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 制造商

        mcauthfield_manufacturer = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 兼容性说明

        mcauthfield_compatibility = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件大小

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 下载链接

        mcauthfield_downloadurl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 固件描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人模型ID关联字段

        mcauthfield_robotmokwkwdelid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否为最新版本

        mcauthfield_islatest = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人固件版本表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 固件ID

        mcauthfield_firmwareid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 固件版本号

        mcauthfield_firmwareversion = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 发布日期

        mcauthfield_relekwkwasedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 制造商

        mcauthfield_manufacturer = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 兼容性说明

        mcauthfield_compatibility = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 文件大小

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 下载链接

        mcauthfield_downloadurl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 固件描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人模型ID关联字段

        mcauthfield_robotmokwkwdelid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否为最新版本

        mcauthfield_islatest = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotfirmwareversion.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotfirmwareversion().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotfirmwareversion.objects.filter(**filter)
        else:
            records = mc_robotfirmwareversion.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_robotinfo_55760 = []
        for m in mc_robotinfo.objects.all():
            mobj = m.toJson()
            data_mc_robotinfo_55760.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("robotname"),
                }
            )
        return render(request, "config_busi/robotfirmwareversion.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotfirmwareversion()

        # 固件ID

        if mcauthfield_firmwareid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.firmwareid = str(uuid.uuid4())
        # 固件版本号

        if mcauthfield_firmwareversion["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.firmwareversion = obj.get("firmwareversion")
        # 发布日期

        if mcauthfield_relekwkwasedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.relekwkwasedate = obj.get("relekwkwasedate")
        # 制造商

        if mcauthfield_manufacturer["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.manufacturer = obj.get("manufacturer")
        # 兼容性说明

        if mcauthfield_compatibility["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.compatibility = obj.get("compatibility")
        # 文件大小

        if mcauthfield_filesize["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 下载链接

        if mcauthfield_downloadurl["mcauthchange"]:

            # URLField # 其他情况/待补充

            ins_table_busi.downloadurl = obj.get("downloadurl")
        # 固件描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 机器人模型ID关联字段

        if mcauthfield_robotmokwkwdelid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.robotmokwkwdelid = obj.get("robotmokwkwdelid")
        # 是否为最新版本

        if mcauthfield_islatest["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.islatest = obj.get("islatest")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotfirmwareversion.objects.get(id=obj.get("_id_upd"))

        # 固件ID

        if mcauthfield_firmwareid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.firmwareid = str(uuid.uuid4())

            ins_table_busi.firmwareid = str(ins_table_busi.firmwareid)
        # 固件版本号

        if mcauthfield_firmwareversion["mcauthchange"]:

            # CharField

            ins_table_busi.firmwareversion = obj.get("firmwareversion")
        # 发布日期

        if mcauthfield_relekwkwasedate["mcauthchange"]:

            # DateField

            ins_table_busi.relekwkwasedate = obj.get("relekwkwasedate")
        # 制造商

        if mcauthfield_manufacturer["mcauthchange"]:

            # CharField

            ins_table_busi.manufacturer = obj.get("manufacturer")
        # 兼容性说明

        if mcauthfield_compatibility["mcauthchange"]:

            # CharField

            ins_table_busi.compatibility = obj.get("compatibility")
        # 文件大小

        if mcauthfield_filesize["mcauthchange"]:

            # Save File FileField

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 下载链接

        if mcauthfield_downloadurl["mcauthchange"]:

            # URLField

            ins_table_busi.downloadurl = obj.get("downloadurl")
        # 固件描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 机器人模型ID关联字段

        if mcauthfield_robotmokwkwdelid["mcauthchange"]:

            # SelectField

            ins_table_busi.robotmokwkwdelid = obj.get("robotmokwkwdelid")
        # 是否为最新版本

        if mcauthfield_islatest["mcauthchange"]:

            # BooleanField

            ins_table_busi.islatest = obj.get("islatest")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotfirmwareversion.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotfirmwareversion.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotfirmwareversion")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_productionlkwkwinesafetyrule(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 生产线安全规则表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 规则ID

        mcauthfield_ruleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 规则名称

        mcauthfield_rulename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线ID

        mcauthfield_productionlkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 规则描述

        mcauthfield_ruledescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 严重等级

        mcauthfield_severitylevel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 检测方式

        mcauthfield_detectionmethod = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警阈值

        mcauthfield_alertthreshold = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警接收人

        mcauthfield_alertrecipients = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改时间

        mcauthfield_modkwkwifiedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 生产线安全规则表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 规则ID

        mcauthfield_ruleid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 规则名称

        mcauthfield_rulename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线ID

        mcauthfield_productionlkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 规则描述

        mcauthfield_ruledescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 严重等级

        mcauthfield_severitylevel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 检测方式

        mcauthfield_detectionmethod = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警阈值

        mcauthfield_alertthreshold = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 报警接收人

        mcauthfield_alertrecipients = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 修改时间

        mcauthfield_modkwkwifiedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_productionlkwkwinesafetyrule.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_productionlkwkwinesafetyrule().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_productionlkwkwinesafetyrule.objects.filter(**filter)
        else:
            records = mc_productionlkwkwinesafetyrule.objects.all()
        # 加载界面中下拉框所需数据

        return render(
            request, "config_busi/productionlkwkwinesafetyrule.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_productionlkwkwinesafetyrule()

        # 规则ID

        if mcauthfield_ruleid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.ruleid = str(uuid.uuid4())
        # 规则名称

        if mcauthfield_rulename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rulename = obj.get("rulename")
        # 生产线ID

        if mcauthfield_productionlkwkwineid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.productionlkwkwineid = str(uuid.uuid4())
        # 规则描述

        if mcauthfield_ruledescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.ruledescription = obj.get("ruledescription")
        # 严重等级

        if mcauthfield_severitylevel["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.severitylevel = obj.get("severitylevel")
        # 检测方式

        if mcauthfield_detectionmethod["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.detectionmethod = obj.get("detectionmethod")
        # 报警阈值

        if mcauthfield_alertthreshold["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.alertthreshold = obj.get("alertthreshold")
        # 报警接收人

        if mcauthfield_alertrecipients["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.alertrecipients = obj.get("alertrecipients")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 修改时间

        if mcauthfield_modkwkwifiedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.modkwkwifiedat = obj.get("modkwkwifiedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_productionlkwkwinesafetyrule.objects.get(
            id=obj.get("_id_upd")
        )

        # 规则ID

        if mcauthfield_ruleid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.ruleid = str(uuid.uuid4())

            ins_table_busi.ruleid = str(ins_table_busi.ruleid)
        # 规则名称

        if mcauthfield_rulename["mcauthchange"]:

            # CharField

            ins_table_busi.rulename = obj.get("rulename")
        # 生产线ID

        if mcauthfield_productionlkwkwineid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.productionlkwkwineid = str(uuid.uuid4())

            ins_table_busi.productionlkwkwineid = str(
                ins_table_busi.productionlkwkwineid
            )
        # 规则描述

        if mcauthfield_ruledescription["mcauthchange"]:

            # TextField

            ins_table_busi.ruledescription = obj.get("ruledescription")
        # 严重等级

        if mcauthfield_severitylevel["mcauthchange"]:

            # CharField

            ins_table_busi.severitylevel = obj.get("severitylevel")
        # 检测方式

        if mcauthfield_detectionmethod["mcauthchange"]:

            # CharField

            ins_table_busi.detectionmethod = obj.get("detectionmethod")
        # 报警阈值

        if mcauthfield_alertthreshold["mcauthchange"]:

            # CharField

            ins_table_busi.alertthreshold = obj.get("alertthreshold")
        # 报警接收人

        if mcauthfield_alertrecipients["mcauthchange"]:

            # CharField

            ins_table_busi.alertrecipients = obj.get("alertrecipients")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 修改时间

        if mcauthfield_modkwkwifiedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.modkwkwifiedat = obj.get("modkwkwifiedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_productionlkwkwinesafetyrule.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_productionlkwkwinesafetyrule.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/productionlkwkwinesafetyrule")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotsafetyconfig(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人安全配置表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 安全等级

        mcauthfield_safetylevel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 警报阈值

        mcauthfield_alertthreshold = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 紧急停止码

        mcauthfield_emergencystopcode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护间隔

        mcauthfield_makwkwintenanceinterval = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 运行状态

        mcauthfield_operatkwkwingstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障历史

        mcauthfield_faulthkwkwistkwkwory = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联工作站ID

        mcauthfield_associatedwkwkworkstationid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人安全配置表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 安全等级

        mcauthfield_safetylevel = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 警报阈值

        mcauthfield_alertthreshold = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 紧急停止码

        mcauthfield_emergencystopcode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护间隔

        mcauthfield_makwkwintenanceinterval = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 运行状态

        mcauthfield_operatkwkwingstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障历史

        mcauthfield_faulthkwkwistkwkwory = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联工作站ID

        mcauthfield_associatedwkwkworkstationid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotsafetyconfig.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotsafetyconfig().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotsafetyconfig.objects.filter(**filter)
        else:
            records = mc_robotsafetyconfig.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_productionlkwkwineinfo_55780 = []
        for m in mc_productionlkwkwineinfo.objects.all():
            mobj = m.toJson()
            data_mc_productionlkwkwineinfo_55780.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("productionlkwkwinename"),
                }
            )
        return render(request, "config_busi/robotsafetyconfig.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotsafetyconfig()

        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 安全等级

        if mcauthfield_safetylevel["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.safetylevel = obj.get("safetylevel")
        # 警报阈值

        if mcauthfield_alertthreshold["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.alertthreshold = obj.get("alertthreshold")
        # 紧急停止码

        if mcauthfield_emergencystopcode["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.emergencystopcode = obj.get("emergencystopcode")
        # 维护间隔

        if mcauthfield_makwkwintenanceinterval["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenanceinterval = obj.get("makwkwintenanceinterval")
        # 上次维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 运行状态

        if mcauthfield_operatkwkwingstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.operatkwkwingstatus = obj.get("operatkwkwingstatus")
        # 故障历史

        if mcauthfield_faulthkwkwistkwkwory["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.faulthkwkwistkwkwory = obj.get("faulthkwkwistkwkwory")
        # 关联工作站ID

        if mcauthfield_associatedwkwkworkstationid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.associatedwkwkworkstationid = obj.get(
                "associatedwkwkworkstationid"
            )
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotsafetyconfig.objects.get(id=obj.get("_id_upd"))

        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 安全等级

        if mcauthfield_safetylevel["mcauthchange"]:

            # CharField

            ins_table_busi.safetylevel = obj.get("safetylevel")
        # 警报阈值

        if mcauthfield_alertthreshold["mcauthchange"]:

            # CharField

            ins_table_busi.alertthreshold = obj.get("alertthreshold")
        # 紧急停止码

        if mcauthfield_emergencystopcode["mcauthchange"]:

            # CharField

            ins_table_busi.emergencystopcode = obj.get("emergencystopcode")
        # 维护间隔

        if mcauthfield_makwkwintenanceinterval["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenanceinterval = obj.get("makwkwintenanceinterval")
        # 上次维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 运行状态

        if mcauthfield_operatkwkwingstatus["mcauthchange"]:

            # CharField

            ins_table_busi.operatkwkwingstatus = obj.get("operatkwkwingstatus")
        # 故障历史

        if mcauthfield_faulthkwkwistkwkwory["mcauthchange"]:

            # CharField

            ins_table_busi.faulthkwkwistkwkwory = obj.get("faulthkwkwistkwkwory")
        # 关联工作站ID

        if mcauthfield_associatedwkwkworkstationid["mcauthchange"]:

            # SelectField

            ins_table_busi.associatedwkwkworkstationid = obj.get(
                "associatedwkwkworkstationid"
            )
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotsafetyconfig.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotsafetyconfig.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotsafetyconfig")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotinspectionplan(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人巡检计划表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 计划ID

        mcauthfield_planid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 开始时间

        mcauthfield_starttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 结束时间

        mcauthfield_endtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 巡检频率

        mcauthfield_frequency = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 巡检区域

        mcauthfield_inspectionarea = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 计划状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者

        mcauthfield_lkwkwastmodkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改时间

        mcauthfield_lkwkwastmodkwkwifiedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联任务ID

        mcauthfield_associatedtkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人巡检计划表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 计划ID

        mcauthfield_planid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 开始时间

        mcauthfield_starttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 结束时间

        mcauthfield_endtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 巡检频率

        mcauthfield_frequency = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 巡检区域

        mcauthfield_inspectionarea = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 计划状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者

        mcauthfield_lkwkwastmodkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改时间

        mcauthfield_lkwkwastmodkwkwifiedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 关联任务ID

        mcauthfield_associatedtkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotinspectionplan.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotinspectionplan().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotinspectionplan.objects.filter(**filter)
        else:
            records = mc_robotinspectionplan.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_robottkwkwask_55791 = []
        for m in mc_robottkwkwask.objects.all():
            mobj = m.toJson()
            data_mc_robottkwkwask_55791.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("tkwkwaskname"),
                }
            )
        return render(request, "config_busi/robotinspectionplan.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotinspectionplan()

        # 计划ID

        if mcauthfield_planid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.planid = str(uuid.uuid4())
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 开始时间

        if mcauthfield_starttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.starttime = obj.get("starttime")
        # 结束时间

        if mcauthfield_endtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.endtime = obj.get("endtime")
        # 巡检频率

        if mcauthfield_frequency["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.frequency = obj.get("frequency")
        # 巡检区域

        if mcauthfield_inspectionarea["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.inspectionarea = obj.get("inspectionarea")
        # 计划状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 创建者

        if mcauthfield_createdby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.createdby = obj.get("createdby")
        # 最后修改者

        if mcauthfield_lkwkwastmodkwkwifiedby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwifiedby = obj.get("lkwkwastmodkwkwifiedby")
        # 最后修改时间

        if mcauthfield_lkwkwastmodkwkwifiedtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwifiedtime = obj.get(
                "lkwkwastmodkwkwifiedtime"
            )
        # 关联任务ID

        if mcauthfield_associatedtkwkwaskid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.associatedtkwkwaskid = obj.get("associatedtkwkwaskid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotinspectionplan.objects.get(id=obj.get("_id_upd"))

        # 计划ID

        if mcauthfield_planid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.planid = str(uuid.uuid4())

            ins_table_busi.planid = str(ins_table_busi.planid)
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 开始时间

        if mcauthfield_starttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.starttime = obj.get("starttime")
        # 结束时间

        if mcauthfield_endtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.endtime = obj.get("endtime")
        # 巡检频率

        if mcauthfield_frequency["mcauthchange"]:

            # CharField

            ins_table_busi.frequency = obj.get("frequency")
        # 巡检区域

        if mcauthfield_inspectionarea["mcauthchange"]:

            # CharField

            ins_table_busi.inspectionarea = obj.get("inspectionarea")
        # 计划状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 创建者

        if mcauthfield_createdby["mcauthchange"]:

            # CharField

            ins_table_busi.createdby = obj.get("createdby")
        # 最后修改者

        if mcauthfield_lkwkwastmodkwkwifiedby["mcauthchange"]:

            # CharField

            ins_table_busi.lkwkwastmodkwkwifiedby = obj.get("lkwkwastmodkwkwifiedby")
        # 最后修改时间

        if mcauthfield_lkwkwastmodkwkwifiedtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastmodkwkwifiedtime = obj.get(
                "lkwkwastmodkwkwifiedtime"
            )
        # 关联任务ID

        if mcauthfield_associatedtkwkwaskid["mcauthchange"]:

            # SelectField

            ins_table_busi.associatedtkwkwaskid = obj.get("associatedtkwkwaskid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotinspectionplan.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotinspectionplan.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotinspectionplan")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_inspectionresult(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 巡检结果表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 巡检编号

        mcauthfield_inspectionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 巡检时间

        mcauthfield_inspectiontime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人编号

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 安全状态

        mcauthfield_safetystatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障描述

        mcauthfield_faultdescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修状态

        mcauthfield_repairstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 巡检员

        mcauthfield_inspectkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修人员

        mcauthfield_repairer = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修时间

        mcauthfield_repairtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 巡检结果表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 巡检编号

        mcauthfield_inspectionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 巡检时间

        mcauthfield_inspectiontime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人编号

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 安全状态

        mcauthfield_safetystatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 故障描述

        mcauthfield_faultdescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修状态

        mcauthfield_repairstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 巡检员

        mcauthfield_inspectkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修人员

        mcauthfield_repairer = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修时间

        mcauthfield_repairtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_inspectionresult.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_inspectionresult().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_inspectionresult.objects.filter(**filter)
        else:
            records = mc_inspectionresult.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/inspectionresult.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_inspectionresult()

        # 巡检编号

        if mcauthfield_inspectionid["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.inspectionid = obj.get("inspectionid")
        # 巡检时间

        if mcauthfield_inspectiontime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.inspectiontime = obj.get("inspectiontime")
        # 机器人编号

        if mcauthfield_robotid["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.robotid = obj.get("robotid")
        # 安全状态

        if mcauthfield_safetystatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.safetystatus = obj.get("safetystatus")
        # 故障描述

        if mcauthfield_faultdescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.faultdescription = obj.get("faultdescription")
        # 维修状态

        if mcauthfield_repairstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repairstatus = obj.get("repairstatus")
        # 巡检员

        if mcauthfield_inspectkwkwor["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.inspectkwkwor = obj.get("inspectkwkwor")
        # 维修人员

        if mcauthfield_repairer["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.repairer = obj.get("repairer")
        # 维修时间

        if mcauthfield_repairtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.repairtime = obj.get("repairtime")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_inspectionresult.objects.get(id=obj.get("_id_upd"))

        # 巡检编号

        if mcauthfield_inspectionid["mcauthchange"]:

            # CharField

            ins_table_busi.inspectionid = obj.get("inspectionid")
        # 巡检时间

        if mcauthfield_inspectiontime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.inspectiontime = obj.get("inspectiontime")
        # 机器人编号

        if mcauthfield_robotid["mcauthchange"]:

            # CharField

            ins_table_busi.robotid = obj.get("robotid")
        # 安全状态

        if mcauthfield_safetystatus["mcauthchange"]:

            # CharField

            ins_table_busi.safetystatus = obj.get("safetystatus")
        # 故障描述

        if mcauthfield_faultdescription["mcauthchange"]:

            # TextField

            ins_table_busi.faultdescription = obj.get("faultdescription")
        # 维修状态

        if mcauthfield_repairstatus["mcauthchange"]:

            # CharField

            ins_table_busi.repairstatus = obj.get("repairstatus")
        # 巡检员

        if mcauthfield_inspectkwkwor["mcauthchange"]:

            # CharField

            ins_table_busi.inspectkwkwor = obj.get("inspectkwkwor")
        # 维修人员

        if mcauthfield_repairer["mcauthchange"]:

            # CharField

            ins_table_busi.repairer = obj.get("repairer")
        # 维修时间

        if mcauthfield_repairtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.repairtime = obj.get("repairtime")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_inspectionresult.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_inspectionresult.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/inspectionresult")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotmakwkwintenancecycle(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人维护周期表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护周期天数

        mcauthfield_makwkwintenancecycle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 下次维护日期

        mcauthfield_nextmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护状态如待维护、维护中、已完成

        mcauthfield_makwkwintenancestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护类型如常规检查、深度保养、故障修复

        mcauthfield_makwkwintenancetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护备注

        mcauthfield_makwkwintenancenotes = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建人

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人维护周期表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护周期天数

        mcauthfield_makwkwintenancecycle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 上次维护日期

        mcauthfield_lkwkwastmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 下次维护日期

        mcauthfield_nextmakwkwintenancedate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护状态如待维护、维护中、已完成

        mcauthfield_makwkwintenancestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护类型如常规检查、深度保养、故障修复

        mcauthfield_makwkwintenancetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维护备注

        mcauthfield_makwkwintenancenotes = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建人

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotmakwkwintenancecycle.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotmakwkwintenancecycle().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotmakwkwintenancecycle.objects.filter(**filter)
        else:
            records = mc_robotmakwkwintenancecycle.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/robotmakwkwintenancecycle.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotmakwkwintenancecycle()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 维护周期天数

        if mcauthfield_makwkwintenancecycle["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenancecycle = obj.get("makwkwintenancecycle")
        # 上次维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 下次维护日期

        if mcauthfield_nextmakwkwintenancedate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.nextmakwkwintenancedate = obj.get("nextmakwkwintenancedate")
        # 维护状态如待维护、维护中、已完成

        if mcauthfield_makwkwintenancestatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenancestatus = obj.get("makwkwintenancestatus")
        # 维护类型如常规检查、深度保养、故障修复

        if mcauthfield_makwkwintenancetype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenancetype = obj.get("makwkwintenancetype")
        # 维护备注

        if mcauthfield_makwkwintenancenotes["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.makwkwintenancenotes = obj.get("makwkwintenancenotes")
        # 创建人

        if mcauthfield_createdby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.createdby = obj.get("createdby")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotmakwkwintenancecycle.objects.get(id=obj.get("_id_upd"))

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 维护周期天数

        if mcauthfield_makwkwintenancecycle["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenancecycle = obj.get("makwkwintenancecycle")
        # 上次维护日期

        if mcauthfield_lkwkwastmakwkwintenancedate["mcauthchange"]:

            # DateField

            ins_table_busi.lkwkwastmakwkwintenancedate = obj.get(
                "lkwkwastmakwkwintenancedate"
            )
        # 下次维护日期

        if mcauthfield_nextmakwkwintenancedate["mcauthchange"]:

            # DateField

            ins_table_busi.nextmakwkwintenancedate = obj.get("nextmakwkwintenancedate")
        # 维护状态如待维护、维护中、已完成

        if mcauthfield_makwkwintenancestatus["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenancestatus = obj.get("makwkwintenancestatus")
        # 维护类型如常规检查、深度保养、故障修复

        if mcauthfield_makwkwintenancetype["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenancetype = obj.get("makwkwintenancetype")
        # 维护备注

        if mcauthfield_makwkwintenancenotes["mcauthchange"]:

            # CharField

            ins_table_busi.makwkwintenancenotes = obj.get("makwkwintenancenotes")
        # 创建人

        if mcauthfield_createdby["mcauthchange"]:

            # CharField

            ins_table_busi.createdby = obj.get("createdby")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotmakwkwintenancecycle.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotmakwkwintenancecycle.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotmakwkwintenancecycle")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_productionlkwkwinedowntimereckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 生产线停机记录表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 记录ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线ID

        mcauthfield_productionlkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 停机开始时间

        mcauthfield_downtimestarttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 停机结束时间

        mcauthfield_downtimeendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 停机原因

        mcauthfield_downtimerekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 停机时长分钟

        mcauthfield_downtimeduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作员ID

        mcauthfield_operatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修员ID

        mcauthfield_repairmanid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已解决0未解决1已解决

        mcauthfield_kwkwisresolved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 备注

        mcauthfield_remark = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 生产线停机记录表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 记录ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 生产线ID

        mcauthfield_productionlkwkwineid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 停机开始时间

        mcauthfield_downtimestarttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 停机结束时间

        mcauthfield_downtimeendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 停机原因

        mcauthfield_downtimerekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 停机时长分钟

        mcauthfield_downtimeduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 操作员ID

        mcauthfield_operatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 维修员ID

        mcauthfield_repairmanid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否已解决0未解决1已解决

        mcauthfield_kwkwisresolved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 备注

        mcauthfield_remark = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_productionlkwkwinedowntimereckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_productionlkwkwinedowntimereckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_productionlkwkwinedowntimereckwkword.objects.filter(**filter)
        else:
            records = mc_productionlkwkwinedowntimereckwkword.objects.all()
        # 加载界面中下拉框所需数据

        return render(
            request, "config_busi/productionlkwkwinedowntimereckwkword.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_productionlkwkwinedowntimereckwkword()

        # 记录ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 生产线ID

        if mcauthfield_productionlkwkwineid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.productionlkwkwineid = str(uuid.uuid4())
        # 停机开始时间

        if mcauthfield_downtimestarttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.downtimestarttime = obj.get("downtimestarttime")
        # 停机结束时间

        if mcauthfield_downtimeendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.downtimeendtime = obj.get("downtimeendtime")
        # 停机原因

        if mcauthfield_downtimerekwkwason["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.downtimerekwkwason = obj.get("downtimerekwkwason")
        # 停机时长分钟

        if mcauthfield_downtimeduration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.downtimeduration = obj.get("downtimeduration")
        # 操作员ID

        if mcauthfield_operatkwkworid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.operatkwkworid = str(uuid.uuid4())
        # 维修员ID

        if mcauthfield_repairmanid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.repairmanid = str(uuid.uuid4())
        # 是否已解决0未解决1已解决

        if mcauthfield_kwkwisresolved["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisresolved = obj.get("kwkwisresolved")
        # 备注

        if mcauthfield_remark["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.remark = obj.get("remark")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_productionlkwkwinedowntimereckwkword.objects.get(
            id=obj.get("_id_upd")
        )

        # 记录ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 生产线ID

        if mcauthfield_productionlkwkwineid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.productionlkwkwineid = str(uuid.uuid4())

            ins_table_busi.productionlkwkwineid = str(
                ins_table_busi.productionlkwkwineid
            )
        # 停机开始时间

        if mcauthfield_downtimestarttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.downtimestarttime = obj.get("downtimestarttime")
        # 停机结束时间

        if mcauthfield_downtimeendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.downtimeendtime = obj.get("downtimeendtime")
        # 停机原因

        if mcauthfield_downtimerekwkwason["mcauthchange"]:

            # CharField

            ins_table_busi.downtimerekwkwason = obj.get("downtimerekwkwason")
        # 停机时长分钟

        if mcauthfield_downtimeduration["mcauthchange"]:

            # CharField

            ins_table_busi.downtimeduration = obj.get("downtimeduration")
        # 操作员ID

        if mcauthfield_operatkwkworid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.operatkwkworid = str(uuid.uuid4())

            ins_table_busi.operatkwkworid = str(ins_table_busi.operatkwkworid)
        # 维修员ID

        if mcauthfield_repairmanid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.repairmanid = str(uuid.uuid4())

            ins_table_busi.repairmanid = str(ins_table_busi.repairmanid)
        # 是否已解决0未解决1已解决

        if mcauthfield_kwkwisresolved["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisresolved = obj.get("kwkwisresolved")
        # 备注

        if mcauthfield_remark["mcauthchange"]:

            # CharField

            ins_table_busi.remark = obj.get("remark")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_productionlkwkwinedowntimereckwkword.objects.get(
            id=obj.get("_id")
        )
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_productionlkwkwinedowntimereckwkword.objects.get(
            id=obj.get("_id")
        )
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/productionlkwkwinedowntimereckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_robotpermkwkwissionassignment(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 机器人权限分配表 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限ID

        mcauthfield_permkwkwissionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 分配日期

        mcauthfield_assignmentdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 过期日期

        mcauthfield_expirydate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者

        mcauthfield_lkwkwastmodkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID关联字段

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 机器人权限分配表 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 唯一标识符

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 机器人ID

        mcauthfield_robotid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 权限ID

        mcauthfield_permkwkwissionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 分配日期

        mcauthfield_assignmentdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 过期日期

        mcauthfield_expirydate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 创建者

        mcauthfield_createdby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 最后修改者

        mcauthfield_lkwkwastmodkwkwifiedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }

        # 部门ID关联字段

        mcauthfield_departmentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_robotpermkwkwissionassignment.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_robotpermkwkwissionassignment().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_robotpermkwkwissionassignment.objects.filter(**filter)
        else:
            records = mc_robotpermkwkwissionassignment.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_permkwkwissionmanagement_55829 = []
        for m in mc_permkwkwissionmanagement.objects.all():
            mobj = m.toJson()
            data_mc_permkwkwissionmanagement_55829.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("permkwkwissionname"),
                }
            )
        return render(
            request, "config_busi/robotpermkwkwissionassignment.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_robotpermkwkwissionassignment()

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.robotid = str(uuid.uuid4())
        # 权限ID

        if mcauthfield_permkwkwissionid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.permkwkwissionid = str(uuid.uuid4())
        # 分配日期

        if mcauthfield_assignmentdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.assignmentdate = obj.get("assignmentdate")
        # 过期日期

        if mcauthfield_expirydate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.expirydate = obj.get("expirydate")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 创建者

        if mcauthfield_createdby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.createdby = obj.get("createdby")
        # 最后修改者

        if mcauthfield_lkwkwastmodkwkwifiedby["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.lkwkwastmodkwkwifiedby = obj.get("lkwkwastmodkwkwifiedby")
        # 部门ID关联字段

        if mcauthfield_departmentid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.departmentid = obj.get("departmentid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_robotpermkwkwissionassignment.objects.get(
            id=obj.get("_id_upd")
        )

        # 唯一标识符

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 机器人ID

        if mcauthfield_robotid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.robotid = str(uuid.uuid4())

            ins_table_busi.robotid = str(ins_table_busi.robotid)
        # 权限ID

        if mcauthfield_permkwkwissionid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.permkwkwissionid = str(uuid.uuid4())

            ins_table_busi.permkwkwissionid = str(ins_table_busi.permkwkwissionid)
        # 分配日期

        if mcauthfield_assignmentdate["mcauthchange"]:

            # DateField

            ins_table_busi.assignmentdate = obj.get("assignmentdate")
        # 过期日期

        if mcauthfield_expirydate["mcauthchange"]:

            # DateField

            ins_table_busi.expirydate = obj.get("expirydate")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 创建者

        if mcauthfield_createdby["mcauthchange"]:

            # CharField

            ins_table_busi.createdby = obj.get("createdby")
        # 最后修改者

        if mcauthfield_lkwkwastmodkwkwifiedby["mcauthchange"]:

            # CharField

            ins_table_busi.lkwkwastmodkwkwifiedby = obj.get("lkwkwastmodkwkwifiedby")
        # 部门ID关联字段

        if mcauthfield_departmentid["mcauthchange"]:

            # SelectField

            ins_table_busi.departmentid = obj.get("departmentid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_robotpermkwkwissionassignment.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_robotpermkwkwissionassignment.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/robotpermkwkwissionassignment")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_supermanager(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 系统管理员 用户信息表(8137)

    if user_table_id == str(8137):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 系统管理员 系统管理员(8158)

    if user_table_id == str(8158):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": True and has_view,
            "mcauthchange": True and has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_supermanager.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_supermanager().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_supermanager.objects.filter(**filter)
        else:
            records = mc_supermanager.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/supermanager.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_supermanager()

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id_upd"))

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/supermanager")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


def auto_detect(request):
    if request.method == "GET":
        detect = False

        return render(request, "config_algorithm/auto_detect.html", locals())
    obj = mydict(request.POST)

    if "img" not in request.FILES:
        return HttpResponse("请上传图片")
    img = request.FILES["img"]
    # mc_

    detect = True

    detect_result = "算法结果展示"

    # 保存提交的内容
    # 保存分析的结果
    # 若源码中缺少需要的表和字段.联系 qq952934650

    return render(request, "config_algorithm/auto_detect.html", locals())

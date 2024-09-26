from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from sys_user.func import *

# 词云

from a_simulink_unit.generate_wordcloud import generate_wordcloud_base64

# Create your views here.


def index(request):

    return render(request, "config_visual/index.html", locals())


"""

# 系统中所有数据表名/中英文+字段中英文
用于快速创建查询语句和分析
测试通过后删除此段.
__deprected__ mark_appcenter_views_all_tables_and_fields
__deprected__ mark_appcenter_views_all_tables_and__two_field_fields
# 根据需要按照表结构和csv文件依次导入数据库.
"""


def bi(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    # robotinfo(机器人信息表)->robotid(机器人ID)

    if obj.get("optype") == "robotinfo.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "robotinfo.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotinfo.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotinfo.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotinfo.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotinfo.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotid",
            "机器人ID",
        )
    # robotinfo(机器人信息表)->robotname(机器人名称)

    if obj.get("optype") == "robotinfo.robotname_pie":
        res = get_pie(
            "select robotname x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotname order by x desc",
            "机器人名称",
        )
    if obj.get("optype") == "robotinfo.robotname_pie_v1":
        res = get_pie_v1(
            "select robotname x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotname",
            "机器人名称",
        )
    if obj.get("optype") == "robotinfo.robotname_pie_v2":
        res = get_pie_v2(
            "select robotname x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotname",
            "机器人名称",
        )
    if obj.get("optype") == "robotinfo.robotname_line":
        res = get_line(
            "select robotname x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotname",
            "机器人名称",
        )
    if obj.get("optype") == "robotinfo.robotname_bar":
        res = get_bar(
            "select robotname x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotname",
            "机器人名称",
        )
    if obj.get("optype") == "robotinfo.robotname_bar_v1":
        res = get_bar_v1(
            "select robotname x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by robotname",
            "机器人名称",
        )
    # robotinfo(机器人信息表)->mokwkwdelnumber(型号编号)

    if obj.get("optype") == "robotinfo.mokwkwdelnumber_pie":
        res = get_pie(
            "select mokwkwdelnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by mokwkwdelnumber order by x desc",
            "型号编号",
        )
    if obj.get("optype") == "robotinfo.mokwkwdelnumber_pie_v1":
        res = get_pie_v1(
            "select mokwkwdelnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by mokwkwdelnumber",
            "型号编号",
        )
    if obj.get("optype") == "robotinfo.mokwkwdelnumber_pie_v2":
        res = get_pie_v2(
            "select mokwkwdelnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by mokwkwdelnumber",
            "型号编号",
        )
    if obj.get("optype") == "robotinfo.mokwkwdelnumber_line":
        res = get_line(
            "select mokwkwdelnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by mokwkwdelnumber",
            "型号编号",
        )
    if obj.get("optype") == "robotinfo.mokwkwdelnumber_bar":
        res = get_bar(
            "select mokwkwdelnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by mokwkwdelnumber",
            "型号编号",
        )
    if obj.get("optype") == "robotinfo.mokwkwdelnumber_bar_v1":
        res = get_bar_v1(
            "select mokwkwdelnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by mokwkwdelnumber",
            "型号编号",
        )
    # robotinfo(机器人信息表)->serialnumber(序列号)

    if obj.get("optype") == "robotinfo.serialnumber_pie":
        res = get_pie(
            "select serialnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by serialnumber order by x desc",
            "序列号",
        )
    if obj.get("optype") == "robotinfo.serialnumber_pie_v1":
        res = get_pie_v1(
            "select serialnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by serialnumber",
            "序列号",
        )
    if obj.get("optype") == "robotinfo.serialnumber_pie_v2":
        res = get_pie_v2(
            "select serialnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by serialnumber",
            "序列号",
        )
    if obj.get("optype") == "robotinfo.serialnumber_line":
        res = get_line(
            "select serialnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by serialnumber",
            "序列号",
        )
    if obj.get("optype") == "robotinfo.serialnumber_bar":
        res = get_bar(
            "select serialnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by serialnumber",
            "序列号",
        )
    if obj.get("optype") == "robotinfo.serialnumber_bar_v1":
        res = get_bar_v1(
            "select serialnumber x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by serialnumber",
            "序列号",
        )
    if obj.get("optype") == "robotinfo.manufacturedate_line":
        res = get_line(
            "select manufacturedate x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by manufacturedate order by x",
            "生产日期",
        )
    if obj.get("optype") == "robotinfo.lkwkwastmakwkwintenancedate_line":
        res = get_line(
            "select lkwkwastmakwkwintenancedate x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by lkwkwastmakwkwintenancedate order by x",
            "最近维护日期",
        )
    # robotinfo(机器人信息表)->operationalstatus(运行状态)

    if obj.get("optype") == "robotinfo.operationalstatus_pie":
        res = get_pie(
            "select operationalstatus x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by operationalstatus order by x desc",
            "运行状态",
        )
    if obj.get("optype") == "robotinfo.operationalstatus_pie_v1":
        res = get_pie_v1(
            "select operationalstatus x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by operationalstatus",
            "运行状态",
        )
    if obj.get("optype") == "robotinfo.operationalstatus_pie_v2":
        res = get_pie_v2(
            "select operationalstatus x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by operationalstatus",
            "运行状态",
        )
    if obj.get("optype") == "robotinfo.operationalstatus_line":
        res = get_line(
            "select operationalstatus x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by operationalstatus",
            "运行状态",
        )
    if obj.get("optype") == "robotinfo.operationalstatus_bar":
        res = get_bar(
            "select operationalstatus x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by operationalstatus",
            "运行状态",
        )
    if obj.get("optype") == "robotinfo.operationalstatus_bar_v1":
        res = get_bar_v1(
            "select operationalstatus x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by operationalstatus",
            "运行状态",
        )
    # robotinfo(机器人信息表)->location(位置)

    if obj.get("optype") == "robotinfo.location_pie":
        res = get_pie(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by location order by x desc",
            "位置",
        )
    if obj.get("optype") == "robotinfo.location_pie_v1":
        res = get_pie_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by location",
            "位置",
        )
    if obj.get("optype") == "robotinfo.location_pie_v2":
        res = get_pie_v2(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by location",
            "位置",
        )
    if obj.get("optype") == "robotinfo.location_line":
        res = get_line(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by location",
            "位置",
        )
    if obj.get("optype") == "robotinfo.location_bar":
        res = get_bar(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by location",
            "位置",
        )
    if obj.get("optype") == "robotinfo.location_bar_v1":
        res = get_bar_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by location",
            "位置",
        )
    # robotinfo(机器人信息表)->departmentid(部门ID)

    if obj.get("optype") == "robotinfo.departmentid_pie":
        res = get_pie(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by departmentid order by x desc",
            "部门ID",
        )
    if obj.get("optype") == "robotinfo.departmentid_pie_v1":
        res = get_pie_v1(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "robotinfo.departmentid_pie_v2":
        res = get_pie_v2(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "robotinfo.departmentid_line":
        res = get_line(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "robotinfo.departmentid_bar":
        res = get_bar(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "robotinfo.departmentid_bar_v1":
        res = get_bar_v1(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotinfo group by departmentid",
            "部门ID",
        )
    # productionlkwkwineinfo(生产线信息表)->productionlkwkwineid(生产线ID)

    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwineid_pie":
        res = get_pie(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwineid order by x desc",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwineid_pie_v1":
        res = get_pie_v1(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwineid_pie_v2":
        res = get_pie_v2(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwineid_line":
        res = get_line(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwineid_bar":
        res = get_bar(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwineid_bar_v1":
        res = get_bar_v1(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwineid",
            "生产线ID",
        )
    # productionlkwkwineinfo(生产线信息表)->productionlkwkwinename(生产线名称)

    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwinename_pie":
        res = get_pie(
            "select productionlkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwinename order by x desc",
            "生产线名称",
        )
    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwinename_pie_v1":
        res = get_pie_v1(
            "select productionlkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwinename",
            "生产线名称",
        )
    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwinename_pie_v2":
        res = get_pie_v2(
            "select productionlkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwinename",
            "生产线名称",
        )
    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwinename_line":
        res = get_line(
            "select productionlkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwinename",
            "生产线名称",
        )
    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwinename_bar":
        res = get_bar(
            "select productionlkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwinename",
            "生产线名称",
        )
    if obj.get("optype") == "productionlkwkwineinfo.productionlkwkwinename_bar_v1":
        res = get_bar_v1(
            "select productionlkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by productionlkwkwinename",
            "生产线名称",
        )
    # productionlkwkwineinfo(生产线信息表)->location(生产线位置)

    if obj.get("optype") == "productionlkwkwineinfo.location_pie":
        res = get_pie(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by location order by x desc",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineinfo.location_pie_v1":
        res = get_pie_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by location",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineinfo.location_pie_v2":
        res = get_pie_v2(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by location",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineinfo.location_line":
        res = get_line(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by location",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineinfo.location_bar":
        res = get_bar(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by location",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineinfo.location_bar_v1":
        res = get_bar_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by location",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineinfo.creationdate_line":
        res = get_line(
            "select creationdate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by creationdate order by x",
            "创建日期",
        )
    # productionlkwkwineinfo(生产线信息表)->isactive(是否激活)

    if obj.get("optype") == "productionlkwkwineinfo.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "productionlkwkwineinfo.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "productionlkwkwineinfo.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "productionlkwkwineinfo.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "productionlkwkwineinfo.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "productionlkwkwineinfo.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by isactive",
            "是否激活",
        )
    # productionlkwkwineinfo(生产线信息表)->maxcapacity(最大产能)

    if obj.get("optype") == "productionlkwkwineinfo.maxcapacity_pie":
        res = get_pie(
            "select maxcapacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by maxcapacity order by x desc",
            "最大产能",
        )
    if obj.get("optype") == "productionlkwkwineinfo.maxcapacity_pie_v1":
        res = get_pie_v1(
            "select maxcapacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by maxcapacity",
            "最大产能",
        )
    if obj.get("optype") == "productionlkwkwineinfo.maxcapacity_pie_v2":
        res = get_pie_v2(
            "select maxcapacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by maxcapacity",
            "最大产能",
        )
    if obj.get("optype") == "productionlkwkwineinfo.maxcapacity_line":
        res = get_line(
            "select maxcapacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by maxcapacity",
            "最大产能",
        )
    if obj.get("optype") == "productionlkwkwineinfo.maxcapacity_bar":
        res = get_bar(
            "select maxcapacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by maxcapacity",
            "最大产能",
        )
    if obj.get("optype") == "productionlkwkwineinfo.maxcapacity_bar_v1":
        res = get_bar_v1(
            "select maxcapacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by maxcapacity",
            "最大产能",
        )
    # productionlkwkwineinfo(生产线信息表)->makwkwintenancecycle(维护周期)

    if obj.get("optype") == "productionlkwkwineinfo.makwkwintenancecycle_pie":
        res = get_pie(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by makwkwintenancecycle order by x desc",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineinfo.makwkwintenancecycle_pie_v1":
        res = get_pie_v1(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by makwkwintenancecycle",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineinfo.makwkwintenancecycle_pie_v2":
        res = get_pie_v2(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by makwkwintenancecycle",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineinfo.makwkwintenancecycle_line":
        res = get_line(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by makwkwintenancecycle",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineinfo.makwkwintenancecycle_bar":
        res = get_bar(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by makwkwintenancecycle",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineinfo.makwkwintenancecycle_bar_v1":
        res = get_bar_v1(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by makwkwintenancecycle",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineinfo.lkwkwastmakwkwintenancedate_line":
        res = get_line(
            "select lkwkwastmakwkwintenancedate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by lkwkwastmakwkwintenancedate order by x",
            "上次维护日期",
        )
    # productionlkwkwineinfo(生产线信息表)->robotcount(机器人数量)

    if obj.get("optype") == "productionlkwkwineinfo.robotcount_pie":
        res = get_pie(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by robotcount order by x desc",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineinfo.robotcount_pie_v1":
        res = get_pie_v1(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineinfo.robotcount_pie_v2":
        res = get_pie_v2(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineinfo.robotcount_line":
        res = get_line(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineinfo.robotcount_bar":
        res = get_bar(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineinfo.robotcount_bar_v1":
        res = get_bar_v1(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by robotcount",
            "机器人数量",
        )
    # productionlkwkwineinfo(生产线信息表)->associatedfactkwkworyid(关联工厂ID)

    if obj.get("optype") == "productionlkwkwineinfo.associatedfactkwkworyid_pie":
        res = get_pie(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by associatedfactkwkworyid order by x desc",
            "关联工厂ID",
        )
    if obj.get("optype") == "productionlkwkwineinfo.associatedfactkwkworyid_pie_v1":
        res = get_pie_v1(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by associatedfactkwkworyid",
            "关联工厂ID",
        )
    if obj.get("optype") == "productionlkwkwineinfo.associatedfactkwkworyid_pie_v2":
        res = get_pie_v2(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by associatedfactkwkworyid",
            "关联工厂ID",
        )
    if obj.get("optype") == "productionlkwkwineinfo.associatedfactkwkworyid_line":
        res = get_line(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by associatedfactkwkworyid",
            "关联工厂ID",
        )
    if obj.get("optype") == "productionlkwkwineinfo.associatedfactkwkworyid_bar":
        res = get_bar(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by associatedfactkwkworyid",
            "关联工厂ID",
        )
    if obj.get("optype") == "productionlkwkwineinfo.associatedfactkwkworyid_bar_v1":
        res = get_bar_v1(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineinfo group by associatedfactkwkworyid",
            "关联工厂ID",
        )
    # safetymonitkwkworlog(安全监控日志表)->logid(日志ID)

    if obj.get("optype") == "safetymonitkwkworlog.logid_pie":
        res = get_pie(
            "select logid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by logid order by x desc",
            "日志ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.logid_pie_v1":
        res = get_pie_v1(
            "select logid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by logid",
            "日志ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.logid_pie_v2":
        res = get_pie_v2(
            "select logid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by logid",
            "日志ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.logid_line":
        res = get_line(
            "select logid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by logid",
            "日志ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.logid_bar":
        res = get_bar(
            "select logid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by logid",
            "日志ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.logid_bar_v1":
        res = get_bar_v1(
            "select logid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by logid",
            "日志ID",
        )
    # safetymonitkwkworlog(安全监控日志表)->deviceid(设备ID)

    if obj.get("optype") == "safetymonitkwkworlog.deviceid_pie":
        res = get_pie(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by deviceid order by x desc",
            "设备ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.deviceid_pie_v1":
        res = get_pie_v1(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by deviceid",
            "设备ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.deviceid_pie_v2":
        res = get_pie_v2(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by deviceid",
            "设备ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.deviceid_line":
        res = get_line(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by deviceid",
            "设备ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.deviceid_bar":
        res = get_bar(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by deviceid",
            "设备ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.deviceid_bar_v1":
        res = get_bar_v1(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by deviceid",
            "设备ID",
        )
    # safetymonitkwkworlog(安全监控日志表)->robotid(机器人ID)

    if obj.get("optype") == "safetymonitkwkworlog.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by robotid",
            "机器人ID",
        )
    # safetymonitkwkworlog(安全监控日志表)->eventtype(事件类型)

    if obj.get("optype") == "safetymonitkwkworlog.eventtype_pie":
        res = get_pie(
            "select eventtype x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by eventtype order by x desc",
            "事件类型",
        )
    if obj.get("optype") == "safetymonitkwkworlog.eventtype_pie_v1":
        res = get_pie_v1(
            "select eventtype x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by eventtype",
            "事件类型",
        )
    if obj.get("optype") == "safetymonitkwkworlog.eventtype_pie_v2":
        res = get_pie_v2(
            "select eventtype x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by eventtype",
            "事件类型",
        )
    if obj.get("optype") == "safetymonitkwkworlog.eventtype_line":
        res = get_line(
            "select eventtype x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by eventtype",
            "事件类型",
        )
    if obj.get("optype") == "safetymonitkwkworlog.eventtype_bar":
        res = get_bar(
            "select eventtype x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by eventtype",
            "事件类型",
        )
    if obj.get("optype") == "safetymonitkwkworlog.eventtype_bar_v1":
        res = get_bar_v1(
            "select eventtype x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by eventtype",
            "事件类型",
        )
    if obj.get("optype") == "safetymonitkwkworlog.eventtime_line":
        res = get_line(
            "select eventtime x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by eventtime order by x",
            "事件发生时间",
        )
    if obj.get("optype") == "safetymonitkwkworlog.eventdescription_wordcloud":
        textlist = get_data(
            "SELECT eventdescription result FROM vm780_bb1ff2b101947be5.safetymonitkwkworlog;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # safetymonitkwkworlog(安全监控日志表)->severity(严重程度)

    if obj.get("optype") == "safetymonitkwkworlog.severity_pie":
        res = get_pie(
            "select severity x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by severity order by x desc",
            "严重程度",
        )
    if obj.get("optype") == "safetymonitkwkworlog.severity_pie_v1":
        res = get_pie_v1(
            "select severity x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by severity",
            "严重程度",
        )
    if obj.get("optype") == "safetymonitkwkworlog.severity_pie_v2":
        res = get_pie_v2(
            "select severity x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by severity",
            "严重程度",
        )
    if obj.get("optype") == "safetymonitkwkworlog.severity_line":
        res = get_line(
            "select severity x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by severity",
            "严重程度",
        )
    if obj.get("optype") == "safetymonitkwkworlog.severity_bar":
        res = get_bar(
            "select severity x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by severity",
            "严重程度",
        )
    if obj.get("optype") == "safetymonitkwkworlog.severity_bar_v1":
        res = get_bar_v1(
            "select severity x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by severity",
            "严重程度",
        )
    # safetymonitkwkworlog(安全监控日志表)->actiontaken(采取的措施)

    if obj.get("optype") == "safetymonitkwkworlog.actiontaken_pie":
        res = get_pie(
            "select actiontaken x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by actiontaken order by x desc",
            "采取的措施",
        )
    if obj.get("optype") == "safetymonitkwkworlog.actiontaken_pie_v1":
        res = get_pie_v1(
            "select actiontaken x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by actiontaken",
            "采取的措施",
        )
    if obj.get("optype") == "safetymonitkwkworlog.actiontaken_pie_v2":
        res = get_pie_v2(
            "select actiontaken x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by actiontaken",
            "采取的措施",
        )
    if obj.get("optype") == "safetymonitkwkworlog.actiontaken_line":
        res = get_line(
            "select actiontaken x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by actiontaken",
            "采取的措施",
        )
    if obj.get("optype") == "safetymonitkwkworlog.actiontaken_bar":
        res = get_bar(
            "select actiontaken x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by actiontaken",
            "采取的措施",
        )
    if obj.get("optype") == "safetymonitkwkworlog.actiontaken_bar_v1":
        res = get_bar_v1(
            "select actiontaken x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by actiontaken",
            "采取的措施",
        )
    # safetymonitkwkworlog(安全监控日志表)->operatkwkworid(操作人员ID)

    if obj.get("optype") == "safetymonitkwkworlog.operatkwkworid_pie":
        res = get_pie(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by operatkwkworid order by x desc",
            "操作人员ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.operatkwkworid_pie_v1":
        res = get_pie_v1(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by operatkwkworid",
            "操作人员ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.operatkwkworid_pie_v2":
        res = get_pie_v2(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by operatkwkworid",
            "操作人员ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.operatkwkworid_line":
        res = get_line(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by operatkwkworid",
            "操作人员ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.operatkwkworid_bar":
        res = get_bar(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by operatkwkworid",
            "操作人员ID",
        )
    if obj.get("optype") == "safetymonitkwkworlog.operatkwkworid_bar_v1":
        res = get_bar_v1(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.safetymonitkwkworlog group by operatkwkworid",
            "操作人员ID",
        )
    if obj.get("optype") == "alarmreckwkword.alarmtime_line":
        res = get_line(
            "select alarmtime x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmtime order by x",
            "报警时间",
        )
    # alarmreckwkword(报警记录表)->alarmtype(报警类型)

    if obj.get("optype") == "alarmreckwkword.alarmtype_pie":
        res = get_pie(
            "select alarmtype x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmtype order by x desc",
            "报警类型",
        )
    if obj.get("optype") == "alarmreckwkword.alarmtype_pie_v1":
        res = get_pie_v1(
            "select alarmtype x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmtype",
            "报警类型",
        )
    if obj.get("optype") == "alarmreckwkword.alarmtype_pie_v2":
        res = get_pie_v2(
            "select alarmtype x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmtype",
            "报警类型",
        )
    if obj.get("optype") == "alarmreckwkword.alarmtype_line":
        res = get_line(
            "select alarmtype x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmtype",
            "报警类型",
        )
    if obj.get("optype") == "alarmreckwkword.alarmtype_bar":
        res = get_bar(
            "select alarmtype x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmtype",
            "报警类型",
        )
    if obj.get("optype") == "alarmreckwkword.alarmtype_bar_v1":
        res = get_bar_v1(
            "select alarmtype x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmtype",
            "报警类型",
        )
    # alarmreckwkword(报警记录表)->alarmlevel(报警等级)

    if obj.get("optype") == "alarmreckwkword.alarmlevel_pie":
        res = get_pie(
            "select alarmlevel x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmlevel order by x desc",
            "报警等级",
        )
    if obj.get("optype") == "alarmreckwkword.alarmlevel_pie_v1":
        res = get_pie_v1(
            "select alarmlevel x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmlevel",
            "报警等级",
        )
    if obj.get("optype") == "alarmreckwkword.alarmlevel_pie_v2":
        res = get_pie_v2(
            "select alarmlevel x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmlevel",
            "报警等级",
        )
    if obj.get("optype") == "alarmreckwkword.alarmlevel_line":
        res = get_line(
            "select alarmlevel x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmlevel",
            "报警等级",
        )
    if obj.get("optype") == "alarmreckwkword.alarmlevel_bar":
        res = get_bar(
            "select alarmlevel x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmlevel",
            "报警等级",
        )
    if obj.get("optype") == "alarmreckwkword.alarmlevel_bar_v1":
        res = get_bar_v1(
            "select alarmlevel x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by alarmlevel",
            "报警等级",
        )
    if obj.get("optype") == "alarmreckwkword.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm780_bb1ff2b101947be5.alarmreckwkword;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # alarmreckwkword(报警记录表)->robotid(机器人ID关联字段)

    if obj.get("optype") == "alarmreckwkword.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by robotid order by x desc",
            "机器人ID关联字段",
        )
    if obj.get("optype") == "alarmreckwkword.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by robotid",
            "机器人ID关联字段",
        )
    if obj.get("optype") == "alarmreckwkword.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by robotid",
            "机器人ID关联字段",
        )
    if obj.get("optype") == "alarmreckwkword.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by robotid",
            "机器人ID关联字段",
        )
    if obj.get("optype") == "alarmreckwkword.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by robotid",
            "机器人ID关联字段",
        )
    if obj.get("optype") == "alarmreckwkword.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by robotid",
            "机器人ID关联字段",
        )
    # alarmreckwkword(报警记录表)->resolved(是否已解决)

    if obj.get("optype") == "alarmreckwkword.resolved_pie":
        res = get_pie(
            "select resolved x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by resolved order by x desc",
            "是否已解决",
        )
    if obj.get("optype") == "alarmreckwkword.resolved_pie_v1":
        res = get_pie_v1(
            "select resolved x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by resolved",
            "是否已解决",
        )
    if obj.get("optype") == "alarmreckwkword.resolved_pie_v2":
        res = get_pie_v2(
            "select resolved x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by resolved",
            "是否已解决",
        )
    if obj.get("optype") == "alarmreckwkword.resolved_line":
        res = get_line(
            "select resolved x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by resolved",
            "是否已解决",
        )
    if obj.get("optype") == "alarmreckwkword.resolved_bar":
        res = get_bar(
            "select resolved x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by resolved",
            "是否已解决",
        )
    if obj.get("optype") == "alarmreckwkword.resolved_bar_v1":
        res = get_bar_v1(
            "select resolved x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by resolved",
            "是否已解决",
        )
    if obj.get("optype") == "alarmreckwkword.resolvedtime_line":
        res = get_line(
            "select resolvedtime x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by resolvedtime order by x",
            "解决时间",
        )
    # alarmreckwkword(报警记录表)->location(报警位置)

    if obj.get("optype") == "alarmreckwkword.location_pie":
        res = get_pie(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by location order by x desc",
            "报警位置",
        )
    if obj.get("optype") == "alarmreckwkword.location_pie_v1":
        res = get_pie_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by location",
            "报警位置",
        )
    if obj.get("optype") == "alarmreckwkword.location_pie_v2":
        res = get_pie_v2(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by location",
            "报警位置",
        )
    if obj.get("optype") == "alarmreckwkword.location_line":
        res = get_line(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by location",
            "报警位置",
        )
    if obj.get("optype") == "alarmreckwkword.location_bar":
        res = get_bar(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by location",
            "报警位置",
        )
    if obj.get("optype") == "alarmreckwkword.location_bar_v1":
        res = get_bar_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.alarmreckwkword group by location",
            "报警位置",
        )
    # robotlocation(机器人位置表)->robotid(机器人ID唯一标识每一个智能机器人的编号)

    if obj.get("optype") == "robotlocation.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by robotid order by x desc",
            "机器人ID唯一标识每一个智能机器人的编号",
        )
    if obj.get("optype") == "robotlocation.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by robotid",
            "机器人ID唯一标识每一个智能机器人的编号",
        )
    if obj.get("optype") == "robotlocation.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by robotid",
            "机器人ID唯一标识每一个智能机器人的编号",
        )
    if obj.get("optype") == "robotlocation.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by robotid",
            "机器人ID唯一标识每一个智能机器人的编号",
        )
    if obj.get("optype") == "robotlocation.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by robotid",
            "机器人ID唯一标识每一个智能机器人的编号",
        )
    if obj.get("optype") == "robotlocation.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by robotid",
            "机器人ID唯一标识每一个智能机器人的编号",
        )
    # robotlocation(机器人位置表)->locationcode(位置编码机器人当前所在位置的唯一编码)

    if obj.get("optype") == "robotlocation.locationcode_pie":
        res = get_pie(
            "select locationcode x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by locationcode order by x desc",
            "位置编码机器人当前所在位置的唯一编码",
        )
    if obj.get("optype") == "robotlocation.locationcode_pie_v1":
        res = get_pie_v1(
            "select locationcode x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by locationcode",
            "位置编码机器人当前所在位置的唯一编码",
        )
    if obj.get("optype") == "robotlocation.locationcode_pie_v2":
        res = get_pie_v2(
            "select locationcode x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by locationcode",
            "位置编码机器人当前所在位置的唯一编码",
        )
    if obj.get("optype") == "robotlocation.locationcode_line":
        res = get_line(
            "select locationcode x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by locationcode",
            "位置编码机器人当前所在位置的唯一编码",
        )
    if obj.get("optype") == "robotlocation.locationcode_bar":
        res = get_bar(
            "select locationcode x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by locationcode",
            "位置编码机器人当前所在位置的唯一编码",
        )
    if obj.get("optype") == "robotlocation.locationcode_bar_v1":
        res = get_bar_v1(
            "select locationcode x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by locationcode",
            "位置编码机器人当前所在位置的唯一编码",
        )
    # robotlocation(机器人位置表)->areaname(区域名称机器人所在区域的名称)

    if obj.get("optype") == "robotlocation.areaname_pie":
        res = get_pie(
            "select areaname x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by areaname order by x desc",
            "区域名称机器人所在区域的名称",
        )
    if obj.get("optype") == "robotlocation.areaname_pie_v1":
        res = get_pie_v1(
            "select areaname x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by areaname",
            "区域名称机器人所在区域的名称",
        )
    if obj.get("optype") == "robotlocation.areaname_pie_v2":
        res = get_pie_v2(
            "select areaname x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by areaname",
            "区域名称机器人所在区域的名称",
        )
    if obj.get("optype") == "robotlocation.areaname_line":
        res = get_line(
            "select areaname x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by areaname",
            "区域名称机器人所在区域的名称",
        )
    if obj.get("optype") == "robotlocation.areaname_bar":
        res = get_bar(
            "select areaname x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by areaname",
            "区域名称机器人所在区域的名称",
        )
    if obj.get("optype") == "robotlocation.areaname_bar_v1":
        res = get_bar_v1(
            "select areaname x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by areaname",
            "区域名称机器人所在区域的名称",
        )
    # robotlocation(机器人位置表)->xcokwkwordkwkwinatex(坐标机器人在该区域内的X轴坐标)

    if obj.get("optype") == "robotlocation.xcokwkwordkwkwinatex_pie":
        res = get_pie(
            "select xcokwkwordkwkwinatex x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by xcokwkwordkwkwinatex order by x desc",
            "坐标机器人在该区域内的X轴坐标",
        )
    if obj.get("optype") == "robotlocation.xcokwkwordkwkwinatex_pie_v1":
        res = get_pie_v1(
            "select xcokwkwordkwkwinatex x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by xcokwkwordkwkwinatex",
            "坐标机器人在该区域内的X轴坐标",
        )
    if obj.get("optype") == "robotlocation.xcokwkwordkwkwinatex_pie_v2":
        res = get_pie_v2(
            "select xcokwkwordkwkwinatex x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by xcokwkwordkwkwinatex",
            "坐标机器人在该区域内的X轴坐标",
        )
    if obj.get("optype") == "robotlocation.xcokwkwordkwkwinatex_line":
        res = get_line(
            "select xcokwkwordkwkwinatex x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by xcokwkwordkwkwinatex",
            "坐标机器人在该区域内的X轴坐标",
        )
    if obj.get("optype") == "robotlocation.xcokwkwordkwkwinatex_bar":
        res = get_bar(
            "select xcokwkwordkwkwinatex x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by xcokwkwordkwkwinatex",
            "坐标机器人在该区域内的X轴坐标",
        )
    if obj.get("optype") == "robotlocation.xcokwkwordkwkwinatex_bar_v1":
        res = get_bar_v1(
            "select xcokwkwordkwkwinatex x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by xcokwkwordkwkwinatex",
            "坐标机器人在该区域内的X轴坐标",
        )
    # robotlocation(机器人位置表)->ycokwkwordkwkwinatey(坐标机器人在该区域内的Y轴坐标)

    if obj.get("optype") == "robotlocation.ycokwkwordkwkwinatey_pie":
        res = get_pie(
            "select ycokwkwordkwkwinatey x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by ycokwkwordkwkwinatey order by x desc",
            "坐标机器人在该区域内的Y轴坐标",
        )
    if obj.get("optype") == "robotlocation.ycokwkwordkwkwinatey_pie_v1":
        res = get_pie_v1(
            "select ycokwkwordkwkwinatey x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by ycokwkwordkwkwinatey",
            "坐标机器人在该区域内的Y轴坐标",
        )
    if obj.get("optype") == "robotlocation.ycokwkwordkwkwinatey_pie_v2":
        res = get_pie_v2(
            "select ycokwkwordkwkwinatey x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by ycokwkwordkwkwinatey",
            "坐标机器人在该区域内的Y轴坐标",
        )
    if obj.get("optype") == "robotlocation.ycokwkwordkwkwinatey_line":
        res = get_line(
            "select ycokwkwordkwkwinatey x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by ycokwkwordkwkwinatey",
            "坐标机器人在该区域内的Y轴坐标",
        )
    if obj.get("optype") == "robotlocation.ycokwkwordkwkwinatey_bar":
        res = get_bar(
            "select ycokwkwordkwkwinatey x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by ycokwkwordkwkwinatey",
            "坐标机器人在该区域内的Y轴坐标",
        )
    if obj.get("optype") == "robotlocation.ycokwkwordkwkwinatey_bar_v1":
        res = get_bar_v1(
            "select ycokwkwordkwkwinatey x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by ycokwkwordkwkwinatey",
            "坐标机器人在该区域内的Y轴坐标",
        )
    # robotlocation(机器人位置表)->zcokwkwordkwkwinatez(坐标机器人在该区域内的Z轴坐标如果适用)

    if obj.get("optype") == "robotlocation.zcokwkwordkwkwinatez_pie":
        res = get_pie(
            "select zcokwkwordkwkwinatez x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by zcokwkwordkwkwinatez order by x desc",
            "坐标机器人在该区域内的Z轴坐标如果适用",
        )
    if obj.get("optype") == "robotlocation.zcokwkwordkwkwinatez_pie_v1":
        res = get_pie_v1(
            "select zcokwkwordkwkwinatez x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by zcokwkwordkwkwinatez",
            "坐标机器人在该区域内的Z轴坐标如果适用",
        )
    if obj.get("optype") == "robotlocation.zcokwkwordkwkwinatez_pie_v2":
        res = get_pie_v2(
            "select zcokwkwordkwkwinatez x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by zcokwkwordkwkwinatez",
            "坐标机器人在该区域内的Z轴坐标如果适用",
        )
    if obj.get("optype") == "robotlocation.zcokwkwordkwkwinatez_line":
        res = get_line(
            "select zcokwkwordkwkwinatez x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by zcokwkwordkwkwinatez",
            "坐标机器人在该区域内的Z轴坐标如果适用",
        )
    if obj.get("optype") == "robotlocation.zcokwkwordkwkwinatez_bar":
        res = get_bar(
            "select zcokwkwordkwkwinatez x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by zcokwkwordkwkwinatez",
            "坐标机器人在该区域内的Z轴坐标如果适用",
        )
    if obj.get("optype") == "robotlocation.zcokwkwordkwkwinatez_bar_v1":
        res = get_bar_v1(
            "select zcokwkwordkwkwinatez x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by zcokwkwordkwkwinatez",
            "坐标机器人在该区域内的Z轴坐标如果适用",
        )
    # robotlocation(机器人位置表)->status(状态机器人的当前状态如“运行中”、“空闲”、“故障”等)

    if obj.get("optype") == "robotlocation.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by status order by x desc",
            "状态机器人的当前状态如“运行中”、“空闲”、“故障”等",
        )
    if obj.get("optype") == "robotlocation.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by status",
            "状态机器人的当前状态如“运行中”、“空闲”、“故障”等",
        )
    if obj.get("optype") == "robotlocation.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by status",
            "状态机器人的当前状态如“运行中”、“空闲”、“故障”等",
        )
    if obj.get("optype") == "robotlocation.status_line":
        res = get_line(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by status",
            "状态机器人的当前状态如“运行中”、“空闲”、“故障”等",
        )
    if obj.get("optype") == "robotlocation.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by status",
            "状态机器人的当前状态如“运行中”、“空闲”、“故障”等",
        )
    if obj.get("optype") == "robotlocation.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by status",
            "状态机器人的当前状态如“运行中”、“空闲”、“故障”等",
        )
    if obj.get("optype") == "robotlocation.lkwkwastupdatetime_line":
        res = get_line(
            "select lkwkwastupdatetime x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by lkwkwastupdatetime order by x",
            "最后更新时间机器人位置信息最后一次更新的时间",
        )
    # robotlocation(机器人位置表)->wkwkworkstationid(工作站ID机器人当前所在的工作站的ID关联字段)

    if obj.get("optype") == "robotlocation.wkwkworkstationid_pie":
        res = get_pie(
            "select wkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by wkwkworkstationid order by x desc",
            "工作站ID机器人当前所在的工作站的ID关联字段",
        )
    if obj.get("optype") == "robotlocation.wkwkworkstationid_pie_v1":
        res = get_pie_v1(
            "select wkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by wkwkworkstationid",
            "工作站ID机器人当前所在的工作站的ID关联字段",
        )
    if obj.get("optype") == "robotlocation.wkwkworkstationid_pie_v2":
        res = get_pie_v2(
            "select wkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by wkwkworkstationid",
            "工作站ID机器人当前所在的工作站的ID关联字段",
        )
    if obj.get("optype") == "robotlocation.wkwkworkstationid_line":
        res = get_line(
            "select wkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by wkwkworkstationid",
            "工作站ID机器人当前所在的工作站的ID关联字段",
        )
    if obj.get("optype") == "robotlocation.wkwkworkstationid_bar":
        res = get_bar(
            "select wkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by wkwkworkstationid",
            "工作站ID机器人当前所在的工作站的ID关联字段",
        )
    if obj.get("optype") == "robotlocation.wkwkworkstationid_bar_v1":
        res = get_bar_v1(
            "select wkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotlocation group by wkwkworkstationid",
            "工作站ID机器人当前所在的工作站的ID关联字段",
        )
    # robotstatus(机器人状态表)->robotid(机器人ID)

    if obj.get("optype") == "robotstatus.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "robotstatus.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotstatus.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotstatus.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotstatus.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotstatus.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by robotid",
            "机器人ID",
        )
    # robotstatus(机器人状态表)->status(状态)

    if obj.get("optype") == "robotstatus.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by status order by x desc",
            "状态",
        )
    if obj.get("optype") == "robotstatus.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by status",
            "状态",
        )
    if obj.get("optype") == "robotstatus.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by status",
            "状态",
        )
    if obj.get("optype") == "robotstatus.status_line":
        res = get_line(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by status",
            "状态",
        )
    if obj.get("optype") == "robotstatus.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by status",
            "状态",
        )
    if obj.get("optype") == "robotstatus.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by status",
            "状态",
        )
    if obj.get("optype") == "robotstatus.timestamp_line":
        res = get_line(
            "select timestamp x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by timestamp order by x",
            "时间戳",
        )
    # robotstatus(机器人状态表)->location(位置)

    if obj.get("optype") == "robotstatus.location_pie":
        res = get_pie(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by location order by x desc",
            "位置",
        )
    if obj.get("optype") == "robotstatus.location_pie_v1":
        res = get_pie_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by location",
            "位置",
        )
    if obj.get("optype") == "robotstatus.location_pie_v2":
        res = get_pie_v2(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by location",
            "位置",
        )
    if obj.get("optype") == "robotstatus.location_line":
        res = get_line(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by location",
            "位置",
        )
    if obj.get("optype") == "robotstatus.location_bar":
        res = get_bar(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by location",
            "位置",
        )
    if obj.get("optype") == "robotstatus.location_bar_v1":
        res = get_bar_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by location",
            "位置",
        )
    # robotstatus(机器人状态表)->tkwkwaskid(任务ID)

    if obj.get("optype") == "robotstatus.tkwkwaskid_pie":
        res = get_pie(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by tkwkwaskid order by x desc",
            "任务ID",
        )
    if obj.get("optype") == "robotstatus.tkwkwaskid_pie_v1":
        res = get_pie_v1(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "robotstatus.tkwkwaskid_pie_v2":
        res = get_pie_v2(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "robotstatus.tkwkwaskid_line":
        res = get_line(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "robotstatus.tkwkwaskid_bar":
        res = get_bar(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "robotstatus.tkwkwaskid_bar_v1":
        res = get_bar_v1(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by tkwkwaskid",
            "任务ID",
        )
    # robotstatus(机器人状态表)->faultcode(故障代码)

    if obj.get("optype") == "robotstatus.faultcode_pie":
        res = get_pie(
            "select faultcode x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by faultcode order by x desc",
            "故障代码",
        )
    if obj.get("optype") == "robotstatus.faultcode_pie_v1":
        res = get_pie_v1(
            "select faultcode x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by faultcode",
            "故障代码",
        )
    if obj.get("optype") == "robotstatus.faultcode_pie_v2":
        res = get_pie_v2(
            "select faultcode x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by faultcode",
            "故障代码",
        )
    if obj.get("optype") == "robotstatus.faultcode_line":
        res = get_line(
            "select faultcode x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by faultcode",
            "故障代码",
        )
    if obj.get("optype") == "robotstatus.faultcode_bar":
        res = get_bar(
            "select faultcode x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by faultcode",
            "故障代码",
        )
    if obj.get("optype") == "robotstatus.faultcode_bar_v1":
        res = get_bar_v1(
            "select faultcode x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by faultcode",
            "故障代码",
        )
    # robotstatus(机器人状态表)->makwkwintenanceflag(维护标志)

    if obj.get("optype") == "robotstatus.makwkwintenanceflag_pie":
        res = get_pie(
            "select makwkwintenanceflag x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by makwkwintenanceflag order by x desc",
            "维护标志",
        )
    if obj.get("optype") == "robotstatus.makwkwintenanceflag_pie_v1":
        res = get_pie_v1(
            "select makwkwintenanceflag x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by makwkwintenanceflag",
            "维护标志",
        )
    if obj.get("optype") == "robotstatus.makwkwintenanceflag_pie_v2":
        res = get_pie_v2(
            "select makwkwintenanceflag x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by makwkwintenanceflag",
            "维护标志",
        )
    if obj.get("optype") == "robotstatus.makwkwintenanceflag_line":
        res = get_line(
            "select makwkwintenanceflag x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by makwkwintenanceflag",
            "维护标志",
        )
    if obj.get("optype") == "robotstatus.makwkwintenanceflag_bar":
        res = get_bar(
            "select makwkwintenanceflag x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by makwkwintenanceflag",
            "维护标志",
        )
    if obj.get("optype") == "robotstatus.makwkwintenanceflag_bar_v1":
        res = get_bar_v1(
            "select makwkwintenanceflag x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by makwkwintenanceflag",
            "维护标志",
        )
    # robotstatus(机器人状态表)->powerlevel(电量水平)

    if obj.get("optype") == "robotstatus.powerlevel_pie":
        res = get_pie(
            "select powerlevel x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by powerlevel order by x desc",
            "电量水平",
        )
    if obj.get("optype") == "robotstatus.powerlevel_pie_v1":
        res = get_pie_v1(
            "select powerlevel x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by powerlevel",
            "电量水平",
        )
    if obj.get("optype") == "robotstatus.powerlevel_pie_v2":
        res = get_pie_v2(
            "select powerlevel x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by powerlevel",
            "电量水平",
        )
    if obj.get("optype") == "robotstatus.powerlevel_line":
        res = get_line(
            "select powerlevel x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by powerlevel",
            "电量水平",
        )
    if obj.get("optype") == "robotstatus.powerlevel_bar":
        res = get_bar(
            "select powerlevel x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by powerlevel",
            "电量水平",
        )
    if obj.get("optype") == "robotstatus.powerlevel_bar_v1":
        res = get_bar_v1(
            "select powerlevel x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by powerlevel",
            "电量水平",
        )
    if obj.get("optype") == "robotstatus.lkwkwastmakwkwintenancedate_line":
        res = get_line(
            "select lkwkwastmakwkwintenancedate x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by lkwkwastmakwkwintenancedate order by x",
            "上次维护日期",
        )
    # robotstatus(机器人状态表)->associatedwkwkworkstationid(关联工作站ID)

    if obj.get("optype") == "robotstatus.associatedwkwkworkstationid_pie":
        res = get_pie(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by associatedwkwkworkstationid order by x desc",
            "关联工作站ID",
        )
    if obj.get("optype") == "robotstatus.associatedwkwkworkstationid_pie_v1":
        res = get_pie_v1(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by associatedwkwkworkstationid",
            "关联工作站ID",
        )
    if obj.get("optype") == "robotstatus.associatedwkwkworkstationid_pie_v2":
        res = get_pie_v2(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by associatedwkwkworkstationid",
            "关联工作站ID",
        )
    if obj.get("optype") == "robotstatus.associatedwkwkworkstationid_line":
        res = get_line(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by associatedwkwkworkstationid",
            "关联工作站ID",
        )
    if obj.get("optype") == "robotstatus.associatedwkwkworkstationid_bar":
        res = get_bar(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by associatedwkwkworkstationid",
            "关联工作站ID",
        )
    if obj.get("optype") == "robotstatus.associatedwkwkworkstationid_bar_v1":
        res = get_bar_v1(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotstatus group by associatedwkwkworkstationid",
            "关联工作站ID",
        )
    # robottkwkwask(机器人任务表)->tkwkwaskid(任务ID)

    if obj.get("optype") == "robottkwkwask.tkwkwaskid_pie":
        res = get_pie(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskid order by x desc",
            "任务ID",
        )
    if obj.get("optype") == "robottkwkwask.tkwkwaskid_pie_v1":
        res = get_pie_v1(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "robottkwkwask.tkwkwaskid_pie_v2":
        res = get_pie_v2(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "robottkwkwask.tkwkwaskid_line":
        res = get_line(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "robottkwkwask.tkwkwaskid_bar":
        res = get_bar(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "robottkwkwask.tkwkwaskid_bar_v1":
        res = get_bar_v1(
            "select tkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskid",
            "任务ID",
        )
    # robottkwkwask(机器人任务表)->robotid(机器人ID)

    if obj.get("optype") == "robottkwkwask.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "robottkwkwask.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robottkwkwask.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robottkwkwask.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robottkwkwask.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robottkwkwask.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by robotid",
            "机器人ID",
        )
    # robottkwkwask(机器人任务表)->tkwkwaskname(任务名称)

    if obj.get("optype") == "robottkwkwask.tkwkwaskname_pie":
        res = get_pie(
            "select tkwkwaskname x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskname order by x desc",
            "任务名称",
        )
    if obj.get("optype") == "robottkwkwask.tkwkwaskname_pie_v1":
        res = get_pie_v1(
            "select tkwkwaskname x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "robottkwkwask.tkwkwaskname_pie_v2":
        res = get_pie_v2(
            "select tkwkwaskname x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "robottkwkwask.tkwkwaskname_line":
        res = get_line(
            "select tkwkwaskname x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "robottkwkwask.tkwkwaskname_bar":
        res = get_bar(
            "select tkwkwaskname x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "robottkwkwask.tkwkwaskname_bar_v1":
        res = get_bar_v1(
            "select tkwkwaskname x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by tkwkwaskname",
            "任务名称",
        )
    if obj.get("optype") == "robottkwkwask.starttime_line":
        res = get_line(
            "select starttime x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by starttime order by x",
            "开始时间",
        )
    if obj.get("optype") == "robottkwkwask.endtime_line":
        res = get_line(
            "select endtime x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by endtime order by x",
            "结束时间",
        )
    # robottkwkwask(机器人任务表)->status(任务状态)

    if obj.get("optype") == "robottkwkwask.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by status order by x desc",
            "任务状态",
        )
    if obj.get("optype") == "robottkwkwask.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by status",
            "任务状态",
        )
    if obj.get("optype") == "robottkwkwask.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by status",
            "任务状态",
        )
    if obj.get("optype") == "robottkwkwask.status_line":
        res = get_line(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by status",
            "任务状态",
        )
    if obj.get("optype") == "robottkwkwask.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by status",
            "任务状态",
        )
    if obj.get("optype") == "robottkwkwask.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by status",
            "任务状态",
        )
    # robottkwkwask(机器人任务表)->prikwkwority(任务优先级)

    if obj.get("optype") == "robottkwkwask.prikwkwority_pie":
        res = get_pie(
            "select prikwkwority x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by prikwkwority order by x desc",
            "任务优先级",
        )
    if obj.get("optype") == "robottkwkwask.prikwkwority_pie_v1":
        res = get_pie_v1(
            "select prikwkwority x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by prikwkwority",
            "任务优先级",
        )
    if obj.get("optype") == "robottkwkwask.prikwkwority_pie_v2":
        res = get_pie_v2(
            "select prikwkwority x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by prikwkwority",
            "任务优先级",
        )
    if obj.get("optype") == "robottkwkwask.prikwkwority_line":
        res = get_line(
            "select prikwkwority x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by prikwkwority",
            "任务优先级",
        )
    if obj.get("optype") == "robottkwkwask.prikwkwority_bar":
        res = get_bar(
            "select prikwkwority x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by prikwkwority",
            "任务优先级",
        )
    if obj.get("optype") == "robottkwkwask.prikwkwority_bar_v1":
        res = get_bar_v1(
            "select prikwkwority x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by prikwkwority",
            "任务优先级",
        )
    # robottkwkwask(机器人任务表)->details(任务详情)

    if obj.get("optype") == "robottkwkwask.details_pie":
        res = get_pie(
            "select details x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by details order by x desc",
            "任务详情",
        )
    if obj.get("optype") == "robottkwkwask.details_pie_v1":
        res = get_pie_v1(
            "select details x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by details",
            "任务详情",
        )
    if obj.get("optype") == "robottkwkwask.details_pie_v2":
        res = get_pie_v2(
            "select details x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by details",
            "任务详情",
        )
    if obj.get("optype") == "robottkwkwask.details_line":
        res = get_line(
            "select details x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by details",
            "任务详情",
        )
    if obj.get("optype") == "robottkwkwask.details_bar":
        res = get_bar(
            "select details x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by details",
            "任务详情",
        )
    if obj.get("optype") == "robottkwkwask.details_bar_v1":
        res = get_bar_v1(
            "select details x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by details",
            "任务详情",
        )
    # robottkwkwask(机器人任务表)->failurerekwkwason(失败原因)

    if obj.get("optype") == "robottkwkwask.failurerekwkwason_pie":
        res = get_pie(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by failurerekwkwason order by x desc",
            "失败原因",
        )
    if obj.get("optype") == "robottkwkwask.failurerekwkwason_pie_v1":
        res = get_pie_v1(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "robottkwkwask.failurerekwkwason_pie_v2":
        res = get_pie_v2(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "robottkwkwask.failurerekwkwason_line":
        res = get_line(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "robottkwkwask.failurerekwkwason_bar":
        res = get_bar(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "robottkwkwask.failurerekwkwason_bar_v1":
        res = get_bar_v1(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by failurerekwkwason",
            "失败原因",
        )
    # robottkwkwask(机器人任务表)->associatedprocessid(关联流程ID)

    if obj.get("optype") == "robottkwkwask.associatedprocessid_pie":
        res = get_pie(
            "select associatedprocessid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by associatedprocessid order by x desc",
            "关联流程ID",
        )
    if obj.get("optype") == "robottkwkwask.associatedprocessid_pie_v1":
        res = get_pie_v1(
            "select associatedprocessid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by associatedprocessid",
            "关联流程ID",
        )
    if obj.get("optype") == "robottkwkwask.associatedprocessid_pie_v2":
        res = get_pie_v2(
            "select associatedprocessid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by associatedprocessid",
            "关联流程ID",
        )
    if obj.get("optype") == "robottkwkwask.associatedprocessid_line":
        res = get_line(
            "select associatedprocessid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by associatedprocessid",
            "关联流程ID",
        )
    if obj.get("optype") == "robottkwkwask.associatedprocessid_bar":
        res = get_bar(
            "select associatedprocessid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by associatedprocessid",
            "关联流程ID",
        )
    if obj.get("optype") == "robottkwkwask.associatedprocessid_bar_v1":
        res = get_bar_v1(
            "select associatedprocessid x,count(*) y from vm780_bb1ff2b101947be5.robottkwkwask group by associatedprocessid",
            "关联流程ID",
        )
    # productionlkwkwineconfig(生产线配置表)->lkwkwineid(生产线ID)

    if obj.get("optype") == "productionlkwkwineconfig.lkwkwineid_pie":
        res = get_pie(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwineid order by x desc",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwineid_pie_v1":
        res = get_pie_v1(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwineid_pie_v2":
        res = get_pie_v2(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwineid_line":
        res = get_line(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwineid_bar":
        res = get_bar(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwineid_bar_v1":
        res = get_bar_v1(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwineid",
            "生产线ID",
        )
    # productionlkwkwineconfig(生产线配置表)->lkwkwinename(生产线名称)

    if obj.get("optype") == "productionlkwkwineconfig.lkwkwinename_pie":
        res = get_pie(
            "select lkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwinename order by x desc",
            "生产线名称",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwinename_pie_v1":
        res = get_pie_v1(
            "select lkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwinename",
            "生产线名称",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwinename_pie_v2":
        res = get_pie_v2(
            "select lkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwinename",
            "生产线名称",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwinename_line":
        res = get_line(
            "select lkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwinename",
            "生产线名称",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwinename_bar":
        res = get_bar(
            "select lkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwinename",
            "生产线名称",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwinename_bar_v1":
        res = get_bar_v1(
            "select lkwkwinename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwinename",
            "生产线名称",
        )
    # productionlkwkwineconfig(生产线配置表)->location(生产线位置)

    if obj.get("optype") == "productionlkwkwineconfig.location_pie":
        res = get_pie(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by location order by x desc",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineconfig.location_pie_v1":
        res = get_pie_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by location",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineconfig.location_pie_v2":
        res = get_pie_v2(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by location",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineconfig.location_line":
        res = get_line(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by location",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineconfig.location_bar":
        res = get_bar(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by location",
            "生产线位置",
        )
    if obj.get("optype") == "productionlkwkwineconfig.location_bar_v1":
        res = get_bar_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by location",
            "生产线位置",
        )
    # productionlkwkwineconfig(生产线配置表)->capacity(产能)

    if obj.get("optype") == "productionlkwkwineconfig.capacity_pie":
        res = get_pie(
            "select capacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by capacity order by x desc",
            "产能",
        )
    if obj.get("optype") == "productionlkwkwineconfig.capacity_pie_v1":
        res = get_pie_v1(
            "select capacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by capacity",
            "产能",
        )
    if obj.get("optype") == "productionlkwkwineconfig.capacity_pie_v2":
        res = get_pie_v2(
            "select capacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by capacity",
            "产能",
        )
    if obj.get("optype") == "productionlkwkwineconfig.capacity_line":
        res = get_line(
            "select capacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by capacity",
            "产能",
        )
    if obj.get("optype") == "productionlkwkwineconfig.capacity_bar":
        res = get_bar(
            "select capacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by capacity",
            "产能",
        )
    if obj.get("optype") == "productionlkwkwineconfig.capacity_bar_v1":
        res = get_bar_v1(
            "select capacity x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by capacity",
            "产能",
        )
    # productionlkwkwineconfig(生产线配置表)->status(生产线状态)

    if obj.get("optype") == "productionlkwkwineconfig.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by status order by x desc",
            "生产线状态",
        )
    if obj.get("optype") == "productionlkwkwineconfig.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by status",
            "生产线状态",
        )
    if obj.get("optype") == "productionlkwkwineconfig.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by status",
            "生产线状态",
        )
    if obj.get("optype") == "productionlkwkwineconfig.status_line":
        res = get_line(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by status",
            "生产线状态",
        )
    if obj.get("optype") == "productionlkwkwineconfig.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by status",
            "生产线状态",
        )
    if obj.get("optype") == "productionlkwkwineconfig.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by status",
            "生产线状态",
        )
    if obj.get("optype") == "productionlkwkwineconfig.creationtime_line":
        res = get_line(
            "select creationtime x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by creationtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "productionlkwkwineconfig.lkwkwastupdatetime_line":
        res = get_line(
            "select lkwkwastupdatetime x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by lkwkwastupdatetime order by x",
            "最后更新时间",
        )
    # productionlkwkwineconfig(生产线配置表)->robotcount(机器人数量)

    if obj.get("optype") == "productionlkwkwineconfig.robotcount_pie":
        res = get_pie(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by robotcount order by x desc",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineconfig.robotcount_pie_v1":
        res = get_pie_v1(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineconfig.robotcount_pie_v2":
        res = get_pie_v2(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineconfig.robotcount_line":
        res = get_line(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineconfig.robotcount_bar":
        res = get_bar(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineconfig.robotcount_bar_v1":
        res = get_bar_v1(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by robotcount",
            "机器人数量",
        )
    # productionlkwkwineconfig(生产线配置表)->makwkwintenancecycle(维护周期)

    if obj.get("optype") == "productionlkwkwineconfig.makwkwintenancecycle_pie":
        res = get_pie(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by makwkwintenancecycle order by x desc",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineconfig.makwkwintenancecycle_pie_v1":
        res = get_pie_v1(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by makwkwintenancecycle",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineconfig.makwkwintenancecycle_pie_v2":
        res = get_pie_v2(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by makwkwintenancecycle",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineconfig.makwkwintenancecycle_line":
        res = get_line(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by makwkwintenancecycle",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineconfig.makwkwintenancecycle_bar":
        res = get_bar(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by makwkwintenancecycle",
            "维护周期",
        )
    if obj.get("optype") == "productionlkwkwineconfig.makwkwintenancecycle_bar_v1":
        res = get_bar_v1(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by makwkwintenancecycle",
            "维护周期",
        )
    # productionlkwkwineconfig(生产线配置表)->associatedfactkwkworyid(关联工厂ID)

    if obj.get("optype") == "productionlkwkwineconfig.associatedfactkwkworyid_pie":
        res = get_pie(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by associatedfactkwkworyid order by x desc",
            "关联工厂ID",
        )
    if obj.get("optype") == "productionlkwkwineconfig.associatedfactkwkworyid_pie_v1":
        res = get_pie_v1(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by associatedfactkwkworyid",
            "关联工厂ID",
        )
    if obj.get("optype") == "productionlkwkwineconfig.associatedfactkwkworyid_pie_v2":
        res = get_pie_v2(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by associatedfactkwkworyid",
            "关联工厂ID",
        )
    if obj.get("optype") == "productionlkwkwineconfig.associatedfactkwkworyid_line":
        res = get_line(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by associatedfactkwkworyid",
            "关联工厂ID",
        )
    if obj.get("optype") == "productionlkwkwineconfig.associatedfactkwkworyid_bar":
        res = get_bar(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by associatedfactkwkworyid",
            "关联工厂ID",
        )
    if obj.get("optype") == "productionlkwkwineconfig.associatedfactkwkworyid_bar_v1":
        res = get_bar_v1(
            "select associatedfactkwkworyid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineconfig group by associatedfactkwkworyid",
            "关联工厂ID",
        )
    # permkwkwissionmanagement(权限管理表)->permkwkwissionname(权限名称)

    if obj.get("optype") == "permkwkwissionmanagement.permkwkwissionname_pie":
        res = get_pie(
            "select permkwkwissionname x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by permkwkwissionname order by x desc",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissionmanagement.permkwkwissionname_pie_v1":
        res = get_pie_v1(
            "select permkwkwissionname x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissionmanagement.permkwkwissionname_pie_v2":
        res = get_pie_v2(
            "select permkwkwissionname x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissionmanagement.permkwkwissionname_line":
        res = get_line(
            "select permkwkwissionname x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissionmanagement.permkwkwissionname_bar":
        res = get_bar(
            "select permkwkwissionname x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissionmanagement.permkwkwissionname_bar_v1":
        res = get_bar_v1(
            "select permkwkwissionname x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "permkwkwissionmanagement.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm780_bb1ff2b101947be5.permkwkwissionmanagement;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "permkwkwissionmanagement.createdtime_line":
        res = get_line(
            "select createdtime x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by createdtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "permkwkwissionmanagement.updatedtime_line":
        res = get_line(
            "select updatedtime x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by updatedtime order by x",
            "更新时间",
        )
    # permkwkwissionmanagement(权限管理表)->status(状态如启用禁用)

    if obj.get("optype") == "permkwkwissionmanagement.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by status order by x desc",
            "状态如启用禁用",
        )
    if obj.get("optype") == "permkwkwissionmanagement.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by status",
            "状态如启用禁用",
        )
    if obj.get("optype") == "permkwkwissionmanagement.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by status",
            "状态如启用禁用",
        )
    if obj.get("optype") == "permkwkwissionmanagement.status_line":
        res = get_line(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by status",
            "状态如启用禁用",
        )
    if obj.get("optype") == "permkwkwissionmanagement.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by status",
            "状态如启用禁用",
        )
    if obj.get("optype") == "permkwkwissionmanagement.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by status",
            "状态如启用禁用",
        )
    # permkwkwissionmanagement(权限管理表)->roleid(关联角色ID)

    if obj.get("optype") == "permkwkwissionmanagement.roleid_pie":
        res = get_pie(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by roleid order by x desc",
            "关联角色ID",
        )
    if obj.get("optype") == "permkwkwissionmanagement.roleid_pie_v1":
        res = get_pie_v1(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by roleid",
            "关联角色ID",
        )
    if obj.get("optype") == "permkwkwissionmanagement.roleid_pie_v2":
        res = get_pie_v2(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by roleid",
            "关联角色ID",
        )
    if obj.get("optype") == "permkwkwissionmanagement.roleid_line":
        res = get_line(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by roleid",
            "关联角色ID",
        )
    if obj.get("optype") == "permkwkwissionmanagement.roleid_bar":
        res = get_bar(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by roleid",
            "关联角色ID",
        )
    if obj.get("optype") == "permkwkwissionmanagement.roleid_bar_v1":
        res = get_bar_v1(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by roleid",
            "关联角色ID",
        )
    # permkwkwissionmanagement(权限管理表)->userid(关联用户ID可选用于特定用户权限)

    if obj.get("optype") == "permkwkwissionmanagement.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by userid order by x desc",
            "关联用户ID可选用于特定用户权限",
        )
    if obj.get("optype") == "permkwkwissionmanagement.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by userid",
            "关联用户ID可选用于特定用户权限",
        )
    if obj.get("optype") == "permkwkwissionmanagement.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by userid",
            "关联用户ID可选用于特定用户权限",
        )
    if obj.get("optype") == "permkwkwissionmanagement.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by userid",
            "关联用户ID可选用于特定用户权限",
        )
    if obj.get("optype") == "permkwkwissionmanagement.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by userid",
            "关联用户ID可选用于特定用户权限",
        )
    if obj.get("optype") == "permkwkwissionmanagement.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by userid",
            "关联用户ID可选用于特定用户权限",
        )
    # permkwkwissionmanagement(权限管理表)->systemmodule(系统模块如生产监控、设备控制等)

    if obj.get("optype") == "permkwkwissionmanagement.systemmodule_pie":
        res = get_pie(
            "select systemmodule x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by systemmodule order by x desc",
            "系统模块如生产监控、设备控制等",
        )
    if obj.get("optype") == "permkwkwissionmanagement.systemmodule_pie_v1":
        res = get_pie_v1(
            "select systemmodule x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by systemmodule",
            "系统模块如生产监控、设备控制等",
        )
    if obj.get("optype") == "permkwkwissionmanagement.systemmodule_pie_v2":
        res = get_pie_v2(
            "select systemmodule x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by systemmodule",
            "系统模块如生产监控、设备控制等",
        )
    if obj.get("optype") == "permkwkwissionmanagement.systemmodule_line":
        res = get_line(
            "select systemmodule x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by systemmodule",
            "系统模块如生产监控、设备控制等",
        )
    if obj.get("optype") == "permkwkwissionmanagement.systemmodule_bar":
        res = get_bar(
            "select systemmodule x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by systemmodule",
            "系统模块如生产监控、设备控制等",
        )
    if obj.get("optype") == "permkwkwissionmanagement.systemmodule_bar_v1":
        res = get_bar_v1(
            "select systemmodule x,count(*) y from vm780_bb1ff2b101947be5.permkwkwissionmanagement group by systemmodule",
            "系统模块如生产监控、设备控制等",
        )
    # userinfo(用户信息表)->userid(用户ID)

    if obj.get("optype") == "userinfo.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "userinfo.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userinfo.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userinfo.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userinfo.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userinfo.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by userid",
            "用户ID",
        )
    # userinfo(用户信息表)->username(用户名)

    if obj.get("optype") == "userinfo.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by username order by x desc",
            "用户名",
        )
    if obj.get("optype") == "userinfo.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by username",
            "用户名",
        )
    if obj.get("optype") == "userinfo.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by username",
            "用户名",
        )
    if obj.get("optype") == "userinfo.username_line":
        res = get_line(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by username",
            "用户名",
        )
    if obj.get("optype") == "userinfo.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by username",
            "用户名",
        )
    if obj.get("optype") == "userinfo.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by username",
            "用户名",
        )
    # userinfo(用户信息表)->pkwkwasswkwkword(密码)

    if obj.get("optype") == "userinfo.pkwkwasswkwkword_pie":
        res = get_pie(
            "select pkwkwasswkwkword x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by pkwkwasswkwkword order by x desc",
            "密码",
        )
    if obj.get("optype") == "userinfo.pkwkwasswkwkword_pie_v1":
        res = get_pie_v1(
            "select pkwkwasswkwkword x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by pkwkwasswkwkword",
            "密码",
        )
    if obj.get("optype") == "userinfo.pkwkwasswkwkword_pie_v2":
        res = get_pie_v2(
            "select pkwkwasswkwkword x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by pkwkwasswkwkword",
            "密码",
        )
    if obj.get("optype") == "userinfo.pkwkwasswkwkword_line":
        res = get_line(
            "select pkwkwasswkwkword x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by pkwkwasswkwkword",
            "密码",
        )
    if obj.get("optype") == "userinfo.pkwkwasswkwkword_bar":
        res = get_bar(
            "select pkwkwasswkwkword x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by pkwkwasswkwkword",
            "密码",
        )
    if obj.get("optype") == "userinfo.pkwkwasswkwkword_bar_v1":
        res = get_bar_v1(
            "select pkwkwasswkwkword x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by pkwkwasswkwkword",
            "密码",
        )
    # userinfo(用户信息表)->email(电子邮箱)

    if obj.get("optype") == "userinfo.email_pie":
        res = get_pie(
            "select email x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by email order by x desc",
            "电子邮箱",
        )
    if obj.get("optype") == "userinfo.email_pie_v1":
        res = get_pie_v1(
            "select email x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by email",
            "电子邮箱",
        )
    if obj.get("optype") == "userinfo.email_pie_v2":
        res = get_pie_v2(
            "select email x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by email",
            "电子邮箱",
        )
    if obj.get("optype") == "userinfo.email_line":
        res = get_line(
            "select email x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by email",
            "电子邮箱",
        )
    if obj.get("optype") == "userinfo.email_bar":
        res = get_bar(
            "select email x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by email",
            "电子邮箱",
        )
    if obj.get("optype") == "userinfo.email_bar_v1":
        res = get_bar_v1(
            "select email x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by email",
            "电子邮箱",
        )
    # userinfo(用户信息表)->phonenumber(电话号码)

    if obj.get("optype") == "userinfo.phonenumber_pie":
        res = get_pie(
            "select phonenumber x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by phonenumber order by x desc",
            "电话号码",
        )
    if obj.get("optype") == "userinfo.phonenumber_pie_v1":
        res = get_pie_v1(
            "select phonenumber x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "userinfo.phonenumber_pie_v2":
        res = get_pie_v2(
            "select phonenumber x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "userinfo.phonenumber_line":
        res = get_line(
            "select phonenumber x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "userinfo.phonenumber_bar":
        res = get_bar(
            "select phonenumber x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "userinfo.phonenumber_bar_v1":
        res = get_bar_v1(
            "select phonenumber x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by phonenumber",
            "电话号码",
        )
    # userinfo(用户信息表)->roleid(角色ID)

    if obj.get("optype") == "userinfo.roleid_pie":
        res = get_pie(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by roleid order by x desc",
            "角色ID",
        )
    if obj.get("optype") == "userinfo.roleid_pie_v1":
        res = get_pie_v1(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "userinfo.roleid_pie_v2":
        res = get_pie_v2(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "userinfo.roleid_line":
        res = get_line(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "userinfo.roleid_bar":
        res = get_bar(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "userinfo.roleid_bar_v1":
        res = get_bar_v1(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "userinfo.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "userinfo.lkwkwastlogkwkwintime_line":
        res = get_line(
            "select lkwkwastlogkwkwintime x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by lkwkwastlogkwkwintime order by x",
            "最后登录时间",
        )
    # userinfo(用户信息表)->isactive(是否激活)

    if obj.get("optype") == "userinfo.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "userinfo.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userinfo.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userinfo.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userinfo.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userinfo.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by isactive",
            "是否激活",
        )
    # userinfo(用户信息表)->departmentid(部门ID)

    if obj.get("optype") == "userinfo.departmentid_pie":
        res = get_pie(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by departmentid order by x desc",
            "部门ID",
        )
    if obj.get("optype") == "userinfo.departmentid_pie_v1":
        res = get_pie_v1(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "userinfo.departmentid_pie_v2":
        res = get_pie_v2(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "userinfo.departmentid_line":
        res = get_line(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "userinfo.departmentid_bar":
        res = get_bar(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by departmentid",
            "部门ID",
        )
    if obj.get("optype") == "userinfo.departmentid_bar_v1":
        res = get_bar_v1(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.userinfo group by departmentid",
            "部门ID",
        )
    # roleinfo(角色信息表)->roleid(角色ID)

    if obj.get("optype") == "roleinfo.roleid_pie":
        res = get_pie(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by roleid order by x desc",
            "角色ID",
        )
    if obj.get("optype") == "roleinfo.roleid_pie_v1":
        res = get_pie_v1(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "roleinfo.roleid_pie_v2":
        res = get_pie_v2(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "roleinfo.roleid_line":
        res = get_line(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "roleinfo.roleid_bar":
        res = get_bar(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by roleid",
            "角色ID",
        )
    if obj.get("optype") == "roleinfo.roleid_bar_v1":
        res = get_bar_v1(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by roleid",
            "角色ID",
        )
    # roleinfo(角色信息表)->rolename(角色名称)

    if obj.get("optype") == "roleinfo.rolename_pie":
        res = get_pie(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by rolename order by x desc",
            "角色名称",
        )
    if obj.get("optype") == "roleinfo.rolename_pie_v1":
        res = get_pie_v1(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roleinfo.rolename_pie_v2":
        res = get_pie_v2(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roleinfo.rolename_line":
        res = get_line(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roleinfo.rolename_bar":
        res = get_bar(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roleinfo.rolename_bar_v1":
        res = get_bar_v1(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "roleinfo.roledescription_wordcloud":
        textlist = get_data(
            "SELECT roledescription result FROM vm780_bb1ff2b101947be5.roleinfo;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "roleinfo.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "roleinfo.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by updatetime order by x",
            "更新时间",
        )
    # roleinfo(角色信息表)->isactive(是否激活)

    if obj.get("optype") == "roleinfo.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "roleinfo.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "roleinfo.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "roleinfo.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "roleinfo.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "roleinfo.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by isactive",
            "是否激活",
        )
    # roleinfo(角色信息表)->permkwkwissionids(权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储)

    if obj.get("optype") == "roleinfo.permkwkwissionids_pie":
        res = get_pie(
            "select permkwkwissionids x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by permkwkwissionids order by x desc",
            "权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储",
        )
    if obj.get("optype") == "roleinfo.permkwkwissionids_pie_v1":
        res = get_pie_v1(
            "select permkwkwissionids x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by permkwkwissionids",
            "权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储",
        )
    if obj.get("optype") == "roleinfo.permkwkwissionids_pie_v2":
        res = get_pie_v2(
            "select permkwkwissionids x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by permkwkwissionids",
            "权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储",
        )
    if obj.get("optype") == "roleinfo.permkwkwissionids_line":
        res = get_line(
            "select permkwkwissionids x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by permkwkwissionids",
            "权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储",
        )
    if obj.get("optype") == "roleinfo.permkwkwissionids_bar":
        res = get_bar(
            "select permkwkwissionids x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by permkwkwissionids",
            "权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储",
        )
    if obj.get("optype") == "roleinfo.permkwkwissionids_bar_v1":
        res = get_bar_v1(
            "select permkwkwissionids x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by permkwkwissionids",
            "权限ID列关联字段存储该角色拥有的权限ID集合以逗号分隔或采用其他方式存储",
        )
    # roleinfo(角色信息表)->createdby(创建者ID关联字段指向创建该角色的用户ID)

    if obj.get("optype") == "roleinfo.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by createdby order by x desc",
            "创建者ID关联字段指向创建该角色的用户ID",
        )
    if obj.get("optype") == "roleinfo.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by createdby",
            "创建者ID关联字段指向创建该角色的用户ID",
        )
    if obj.get("optype") == "roleinfo.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by createdby",
            "创建者ID关联字段指向创建该角色的用户ID",
        )
    if obj.get("optype") == "roleinfo.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by createdby",
            "创建者ID关联字段指向创建该角色的用户ID",
        )
    if obj.get("optype") == "roleinfo.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by createdby",
            "创建者ID关联字段指向创建该角色的用户ID",
        )
    if obj.get("optype") == "roleinfo.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by createdby",
            "创建者ID关联字段指向创建该角色的用户ID",
        )
    # roleinfo(角色信息表)->updatedby(更新者ID关联字段指向最后更新该角色的用户ID)

    if obj.get("optype") == "roleinfo.updatedby_pie":
        res = get_pie(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by updatedby order by x desc",
            "更新者ID关联字段指向最后更新该角色的用户ID",
        )
    if obj.get("optype") == "roleinfo.updatedby_pie_v1":
        res = get_pie_v1(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by updatedby",
            "更新者ID关联字段指向最后更新该角色的用户ID",
        )
    if obj.get("optype") == "roleinfo.updatedby_pie_v2":
        res = get_pie_v2(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by updatedby",
            "更新者ID关联字段指向最后更新该角色的用户ID",
        )
    if obj.get("optype") == "roleinfo.updatedby_line":
        res = get_line(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by updatedby",
            "更新者ID关联字段指向最后更新该角色的用户ID",
        )
    if obj.get("optype") == "roleinfo.updatedby_bar":
        res = get_bar(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by updatedby",
            "更新者ID关联字段指向最后更新该角色的用户ID",
        )
    if obj.get("optype") == "roleinfo.updatedby_bar_v1":
        res = get_bar_v1(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.roleinfo group by updatedby",
            "更新者ID关联字段指向最后更新该角色的用户ID",
        )
    # userrolerelation(用户角色关联表)->userid(用户ID)

    if obj.get("optype") == "userrolerelation.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "userrolerelation.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userrolerelation.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userrolerelation.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userrolerelation.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userrolerelation.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by userid",
            "用户ID",
        )
    # userrolerelation(用户角色关联表)->rolename(角色名)

    if obj.get("optype") == "userrolerelation.rolename_pie":
        res = get_pie(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by rolename order by x desc",
            "角色名",
        )
    if obj.get("optype") == "userrolerelation.rolename_pie_v1":
        res = get_pie_v1(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by rolename",
            "角色名",
        )
    if obj.get("optype") == "userrolerelation.rolename_pie_v2":
        res = get_pie_v2(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by rolename",
            "角色名",
        )
    if obj.get("optype") == "userrolerelation.rolename_line":
        res = get_line(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by rolename",
            "角色名",
        )
    if obj.get("optype") == "userrolerelation.rolename_bar":
        res = get_bar(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by rolename",
            "角色名",
        )
    if obj.get("optype") == "userrolerelation.rolename_bar_v1":
        res = get_bar_v1(
            "select rolename x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by rolename",
            "角色名",
        )
    # userrolerelation(用户角色关联表)->relationid(关联ID)

    if obj.get("optype") == "userrolerelation.relationid_pie":
        res = get_pie(
            "select relationid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by relationid order by x desc",
            "关联ID",
        )
    if obj.get("optype") == "userrolerelation.relationid_pie_v1":
        res = get_pie_v1(
            "select relationid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by relationid",
            "关联ID",
        )
    if obj.get("optype") == "userrolerelation.relationid_pie_v2":
        res = get_pie_v2(
            "select relationid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by relationid",
            "关联ID",
        )
    if obj.get("optype") == "userrolerelation.relationid_line":
        res = get_line(
            "select relationid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by relationid",
            "关联ID",
        )
    if obj.get("optype") == "userrolerelation.relationid_bar":
        res = get_bar(
            "select relationid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by relationid",
            "关联ID",
        )
    if obj.get("optype") == "userrolerelation.relationid_bar_v1":
        res = get_bar_v1(
            "select relationid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by relationid",
            "关联ID",
        )
    if obj.get("optype") == "userrolerelation.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "userrolerelation.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by updatetime order by x",
            "更新时间",
        )
    # userrolerelation(用户角色关联表)->isactive(是否激活用于控制用户角色关系的有效性)

    if obj.get("optype") == "userrolerelation.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by isactive order by x desc",
            "是否激活用于控制用户角色关系的有效性",
        )
    if obj.get("optype") == "userrolerelation.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by isactive",
            "是否激活用于控制用户角色关系的有效性",
        )
    if obj.get("optype") == "userrolerelation.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by isactive",
            "是否激活用于控制用户角色关系的有效性",
        )
    if obj.get("optype") == "userrolerelation.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by isactive",
            "是否激活用于控制用户角色关系的有效性",
        )
    if obj.get("optype") == "userrolerelation.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by isactive",
            "是否激活用于控制用户角色关系的有效性",
        )
    if obj.get("optype") == "userrolerelation.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by isactive",
            "是否激活用于控制用户角色关系的有效性",
        )
    # userrolerelation(用户角色关联表)->createdby(创建者ID)

    if obj.get("optype") == "userrolerelation.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by createdby order by x desc",
            "创建者ID",
        )
    if obj.get("optype") == "userrolerelation.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "userrolerelation.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "userrolerelation.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "userrolerelation.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by createdby",
            "创建者ID",
        )
    if obj.get("optype") == "userrolerelation.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by createdby",
            "创建者ID",
        )
    # userrolerelation(用户角色关联表)->updatedby(更新者ID)

    if obj.get("optype") == "userrolerelation.updatedby_pie":
        res = get_pie(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by updatedby order by x desc",
            "更新者ID",
        )
    if obj.get("optype") == "userrolerelation.updatedby_pie_v1":
        res = get_pie_v1(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "userrolerelation.updatedby_pie_v2":
        res = get_pie_v2(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "userrolerelation.updatedby_line":
        res = get_line(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "userrolerelation.updatedby_bar":
        res = get_bar(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by updatedby",
            "更新者ID",
        )
    if obj.get("optype") == "userrolerelation.updatedby_bar_v1":
        res = get_bar_v1(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by updatedby",
            "更新者ID",
        )
    # userrolerelation(用户角色关联表)->roleid(角色ID关联到角色的ID)

    if obj.get("optype") == "userrolerelation.roleid_pie":
        res = get_pie(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by roleid order by x desc",
            "角色ID关联到角色的ID",
        )
    if obj.get("optype") == "userrolerelation.roleid_pie_v1":
        res = get_pie_v1(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by roleid",
            "角色ID关联到角色的ID",
        )
    if obj.get("optype") == "userrolerelation.roleid_pie_v2":
        res = get_pie_v2(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by roleid",
            "角色ID关联到角色的ID",
        )
    if obj.get("optype") == "userrolerelation.roleid_line":
        res = get_line(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by roleid",
            "角色ID关联到角色的ID",
        )
    if obj.get("optype") == "userrolerelation.roleid_bar":
        res = get_bar(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by roleid",
            "角色ID关联到角色的ID",
        )
    if obj.get("optype") == "userrolerelation.roleid_bar_v1":
        res = get_bar_v1(
            "select roleid x,count(*) y from vm780_bb1ff2b101947be5.userrolerelation group by roleid",
            "角色ID关联到角色的ID",
        )
    # robotfault(机器人故障表)->faultid(故障ID)

    if obj.get("optype") == "robotfault.faultid_pie":
        res = get_pie(
            "select faultid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultid order by x desc",
            "故障ID",
        )
    if obj.get("optype") == "robotfault.faultid_pie_v1":
        res = get_pie_v1(
            "select faultid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultid",
            "故障ID",
        )
    if obj.get("optype") == "robotfault.faultid_pie_v2":
        res = get_pie_v2(
            "select faultid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultid",
            "故障ID",
        )
    if obj.get("optype") == "robotfault.faultid_line":
        res = get_line(
            "select faultid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultid",
            "故障ID",
        )
    if obj.get("optype") == "robotfault.faultid_bar":
        res = get_bar(
            "select faultid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultid",
            "故障ID",
        )
    if obj.get("optype") == "robotfault.faultid_bar_v1":
        res = get_bar_v1(
            "select faultid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultid",
            "故障ID",
        )
    # robotfault(机器人故障表)->robotid(机器人ID)

    if obj.get("optype") == "robotfault.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "robotfault.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotfault.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotfault.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotfault.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotfault.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by robotid",
            "机器人ID",
        )
    # robotfault(机器人故障表)->faulttype(故障类型)

    if obj.get("optype") == "robotfault.faulttype_pie":
        res = get_pie(
            "select faulttype x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faulttype order by x desc",
            "故障类型",
        )
    if obj.get("optype") == "robotfault.faulttype_pie_v1":
        res = get_pie_v1(
            "select faulttype x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faulttype",
            "故障类型",
        )
    if obj.get("optype") == "robotfault.faulttype_pie_v2":
        res = get_pie_v2(
            "select faulttype x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faulttype",
            "故障类型",
        )
    if obj.get("optype") == "robotfault.faulttype_line":
        res = get_line(
            "select faulttype x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faulttype",
            "故障类型",
        )
    if obj.get("optype") == "robotfault.faulttype_bar":
        res = get_bar(
            "select faulttype x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faulttype",
            "故障类型",
        )
    if obj.get("optype") == "robotfault.faulttype_bar_v1":
        res = get_bar_v1(
            "select faulttype x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faulttype",
            "故障类型",
        )
    if obj.get("optype") == "robotfault.faultdescription_wordcloud":
        textlist = get_data(
            "SELECT faultdescription result FROM vm780_bb1ff2b101947be5.robotfault;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "robotfault.faulttime_line":
        res = get_line(
            "select faulttime x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faulttime order by x",
            "故障时间",
        )
    # robotfault(机器人故障表)->repairstatus(维修状态)

    if obj.get("optype") == "robotfault.repairstatus_pie":
        res = get_pie(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairstatus order by x desc",
            "维修状态",
        )
    if obj.get("optype") == "robotfault.repairstatus_pie_v1":
        res = get_pie_v1(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "robotfault.repairstatus_pie_v2":
        res = get_pie_v2(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "robotfault.repairstatus_line":
        res = get_line(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "robotfault.repairstatus_bar":
        res = get_bar(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "robotfault.repairstatus_bar_v1":
        res = get_bar_v1(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "robotfault.repairtime_line":
        res = get_line(
            "select repairtime x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairtime order by x",
            "维修时间",
        )
    # robotfault(机器人故障表)->repairperson(维修人员)

    if obj.get("optype") == "robotfault.repairperson_pie":
        res = get_pie(
            "select repairperson x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairperson order by x desc",
            "维修人员",
        )
    if obj.get("optype") == "robotfault.repairperson_pie_v1":
        res = get_pie_v1(
            "select repairperson x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairperson",
            "维修人员",
        )
    if obj.get("optype") == "robotfault.repairperson_pie_v2":
        res = get_pie_v2(
            "select repairperson x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairperson",
            "维修人员",
        )
    if obj.get("optype") == "robotfault.repairperson_line":
        res = get_line(
            "select repairperson x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairperson",
            "维修人员",
        )
    if obj.get("optype") == "robotfault.repairperson_bar":
        res = get_bar(
            "select repairperson x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairperson",
            "维修人员",
        )
    if obj.get("optype") == "robotfault.repairperson_bar_v1":
        res = get_bar_v1(
            "select repairperson x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by repairperson",
            "维修人员",
        )
    # robotfault(机器人故障表)->faultseverity(故障严重程度)

    if obj.get("optype") == "robotfault.faultseverity_pie":
        res = get_pie(
            "select faultseverity x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultseverity order by x desc",
            "故障严重程度",
        )
    if obj.get("optype") == "robotfault.faultseverity_pie_v1":
        res = get_pie_v1(
            "select faultseverity x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultseverity",
            "故障严重程度",
        )
    if obj.get("optype") == "robotfault.faultseverity_pie_v2":
        res = get_pie_v2(
            "select faultseverity x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultseverity",
            "故障严重程度",
        )
    if obj.get("optype") == "robotfault.faultseverity_line":
        res = get_line(
            "select faultseverity x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultseverity",
            "故障严重程度",
        )
    if obj.get("optype") == "robotfault.faultseverity_bar":
        res = get_bar(
            "select faultseverity x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultseverity",
            "故障严重程度",
        )
    if obj.get("optype") == "robotfault.faultseverity_bar_v1":
        res = get_bar_v1(
            "select faultseverity x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by faultseverity",
            "故障严重程度",
        )
    # robotfault(机器人故障表)->relatedcomponent(关联组件)

    if obj.get("optype") == "robotfault.relatedcomponent_pie":
        res = get_pie(
            "select relatedcomponent x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by relatedcomponent order by x desc",
            "关联组件",
        )
    if obj.get("optype") == "robotfault.relatedcomponent_pie_v1":
        res = get_pie_v1(
            "select relatedcomponent x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by relatedcomponent",
            "关联组件",
        )
    if obj.get("optype") == "robotfault.relatedcomponent_pie_v2":
        res = get_pie_v2(
            "select relatedcomponent x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by relatedcomponent",
            "关联组件",
        )
    if obj.get("optype") == "robotfault.relatedcomponent_line":
        res = get_line(
            "select relatedcomponent x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by relatedcomponent",
            "关联组件",
        )
    if obj.get("optype") == "robotfault.relatedcomponent_bar":
        res = get_bar(
            "select relatedcomponent x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by relatedcomponent",
            "关联组件",
        )
    if obj.get("optype") == "robotfault.relatedcomponent_bar_v1":
        res = get_bar_v1(
            "select relatedcomponent x,count(*) y from vm780_bb1ff2b101947be5.robotfault group by relatedcomponent",
            "关联组件",
        )
    # makwkwintenancereckwkword(维修记录表)->reckwkwordid(记录ID)

    if obj.get("optype") == "makwkwintenancereckwkword.reckwkwordid_pie":
        res = get_pie(
            "select reckwkwordid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by reckwkwordid order by x desc",
            "记录ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.reckwkwordid_pie_v1":
        res = get_pie_v1(
            "select reckwkwordid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by reckwkwordid",
            "记录ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.reckwkwordid_pie_v2":
        res = get_pie_v2(
            "select reckwkwordid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by reckwkwordid",
            "记录ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.reckwkwordid_line":
        res = get_line(
            "select reckwkwordid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by reckwkwordid",
            "记录ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.reckwkwordid_bar":
        res = get_bar(
            "select reckwkwordid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by reckwkwordid",
            "记录ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.reckwkwordid_bar_v1":
        res = get_bar_v1(
            "select reckwkwordid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by reckwkwordid",
            "记录ID",
        )
    # makwkwintenancereckwkword(维修记录表)->robotid(机器人ID)

    if obj.get("optype") == "makwkwintenancereckwkword.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.makwkwintenancedate_line":
        res = get_line(
            "select makwkwintenancedate x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by makwkwintenancedate order by x",
            "维修日期",
        )
    # makwkwintenancereckwkword(维修记录表)->makwkwintenancetype(维修类型)

    if obj.get("optype") == "makwkwintenancereckwkword.makwkwintenancetype_pie":
        res = get_pie(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by makwkwintenancetype order by x desc",
            "维修类型",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.makwkwintenancetype_pie_v1":
        res = get_pie_v1(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by makwkwintenancetype",
            "维修类型",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.makwkwintenancetype_pie_v2":
        res = get_pie_v2(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by makwkwintenancetype",
            "维修类型",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.makwkwintenancetype_line":
        res = get_line(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by makwkwintenancetype",
            "维修类型",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.makwkwintenancetype_bar":
        res = get_bar(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by makwkwintenancetype",
            "维修类型",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.makwkwintenancetype_bar_v1":
        res = get_bar_v1(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by makwkwintenancetype",
            "维修类型",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.problemdescription_wordcloud":
        textlist = get_data(
            "SELECT problemdescription result FROM vm780_bb1ff2b101947be5.makwkwintenancereckwkword;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # makwkwintenancereckwkword(维修记录表)->repairstatus(维修状态)

    if obj.get("optype") == "makwkwintenancereckwkword.repairstatus_pie":
        res = get_pie(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairstatus order by x desc",
            "维修状态",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repairstatus_pie_v1":
        res = get_pie_v1(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repairstatus_pie_v2":
        res = get_pie_v2(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repairstatus_line":
        res = get_line(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repairstatus_bar":
        res = get_bar(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repairstatus_bar_v1":
        res = get_bar_v1(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairstatus",
            "维修状态",
        )
    # makwkwintenancereckwkword(维修记录表)->technicianid(技术员ID)

    if obj.get("optype") == "makwkwintenancereckwkword.technicianid_pie":
        res = get_pie(
            "select technicianid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by technicianid order by x desc",
            "技术员ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.technicianid_pie_v1":
        res = get_pie_v1(
            "select technicianid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by technicianid",
            "技术员ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.technicianid_pie_v2":
        res = get_pie_v2(
            "select technicianid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by technicianid",
            "技术员ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.technicianid_line":
        res = get_line(
            "select technicianid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by technicianid",
            "技术员ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.technicianid_bar":
        res = get_bar(
            "select technicianid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by technicianid",
            "技术员ID",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.technicianid_bar_v1":
        res = get_bar_v1(
            "select technicianid x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by technicianid",
            "技术员ID",
        )
    # makwkwintenancereckwkword(维修记录表)->repaircost(维修费用)

    if obj.get("optype") == "makwkwintenancereckwkword.repaircost_pie":
        res = get_pie(
            "select repaircost x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repaircost order by x desc",
            "维修费用",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repaircost_pie_v1":
        res = get_pie_v1(
            "select repaircost x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repaircost",
            "维修费用",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repaircost_pie_v2":
        res = get_pie_v2(
            "select repaircost x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repaircost",
            "维修费用",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repaircost_line":
        res = get_line(
            "select repaircost x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repaircost",
            "维修费用",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repaircost_bar":
        res = get_bar(
            "select repaircost x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repaircost",
            "维修费用",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repaircost_bar_v1":
        res = get_bar_v1(
            "select repaircost x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repaircost",
            "维修费用",
        )
    # makwkwintenancereckwkword(维修记录表)->repairduration(维修时长)

    if obj.get("optype") == "makwkwintenancereckwkword.repairduration_pie":
        res = get_pie(
            "select repairduration x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairduration order by x desc",
            "维修时长",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repairduration_pie_v1":
        res = get_pie_v1(
            "select repairduration x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairduration",
            "维修时长",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repairduration_pie_v2":
        res = get_pie_v2(
            "select repairduration x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairduration",
            "维修时长",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repairduration_line":
        res = get_line(
            "select repairduration x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairduration",
            "维修时长",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repairduration_bar":
        res = get_bar(
            "select repairduration x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairduration",
            "维修时长",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.repairduration_bar_v1":
        res = get_bar_v1(
            "select repairduration x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by repairduration",
            "维修时长",
        )
    # makwkwintenancereckwkword(维修记录表)->relatedparts(相关部件)

    if obj.get("optype") == "makwkwintenancereckwkword.relatedparts_pie":
        res = get_pie(
            "select relatedparts x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by relatedparts order by x desc",
            "相关部件",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.relatedparts_pie_v1":
        res = get_pie_v1(
            "select relatedparts x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by relatedparts",
            "相关部件",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.relatedparts_pie_v2":
        res = get_pie_v2(
            "select relatedparts x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by relatedparts",
            "相关部件",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.relatedparts_line":
        res = get_line(
            "select relatedparts x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by relatedparts",
            "相关部件",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.relatedparts_bar":
        res = get_bar(
            "select relatedparts x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by relatedparts",
            "相关部件",
        )
    if obj.get("optype") == "makwkwintenancereckwkword.relatedparts_bar_v1":
        res = get_bar_v1(
            "select relatedparts x,count(*) y from vm780_bb1ff2b101947be5.makwkwintenancereckwkword group by relatedparts",
            "相关部件",
        )
    # robotmokwkwdel(机器人型号表)->robotmokwkwdelid(机器人型号ID)

    if obj.get("optype") == "robotmokwkwdel.robotmokwkwdelid_pie":
        res = get_pie(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by robotmokwkwdelid order by x desc",
            "机器人型号ID",
        )
    if obj.get("optype") == "robotmokwkwdel.robotmokwkwdelid_pie_v1":
        res = get_pie_v1(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by robotmokwkwdelid",
            "机器人型号ID",
        )
    if obj.get("optype") == "robotmokwkwdel.robotmokwkwdelid_pie_v2":
        res = get_pie_v2(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by robotmokwkwdelid",
            "机器人型号ID",
        )
    if obj.get("optype") == "robotmokwkwdel.robotmokwkwdelid_line":
        res = get_line(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by robotmokwkwdelid",
            "机器人型号ID",
        )
    if obj.get("optype") == "robotmokwkwdel.robotmokwkwdelid_bar":
        res = get_bar(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by robotmokwkwdelid",
            "机器人型号ID",
        )
    if obj.get("optype") == "robotmokwkwdel.robotmokwkwdelid_bar_v1":
        res = get_bar_v1(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by robotmokwkwdelid",
            "机器人型号ID",
        )
    # robotmokwkwdel(机器人型号表)->mokwkwdelname(机器人型号名称)

    if obj.get("optype") == "robotmokwkwdel.mokwkwdelname_pie":
        res = get_pie(
            "select mokwkwdelname x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by mokwkwdelname order by x desc",
            "机器人型号名称",
        )
    if obj.get("optype") == "robotmokwkwdel.mokwkwdelname_pie_v1":
        res = get_pie_v1(
            "select mokwkwdelname x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by mokwkwdelname",
            "机器人型号名称",
        )
    if obj.get("optype") == "robotmokwkwdel.mokwkwdelname_pie_v2":
        res = get_pie_v2(
            "select mokwkwdelname x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by mokwkwdelname",
            "机器人型号名称",
        )
    if obj.get("optype") == "robotmokwkwdel.mokwkwdelname_line":
        res = get_line(
            "select mokwkwdelname x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by mokwkwdelname",
            "机器人型号名称",
        )
    if obj.get("optype") == "robotmokwkwdel.mokwkwdelname_bar":
        res = get_bar(
            "select mokwkwdelname x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by mokwkwdelname",
            "机器人型号名称",
        )
    if obj.get("optype") == "robotmokwkwdel.mokwkwdelname_bar_v1":
        res = get_bar_v1(
            "select mokwkwdelname x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by mokwkwdelname",
            "机器人型号名称",
        )
    # robotmokwkwdel(机器人型号表)->manufacturer(制造商)

    if obj.get("optype") == "robotmokwkwdel.manufacturer_pie":
        res = get_pie(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by manufacturer order by x desc",
            "制造商",
        )
    if obj.get("optype") == "robotmokwkwdel.manufacturer_pie_v1":
        res = get_pie_v1(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by manufacturer",
            "制造商",
        )
    if obj.get("optype") == "robotmokwkwdel.manufacturer_pie_v2":
        res = get_pie_v2(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by manufacturer",
            "制造商",
        )
    if obj.get("optype") == "robotmokwkwdel.manufacturer_line":
        res = get_line(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by manufacturer",
            "制造商",
        )
    if obj.get("optype") == "robotmokwkwdel.manufacturer_bar":
        res = get_bar(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by manufacturer",
            "制造商",
        )
    if obj.get("optype") == "robotmokwkwdel.manufacturer_bar_v1":
        res = get_bar_v1(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by manufacturer",
            "制造商",
        )
    # robotmokwkwdel(机器人型号表)->productionyear(生产年份)

    if obj.get("optype") == "robotmokwkwdel.productionyear_pie":
        res = get_pie(
            "select productionyear x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by productionyear order by x desc",
            "生产年份",
        )
    if obj.get("optype") == "robotmokwkwdel.productionyear_pie_v1":
        res = get_pie_v1(
            "select productionyear x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by productionyear",
            "生产年份",
        )
    if obj.get("optype") == "robotmokwkwdel.productionyear_pie_v2":
        res = get_pie_v2(
            "select productionyear x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by productionyear",
            "生产年份",
        )
    if obj.get("optype") == "robotmokwkwdel.productionyear_line":
        res = get_line(
            "select productionyear x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by productionyear",
            "生产年份",
        )
    if obj.get("optype") == "robotmokwkwdel.productionyear_bar":
        res = get_bar(
            "select productionyear x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by productionyear",
            "生产年份",
        )
    if obj.get("optype") == "robotmokwkwdel.productionyear_bar_v1":
        res = get_bar_v1(
            "select productionyear x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by productionyear",
            "生产年份",
        )
    # robotmokwkwdel(机器人型号表)->maxpayload(最大负载能力)

    if obj.get("optype") == "robotmokwkwdel.maxpayload_pie":
        res = get_pie(
            "select maxpayload x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by maxpayload order by x desc",
            "最大负载能力",
        )
    if obj.get("optype") == "robotmokwkwdel.maxpayload_pie_v1":
        res = get_pie_v1(
            "select maxpayload x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by maxpayload",
            "最大负载能力",
        )
    if obj.get("optype") == "robotmokwkwdel.maxpayload_pie_v2":
        res = get_pie_v2(
            "select maxpayload x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by maxpayload",
            "最大负载能力",
        )
    if obj.get("optype") == "robotmokwkwdel.maxpayload_line":
        res = get_line(
            "select maxpayload x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by maxpayload",
            "最大负载能力",
        )
    if obj.get("optype") == "robotmokwkwdel.maxpayload_bar":
        res = get_bar(
            "select maxpayload x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by maxpayload",
            "最大负载能力",
        )
    if obj.get("optype") == "robotmokwkwdel.maxpayload_bar_v1":
        res = get_bar_v1(
            "select maxpayload x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by maxpayload",
            "最大负载能力",
        )
    # robotmokwkwdel(机器人型号表)->operatkwkwingvoltage(工作电压)

    if obj.get("optype") == "robotmokwkwdel.operatkwkwingvoltage_pie":
        res = get_pie(
            "select operatkwkwingvoltage x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by operatkwkwingvoltage order by x desc",
            "工作电压",
        )
    if obj.get("optype") == "robotmokwkwdel.operatkwkwingvoltage_pie_v1":
        res = get_pie_v1(
            "select operatkwkwingvoltage x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by operatkwkwingvoltage",
            "工作电压",
        )
    if obj.get("optype") == "robotmokwkwdel.operatkwkwingvoltage_pie_v2":
        res = get_pie_v2(
            "select operatkwkwingvoltage x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by operatkwkwingvoltage",
            "工作电压",
        )
    if obj.get("optype") == "robotmokwkwdel.operatkwkwingvoltage_line":
        res = get_line(
            "select operatkwkwingvoltage x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by operatkwkwingvoltage",
            "工作电压",
        )
    if obj.get("optype") == "robotmokwkwdel.operatkwkwingvoltage_bar":
        res = get_bar(
            "select operatkwkwingvoltage x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by operatkwkwingvoltage",
            "工作电压",
        )
    if obj.get("optype") == "robotmokwkwdel.operatkwkwingvoltage_bar_v1":
        res = get_bar_v1(
            "select operatkwkwingvoltage x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by operatkwkwingvoltage",
            "工作电压",
        )
    # robotmokwkwdel(机器人型号表)->connectivitytype(连接类型)

    if obj.get("optype") == "robotmokwkwdel.connectivitytype_pie":
        res = get_pie(
            "select connectivitytype x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by connectivitytype order by x desc",
            "连接类型",
        )
    if obj.get("optype") == "robotmokwkwdel.connectivitytype_pie_v1":
        res = get_pie_v1(
            "select connectivitytype x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by connectivitytype",
            "连接类型",
        )
    if obj.get("optype") == "robotmokwkwdel.connectivitytype_pie_v2":
        res = get_pie_v2(
            "select connectivitytype x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by connectivitytype",
            "连接类型",
        )
    if obj.get("optype") == "robotmokwkwdel.connectivitytype_line":
        res = get_line(
            "select connectivitytype x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by connectivitytype",
            "连接类型",
        )
    if obj.get("optype") == "robotmokwkwdel.connectivitytype_bar":
        res = get_bar(
            "select connectivitytype x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by connectivitytype",
            "连接类型",
        )
    if obj.get("optype") == "robotmokwkwdel.connectivitytype_bar_v1":
        res = get_bar_v1(
            "select connectivitytype x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by connectivitytype",
            "连接类型",
        )
    # robotmokwkwdel(机器人型号表)->safetycertkwkwification(安全认证)

    if obj.get("optype") == "robotmokwkwdel.safetycertkwkwification_pie":
        res = get_pie(
            "select safetycertkwkwification x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by safetycertkwkwification order by x desc",
            "安全认证",
        )
    if obj.get("optype") == "robotmokwkwdel.safetycertkwkwification_pie_v1":
        res = get_pie_v1(
            "select safetycertkwkwification x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by safetycertkwkwification",
            "安全认证",
        )
    if obj.get("optype") == "robotmokwkwdel.safetycertkwkwification_pie_v2":
        res = get_pie_v2(
            "select safetycertkwkwification x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by safetycertkwkwification",
            "安全认证",
        )
    if obj.get("optype") == "robotmokwkwdel.safetycertkwkwification_line":
        res = get_line(
            "select safetycertkwkwification x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by safetycertkwkwification",
            "安全认证",
        )
    if obj.get("optype") == "robotmokwkwdel.safetycertkwkwification_bar":
        res = get_bar(
            "select safetycertkwkwification x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by safetycertkwkwification",
            "安全认证",
        )
    if obj.get("optype") == "robotmokwkwdel.safetycertkwkwification_bar_v1":
        res = get_bar_v1(
            "select safetycertkwkwification x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by safetycertkwkwification",
            "安全认证",
        )
    # robotmokwkwdel(机器人型号表)->makwkwintenanceinterval(维护周期)

    if obj.get("optype") == "robotmokwkwdel.makwkwintenanceinterval_pie":
        res = get_pie(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by makwkwintenanceinterval order by x desc",
            "维护周期",
        )
    if obj.get("optype") == "robotmokwkwdel.makwkwintenanceinterval_pie_v1":
        res = get_pie_v1(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by makwkwintenanceinterval",
            "维护周期",
        )
    if obj.get("optype") == "robotmokwkwdel.makwkwintenanceinterval_pie_v2":
        res = get_pie_v2(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by makwkwintenanceinterval",
            "维护周期",
        )
    if obj.get("optype") == "robotmokwkwdel.makwkwintenanceinterval_line":
        res = get_line(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by makwkwintenanceinterval",
            "维护周期",
        )
    if obj.get("optype") == "robotmokwkwdel.makwkwintenanceinterval_bar":
        res = get_bar(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by makwkwintenanceinterval",
            "维护周期",
        )
    if obj.get("optype") == "robotmokwkwdel.makwkwintenanceinterval_bar_v1":
        res = get_bar_v1(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by makwkwintenanceinterval",
            "维护周期",
        )
    # robotmokwkwdel(机器人型号表)->relatedcomponentid(相关组件ID关联字段指向其他如组件)

    if obj.get("optype") == "robotmokwkwdel.relatedcomponentid_pie":
        res = get_pie(
            "select relatedcomponentid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by relatedcomponentid order by x desc",
            "相关组件ID关联字段指向其他如组件",
        )
    if obj.get("optype") == "robotmokwkwdel.relatedcomponentid_pie_v1":
        res = get_pie_v1(
            "select relatedcomponentid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by relatedcomponentid",
            "相关组件ID关联字段指向其他如组件",
        )
    if obj.get("optype") == "robotmokwkwdel.relatedcomponentid_pie_v2":
        res = get_pie_v2(
            "select relatedcomponentid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by relatedcomponentid",
            "相关组件ID关联字段指向其他如组件",
        )
    if obj.get("optype") == "robotmokwkwdel.relatedcomponentid_line":
        res = get_line(
            "select relatedcomponentid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by relatedcomponentid",
            "相关组件ID关联字段指向其他如组件",
        )
    if obj.get("optype") == "robotmokwkwdel.relatedcomponentid_bar":
        res = get_bar(
            "select relatedcomponentid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by relatedcomponentid",
            "相关组件ID关联字段指向其他如组件",
        )
    if obj.get("optype") == "robotmokwkwdel.relatedcomponentid_bar_v1":
        res = get_bar_v1(
            "select relatedcomponentid x,count(*) y from vm780_bb1ff2b101947be5.robotmokwkwdel group by relatedcomponentid",
            "相关组件ID关联字段指向其他如组件",
        )
    # senskwkworinfo(传感器信息表)->senskwkworid(传感器ID)

    if obj.get("optype") == "senskwkworinfo.senskwkworid_pie":
        res = get_pie(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworid order by x desc",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkworid_pie_v1":
        res = get_pie_v1(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworid",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkworid_pie_v2":
        res = get_pie_v2(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworid",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkworid_line":
        res = get_line(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworid",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkworid_bar":
        res = get_bar(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworid",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkworid_bar_v1":
        res = get_bar_v1(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworid",
            "传感器ID",
        )
    # senskwkworinfo(传感器信息表)->senskwkworname(传感器名称)

    if obj.get("optype") == "senskwkworinfo.senskwkworname_pie":
        res = get_pie(
            "select senskwkworname x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworname order by x desc",
            "传感器名称",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkworname_pie_v1":
        res = get_pie_v1(
            "select senskwkworname x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworname",
            "传感器名称",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkworname_pie_v2":
        res = get_pie_v2(
            "select senskwkworname x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworname",
            "传感器名称",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkworname_line":
        res = get_line(
            "select senskwkworname x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworname",
            "传感器名称",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkworname_bar":
        res = get_bar(
            "select senskwkworname x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworname",
            "传感器名称",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkworname_bar_v1":
        res = get_bar_v1(
            "select senskwkworname x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkworname",
            "传感器名称",
        )
    # senskwkworinfo(传感器信息表)->senskwkwortype(传感器类型)

    if obj.get("optype") == "senskwkworinfo.senskwkwortype_pie":
        res = get_pie(
            "select senskwkwortype x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkwortype order by x desc",
            "传感器类型",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkwortype_pie_v1":
        res = get_pie_v1(
            "select senskwkwortype x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkwortype",
            "传感器类型",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkwortype_pie_v2":
        res = get_pie_v2(
            "select senskwkwortype x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkwortype",
            "传感器类型",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkwortype_line":
        res = get_line(
            "select senskwkwortype x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkwortype",
            "传感器类型",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkwortype_bar":
        res = get_bar(
            "select senskwkwortype x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkwortype",
            "传感器类型",
        )
    if obj.get("optype") == "senskwkworinfo.senskwkwortype_bar_v1":
        res = get_bar_v1(
            "select senskwkwortype x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by senskwkwortype",
            "传感器类型",
        )
    # senskwkworinfo(传感器信息表)->location(位置)

    if obj.get("optype") == "senskwkworinfo.location_pie":
        res = get_pie(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by location order by x desc",
            "位置",
        )
    if obj.get("optype") == "senskwkworinfo.location_pie_v1":
        res = get_pie_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by location",
            "位置",
        )
    if obj.get("optype") == "senskwkworinfo.location_pie_v2":
        res = get_pie_v2(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by location",
            "位置",
        )
    if obj.get("optype") == "senskwkworinfo.location_line":
        res = get_line(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by location",
            "位置",
        )
    if obj.get("optype") == "senskwkworinfo.location_bar":
        res = get_bar(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by location",
            "位置",
        )
    if obj.get("optype") == "senskwkworinfo.location_bar_v1":
        res = get_bar_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by location",
            "位置",
        )
    # senskwkworinfo(传感器信息表)->status(状态)

    if obj.get("optype") == "senskwkworinfo.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by status order by x desc",
            "状态",
        )
    if obj.get("optype") == "senskwkworinfo.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by status",
            "状态",
        )
    if obj.get("optype") == "senskwkworinfo.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by status",
            "状态",
        )
    if obj.get("optype") == "senskwkworinfo.status_line":
        res = get_line(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by status",
            "状态",
        )
    if obj.get("optype") == "senskwkworinfo.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by status",
            "状态",
        )
    if obj.get("optype") == "senskwkworinfo.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by status",
            "状态",
        )
    if obj.get("optype") == "senskwkworinfo.lkwkwastupdatetime_line":
        res = get_line(
            "select lkwkwastupdatetime x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by lkwkwastupdatetime order by x",
            "最后更新时间",
        )
    # senskwkworinfo(传感器信息表)->mekwkwasurementvalue(测量值)

    if obj.get("optype") == "senskwkworinfo.mekwkwasurementvalue_pie":
        res = get_pie(
            "select mekwkwasurementvalue x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by mekwkwasurementvalue order by x desc",
            "测量值",
        )
    if obj.get("optype") == "senskwkworinfo.mekwkwasurementvalue_pie_v1":
        res = get_pie_v1(
            "select mekwkwasurementvalue x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by mekwkwasurementvalue",
            "测量值",
        )
    if obj.get("optype") == "senskwkworinfo.mekwkwasurementvalue_pie_v2":
        res = get_pie_v2(
            "select mekwkwasurementvalue x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by mekwkwasurementvalue",
            "测量值",
        )
    if obj.get("optype") == "senskwkworinfo.mekwkwasurementvalue_line":
        res = get_line(
            "select mekwkwasurementvalue x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by mekwkwasurementvalue",
            "测量值",
        )
    if obj.get("optype") == "senskwkworinfo.mekwkwasurementvalue_bar":
        res = get_bar(
            "select mekwkwasurementvalue x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by mekwkwasurementvalue",
            "测量值",
        )
    if obj.get("optype") == "senskwkworinfo.mekwkwasurementvalue_bar_v1":
        res = get_bar_v1(
            "select mekwkwasurementvalue x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by mekwkwasurementvalue",
            "测量值",
        )
    # senskwkworinfo(传感器信息表)->unit(单位)

    if obj.get("optype") == "senskwkworinfo.unit_pie":
        res = get_pie(
            "select unit x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by unit order by x desc",
            "单位",
        )
    if obj.get("optype") == "senskwkworinfo.unit_pie_v1":
        res = get_pie_v1(
            "select unit x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by unit",
            "单位",
        )
    if obj.get("optype") == "senskwkworinfo.unit_pie_v2":
        res = get_pie_v2(
            "select unit x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by unit",
            "单位",
        )
    if obj.get("optype") == "senskwkworinfo.unit_line":
        res = get_line(
            "select unit x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by unit",
            "单位",
        )
    if obj.get("optype") == "senskwkworinfo.unit_bar":
        res = get_bar(
            "select unit x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by unit",
            "单位",
        )
    if obj.get("optype") == "senskwkworinfo.unit_bar_v1":
        res = get_bar_v1(
            "select unit x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by unit",
            "单位",
        )
    # senskwkworinfo(传感器信息表)->alarmthreshold(报警阈值)

    if obj.get("optype") == "senskwkworinfo.alarmthreshold_pie":
        res = get_pie(
            "select alarmthreshold x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by alarmthreshold order by x desc",
            "报警阈值",
        )
    if obj.get("optype") == "senskwkworinfo.alarmthreshold_pie_v1":
        res = get_pie_v1(
            "select alarmthreshold x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by alarmthreshold",
            "报警阈值",
        )
    if obj.get("optype") == "senskwkworinfo.alarmthreshold_pie_v2":
        res = get_pie_v2(
            "select alarmthreshold x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by alarmthreshold",
            "报警阈值",
        )
    if obj.get("optype") == "senskwkworinfo.alarmthreshold_line":
        res = get_line(
            "select alarmthreshold x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by alarmthreshold",
            "报警阈值",
        )
    if obj.get("optype") == "senskwkworinfo.alarmthreshold_bar":
        res = get_bar(
            "select alarmthreshold x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by alarmthreshold",
            "报警阈值",
        )
    if obj.get("optype") == "senskwkworinfo.alarmthreshold_bar_v1":
        res = get_bar_v1(
            "select alarmthreshold x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by alarmthreshold",
            "报警阈值",
        )
    # senskwkworinfo(传感器信息表)->associatedrobotid(关联机器人ID)

    if obj.get("optype") == "senskwkworinfo.associatedrobotid_pie":
        res = get_pie(
            "select associatedrobotid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by associatedrobotid order by x desc",
            "关联机器人ID",
        )
    if obj.get("optype") == "senskwkworinfo.associatedrobotid_pie_v1":
        res = get_pie_v1(
            "select associatedrobotid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by associatedrobotid",
            "关联机器人ID",
        )
    if obj.get("optype") == "senskwkworinfo.associatedrobotid_pie_v2":
        res = get_pie_v2(
            "select associatedrobotid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by associatedrobotid",
            "关联机器人ID",
        )
    if obj.get("optype") == "senskwkworinfo.associatedrobotid_line":
        res = get_line(
            "select associatedrobotid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by associatedrobotid",
            "关联机器人ID",
        )
    if obj.get("optype") == "senskwkworinfo.associatedrobotid_bar":
        res = get_bar(
            "select associatedrobotid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by associatedrobotid",
            "关联机器人ID",
        )
    if obj.get("optype") == "senskwkworinfo.associatedrobotid_bar_v1":
        res = get_bar_v1(
            "select associatedrobotid x,count(*) y from vm780_bb1ff2b101947be5.senskwkworinfo group by associatedrobotid",
            "关联机器人ID",
        )
    # senskwkwordata(传感器数据表)->senskwkworid(传感器ID)

    if obj.get("optype") == "senskwkwordata.senskwkworid_pie":
        res = get_pie(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by senskwkworid order by x desc",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkwordata.senskwkworid_pie_v1":
        res = get_pie_v1(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by senskwkworid",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkwordata.senskwkworid_pie_v2":
        res = get_pie_v2(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by senskwkworid",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkwordata.senskwkworid_line":
        res = get_line(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by senskwkworid",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkwordata.senskwkworid_bar":
        res = get_bar(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by senskwkworid",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkwordata.senskwkworid_bar_v1":
        res = get_bar_v1(
            "select senskwkworid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by senskwkworid",
            "传感器ID",
        )
    if obj.get("optype") == "senskwkwordata.timestamp_line":
        res = get_line(
            "select timestamp x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by timestamp order by x",
            "时间戳",
        )
    # senskwkwordata(传感器数据表)->temperature(温度)

    if obj.get("optype") == "senskwkwordata.temperature_pie":
        res = get_pie(
            "select temperature x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by temperature order by x desc",
            "温度",
        )
    if obj.get("optype") == "senskwkwordata.temperature_pie_v1":
        res = get_pie_v1(
            "select temperature x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by temperature",
            "温度",
        )
    if obj.get("optype") == "senskwkwordata.temperature_pie_v2":
        res = get_pie_v2(
            "select temperature x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by temperature",
            "温度",
        )
    if obj.get("optype") == "senskwkwordata.temperature_line":
        res = get_line(
            "select temperature x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by temperature",
            "温度",
        )
    if obj.get("optype") == "senskwkwordata.temperature_bar":
        res = get_bar(
            "select temperature x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by temperature",
            "温度",
        )
    if obj.get("optype") == "senskwkwordata.temperature_bar_v1":
        res = get_bar_v1(
            "select temperature x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by temperature",
            "温度",
        )
    # senskwkwordata(传感器数据表)->humidity(湿度)

    if obj.get("optype") == "senskwkwordata.humidity_pie":
        res = get_pie(
            "select humidity x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by humidity order by x desc",
            "湿度",
        )
    if obj.get("optype") == "senskwkwordata.humidity_pie_v1":
        res = get_pie_v1(
            "select humidity x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by humidity",
            "湿度",
        )
    if obj.get("optype") == "senskwkwordata.humidity_pie_v2":
        res = get_pie_v2(
            "select humidity x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by humidity",
            "湿度",
        )
    if obj.get("optype") == "senskwkwordata.humidity_line":
        res = get_line(
            "select humidity x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by humidity",
            "湿度",
        )
    if obj.get("optype") == "senskwkwordata.humidity_bar":
        res = get_bar(
            "select humidity x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by humidity",
            "湿度",
        )
    if obj.get("optype") == "senskwkwordata.humidity_bar_v1":
        res = get_bar_v1(
            "select humidity x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by humidity",
            "湿度",
        )
    # senskwkwordata(传感器数据表)->pressure(压力)

    if obj.get("optype") == "senskwkwordata.pressure_pie":
        res = get_pie(
            "select pressure x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by pressure order by x desc",
            "压力",
        )
    if obj.get("optype") == "senskwkwordata.pressure_pie_v1":
        res = get_pie_v1(
            "select pressure x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by pressure",
            "压力",
        )
    if obj.get("optype") == "senskwkwordata.pressure_pie_v2":
        res = get_pie_v2(
            "select pressure x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by pressure",
            "压力",
        )
    if obj.get("optype") == "senskwkwordata.pressure_line":
        res = get_line(
            "select pressure x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by pressure",
            "压力",
        )
    if obj.get("optype") == "senskwkwordata.pressure_bar":
        res = get_bar(
            "select pressure x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by pressure",
            "压力",
        )
    if obj.get("optype") == "senskwkwordata.pressure_bar_v1":
        res = get_bar_v1(
            "select pressure x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by pressure",
            "压力",
        )
    # senskwkwordata(传感器数据表)->vibration(振动强度)

    if obj.get("optype") == "senskwkwordata.vibration_pie":
        res = get_pie(
            "select vibration x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by vibration order by x desc",
            "振动强度",
        )
    if obj.get("optype") == "senskwkwordata.vibration_pie_v1":
        res = get_pie_v1(
            "select vibration x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by vibration",
            "振动强度",
        )
    if obj.get("optype") == "senskwkwordata.vibration_pie_v2":
        res = get_pie_v2(
            "select vibration x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by vibration",
            "振动强度",
        )
    if obj.get("optype") == "senskwkwordata.vibration_line":
        res = get_line(
            "select vibration x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by vibration",
            "振动强度",
        )
    if obj.get("optype") == "senskwkwordata.vibration_bar":
        res = get_bar(
            "select vibration x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by vibration",
            "振动强度",
        )
    if obj.get("optype") == "senskwkwordata.vibration_bar_v1":
        res = get_bar_v1(
            "select vibration x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by vibration",
            "振动强度",
        )
    # senskwkwordata(传感器数据表)->status(状态如正常、异常)

    if obj.get("optype") == "senskwkwordata.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by status order by x desc",
            "状态如正常、异常",
        )
    if obj.get("optype") == "senskwkwordata.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by status",
            "状态如正常、异常",
        )
    if obj.get("optype") == "senskwkwordata.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by status",
            "状态如正常、异常",
        )
    if obj.get("optype") == "senskwkwordata.status_line":
        res = get_line(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by status",
            "状态如正常、异常",
        )
    if obj.get("optype") == "senskwkwordata.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by status",
            "状态如正常、异常",
        )
    if obj.get("optype") == "senskwkwordata.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by status",
            "状态如正常、异常",
        )
    # senskwkwordata(传感器数据表)->location(位置)

    if obj.get("optype") == "senskwkwordata.location_pie":
        res = get_pie(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by location order by x desc",
            "位置",
        )
    if obj.get("optype") == "senskwkwordata.location_pie_v1":
        res = get_pie_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by location",
            "位置",
        )
    if obj.get("optype") == "senskwkwordata.location_pie_v2":
        res = get_pie_v2(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by location",
            "位置",
        )
    if obj.get("optype") == "senskwkwordata.location_line":
        res = get_line(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by location",
            "位置",
        )
    if obj.get("optype") == "senskwkwordata.location_bar":
        res = get_bar(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by location",
            "位置",
        )
    if obj.get("optype") == "senskwkwordata.location_bar_v1":
        res = get_bar_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by location",
            "位置",
        )
    # senskwkwordata(传感器数据表)->deviceid(设备ID关联字段指向产生数据的设备)

    if obj.get("optype") == "senskwkwordata.deviceid_pie":
        res = get_pie(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by deviceid order by x desc",
            "设备ID关联字段指向产生数据的设备",
        )
    if obj.get("optype") == "senskwkwordata.deviceid_pie_v1":
        res = get_pie_v1(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by deviceid",
            "设备ID关联字段指向产生数据的设备",
        )
    if obj.get("optype") == "senskwkwordata.deviceid_pie_v2":
        res = get_pie_v2(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by deviceid",
            "设备ID关联字段指向产生数据的设备",
        )
    if obj.get("optype") == "senskwkwordata.deviceid_line":
        res = get_line(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by deviceid",
            "设备ID关联字段指向产生数据的设备",
        )
    if obj.get("optype") == "senskwkwordata.deviceid_bar":
        res = get_bar(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by deviceid",
            "设备ID关联字段指向产生数据的设备",
        )
    if obj.get("optype") == "senskwkwordata.deviceid_bar_v1":
        res = get_bar_v1(
            "select deviceid x,count(*) y from vm780_bb1ff2b101947be5.senskwkwordata group by deviceid",
            "设备ID关联字段指向产生数据的设备",
        )
    # camerainfo(监控摄像头信息表)->cameraid(摄像头ID)

    if obj.get("optype") == "camerainfo.cameraid_pie":
        res = get_pie(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraid order by x desc",
            "摄像头ID",
        )
    if obj.get("optype") == "camerainfo.cameraid_pie_v1":
        res = get_pie_v1(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraid",
            "摄像头ID",
        )
    if obj.get("optype") == "camerainfo.cameraid_pie_v2":
        res = get_pie_v2(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraid",
            "摄像头ID",
        )
    if obj.get("optype") == "camerainfo.cameraid_line":
        res = get_line(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraid",
            "摄像头ID",
        )
    if obj.get("optype") == "camerainfo.cameraid_bar":
        res = get_bar(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraid",
            "摄像头ID",
        )
    if obj.get("optype") == "camerainfo.cameraid_bar_v1":
        res = get_bar_v1(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraid",
            "摄像头ID",
        )
    # camerainfo(监控摄像头信息表)->cameraname(摄像头名称)

    if obj.get("optype") == "camerainfo.cameraname_pie":
        res = get_pie(
            "select cameraname x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraname order by x desc",
            "摄像头名称",
        )
    if obj.get("optype") == "camerainfo.cameraname_pie_v1":
        res = get_pie_v1(
            "select cameraname x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraname",
            "摄像头名称",
        )
    if obj.get("optype") == "camerainfo.cameraname_pie_v2":
        res = get_pie_v2(
            "select cameraname x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraname",
            "摄像头名称",
        )
    if obj.get("optype") == "camerainfo.cameraname_line":
        res = get_line(
            "select cameraname x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraname",
            "摄像头名称",
        )
    if obj.get("optype") == "camerainfo.cameraname_bar":
        res = get_bar(
            "select cameraname x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraname",
            "摄像头名称",
        )
    if obj.get("optype") == "camerainfo.cameraname_bar_v1":
        res = get_bar_v1(
            "select cameraname x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by cameraname",
            "摄像头名称",
        )
    # camerainfo(监控摄像头信息表)->location(安装位置)

    if obj.get("optype") == "camerainfo.location_pie":
        res = get_pie(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by location order by x desc",
            "安装位置",
        )
    if obj.get("optype") == "camerainfo.location_pie_v1":
        res = get_pie_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by location",
            "安装位置",
        )
    if obj.get("optype") == "camerainfo.location_pie_v2":
        res = get_pie_v2(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by location",
            "安装位置",
        )
    if obj.get("optype") == "camerainfo.location_line":
        res = get_line(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by location",
            "安装位置",
        )
    if obj.get("optype") == "camerainfo.location_bar":
        res = get_bar(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by location",
            "安装位置",
        )
    if obj.get("optype") == "camerainfo.location_bar_v1":
        res = get_bar_v1(
            "select location x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by location",
            "安装位置",
        )
    if obj.get("optype") == "camerainfo.ipaddressip_wordcloud":
        textlist = get_data(
            "SELECT ipaddressip result FROM vm780_bb1ff2b101947be5.camerainfo;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # camerainfo(监控摄像头信息表)->pkwkwortnumber(端口号)

    if obj.get("optype") == "camerainfo.pkwkwortnumber_pie":
        res = get_pie(
            "select pkwkwortnumber x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by pkwkwortnumber order by x desc",
            "端口号",
        )
    if obj.get("optype") == "camerainfo.pkwkwortnumber_pie_v1":
        res = get_pie_v1(
            "select pkwkwortnumber x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by pkwkwortnumber",
            "端口号",
        )
    if obj.get("optype") == "camerainfo.pkwkwortnumber_pie_v2":
        res = get_pie_v2(
            "select pkwkwortnumber x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by pkwkwortnumber",
            "端口号",
        )
    if obj.get("optype") == "camerainfo.pkwkwortnumber_line":
        res = get_line(
            "select pkwkwortnumber x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by pkwkwortnumber",
            "端口号",
        )
    if obj.get("optype") == "camerainfo.pkwkwortnumber_bar":
        res = get_bar(
            "select pkwkwortnumber x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by pkwkwortnumber",
            "端口号",
        )
    if obj.get("optype") == "camerainfo.pkwkwortnumber_bar_v1":
        res = get_bar_v1(
            "select pkwkwortnumber x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by pkwkwortnumber",
            "端口号",
        )
    # camerainfo(监控摄像头信息表)->resolution(分辨率)

    if obj.get("optype") == "camerainfo.resolution_pie":
        res = get_pie(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by resolution order by x desc",
            "分辨率",
        )
    if obj.get("optype") == "camerainfo.resolution_pie_v1":
        res = get_pie_v1(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "camerainfo.resolution_pie_v2":
        res = get_pie_v2(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "camerainfo.resolution_line":
        res = get_line(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "camerainfo.resolution_bar":
        res = get_bar(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "camerainfo.resolution_bar_v1":
        res = get_bar_v1(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by resolution",
            "分辨率",
        )
    # camerainfo(监控摄像头信息表)->status(状态如在线、离线)

    if obj.get("optype") == "camerainfo.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by status order by x desc",
            "状态如在线、离线",
        )
    if obj.get("optype") == "camerainfo.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by status",
            "状态如在线、离线",
        )
    if obj.get("optype") == "camerainfo.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by status",
            "状态如在线、离线",
        )
    if obj.get("optype") == "camerainfo.status_line":
        res = get_line(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by status",
            "状态如在线、离线",
        )
    if obj.get("optype") == "camerainfo.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by status",
            "状态如在线、离线",
        )
    if obj.get("optype") == "camerainfo.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by status",
            "状态如在线、离线",
        )
    if obj.get("optype") == "camerainfo.lkwkwastchecktime_line":
        res = get_line(
            "select lkwkwastchecktime x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by lkwkwastchecktime order by x",
            "最后检查时间",
        )
    # camerainfo(监控摄像头信息表)->connectedrobotid(连接机器人ID关联字段指向机器人信息)

    if obj.get("optype") == "camerainfo.connectedrobotid_pie":
        res = get_pie(
            "select connectedrobotid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by connectedrobotid order by x desc",
            "连接机器人ID关联字段指向机器人信息",
        )
    if obj.get("optype") == "camerainfo.connectedrobotid_pie_v1":
        res = get_pie_v1(
            "select connectedrobotid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by connectedrobotid",
            "连接机器人ID关联字段指向机器人信息",
        )
    if obj.get("optype") == "camerainfo.connectedrobotid_pie_v2":
        res = get_pie_v2(
            "select connectedrobotid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by connectedrobotid",
            "连接机器人ID关联字段指向机器人信息",
        )
    if obj.get("optype") == "camerainfo.connectedrobotid_line":
        res = get_line(
            "select connectedrobotid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by connectedrobotid",
            "连接机器人ID关联字段指向机器人信息",
        )
    if obj.get("optype") == "camerainfo.connectedrobotid_bar":
        res = get_bar(
            "select connectedrobotid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by connectedrobotid",
            "连接机器人ID关联字段指向机器人信息",
        )
    if obj.get("optype") == "camerainfo.connectedrobotid_bar_v1":
        res = get_bar_v1(
            "select connectedrobotid x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by connectedrobotid",
            "连接机器人ID关联字段指向机器人信息",
        )
    if obj.get("optype") == "camerainfo.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm780_bb1ff2b101947be5.camerainfo group by createdat order by x",
            "创建时间",
        )
    # videoreckwkword(视频录像表)->videofilepath(视频文件路径)

    if obj.get("optype") == "videoreckwkword.videofilepath_pie":
        res = get_pie(
            "select videofilepath x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by videofilepath order by x desc",
            "视频文件路径",
        )
    if obj.get("optype") == "videoreckwkword.videofilepath_pie_v1":
        res = get_pie_v1(
            "select videofilepath x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by videofilepath",
            "视频文件路径",
        )
    if obj.get("optype") == "videoreckwkword.videofilepath_pie_v2":
        res = get_pie_v2(
            "select videofilepath x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by videofilepath",
            "视频文件路径",
        )
    if obj.get("optype") == "videoreckwkword.videofilepath_line":
        res = get_line(
            "select videofilepath x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by videofilepath",
            "视频文件路径",
        )
    if obj.get("optype") == "videoreckwkword.videofilepath_bar":
        res = get_bar(
            "select videofilepath x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by videofilepath",
            "视频文件路径",
        )
    if obj.get("optype") == "videoreckwkword.videofilepath_bar_v1":
        res = get_bar_v1(
            "select videofilepath x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by videofilepath",
            "视频文件路径",
        )
    if obj.get("optype") == "videoreckwkword.reckwkwordkwkwingstarttime_line":
        res = get_line(
            "select reckwkwordkwkwingstarttime x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by reckwkwordkwkwingstarttime order by x",
            "录像开始时间",
        )
    if obj.get("optype") == "videoreckwkword.reckwkwordkwkwingendtime_line":
        res = get_line(
            "select reckwkwordkwkwingendtime x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by reckwkwordkwkwingendtime order by x",
            "录像结束时间",
        )
    # videoreckwkword(视频录像表)->cameraid(摄像头ID关联摄像头信息)

    if obj.get("optype") == "videoreckwkword.cameraid_pie":
        res = get_pie(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by cameraid order by x desc",
            "摄像头ID关联摄像头信息",
        )
    if obj.get("optype") == "videoreckwkword.cameraid_pie_v1":
        res = get_pie_v1(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by cameraid",
            "摄像头ID关联摄像头信息",
        )
    if obj.get("optype") == "videoreckwkword.cameraid_pie_v2":
        res = get_pie_v2(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by cameraid",
            "摄像头ID关联摄像头信息",
        )
    if obj.get("optype") == "videoreckwkword.cameraid_line":
        res = get_line(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by cameraid",
            "摄像头ID关联摄像头信息",
        )
    if obj.get("optype") == "videoreckwkword.cameraid_bar":
        res = get_bar(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by cameraid",
            "摄像头ID关联摄像头信息",
        )
    if obj.get("optype") == "videoreckwkword.cameraid_bar_v1":
        res = get_bar_v1(
            "select cameraid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by cameraid",
            "摄像头ID关联摄像头信息",
        )
    # videoreckwkword(视频录像表)->robotid(机器人ID关联机器人信息)

    if obj.get("optype") == "videoreckwkword.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by robotid order by x desc",
            "机器人ID关联机器人信息",
        )
    if obj.get("optype") == "videoreckwkword.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by robotid",
            "机器人ID关联机器人信息",
        )
    if obj.get("optype") == "videoreckwkword.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by robotid",
            "机器人ID关联机器人信息",
        )
    if obj.get("optype") == "videoreckwkword.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by robotid",
            "机器人ID关联机器人信息",
        )
    if obj.get("optype") == "videoreckwkword.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by robotid",
            "机器人ID关联机器人信息",
        )
    if obj.get("optype") == "videoreckwkword.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by robotid",
            "机器人ID关联机器人信息",
        )
    # videoreckwkword(视频录像表)->status(录像状态如正常、异常、删除)

    if obj.get("optype") == "videoreckwkword.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by status order by x desc",
            "录像状态如正常、异常、删除",
        )
    if obj.get("optype") == "videoreckwkword.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by status",
            "录像状态如正常、异常、删除",
        )
    if obj.get("optype") == "videoreckwkword.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by status",
            "录像状态如正常、异常、删除",
        )
    if obj.get("optype") == "videoreckwkword.status_line":
        res = get_line(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by status",
            "录像状态如正常、异常、删除",
        )
    if obj.get("optype") == "videoreckwkword.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by status",
            "录像状态如正常、异常、删除",
        )
    if obj.get("optype") == "videoreckwkword.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by status",
            "录像状态如正常、异常、删除",
        )
    # videoreckwkword(视频录像表)->resolution(录像分辨率)

    if obj.get("optype") == "videoreckwkword.resolution_pie":
        res = get_pie(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by resolution order by x desc",
            "录像分辨率",
        )
    if obj.get("optype") == "videoreckwkword.resolution_pie_v1":
        res = get_pie_v1(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by resolution",
            "录像分辨率",
        )
    if obj.get("optype") == "videoreckwkword.resolution_pie_v2":
        res = get_pie_v2(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by resolution",
            "录像分辨率",
        )
    if obj.get("optype") == "videoreckwkword.resolution_line":
        res = get_line(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by resolution",
            "录像分辨率",
        )
    if obj.get("optype") == "videoreckwkword.resolution_bar":
        res = get_bar(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by resolution",
            "录像分辨率",
        )
    if obj.get("optype") == "videoreckwkword.resolution_bar_v1":
        res = get_bar_v1(
            "select resolution x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by resolution",
            "录像分辨率",
        )
    # videoreckwkword(视频录像表)->duration(录像时长秒)

    if obj.get("optype") == "videoreckwkword.duration_pie":
        res = get_pie(
            "select duration x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by duration order by x desc",
            "录像时长秒",
        )
    if obj.get("optype") == "videoreckwkword.duration_pie_v1":
        res = get_pie_v1(
            "select duration x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by duration",
            "录像时长秒",
        )
    if obj.get("optype") == "videoreckwkword.duration_pie_v2":
        res = get_pie_v2(
            "select duration x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by duration",
            "录像时长秒",
        )
    if obj.get("optype") == "videoreckwkword.duration_line":
        res = get_line(
            "select duration x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by duration",
            "录像时长秒",
        )
    if obj.get("optype") == "videoreckwkword.duration_bar":
        res = get_bar(
            "select duration x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by duration",
            "录像时长秒",
        )
    if obj.get("optype") == "videoreckwkword.duration_bar_v1":
        res = get_bar_v1(
            "select duration x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by duration",
            "录像时长秒",
        )
    if obj.get("optype") == "videoreckwkword.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm780_bb1ff2b101947be5.videoreckwkword group by createdat order by x",
            "创建时间",
        )
    # robotoperationlog(机器人操作日志表)->robotid(机器人ID)

    if obj.get("optype") == "robotoperationlog.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "robotoperationlog.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotoperationlog.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotoperationlog.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotoperationlog.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotoperationlog.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotoperationlog.operationtime_line":
        res = get_line(
            "select operationtime x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationtime order by x",
            "操作时间",
        )
    # robotoperationlog(机器人操作日志表)->operationtype(操作类型)

    if obj.get("optype") == "robotoperationlog.operationtype_pie":
        res = get_pie(
            "select operationtype x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationtype order by x desc",
            "操作类型",
        )
    if obj.get("optype") == "robotoperationlog.operationtype_pie_v1":
        res = get_pie_v1(
            "select operationtype x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationtype",
            "操作类型",
        )
    if obj.get("optype") == "robotoperationlog.operationtype_pie_v2":
        res = get_pie_v2(
            "select operationtype x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationtype",
            "操作类型",
        )
    if obj.get("optype") == "robotoperationlog.operationtype_line":
        res = get_line(
            "select operationtype x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationtype",
            "操作类型",
        )
    if obj.get("optype") == "robotoperationlog.operationtype_bar":
        res = get_bar(
            "select operationtype x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationtype",
            "操作类型",
        )
    if obj.get("optype") == "robotoperationlog.operationtype_bar_v1":
        res = get_bar_v1(
            "select operationtype x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationtype",
            "操作类型",
        )
    # robotoperationlog(机器人操作日志表)->operationresult(操作结果)

    if obj.get("optype") == "robotoperationlog.operationresult_pie":
        res = get_pie(
            "select operationresult x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationresult order by x desc",
            "操作结果",
        )
    if obj.get("optype") == "robotoperationlog.operationresult_pie_v1":
        res = get_pie_v1(
            "select operationresult x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationresult",
            "操作结果",
        )
    if obj.get("optype") == "robotoperationlog.operationresult_pie_v2":
        res = get_pie_v2(
            "select operationresult x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationresult",
            "操作结果",
        )
    if obj.get("optype") == "robotoperationlog.operationresult_line":
        res = get_line(
            "select operationresult x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationresult",
            "操作结果",
        )
    if obj.get("optype") == "robotoperationlog.operationresult_bar":
        res = get_bar(
            "select operationresult x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationresult",
            "操作结果",
        )
    if obj.get("optype") == "robotoperationlog.operationresult_bar_v1":
        res = get_bar_v1(
            "select operationresult x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operationresult",
            "操作结果",
        )
    # robotoperationlog(机器人操作日志表)->operatkwkworid(操作员ID)

    if obj.get("optype") == "robotoperationlog.operatkwkworid_pie":
        res = get_pie(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operatkwkworid order by x desc",
            "操作员ID",
        )
    if obj.get("optype") == "robotoperationlog.operatkwkworid_pie_v1":
        res = get_pie_v1(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operatkwkworid",
            "操作员ID",
        )
    if obj.get("optype") == "robotoperationlog.operatkwkworid_pie_v2":
        res = get_pie_v2(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operatkwkworid",
            "操作员ID",
        )
    if obj.get("optype") == "robotoperationlog.operatkwkworid_line":
        res = get_line(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operatkwkworid",
            "操作员ID",
        )
    if obj.get("optype") == "robotoperationlog.operatkwkworid_bar":
        res = get_bar(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operatkwkworid",
            "操作员ID",
        )
    if obj.get("optype") == "robotoperationlog.operatkwkworid_bar_v1":
        res = get_bar_v1(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by operatkwkworid",
            "操作员ID",
        )
    # robotoperationlog(机器人操作日志表)->errkwkworcode(错误代码)

    if obj.get("optype") == "robotoperationlog.errkwkworcode_pie":
        res = get_pie(
            "select errkwkworcode x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkworcode order by x desc",
            "错误代码",
        )
    if obj.get("optype") == "robotoperationlog.errkwkworcode_pie_v1":
        res = get_pie_v1(
            "select errkwkworcode x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkworcode",
            "错误代码",
        )
    if obj.get("optype") == "robotoperationlog.errkwkworcode_pie_v2":
        res = get_pie_v2(
            "select errkwkworcode x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkworcode",
            "错误代码",
        )
    if obj.get("optype") == "robotoperationlog.errkwkworcode_line":
        res = get_line(
            "select errkwkworcode x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkworcode",
            "错误代码",
        )
    if obj.get("optype") == "robotoperationlog.errkwkworcode_bar":
        res = get_bar(
            "select errkwkworcode x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkworcode",
            "错误代码",
        )
    if obj.get("optype") == "robotoperationlog.errkwkworcode_bar_v1":
        res = get_bar_v1(
            "select errkwkworcode x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkworcode",
            "错误代码",
        )
    # robotoperationlog(机器人操作日志表)->errkwkwormessage(错误信息)

    if obj.get("optype") == "robotoperationlog.errkwkwormessage_pie":
        res = get_pie(
            "select errkwkwormessage x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkwormessage order by x desc",
            "错误信息",
        )
    if obj.get("optype") == "robotoperationlog.errkwkwormessage_pie_v1":
        res = get_pie_v1(
            "select errkwkwormessage x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkwormessage",
            "错误信息",
        )
    if obj.get("optype") == "robotoperationlog.errkwkwormessage_pie_v2":
        res = get_pie_v2(
            "select errkwkwormessage x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkwormessage",
            "错误信息",
        )
    if obj.get("optype") == "robotoperationlog.errkwkwormessage_line":
        res = get_line(
            "select errkwkwormessage x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkwormessage",
            "错误信息",
        )
    if obj.get("optype") == "robotoperationlog.errkwkwormessage_bar":
        res = get_bar(
            "select errkwkwormessage x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkwormessage",
            "错误信息",
        )
    if obj.get("optype") == "robotoperationlog.errkwkwormessage_bar_v1":
        res = get_bar_v1(
            "select errkwkwormessage x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by errkwkwormessage",
            "错误信息",
        )
    # robotoperationlog(机器人操作日志表)->machkwkwinelkwkwineid(生产线ID)

    if obj.get("optype") == "robotoperationlog.machkwkwinelkwkwineid_pie":
        res = get_pie(
            "select machkwkwinelkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by machkwkwinelkwkwineid order by x desc",
            "生产线ID",
        )
    if obj.get("optype") == "robotoperationlog.machkwkwinelkwkwineid_pie_v1":
        res = get_pie_v1(
            "select machkwkwinelkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by machkwkwinelkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "robotoperationlog.machkwkwinelkwkwineid_pie_v2":
        res = get_pie_v2(
            "select machkwkwinelkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by machkwkwinelkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "robotoperationlog.machkwkwinelkwkwineid_line":
        res = get_line(
            "select machkwkwinelkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by machkwkwinelkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "robotoperationlog.machkwkwinelkwkwineid_bar":
        res = get_bar(
            "select machkwkwinelkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by machkwkwinelkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "robotoperationlog.machkwkwinelkwkwineid_bar_v1":
        res = get_bar_v1(
            "select machkwkwinelkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.robotoperationlog group by machkwkwinelkwkwineid",
            "生产线ID",
        )
    # productionlkwkwineefficiency(生产线效率统计表)->lkwkwineid(生产线ID)

    if obj.get("optype") == "productionlkwkwineefficiency.lkwkwineid_pie":
        res = get_pie(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by lkwkwineid order by x desc",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.lkwkwineid_pie_v1":
        res = get_pie_v1(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by lkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.lkwkwineid_pie_v2":
        res = get_pie_v2(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by lkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.lkwkwineid_line":
        res = get_line(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by lkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.lkwkwineid_bar":
        res = get_bar(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by lkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.lkwkwineid_bar_v1":
        res = get_bar_v1(
            "select lkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by lkwkwineid",
            "生产线ID",
        )
    # productionlkwkwineefficiency(生产线效率统计表)->efficiencyrate(效率率)

    if obj.get("optype") == "productionlkwkwineefficiency.efficiencyrate_pie":
        res = get_pie(
            "select efficiencyrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by efficiencyrate order by x desc",
            "效率率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.efficiencyrate_pie_v1":
        res = get_pie_v1(
            "select efficiencyrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by efficiencyrate",
            "效率率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.efficiencyrate_pie_v2":
        res = get_pie_v2(
            "select efficiencyrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by efficiencyrate",
            "效率率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.efficiencyrate_line":
        res = get_line(
            "select efficiencyrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by efficiencyrate",
            "效率率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.efficiencyrate_bar":
        res = get_bar(
            "select efficiencyrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by efficiencyrate",
            "效率率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.efficiencyrate_bar_v1":
        res = get_bar_v1(
            "select efficiencyrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by efficiencyrate",
            "效率率",
        )
    # productionlkwkwineefficiency(生产线效率统计表)->dailyoutput(日产量)

    if obj.get("optype") == "productionlkwkwineefficiency.dailyoutput_pie":
        res = get_pie(
            "select dailyoutput x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by dailyoutput order by x desc",
            "日产量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.dailyoutput_pie_v1":
        res = get_pie_v1(
            "select dailyoutput x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by dailyoutput",
            "日产量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.dailyoutput_pie_v2":
        res = get_pie_v2(
            "select dailyoutput x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by dailyoutput",
            "日产量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.dailyoutput_line":
        res = get_line(
            "select dailyoutput x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by dailyoutput",
            "日产量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.dailyoutput_bar":
        res = get_bar(
            "select dailyoutput x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by dailyoutput",
            "日产量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.dailyoutput_bar_v1":
        res = get_bar_v1(
            "select dailyoutput x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by dailyoutput",
            "日产量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.downtimehours_line":
        res = get_line(
            "select downtimehours x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by downtimehours order by x",
            "停机时间小时",
        )
    # productionlkwkwineefficiency(生产线效率统计表)->makwkwintenancefrequency(维护频率)

    if obj.get("optype") == "productionlkwkwineefficiency.makwkwintenancefrequency_pie":
        res = get_pie(
            "select makwkwintenancefrequency x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by makwkwintenancefrequency order by x desc",
            "维护频率",
        )
    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.makwkwintenancefrequency_pie_v1"
    ):
        res = get_pie_v1(
            "select makwkwintenancefrequency x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by makwkwintenancefrequency",
            "维护频率",
        )
    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.makwkwintenancefrequency_pie_v2"
    ):
        res = get_pie_v2(
            "select makwkwintenancefrequency x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by makwkwintenancefrequency",
            "维护频率",
        )
    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.makwkwintenancefrequency_line"
    ):
        res = get_line(
            "select makwkwintenancefrequency x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by makwkwintenancefrequency",
            "维护频率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.makwkwintenancefrequency_bar":
        res = get_bar(
            "select makwkwintenancefrequency x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by makwkwintenancefrequency",
            "维护频率",
        )
    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.makwkwintenancefrequency_bar_v1"
    ):
        res = get_bar_v1(
            "select makwkwintenancefrequency x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by makwkwintenancefrequency",
            "维护频率",
        )
    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.lkwkwastmakwkwintenancedate_line"
    ):
        res = get_line(
            "select lkwkwastmakwkwintenancedate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by lkwkwastmakwkwintenancedate order by x",
            "上次维护日期",
        )
    # productionlkwkwineefficiency(生产线效率统计表)->robotcount(机器人数量)

    if obj.get("optype") == "productionlkwkwineefficiency.robotcount_pie":
        res = get_pie(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by robotcount order by x desc",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.robotcount_pie_v1":
        res = get_pie_v1(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.robotcount_pie_v2":
        res = get_pie_v2(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.robotcount_line":
        res = get_line(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.robotcount_bar":
        res = get_bar(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by robotcount",
            "机器人数量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.robotcount_bar_v1":
        res = get_bar_v1(
            "select robotcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by robotcount",
            "机器人数量",
        )
    # productionlkwkwineefficiency(生产线效率统计表)->operatkwkworcount(操作人员数量)

    if obj.get("optype") == "productionlkwkwineefficiency.operatkwkworcount_pie":
        res = get_pie(
            "select operatkwkworcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by operatkwkworcount order by x desc",
            "操作人员数量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.operatkwkworcount_pie_v1":
        res = get_pie_v1(
            "select operatkwkworcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by operatkwkworcount",
            "操作人员数量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.operatkwkworcount_pie_v2":
        res = get_pie_v2(
            "select operatkwkworcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by operatkwkworcount",
            "操作人员数量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.operatkwkworcount_line":
        res = get_line(
            "select operatkwkworcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by operatkwkworcount",
            "操作人员数量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.operatkwkworcount_bar":
        res = get_bar(
            "select operatkwkworcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by operatkwkworcount",
            "操作人员数量",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.operatkwkworcount_bar_v1":
        res = get_bar_v1(
            "select operatkwkworcount x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by operatkwkworcount",
            "操作人员数量",
        )
    # productionlkwkwineefficiency(生产线效率统计表)->productdefectrate(产品缺陷率)

    if obj.get("optype") == "productionlkwkwineefficiency.productdefectrate_pie":
        res = get_pie(
            "select productdefectrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by productdefectrate order by x desc",
            "产品缺陷率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.productdefectrate_pie_v1":
        res = get_pie_v1(
            "select productdefectrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by productdefectrate",
            "产品缺陷率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.productdefectrate_pie_v2":
        res = get_pie_v2(
            "select productdefectrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by productdefectrate",
            "产品缺陷率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.productdefectrate_line":
        res = get_line(
            "select productdefectrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by productdefectrate",
            "产品缺陷率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.productdefectrate_bar":
        res = get_bar(
            "select productdefectrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by productdefectrate",
            "产品缺陷率",
        )
    if obj.get("optype") == "productionlkwkwineefficiency.productdefectrate_bar_v1":
        res = get_bar_v1(
            "select productdefectrate x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by productdefectrate",
            "产品缺陷率",
        )
    # productionlkwkwineefficiency(生产线效率统计表)->kwkwassociatedwkwkworkshopid(关联车间ID)

    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.kwkwassociatedwkwkworkshopid_pie"
    ):
        res = get_pie(
            "select kwkwassociatedwkwkworkshopid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by kwkwassociatedwkwkworkshopid order by x desc",
            "关联车间ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.kwkwassociatedwkwkworkshopid_pie_v1"
    ):
        res = get_pie_v1(
            "select kwkwassociatedwkwkworkshopid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by kwkwassociatedwkwkworkshopid",
            "关联车间ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.kwkwassociatedwkwkworkshopid_pie_v2"
    ):
        res = get_pie_v2(
            "select kwkwassociatedwkwkworkshopid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by kwkwassociatedwkwkworkshopid",
            "关联车间ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.kwkwassociatedwkwkworkshopid_line"
    ):
        res = get_line(
            "select kwkwassociatedwkwkworkshopid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by kwkwassociatedwkwkworkshopid",
            "关联车间ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.kwkwassociatedwkwkworkshopid_bar"
    ):
        res = get_bar(
            "select kwkwassociatedwkwkworkshopid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by kwkwassociatedwkwkworkshopid",
            "关联车间ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwineefficiency.kwkwassociatedwkwkworkshopid_bar_v1"
    ):
        res = get_bar_v1(
            "select kwkwassociatedwkwkworkshopid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwineefficiency group by kwkwassociatedwkwkworkshopid",
            "关联车间ID",
        )
    # robotfirmwareupdate(机器人固件更新表)->robotid(机器人ID)

    if obj.get("optype") == "robotfirmwareupdate.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "robotfirmwareupdate.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotfirmwareupdate.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotfirmwareupdate.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotfirmwareupdate.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotfirmwareupdate.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by robotid",
            "机器人ID",
        )
    # robotfirmwareupdate(机器人固件更新表)->firmwareversion(固件版本号)

    if obj.get("optype") == "robotfirmwareupdate.firmwareversion_pie":
        res = get_pie(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by firmwareversion order by x desc",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.firmwareversion_pie_v1":
        res = get_pie_v1(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by firmwareversion",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.firmwareversion_pie_v2":
        res = get_pie_v2(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by firmwareversion",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.firmwareversion_line":
        res = get_line(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by firmwareversion",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.firmwareversion_bar":
        res = get_bar(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by firmwareversion",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.firmwareversion_bar_v1":
        res = get_bar_v1(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by firmwareversion",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatedate_line":
        res = get_line(
            "select updatedate x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatedate order by x",
            "更新日期",
        )
    # robotfirmwareupdate(机器人固件更新表)->updatestatus(更新状态)

    if obj.get("optype") == "robotfirmwareupdate.updatestatus_pie":
        res = get_pie(
            "select updatestatus x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatestatus order by x desc",
            "更新状态",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatestatus_pie_v1":
        res = get_pie_v1(
            "select updatestatus x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatestatus",
            "更新状态",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatestatus_pie_v2":
        res = get_pie_v2(
            "select updatestatus x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatestatus",
            "更新状态",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatestatus_line":
        res = get_line(
            "select updatestatus x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatestatus",
            "更新状态",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatestatus_bar":
        res = get_bar(
            "select updatestatus x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatestatus",
            "更新状态",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatestatus_bar_v1":
        res = get_bar_v1(
            "select updatestatus x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatestatus",
            "更新状态",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatedescription_wordcloud":
        textlist = get_data(
            "SELECT updatedescription result FROM vm780_bb1ff2b101947be5.robotfirmwareupdate;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # robotfirmwareupdate(机器人固件更新表)->previousfirmwareversion(前固件版本号)

    if obj.get("optype") == "robotfirmwareupdate.previousfirmwareversion_pie":
        res = get_pie(
            "select previousfirmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by previousfirmwareversion order by x desc",
            "前固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.previousfirmwareversion_pie_v1":
        res = get_pie_v1(
            "select previousfirmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by previousfirmwareversion",
            "前固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.previousfirmwareversion_pie_v2":
        res = get_pie_v2(
            "select previousfirmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by previousfirmwareversion",
            "前固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.previousfirmwareversion_line":
        res = get_line(
            "select previousfirmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by previousfirmwareversion",
            "前固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.previousfirmwareversion_bar":
        res = get_bar(
            "select previousfirmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by previousfirmwareversion",
            "前固件版本号",
        )
    if obj.get("optype") == "robotfirmwareupdate.previousfirmwareversion_bar_v1":
        res = get_bar_v1(
            "select previousfirmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by previousfirmwareversion",
            "前固件版本号",
        )
    # robotfirmwareupdate(机器人固件更新表)->updatedby(更新者)

    if obj.get("optype") == "robotfirmwareupdate.updatedby_pie":
        res = get_pie(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatedby order by x desc",
            "更新者",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatedby_pie_v1":
        res = get_pie_v1(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatedby",
            "更新者",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatedby_pie_v2":
        res = get_pie_v2(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatedby",
            "更新者",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatedby_line":
        res = get_line(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatedby",
            "更新者",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatedby_bar":
        res = get_bar(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatedby",
            "更新者",
        )
    if obj.get("optype") == "robotfirmwareupdate.updatedby_bar_v1":
        res = get_bar_v1(
            "select updatedby x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by updatedby",
            "更新者",
        )
    # robotfirmwareupdate(机器人固件更新表)->issuccessful(是否成功)

    if obj.get("optype") == "robotfirmwareupdate.issuccessful_pie":
        res = get_pie(
            "select issuccessful x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by issuccessful order by x desc",
            "是否成功",
        )
    if obj.get("optype") == "robotfirmwareupdate.issuccessful_pie_v1":
        res = get_pie_v1(
            "select issuccessful x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by issuccessful",
            "是否成功",
        )
    if obj.get("optype") == "robotfirmwareupdate.issuccessful_pie_v2":
        res = get_pie_v2(
            "select issuccessful x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by issuccessful",
            "是否成功",
        )
    if obj.get("optype") == "robotfirmwareupdate.issuccessful_line":
        res = get_line(
            "select issuccessful x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by issuccessful",
            "是否成功",
        )
    if obj.get("optype") == "robotfirmwareupdate.issuccessful_bar":
        res = get_bar(
            "select issuccessful x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by issuccessful",
            "是否成功",
        )
    if obj.get("optype") == "robotfirmwareupdate.issuccessful_bar_v1":
        res = get_bar_v1(
            "select issuccessful x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by issuccessful",
            "是否成功",
        )
    # robotfirmwareupdate(机器人固件更新表)->failurerekwkwason(失败原因)

    if obj.get("optype") == "robotfirmwareupdate.failurerekwkwason_pie":
        res = get_pie(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by failurerekwkwason order by x desc",
            "失败原因",
        )
    if obj.get("optype") == "robotfirmwareupdate.failurerekwkwason_pie_v1":
        res = get_pie_v1(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "robotfirmwareupdate.failurerekwkwason_pie_v2":
        res = get_pie_v2(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "robotfirmwareupdate.failurerekwkwason_line":
        res = get_line(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "robotfirmwareupdate.failurerekwkwason_bar":
        res = get_bar(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by failurerekwkwason",
            "失败原因",
        )
    if obj.get("optype") == "robotfirmwareupdate.failurerekwkwason_bar_v1":
        res = get_bar_v1(
            "select failurerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareupdate group by failurerekwkwason",
            "失败原因",
        )
    # robotfirmwareversion(机器人固件版本表)->firmwareid(固件ID)

    if obj.get("optype") == "robotfirmwareversion.firmwareid_pie":
        res = get_pie(
            "select firmwareid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareid order by x desc",
            "固件ID",
        )
    if obj.get("optype") == "robotfirmwareversion.firmwareid_pie_v1":
        res = get_pie_v1(
            "select firmwareid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareid",
            "固件ID",
        )
    if obj.get("optype") == "robotfirmwareversion.firmwareid_pie_v2":
        res = get_pie_v2(
            "select firmwareid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareid",
            "固件ID",
        )
    if obj.get("optype") == "robotfirmwareversion.firmwareid_line":
        res = get_line(
            "select firmwareid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareid",
            "固件ID",
        )
    if obj.get("optype") == "robotfirmwareversion.firmwareid_bar":
        res = get_bar(
            "select firmwareid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareid",
            "固件ID",
        )
    if obj.get("optype") == "robotfirmwareversion.firmwareid_bar_v1":
        res = get_bar_v1(
            "select firmwareid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareid",
            "固件ID",
        )
    # robotfirmwareversion(机器人固件版本表)->firmwareversion(固件版本号)

    if obj.get("optype") == "robotfirmwareversion.firmwareversion_pie":
        res = get_pie(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareversion order by x desc",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareversion.firmwareversion_pie_v1":
        res = get_pie_v1(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareversion",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareversion.firmwareversion_pie_v2":
        res = get_pie_v2(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareversion",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareversion.firmwareversion_line":
        res = get_line(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareversion",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareversion.firmwareversion_bar":
        res = get_bar(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareversion",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareversion.firmwareversion_bar_v1":
        res = get_bar_v1(
            "select firmwareversion x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by firmwareversion",
            "固件版本号",
        )
    if obj.get("optype") == "robotfirmwareversion.relekwkwasedate_line":
        res = get_line(
            "select relekwkwasedate x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by relekwkwasedate order by x",
            "发布日期",
        )
    # robotfirmwareversion(机器人固件版本表)->manufacturer(制造商)

    if obj.get("optype") == "robotfirmwareversion.manufacturer_pie":
        res = get_pie(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by manufacturer order by x desc",
            "制造商",
        )
    if obj.get("optype") == "robotfirmwareversion.manufacturer_pie_v1":
        res = get_pie_v1(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by manufacturer",
            "制造商",
        )
    if obj.get("optype") == "robotfirmwareversion.manufacturer_pie_v2":
        res = get_pie_v2(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by manufacturer",
            "制造商",
        )
    if obj.get("optype") == "robotfirmwareversion.manufacturer_line":
        res = get_line(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by manufacturer",
            "制造商",
        )
    if obj.get("optype") == "robotfirmwareversion.manufacturer_bar":
        res = get_bar(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by manufacturer",
            "制造商",
        )
    if obj.get("optype") == "robotfirmwareversion.manufacturer_bar_v1":
        res = get_bar_v1(
            "select manufacturer x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by manufacturer",
            "制造商",
        )
    # robotfirmwareversion(机器人固件版本表)->compatibility(兼容性说明)

    if obj.get("optype") == "robotfirmwareversion.compatibility_pie":
        res = get_pie(
            "select compatibility x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by compatibility order by x desc",
            "兼容性说明",
        )
    if obj.get("optype") == "robotfirmwareversion.compatibility_pie_v1":
        res = get_pie_v1(
            "select compatibility x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by compatibility",
            "兼容性说明",
        )
    if obj.get("optype") == "robotfirmwareversion.compatibility_pie_v2":
        res = get_pie_v2(
            "select compatibility x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by compatibility",
            "兼容性说明",
        )
    if obj.get("optype") == "robotfirmwareversion.compatibility_line":
        res = get_line(
            "select compatibility x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by compatibility",
            "兼容性说明",
        )
    if obj.get("optype") == "robotfirmwareversion.compatibility_bar":
        res = get_bar(
            "select compatibility x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by compatibility",
            "兼容性说明",
        )
    if obj.get("optype") == "robotfirmwareversion.compatibility_bar_v1":
        res = get_bar_v1(
            "select compatibility x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by compatibility",
            "兼容性说明",
        )
    # robotfirmwareversion(机器人固件版本表)->filesize(文件大小)

    if obj.get("optype") == "robotfirmwareversion.filesize_pie":
        res = get_pie(
            "select filesize x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by filesize order by x desc",
            "文件大小",
        )
    if obj.get("optype") == "robotfirmwareversion.filesize_pie_v1":
        res = get_pie_v1(
            "select filesize x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "robotfirmwareversion.filesize_pie_v2":
        res = get_pie_v2(
            "select filesize x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "robotfirmwareversion.filesize_line":
        res = get_line(
            "select filesize x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "robotfirmwareversion.filesize_bar":
        res = get_bar(
            "select filesize x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by filesize",
            "文件大小",
        )
    if obj.get("optype") == "robotfirmwareversion.filesize_bar_v1":
        res = get_bar_v1(
            "select filesize x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by filesize",
            "文件大小",
        )
    # robotfirmwareversion(机器人固件版本表)->downloadurl(下载链接)

    if obj.get("optype") == "robotfirmwareversion.downloadurl_pie":
        res = get_pie(
            "select downloadurl x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by downloadurl order by x desc",
            "下载链接",
        )
    if obj.get("optype") == "robotfirmwareversion.downloadurl_pie_v1":
        res = get_pie_v1(
            "select downloadurl x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by downloadurl",
            "下载链接",
        )
    if obj.get("optype") == "robotfirmwareversion.downloadurl_pie_v2":
        res = get_pie_v2(
            "select downloadurl x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by downloadurl",
            "下载链接",
        )
    if obj.get("optype") == "robotfirmwareversion.downloadurl_line":
        res = get_line(
            "select downloadurl x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by downloadurl",
            "下载链接",
        )
    if obj.get("optype") == "robotfirmwareversion.downloadurl_bar":
        res = get_bar(
            "select downloadurl x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by downloadurl",
            "下载链接",
        )
    if obj.get("optype") == "robotfirmwareversion.downloadurl_bar_v1":
        res = get_bar_v1(
            "select downloadurl x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by downloadurl",
            "下载链接",
        )
    if obj.get("optype") == "robotfirmwareversion.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm780_bb1ff2b101947be5.robotfirmwareversion;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # robotfirmwareversion(机器人固件版本表)->robotmokwkwdelid(机器人模型ID关联字段)

    if obj.get("optype") == "robotfirmwareversion.robotmokwkwdelid_pie":
        res = get_pie(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by robotmokwkwdelid order by x desc",
            "机器人模型ID关联字段",
        )
    if obj.get("optype") == "robotfirmwareversion.robotmokwkwdelid_pie_v1":
        res = get_pie_v1(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by robotmokwkwdelid",
            "机器人模型ID关联字段",
        )
    if obj.get("optype") == "robotfirmwareversion.robotmokwkwdelid_pie_v2":
        res = get_pie_v2(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by robotmokwkwdelid",
            "机器人模型ID关联字段",
        )
    if obj.get("optype") == "robotfirmwareversion.robotmokwkwdelid_line":
        res = get_line(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by robotmokwkwdelid",
            "机器人模型ID关联字段",
        )
    if obj.get("optype") == "robotfirmwareversion.robotmokwkwdelid_bar":
        res = get_bar(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by robotmokwkwdelid",
            "机器人模型ID关联字段",
        )
    if obj.get("optype") == "robotfirmwareversion.robotmokwkwdelid_bar_v1":
        res = get_bar_v1(
            "select robotmokwkwdelid x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by robotmokwkwdelid",
            "机器人模型ID关联字段",
        )
    # robotfirmwareversion(机器人固件版本表)->islatest(是否为最新版本)

    if obj.get("optype") == "robotfirmwareversion.islatest_pie":
        res = get_pie(
            "select islatest x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by islatest order by x desc",
            "是否为最新版本",
        )
    if obj.get("optype") == "robotfirmwareversion.islatest_pie_v1":
        res = get_pie_v1(
            "select islatest x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by islatest",
            "是否为最新版本",
        )
    if obj.get("optype") == "robotfirmwareversion.islatest_pie_v2":
        res = get_pie_v2(
            "select islatest x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by islatest",
            "是否为最新版本",
        )
    if obj.get("optype") == "robotfirmwareversion.islatest_line":
        res = get_line(
            "select islatest x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by islatest",
            "是否为最新版本",
        )
    if obj.get("optype") == "robotfirmwareversion.islatest_bar":
        res = get_bar(
            "select islatest x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by islatest",
            "是否为最新版本",
        )
    if obj.get("optype") == "robotfirmwareversion.islatest_bar_v1":
        res = get_bar_v1(
            "select islatest x,count(*) y from vm780_bb1ff2b101947be5.robotfirmwareversion group by islatest",
            "是否为最新版本",
        )
    # productionlkwkwinesafetyrule(生产线安全规则表)->ruleid(规则ID)

    if obj.get("optype") == "productionlkwkwinesafetyrule.ruleid_pie":
        res = get_pie(
            "select ruleid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by ruleid order by x desc",
            "规则ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.ruleid_pie_v1":
        res = get_pie_v1(
            "select ruleid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by ruleid",
            "规则ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.ruleid_pie_v2":
        res = get_pie_v2(
            "select ruleid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by ruleid",
            "规则ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.ruleid_line":
        res = get_line(
            "select ruleid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by ruleid",
            "规则ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.ruleid_bar":
        res = get_bar(
            "select ruleid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by ruleid",
            "规则ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.ruleid_bar_v1":
        res = get_bar_v1(
            "select ruleid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by ruleid",
            "规则ID",
        )
    # productionlkwkwinesafetyrule(生产线安全规则表)->rulename(规则名称)

    if obj.get("optype") == "productionlkwkwinesafetyrule.rulename_pie":
        res = get_pie(
            "select rulename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by rulename order by x desc",
            "规则名称",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.rulename_pie_v1":
        res = get_pie_v1(
            "select rulename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by rulename",
            "规则名称",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.rulename_pie_v2":
        res = get_pie_v2(
            "select rulename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by rulename",
            "规则名称",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.rulename_line":
        res = get_line(
            "select rulename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by rulename",
            "规则名称",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.rulename_bar":
        res = get_bar(
            "select rulename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by rulename",
            "规则名称",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.rulename_bar_v1":
        res = get_bar_v1(
            "select rulename x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by rulename",
            "规则名称",
        )
    # productionlkwkwinesafetyrule(生产线安全规则表)->productionlkwkwineid(生产线ID)

    if obj.get("optype") == "productionlkwkwinesafetyrule.productionlkwkwineid_pie":
        res = get_pie(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by productionlkwkwineid order by x desc",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.productionlkwkwineid_pie_v1":
        res = get_pie_v1(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by productionlkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.productionlkwkwineid_pie_v2":
        res = get_pie_v2(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by productionlkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.productionlkwkwineid_line":
        res = get_line(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by productionlkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.productionlkwkwineid_bar":
        res = get_bar(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by productionlkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.productionlkwkwineid_bar_v1":
        res = get_bar_v1(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by productionlkwkwineid",
            "生产线ID",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.ruledescription_wordcloud":
        textlist = get_data(
            "SELECT ruledescription result FROM vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # productionlkwkwinesafetyrule(生产线安全规则表)->severitylevel(严重等级)

    if obj.get("optype") == "productionlkwkwinesafetyrule.severitylevel_pie":
        res = get_pie(
            "select severitylevel x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by severitylevel order by x desc",
            "严重等级",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.severitylevel_pie_v1":
        res = get_pie_v1(
            "select severitylevel x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by severitylevel",
            "严重等级",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.severitylevel_pie_v2":
        res = get_pie_v2(
            "select severitylevel x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by severitylevel",
            "严重等级",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.severitylevel_line":
        res = get_line(
            "select severitylevel x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by severitylevel",
            "严重等级",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.severitylevel_bar":
        res = get_bar(
            "select severitylevel x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by severitylevel",
            "严重等级",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.severitylevel_bar_v1":
        res = get_bar_v1(
            "select severitylevel x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by severitylevel",
            "严重等级",
        )
    # productionlkwkwinesafetyrule(生产线安全规则表)->detectionmethod(检测方式)

    if obj.get("optype") == "productionlkwkwinesafetyrule.detectionmethod_pie":
        res = get_pie(
            "select detectionmethod x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by detectionmethod order by x desc",
            "检测方式",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.detectionmethod_pie_v1":
        res = get_pie_v1(
            "select detectionmethod x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by detectionmethod",
            "检测方式",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.detectionmethod_pie_v2":
        res = get_pie_v2(
            "select detectionmethod x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by detectionmethod",
            "检测方式",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.detectionmethod_line":
        res = get_line(
            "select detectionmethod x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by detectionmethod",
            "检测方式",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.detectionmethod_bar":
        res = get_bar(
            "select detectionmethod x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by detectionmethod",
            "检测方式",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.detectionmethod_bar_v1":
        res = get_bar_v1(
            "select detectionmethod x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by detectionmethod",
            "检测方式",
        )
    # productionlkwkwinesafetyrule(生产线安全规则表)->alertthreshold(报警阈值)

    if obj.get("optype") == "productionlkwkwinesafetyrule.alertthreshold_pie":
        res = get_pie(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertthreshold order by x desc",
            "报警阈值",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.alertthreshold_pie_v1":
        res = get_pie_v1(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertthreshold",
            "报警阈值",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.alertthreshold_pie_v2":
        res = get_pie_v2(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertthreshold",
            "报警阈值",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.alertthreshold_line":
        res = get_line(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertthreshold",
            "报警阈值",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.alertthreshold_bar":
        res = get_bar(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertthreshold",
            "报警阈值",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.alertthreshold_bar_v1":
        res = get_bar_v1(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertthreshold",
            "报警阈值",
        )
    # productionlkwkwinesafetyrule(生产线安全规则表)->alertrecipients(报警接收人)

    if obj.get("optype") == "productionlkwkwinesafetyrule.alertrecipients_pie":
        res = get_pie(
            "select alertrecipients x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertrecipients order by x desc",
            "报警接收人",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.alertrecipients_pie_v1":
        res = get_pie_v1(
            "select alertrecipients x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertrecipients",
            "报警接收人",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.alertrecipients_pie_v2":
        res = get_pie_v2(
            "select alertrecipients x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertrecipients",
            "报警接收人",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.alertrecipients_line":
        res = get_line(
            "select alertrecipients x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertrecipients",
            "报警接收人",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.alertrecipients_bar":
        res = get_bar(
            "select alertrecipients x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertrecipients",
            "报警接收人",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.alertrecipients_bar_v1":
        res = get_bar_v1(
            "select alertrecipients x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by alertrecipients",
            "报警接收人",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "productionlkwkwinesafetyrule.modkwkwifiedat_line":
        res = get_line(
            "select modkwkwifiedat x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinesafetyrule group by modkwkwifiedat order by x",
            "修改时间",
        )
    # robotsafetyconfig(机器人安全配置表)->robotid(机器人ID)

    if obj.get("optype") == "robotsafetyconfig.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "robotsafetyconfig.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotsafetyconfig.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotsafetyconfig.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotsafetyconfig.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotsafetyconfig.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by robotid",
            "机器人ID",
        )
    # robotsafetyconfig(机器人安全配置表)->safetylevel(安全等级)

    if obj.get("optype") == "robotsafetyconfig.safetylevel_pie":
        res = get_pie(
            "select safetylevel x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by safetylevel order by x desc",
            "安全等级",
        )
    if obj.get("optype") == "robotsafetyconfig.safetylevel_pie_v1":
        res = get_pie_v1(
            "select safetylevel x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by safetylevel",
            "安全等级",
        )
    if obj.get("optype") == "robotsafetyconfig.safetylevel_pie_v2":
        res = get_pie_v2(
            "select safetylevel x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by safetylevel",
            "安全等级",
        )
    if obj.get("optype") == "robotsafetyconfig.safetylevel_line":
        res = get_line(
            "select safetylevel x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by safetylevel",
            "安全等级",
        )
    if obj.get("optype") == "robotsafetyconfig.safetylevel_bar":
        res = get_bar(
            "select safetylevel x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by safetylevel",
            "安全等级",
        )
    if obj.get("optype") == "robotsafetyconfig.safetylevel_bar_v1":
        res = get_bar_v1(
            "select safetylevel x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by safetylevel",
            "安全等级",
        )
    # robotsafetyconfig(机器人安全配置表)->alertthreshold(警报阈值)

    if obj.get("optype") == "robotsafetyconfig.alertthreshold_pie":
        res = get_pie(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by alertthreshold order by x desc",
            "警报阈值",
        )
    if obj.get("optype") == "robotsafetyconfig.alertthreshold_pie_v1":
        res = get_pie_v1(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by alertthreshold",
            "警报阈值",
        )
    if obj.get("optype") == "robotsafetyconfig.alertthreshold_pie_v2":
        res = get_pie_v2(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by alertthreshold",
            "警报阈值",
        )
    if obj.get("optype") == "robotsafetyconfig.alertthreshold_line":
        res = get_line(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by alertthreshold",
            "警报阈值",
        )
    if obj.get("optype") == "robotsafetyconfig.alertthreshold_bar":
        res = get_bar(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by alertthreshold",
            "警报阈值",
        )
    if obj.get("optype") == "robotsafetyconfig.alertthreshold_bar_v1":
        res = get_bar_v1(
            "select alertthreshold x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by alertthreshold",
            "警报阈值",
        )
    # robotsafetyconfig(机器人安全配置表)->emergencystopcode(紧急停止码)

    if obj.get("optype") == "robotsafetyconfig.emergencystopcode_pie":
        res = get_pie(
            "select emergencystopcode x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by emergencystopcode order by x desc",
            "紧急停止码",
        )
    if obj.get("optype") == "robotsafetyconfig.emergencystopcode_pie_v1":
        res = get_pie_v1(
            "select emergencystopcode x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by emergencystopcode",
            "紧急停止码",
        )
    if obj.get("optype") == "robotsafetyconfig.emergencystopcode_pie_v2":
        res = get_pie_v2(
            "select emergencystopcode x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by emergencystopcode",
            "紧急停止码",
        )
    if obj.get("optype") == "robotsafetyconfig.emergencystopcode_line":
        res = get_line(
            "select emergencystopcode x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by emergencystopcode",
            "紧急停止码",
        )
    if obj.get("optype") == "robotsafetyconfig.emergencystopcode_bar":
        res = get_bar(
            "select emergencystopcode x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by emergencystopcode",
            "紧急停止码",
        )
    if obj.get("optype") == "robotsafetyconfig.emergencystopcode_bar_v1":
        res = get_bar_v1(
            "select emergencystopcode x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by emergencystopcode",
            "紧急停止码",
        )
    # robotsafetyconfig(机器人安全配置表)->makwkwintenanceinterval(维护间隔)

    if obj.get("optype") == "robotsafetyconfig.makwkwintenanceinterval_pie":
        res = get_pie(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by makwkwintenanceinterval order by x desc",
            "维护间隔",
        )
    if obj.get("optype") == "robotsafetyconfig.makwkwintenanceinterval_pie_v1":
        res = get_pie_v1(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by makwkwintenanceinterval",
            "维护间隔",
        )
    if obj.get("optype") == "robotsafetyconfig.makwkwintenanceinterval_pie_v2":
        res = get_pie_v2(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by makwkwintenanceinterval",
            "维护间隔",
        )
    if obj.get("optype") == "robotsafetyconfig.makwkwintenanceinterval_line":
        res = get_line(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by makwkwintenanceinterval",
            "维护间隔",
        )
    if obj.get("optype") == "robotsafetyconfig.makwkwintenanceinterval_bar":
        res = get_bar(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by makwkwintenanceinterval",
            "维护间隔",
        )
    if obj.get("optype") == "robotsafetyconfig.makwkwintenanceinterval_bar_v1":
        res = get_bar_v1(
            "select makwkwintenanceinterval x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by makwkwintenanceinterval",
            "维护间隔",
        )
    if obj.get("optype") == "robotsafetyconfig.lkwkwastmakwkwintenancedate_line":
        res = get_line(
            "select lkwkwastmakwkwintenancedate x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by lkwkwastmakwkwintenancedate order by x",
            "上次维护日期",
        )
    # robotsafetyconfig(机器人安全配置表)->operatkwkwingstatus(运行状态)

    if obj.get("optype") == "robotsafetyconfig.operatkwkwingstatus_pie":
        res = get_pie(
            "select operatkwkwingstatus x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by operatkwkwingstatus order by x desc",
            "运行状态",
        )
    if obj.get("optype") == "robotsafetyconfig.operatkwkwingstatus_pie_v1":
        res = get_pie_v1(
            "select operatkwkwingstatus x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by operatkwkwingstatus",
            "运行状态",
        )
    if obj.get("optype") == "robotsafetyconfig.operatkwkwingstatus_pie_v2":
        res = get_pie_v2(
            "select operatkwkwingstatus x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by operatkwkwingstatus",
            "运行状态",
        )
    if obj.get("optype") == "robotsafetyconfig.operatkwkwingstatus_line":
        res = get_line(
            "select operatkwkwingstatus x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by operatkwkwingstatus",
            "运行状态",
        )
    if obj.get("optype") == "robotsafetyconfig.operatkwkwingstatus_bar":
        res = get_bar(
            "select operatkwkwingstatus x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by operatkwkwingstatus",
            "运行状态",
        )
    if obj.get("optype") == "robotsafetyconfig.operatkwkwingstatus_bar_v1":
        res = get_bar_v1(
            "select operatkwkwingstatus x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by operatkwkwingstatus",
            "运行状态",
        )
    # robotsafetyconfig(机器人安全配置表)->faulthkwkwistkwkwory(故障历史)

    if obj.get("optype") == "robotsafetyconfig.faulthkwkwistkwkwory_pie":
        res = get_pie(
            "select faulthkwkwistkwkwory x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by faulthkwkwistkwkwory order by x desc",
            "故障历史",
        )
    if obj.get("optype") == "robotsafetyconfig.faulthkwkwistkwkwory_pie_v1":
        res = get_pie_v1(
            "select faulthkwkwistkwkwory x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by faulthkwkwistkwkwory",
            "故障历史",
        )
    if obj.get("optype") == "robotsafetyconfig.faulthkwkwistkwkwory_pie_v2":
        res = get_pie_v2(
            "select faulthkwkwistkwkwory x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by faulthkwkwistkwkwory",
            "故障历史",
        )
    if obj.get("optype") == "robotsafetyconfig.faulthkwkwistkwkwory_line":
        res = get_line(
            "select faulthkwkwistkwkwory x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by faulthkwkwistkwkwory",
            "故障历史",
        )
    if obj.get("optype") == "robotsafetyconfig.faulthkwkwistkwkwory_bar":
        res = get_bar(
            "select faulthkwkwistkwkwory x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by faulthkwkwistkwkwory",
            "故障历史",
        )
    if obj.get("optype") == "robotsafetyconfig.faulthkwkwistkwkwory_bar_v1":
        res = get_bar_v1(
            "select faulthkwkwistkwkwory x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by faulthkwkwistkwkwory",
            "故障历史",
        )
    # robotsafetyconfig(机器人安全配置表)->associatedwkwkworkstationid(关联工作站ID)

    if obj.get("optype") == "robotsafetyconfig.associatedwkwkworkstationid_pie":
        res = get_pie(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by associatedwkwkworkstationid order by x desc",
            "关联工作站ID",
        )
    if obj.get("optype") == "robotsafetyconfig.associatedwkwkworkstationid_pie_v1":
        res = get_pie_v1(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by associatedwkwkworkstationid",
            "关联工作站ID",
        )
    if obj.get("optype") == "robotsafetyconfig.associatedwkwkworkstationid_pie_v2":
        res = get_pie_v2(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by associatedwkwkworkstationid",
            "关联工作站ID",
        )
    if obj.get("optype") == "robotsafetyconfig.associatedwkwkworkstationid_line":
        res = get_line(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by associatedwkwkworkstationid",
            "关联工作站ID",
        )
    if obj.get("optype") == "robotsafetyconfig.associatedwkwkworkstationid_bar":
        res = get_bar(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by associatedwkwkworkstationid",
            "关联工作站ID",
        )
    if obj.get("optype") == "robotsafetyconfig.associatedwkwkworkstationid_bar_v1":
        res = get_bar_v1(
            "select associatedwkwkworkstationid x,count(*) y from vm780_bb1ff2b101947be5.robotsafetyconfig group by associatedwkwkworkstationid",
            "关联工作站ID",
        )
    # robotinspectionplan(机器人巡检计划表)->planid(计划ID)

    if obj.get("optype") == "robotinspectionplan.planid_pie":
        res = get_pie(
            "select planid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by planid order by x desc",
            "计划ID",
        )
    if obj.get("optype") == "robotinspectionplan.planid_pie_v1":
        res = get_pie_v1(
            "select planid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by planid",
            "计划ID",
        )
    if obj.get("optype") == "robotinspectionplan.planid_pie_v2":
        res = get_pie_v2(
            "select planid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by planid",
            "计划ID",
        )
    if obj.get("optype") == "robotinspectionplan.planid_line":
        res = get_line(
            "select planid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by planid",
            "计划ID",
        )
    if obj.get("optype") == "robotinspectionplan.planid_bar":
        res = get_bar(
            "select planid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by planid",
            "计划ID",
        )
    if obj.get("optype") == "robotinspectionplan.planid_bar_v1":
        res = get_bar_v1(
            "select planid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by planid",
            "计划ID",
        )
    # robotinspectionplan(机器人巡检计划表)->robotid(机器人ID)

    if obj.get("optype") == "robotinspectionplan.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "robotinspectionplan.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotinspectionplan.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotinspectionplan.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotinspectionplan.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotinspectionplan.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotinspectionplan.starttime_line":
        res = get_line(
            "select starttime x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by starttime order by x",
            "开始时间",
        )
    if obj.get("optype") == "robotinspectionplan.endtime_line":
        res = get_line(
            "select endtime x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by endtime order by x",
            "结束时间",
        )
    # robotinspectionplan(机器人巡检计划表)->frequency(巡检频率)

    if obj.get("optype") == "robotinspectionplan.frequency_pie":
        res = get_pie(
            "select frequency x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by frequency order by x desc",
            "巡检频率",
        )
    if obj.get("optype") == "robotinspectionplan.frequency_pie_v1":
        res = get_pie_v1(
            "select frequency x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by frequency",
            "巡检频率",
        )
    if obj.get("optype") == "robotinspectionplan.frequency_pie_v2":
        res = get_pie_v2(
            "select frequency x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by frequency",
            "巡检频率",
        )
    if obj.get("optype") == "robotinspectionplan.frequency_line":
        res = get_line(
            "select frequency x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by frequency",
            "巡检频率",
        )
    if obj.get("optype") == "robotinspectionplan.frequency_bar":
        res = get_bar(
            "select frequency x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by frequency",
            "巡检频率",
        )
    if obj.get("optype") == "robotinspectionplan.frequency_bar_v1":
        res = get_bar_v1(
            "select frequency x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by frequency",
            "巡检频率",
        )
    # robotinspectionplan(机器人巡检计划表)->inspectionarea(巡检区域)

    if obj.get("optype") == "robotinspectionplan.inspectionarea_pie":
        res = get_pie(
            "select inspectionarea x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by inspectionarea order by x desc",
            "巡检区域",
        )
    if obj.get("optype") == "robotinspectionplan.inspectionarea_pie_v1":
        res = get_pie_v1(
            "select inspectionarea x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by inspectionarea",
            "巡检区域",
        )
    if obj.get("optype") == "robotinspectionplan.inspectionarea_pie_v2":
        res = get_pie_v2(
            "select inspectionarea x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by inspectionarea",
            "巡检区域",
        )
    if obj.get("optype") == "robotinspectionplan.inspectionarea_line":
        res = get_line(
            "select inspectionarea x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by inspectionarea",
            "巡检区域",
        )
    if obj.get("optype") == "robotinspectionplan.inspectionarea_bar":
        res = get_bar(
            "select inspectionarea x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by inspectionarea",
            "巡检区域",
        )
    if obj.get("optype") == "robotinspectionplan.inspectionarea_bar_v1":
        res = get_bar_v1(
            "select inspectionarea x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by inspectionarea",
            "巡检区域",
        )
    # robotinspectionplan(机器人巡检计划表)->status(计划状态)

    if obj.get("optype") == "robotinspectionplan.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by status order by x desc",
            "计划状态",
        )
    if obj.get("optype") == "robotinspectionplan.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by status",
            "计划状态",
        )
    if obj.get("optype") == "robotinspectionplan.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by status",
            "计划状态",
        )
    if obj.get("optype") == "robotinspectionplan.status_line":
        res = get_line(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by status",
            "计划状态",
        )
    if obj.get("optype") == "robotinspectionplan.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by status",
            "计划状态",
        )
    if obj.get("optype") == "robotinspectionplan.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by status",
            "计划状态",
        )
    # robotinspectionplan(机器人巡检计划表)->createdby(创建者)

    if obj.get("optype") == "robotinspectionplan.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by createdby order by x desc",
            "创建者",
        )
    if obj.get("optype") == "robotinspectionplan.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by createdby",
            "创建者",
        )
    if obj.get("optype") == "robotinspectionplan.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by createdby",
            "创建者",
        )
    if obj.get("optype") == "robotinspectionplan.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by createdby",
            "创建者",
        )
    if obj.get("optype") == "robotinspectionplan.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by createdby",
            "创建者",
        )
    if obj.get("optype") == "robotinspectionplan.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by createdby",
            "创建者",
        )
    # robotinspectionplan(机器人巡检计划表)->lkwkwastmodkwkwifiedby(最后修改者)

    if obj.get("optype") == "robotinspectionplan.lkwkwastmodkwkwifiedby_pie":
        res = get_pie(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by lkwkwastmodkwkwifiedby order by x desc",
            "最后修改者",
        )
    if obj.get("optype") == "robotinspectionplan.lkwkwastmodkwkwifiedby_pie_v1":
        res = get_pie_v1(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by lkwkwastmodkwkwifiedby",
            "最后修改者",
        )
    if obj.get("optype") == "robotinspectionplan.lkwkwastmodkwkwifiedby_pie_v2":
        res = get_pie_v2(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by lkwkwastmodkwkwifiedby",
            "最后修改者",
        )
    if obj.get("optype") == "robotinspectionplan.lkwkwastmodkwkwifiedby_line":
        res = get_line(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by lkwkwastmodkwkwifiedby",
            "最后修改者",
        )
    if obj.get("optype") == "robotinspectionplan.lkwkwastmodkwkwifiedby_bar":
        res = get_bar(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by lkwkwastmodkwkwifiedby",
            "最后修改者",
        )
    if obj.get("optype") == "robotinspectionplan.lkwkwastmodkwkwifiedby_bar_v1":
        res = get_bar_v1(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by lkwkwastmodkwkwifiedby",
            "最后修改者",
        )
    if obj.get("optype") == "robotinspectionplan.lkwkwastmodkwkwifiedtime_line":
        res = get_line(
            "select lkwkwastmodkwkwifiedtime x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by lkwkwastmodkwkwifiedtime order by x",
            "最后修改时间",
        )
    # robotinspectionplan(机器人巡检计划表)->associatedtkwkwaskid(关联任务ID)

    if obj.get("optype") == "robotinspectionplan.associatedtkwkwaskid_pie":
        res = get_pie(
            "select associatedtkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by associatedtkwkwaskid order by x desc",
            "关联任务ID",
        )
    if obj.get("optype") == "robotinspectionplan.associatedtkwkwaskid_pie_v1":
        res = get_pie_v1(
            "select associatedtkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by associatedtkwkwaskid",
            "关联任务ID",
        )
    if obj.get("optype") == "robotinspectionplan.associatedtkwkwaskid_pie_v2":
        res = get_pie_v2(
            "select associatedtkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by associatedtkwkwaskid",
            "关联任务ID",
        )
    if obj.get("optype") == "robotinspectionplan.associatedtkwkwaskid_line":
        res = get_line(
            "select associatedtkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by associatedtkwkwaskid",
            "关联任务ID",
        )
    if obj.get("optype") == "robotinspectionplan.associatedtkwkwaskid_bar":
        res = get_bar(
            "select associatedtkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by associatedtkwkwaskid",
            "关联任务ID",
        )
    if obj.get("optype") == "robotinspectionplan.associatedtkwkwaskid_bar_v1":
        res = get_bar_v1(
            "select associatedtkwkwaskid x,count(*) y from vm780_bb1ff2b101947be5.robotinspectionplan group by associatedtkwkwaskid",
            "关联任务ID",
        )
    # inspectionresult(巡检结果表)->inspectionid(巡检编号)

    if obj.get("optype") == "inspectionresult.inspectionid_pie":
        res = get_pie(
            "select inspectionid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectionid order by x desc",
            "巡检编号",
        )
    if obj.get("optype") == "inspectionresult.inspectionid_pie_v1":
        res = get_pie_v1(
            "select inspectionid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectionid",
            "巡检编号",
        )
    if obj.get("optype") == "inspectionresult.inspectionid_pie_v2":
        res = get_pie_v2(
            "select inspectionid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectionid",
            "巡检编号",
        )
    if obj.get("optype") == "inspectionresult.inspectionid_line":
        res = get_line(
            "select inspectionid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectionid",
            "巡检编号",
        )
    if obj.get("optype") == "inspectionresult.inspectionid_bar":
        res = get_bar(
            "select inspectionid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectionid",
            "巡检编号",
        )
    if obj.get("optype") == "inspectionresult.inspectionid_bar_v1":
        res = get_bar_v1(
            "select inspectionid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectionid",
            "巡检编号",
        )
    if obj.get("optype") == "inspectionresult.inspectiontime_line":
        res = get_line(
            "select inspectiontime x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectiontime order by x",
            "巡检时间",
        )
    # inspectionresult(巡检结果表)->robotid(机器人编号)

    if obj.get("optype") == "inspectionresult.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by robotid order by x desc",
            "机器人编号",
        )
    if obj.get("optype") == "inspectionresult.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by robotid",
            "机器人编号",
        )
    if obj.get("optype") == "inspectionresult.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by robotid",
            "机器人编号",
        )
    if obj.get("optype") == "inspectionresult.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by robotid",
            "机器人编号",
        )
    if obj.get("optype") == "inspectionresult.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by robotid",
            "机器人编号",
        )
    if obj.get("optype") == "inspectionresult.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by robotid",
            "机器人编号",
        )
    # inspectionresult(巡检结果表)->safetystatus(安全状态)

    if obj.get("optype") == "inspectionresult.safetystatus_pie":
        res = get_pie(
            "select safetystatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by safetystatus order by x desc",
            "安全状态",
        )
    if obj.get("optype") == "inspectionresult.safetystatus_pie_v1":
        res = get_pie_v1(
            "select safetystatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by safetystatus",
            "安全状态",
        )
    if obj.get("optype") == "inspectionresult.safetystatus_pie_v2":
        res = get_pie_v2(
            "select safetystatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by safetystatus",
            "安全状态",
        )
    if obj.get("optype") == "inspectionresult.safetystatus_line":
        res = get_line(
            "select safetystatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by safetystatus",
            "安全状态",
        )
    if obj.get("optype") == "inspectionresult.safetystatus_bar":
        res = get_bar(
            "select safetystatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by safetystatus",
            "安全状态",
        )
    if obj.get("optype") == "inspectionresult.safetystatus_bar_v1":
        res = get_bar_v1(
            "select safetystatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by safetystatus",
            "安全状态",
        )
    if obj.get("optype") == "inspectionresult.faultdescription_wordcloud":
        textlist = get_data(
            "SELECT faultdescription result FROM vm780_bb1ff2b101947be5.inspectionresult;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # inspectionresult(巡检结果表)->repairstatus(维修状态)

    if obj.get("optype") == "inspectionresult.repairstatus_pie":
        res = get_pie(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairstatus order by x desc",
            "维修状态",
        )
    if obj.get("optype") == "inspectionresult.repairstatus_pie_v1":
        res = get_pie_v1(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "inspectionresult.repairstatus_pie_v2":
        res = get_pie_v2(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "inspectionresult.repairstatus_line":
        res = get_line(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "inspectionresult.repairstatus_bar":
        res = get_bar(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairstatus",
            "维修状态",
        )
    if obj.get("optype") == "inspectionresult.repairstatus_bar_v1":
        res = get_bar_v1(
            "select repairstatus x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairstatus",
            "维修状态",
        )
    # inspectionresult(巡检结果表)->inspectkwkwor(巡检员)

    if obj.get("optype") == "inspectionresult.inspectkwkwor_pie":
        res = get_pie(
            "select inspectkwkwor x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectkwkwor order by x desc",
            "巡检员",
        )
    if obj.get("optype") == "inspectionresult.inspectkwkwor_pie_v1":
        res = get_pie_v1(
            "select inspectkwkwor x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectkwkwor",
            "巡检员",
        )
    if obj.get("optype") == "inspectionresult.inspectkwkwor_pie_v2":
        res = get_pie_v2(
            "select inspectkwkwor x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectkwkwor",
            "巡检员",
        )
    if obj.get("optype") == "inspectionresult.inspectkwkwor_line":
        res = get_line(
            "select inspectkwkwor x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectkwkwor",
            "巡检员",
        )
    if obj.get("optype") == "inspectionresult.inspectkwkwor_bar":
        res = get_bar(
            "select inspectkwkwor x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectkwkwor",
            "巡检员",
        )
    if obj.get("optype") == "inspectionresult.inspectkwkwor_bar_v1":
        res = get_bar_v1(
            "select inspectkwkwor x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by inspectkwkwor",
            "巡检员",
        )
    # inspectionresult(巡检结果表)->repairer(维修人员)

    if obj.get("optype") == "inspectionresult.repairer_pie":
        res = get_pie(
            "select repairer x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairer order by x desc",
            "维修人员",
        )
    if obj.get("optype") == "inspectionresult.repairer_pie_v1":
        res = get_pie_v1(
            "select repairer x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairer",
            "维修人员",
        )
    if obj.get("optype") == "inspectionresult.repairer_pie_v2":
        res = get_pie_v2(
            "select repairer x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairer",
            "维修人员",
        )
    if obj.get("optype") == "inspectionresult.repairer_line":
        res = get_line(
            "select repairer x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairer",
            "维修人员",
        )
    if obj.get("optype") == "inspectionresult.repairer_bar":
        res = get_bar(
            "select repairer x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairer",
            "维修人员",
        )
    if obj.get("optype") == "inspectionresult.repairer_bar_v1":
        res = get_bar_v1(
            "select repairer x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairer",
            "维修人员",
        )
    if obj.get("optype") == "inspectionresult.repairtime_line":
        res = get_line(
            "select repairtime x,count(*) y from vm780_bb1ff2b101947be5.inspectionresult group by repairtime order by x",
            "维修时间",
        )
    # robotmakwkwintenancecycle(机器人维护周期表)->robotid(机器人ID)

    if obj.get("optype") == "robotmakwkwintenancecycle.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by robotid",
            "机器人ID",
        )
    # robotmakwkwintenancecycle(机器人维护周期表)->makwkwintenancecycle(维护周期天数)

    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancecycle_pie":
        res = get_pie(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancecycle order by x desc",
            "维护周期天数",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancecycle_pie_v1":
        res = get_pie_v1(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancecycle",
            "维护周期天数",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancecycle_pie_v2":
        res = get_pie_v2(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancecycle",
            "维护周期天数",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancecycle_line":
        res = get_line(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancecycle",
            "维护周期天数",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancecycle_bar":
        res = get_bar(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancecycle",
            "维护周期天数",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancecycle_bar_v1":
        res = get_bar_v1(
            "select makwkwintenancecycle x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancecycle",
            "维护周期天数",
        )
    if (
        obj.get("optype")
        == "robotmakwkwintenancecycle.lkwkwastmakwkwintenancedate_line"
    ):
        res = get_line(
            "select lkwkwastmakwkwintenancedate x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by lkwkwastmakwkwintenancedate order by x",
            "上次维护日期",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.nextmakwkwintenancedate_line":
        res = get_line(
            "select nextmakwkwintenancedate x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by nextmakwkwintenancedate order by x",
            "下次维护日期",
        )
    # robotmakwkwintenancecycle(机器人维护周期表)->makwkwintenancestatus(维护状态如待维护、维护中、已完成)

    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancestatus_pie":
        res = get_pie(
            "select makwkwintenancestatus x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancestatus order by x desc",
            "维护状态如待维护、维护中、已完成",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancestatus_pie_v1":
        res = get_pie_v1(
            "select makwkwintenancestatus x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancestatus",
            "维护状态如待维护、维护中、已完成",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancestatus_pie_v2":
        res = get_pie_v2(
            "select makwkwintenancestatus x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancestatus",
            "维护状态如待维护、维护中、已完成",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancestatus_line":
        res = get_line(
            "select makwkwintenancestatus x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancestatus",
            "维护状态如待维护、维护中、已完成",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancestatus_bar":
        res = get_bar(
            "select makwkwintenancestatus x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancestatus",
            "维护状态如待维护、维护中、已完成",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancestatus_bar_v1":
        res = get_bar_v1(
            "select makwkwintenancestatus x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancestatus",
            "维护状态如待维护、维护中、已完成",
        )
    # robotmakwkwintenancecycle(机器人维护周期表)->makwkwintenancetype(维护类型如常规检查、深度保养、故障修复)

    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancetype_pie":
        res = get_pie(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancetype order by x desc",
            "维护类型如常规检查、深度保养、故障修复",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancetype_pie_v1":
        res = get_pie_v1(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancetype",
            "维护类型如常规检查、深度保养、故障修复",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancetype_pie_v2":
        res = get_pie_v2(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancetype",
            "维护类型如常规检查、深度保养、故障修复",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancetype_line":
        res = get_line(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancetype",
            "维护类型如常规检查、深度保养、故障修复",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancetype_bar":
        res = get_bar(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancetype",
            "维护类型如常规检查、深度保养、故障修复",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancetype_bar_v1":
        res = get_bar_v1(
            "select makwkwintenancetype x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancetype",
            "维护类型如常规检查、深度保养、故障修复",
        )
    # robotmakwkwintenancecycle(机器人维护周期表)->makwkwintenancenotes(维护备注)

    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancenotes_pie":
        res = get_pie(
            "select makwkwintenancenotes x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancenotes order by x desc",
            "维护备注",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancenotes_pie_v1":
        res = get_pie_v1(
            "select makwkwintenancenotes x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancenotes",
            "维护备注",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancenotes_pie_v2":
        res = get_pie_v2(
            "select makwkwintenancenotes x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancenotes",
            "维护备注",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancenotes_line":
        res = get_line(
            "select makwkwintenancenotes x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancenotes",
            "维护备注",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancenotes_bar":
        res = get_bar(
            "select makwkwintenancenotes x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancenotes",
            "维护备注",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.makwkwintenancenotes_bar_v1":
        res = get_bar_v1(
            "select makwkwintenancenotes x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by makwkwintenancenotes",
            "维护备注",
        )
    # robotmakwkwintenancecycle(机器人维护周期表)->createdby(创建人)

    if obj.get("optype") == "robotmakwkwintenancecycle.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by createdby order by x desc",
            "创建人",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by createdby",
            "创建人",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by createdby",
            "创建人",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by createdby",
            "创建人",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by createdby",
            "创建人",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by createdby",
            "创建人",
        )
    if obj.get("optype") == "robotmakwkwintenancecycle.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm780_bb1ff2b101947be5.robotmakwkwintenancecycle group by createdat order by x",
            "创建时间",
        )
    # productionlkwkwinedowntimereckwkword(生产线停机记录表)->productionlkwkwineid(生产线ID)

    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.productionlkwkwineid_pie"
    ):
        res = get_pie(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by productionlkwkwineid order by x desc",
            "生产线ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.productionlkwkwineid_pie_v1"
    ):
        res = get_pie_v1(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by productionlkwkwineid",
            "生产线ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.productionlkwkwineid_pie_v2"
    ):
        res = get_pie_v2(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by productionlkwkwineid",
            "生产线ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.productionlkwkwineid_line"
    ):
        res = get_line(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by productionlkwkwineid",
            "生产线ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.productionlkwkwineid_bar"
    ):
        res = get_bar(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by productionlkwkwineid",
            "生产线ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.productionlkwkwineid_bar_v1"
    ):
        res = get_bar_v1(
            "select productionlkwkwineid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by productionlkwkwineid",
            "生产线ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimestarttime_line"
    ):
        res = get_line(
            "select downtimestarttime x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimestarttime order by x",
            "停机开始时间",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.downtimeendtime_line":
        res = get_line(
            "select downtimeendtime x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimeendtime order by x",
            "停机结束时间",
        )
    # productionlkwkwinedowntimereckwkword(生产线停机记录表)->downtimerekwkwason(停机原因)

    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimerekwkwason_pie"
    ):
        res = get_pie(
            "select downtimerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimerekwkwason order by x desc",
            "停机原因",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimerekwkwason_pie_v1"
    ):
        res = get_pie_v1(
            "select downtimerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimerekwkwason",
            "停机原因",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimerekwkwason_pie_v2"
    ):
        res = get_pie_v2(
            "select downtimerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimerekwkwason",
            "停机原因",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimerekwkwason_line"
    ):
        res = get_line(
            "select downtimerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimerekwkwason",
            "停机原因",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimerekwkwason_bar"
    ):
        res = get_bar(
            "select downtimerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimerekwkwason",
            "停机原因",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimerekwkwason_bar_v1"
    ):
        res = get_bar_v1(
            "select downtimerekwkwason x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimerekwkwason",
            "停机原因",
        )
    # productionlkwkwinedowntimereckwkword(生产线停机记录表)->downtimeduration(停机时长分钟)

    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.downtimeduration_pie":
        res = get_pie(
            "select downtimeduration x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimeduration order by x desc",
            "停机时长分钟",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimeduration_pie_v1"
    ):
        res = get_pie_v1(
            "select downtimeduration x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimeduration",
            "停机时长分钟",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimeduration_pie_v2"
    ):
        res = get_pie_v2(
            "select downtimeduration x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimeduration",
            "停机时长分钟",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimeduration_line"
    ):
        res = get_line(
            "select downtimeduration x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimeduration",
            "停机时长分钟",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.downtimeduration_bar":
        res = get_bar(
            "select downtimeduration x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimeduration",
            "停机时长分钟",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.downtimeduration_bar_v1"
    ):
        res = get_bar_v1(
            "select downtimeduration x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by downtimeduration",
            "停机时长分钟",
        )
    # productionlkwkwinedowntimereckwkword(生产线停机记录表)->operatkwkworid(操作员ID)

    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.operatkwkworid_pie":
        res = get_pie(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by operatkwkworid order by x desc",
            "操作员ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.operatkwkworid_pie_v1"
    ):
        res = get_pie_v1(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by operatkwkworid",
            "操作员ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.operatkwkworid_pie_v2"
    ):
        res = get_pie_v2(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by operatkwkworid",
            "操作员ID",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.operatkwkworid_line":
        res = get_line(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by operatkwkworid",
            "操作员ID",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.operatkwkworid_bar":
        res = get_bar(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by operatkwkworid",
            "操作员ID",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.operatkwkworid_bar_v1"
    ):
        res = get_bar_v1(
            "select operatkwkworid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by operatkwkworid",
            "操作员ID",
        )
    # productionlkwkwinedowntimereckwkword(生产线停机记录表)->repairmanid(维修员ID)

    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.repairmanid_pie":
        res = get_pie(
            "select repairmanid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by repairmanid order by x desc",
            "维修员ID",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.repairmanid_pie_v1":
        res = get_pie_v1(
            "select repairmanid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by repairmanid",
            "维修员ID",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.repairmanid_pie_v2":
        res = get_pie_v2(
            "select repairmanid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by repairmanid",
            "维修员ID",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.repairmanid_line":
        res = get_line(
            "select repairmanid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by repairmanid",
            "维修员ID",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.repairmanid_bar":
        res = get_bar(
            "select repairmanid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by repairmanid",
            "维修员ID",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.repairmanid_bar_v1":
        res = get_bar_v1(
            "select repairmanid x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by repairmanid",
            "维修员ID",
        )
    # productionlkwkwinedowntimereckwkword(生产线停机记录表)->kwkwisresolved(是否已解决0未解决1已解决)

    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.kwkwisresolved_pie":
        res = get_pie(
            "select kwkwisresolved x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by kwkwisresolved order by x desc",
            "是否已解决0未解决1已解决",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.kwkwisresolved_pie_v1"
    ):
        res = get_pie_v1(
            "select kwkwisresolved x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by kwkwisresolved",
            "是否已解决0未解决1已解决",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.kwkwisresolved_pie_v2"
    ):
        res = get_pie_v2(
            "select kwkwisresolved x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by kwkwisresolved",
            "是否已解决0未解决1已解决",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.kwkwisresolved_line":
        res = get_line(
            "select kwkwisresolved x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by kwkwisresolved",
            "是否已解决0未解决1已解决",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.kwkwisresolved_bar":
        res = get_bar(
            "select kwkwisresolved x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by kwkwisresolved",
            "是否已解决0未解决1已解决",
        )
    if (
        obj.get("optype")
        == "productionlkwkwinedowntimereckwkword.kwkwisresolved_bar_v1"
    ):
        res = get_bar_v1(
            "select kwkwisresolved x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by kwkwisresolved",
            "是否已解决0未解决1已解决",
        )
    # productionlkwkwinedowntimereckwkword(生产线停机记录表)->remark(备注)

    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.remark_pie":
        res = get_pie(
            "select remark x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by remark order by x desc",
            "备注",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.remark_pie_v1":
        res = get_pie_v1(
            "select remark x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by remark",
            "备注",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.remark_pie_v2":
        res = get_pie_v2(
            "select remark x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by remark",
            "备注",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.remark_line":
        res = get_line(
            "select remark x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by remark",
            "备注",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.remark_bar":
        res = get_bar(
            "select remark x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by remark",
            "备注",
        )
    if obj.get("optype") == "productionlkwkwinedowntimereckwkword.remark_bar_v1":
        res = get_bar_v1(
            "select remark x,count(*) y from vm780_bb1ff2b101947be5.productionlkwkwinedowntimereckwkword group by remark",
            "备注",
        )
    # robotpermkwkwissionassignment(机器人权限分配表)->robotid(机器人ID)

    if obj.get("optype") == "robotpermkwkwissionassignment.robotid_pie":
        res = get_pie(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by robotid order by x desc",
            "机器人ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.robotid_pie_v1":
        res = get_pie_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.robotid_pie_v2":
        res = get_pie_v2(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.robotid_line":
        res = get_line(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.robotid_bar":
        res = get_bar(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by robotid",
            "机器人ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.robotid_bar_v1":
        res = get_bar_v1(
            "select robotid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by robotid",
            "机器人ID",
        )
    # robotpermkwkwissionassignment(机器人权限分配表)->permkwkwissionid(权限ID)

    if obj.get("optype") == "robotpermkwkwissionassignment.permkwkwissionid_pie":
        res = get_pie(
            "select permkwkwissionid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by permkwkwissionid order by x desc",
            "权限ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.permkwkwissionid_pie_v1":
        res = get_pie_v1(
            "select permkwkwissionid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.permkwkwissionid_pie_v2":
        res = get_pie_v2(
            "select permkwkwissionid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.permkwkwissionid_line":
        res = get_line(
            "select permkwkwissionid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.permkwkwissionid_bar":
        res = get_bar(
            "select permkwkwissionid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.permkwkwissionid_bar_v1":
        res = get_bar_v1(
            "select permkwkwissionid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by permkwkwissionid",
            "权限ID",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.assignmentdate_line":
        res = get_line(
            "select assignmentdate x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by assignmentdate order by x",
            "分配日期",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.expirydate_line":
        res = get_line(
            "select expirydate x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by expirydate order by x",
            "过期日期",
        )
    # robotpermkwkwissionassignment(机器人权限分配表)->isactive(是否激活)

    if obj.get("optype") == "robotpermkwkwissionassignment.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by isactive",
            "是否激活",
        )
    # robotpermkwkwissionassignment(机器人权限分配表)->createdby(创建者)

    if obj.get("optype") == "robotpermkwkwissionassignment.createdby_pie":
        res = get_pie(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by createdby order by x desc",
            "创建者",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.createdby_pie_v1":
        res = get_pie_v1(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by createdby",
            "创建者",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.createdby_pie_v2":
        res = get_pie_v2(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by createdby",
            "创建者",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.createdby_line":
        res = get_line(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by createdby",
            "创建者",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.createdby_bar":
        res = get_bar(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by createdby",
            "创建者",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.createdby_bar_v1":
        res = get_bar_v1(
            "select createdby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by createdby",
            "创建者",
        )
    # robotpermkwkwissionassignment(机器人权限分配表)->lkwkwastmodkwkwifiedby(最后修改者)

    if obj.get("optype") == "robotpermkwkwissionassignment.lkwkwastmodkwkwifiedby_pie":
        res = get_pie(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by lkwkwastmodkwkwifiedby order by x desc",
            "最后修改者",
        )
    if (
        obj.get("optype")
        == "robotpermkwkwissionassignment.lkwkwastmodkwkwifiedby_pie_v1"
    ):
        res = get_pie_v1(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by lkwkwastmodkwkwifiedby",
            "最后修改者",
        )
    if (
        obj.get("optype")
        == "robotpermkwkwissionassignment.lkwkwastmodkwkwifiedby_pie_v2"
    ):
        res = get_pie_v2(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by lkwkwastmodkwkwifiedby",
            "最后修改者",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.lkwkwastmodkwkwifiedby_line":
        res = get_line(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by lkwkwastmodkwkwifiedby",
            "最后修改者",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.lkwkwastmodkwkwifiedby_bar":
        res = get_bar(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by lkwkwastmodkwkwifiedby",
            "最后修改者",
        )
    if (
        obj.get("optype")
        == "robotpermkwkwissionassignment.lkwkwastmodkwkwifiedby_bar_v1"
    ):
        res = get_bar_v1(
            "select lkwkwastmodkwkwifiedby x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by lkwkwastmodkwkwifiedby",
            "最后修改者",
        )
    # robotpermkwkwissionassignment(机器人权限分配表)->departmentid(部门ID关联字段)

    if obj.get("optype") == "robotpermkwkwissionassignment.departmentid_pie":
        res = get_pie(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by departmentid order by x desc",
            "部门ID关联字段",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.departmentid_pie_v1":
        res = get_pie_v1(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by departmentid",
            "部门ID关联字段",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.departmentid_pie_v2":
        res = get_pie_v2(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by departmentid",
            "部门ID关联字段",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.departmentid_line":
        res = get_line(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by departmentid",
            "部门ID关联字段",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.departmentid_bar":
        res = get_bar(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by departmentid",
            "部门ID关联字段",
        )
    if obj.get("optype") == "robotpermkwkwissionassignment.departmentid_bar_v1":
        res = get_bar_v1(
            "select departmentid x,count(*) y from vm780_bb1ff2b101947be5.robotpermkwkwissionassignment group by departmentid",
            "部门ID关联字段",
        )
    # supermanager(系统管理员)->username(管理员姓名)

    if obj.get("optype") == "supermanager.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.supermanager group by username order by x desc",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_line":
        res = get_line(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm780_bb1ff2b101947be5.supermanager group by username",
            "管理员姓名",
        )
    assert "title" in res
    return JsonResponse(res)


# __config_visual_views


def bi_level_2(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi_level_2.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    return JsonResponse(res)


def bi_new(request):
    if request.method == "GET":
        return HttpResponse(loader.get_template("config_visual/bi_new.html").render())
    obj = mydict(request.POST)
    res = dict()

    # __mark_appcenter_views_all__level_new_bi

    return JsonResponse(res)


def view_robotinfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprobotinfo.html", locals())


def view_productionlkwkwineinfo(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpproductionlkwkwineinfo.html", locals()
        )


def view_safetymonitkwkworlog(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpsafetymonitkwkworlog.html", locals()
        )


def view_alarmreckwkword(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpalarmreckwkword.html", locals())


def view_robotlocation(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprobotlocation.html", locals())


def view_robotstatus(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprobotstatus.html", locals())


def view_robottkwkwask(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprobottkwkwask.html", locals())


def view_productionlkwkwineconfig(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpproductionlkwkwineconfig.html", locals()
        )


def view_permkwkwissionmanagement(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tppermkwkwissionmanagement.html", locals()
        )


def view_userinfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpuserinfo.html", locals())


def view_roleinfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tproleinfo.html", locals())


def view_userrolerelation(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpuserrolerelation.html", locals())


def view_robotfault(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprobotfault.html", locals())


def view_makwkwintenancereckwkword(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpmakwkwintenancereckwkword.html", locals()
        )


def view_robotmokwkwdel(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprobotmokwkwdel.html", locals())


def view_senskwkworinfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsenskwkworinfo.html", locals())


def view_senskwkwordata(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsenskwkwordata.html", locals())


def view_camerainfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpcamerainfo.html", locals())


def view_videoreckwkword(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideoreckwkword.html", locals())


def view_robotoperationlog(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprobotoperationlog.html", locals())


def view_productionlkwkwineefficiency(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpproductionlkwkwineefficiency.html", locals()
        )


def view_robotfirmwareupdate(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprobotfirmwareupdate.html", locals())


def view_robotfirmwareversion(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tprobotfirmwareversion.html", locals()
        )


def view_productionlkwkwinesafetyrule(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpproductionlkwkwinesafetyrule.html", locals()
        )


def view_robotsafetyconfig(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprobotsafetyconfig.html", locals())


def view_robotinspectionplan(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tprobotinspectionplan.html", locals())


def view_inspectionresult(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpinspectionresult.html", locals())


def view_robotmakwkwintenancecycle(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tprobotmakwkwintenancecycle.html", locals()
        )


def view_productionlkwkwinedowntimereckwkword(request):
    if request.method == "GET":
        return render(
            request,
            "config_visual/bi__tpproductionlkwkwinedowntimereckwkword.html",
            locals(),
        )


def view_robotpermkwkwissionassignment(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tprobotpermkwkwissionassignment.html", locals()
        )


def view_supermanager(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsupermanager.html", locals())

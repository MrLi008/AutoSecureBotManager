from django.db import models
from appcenter.models import *
from config_visual.models import *
from sys_user.models import *
from sys_user.func import *

all_tables = dict()
gl = dict()

# Create your models here.

all_tables = {
    "robotinfo": mymeta(mc_robotinfo),
    "productionlkwkwineinfo": mymeta(mc_productionlkwkwineinfo),
    "safetymonitkwkworlog": mymeta(mc_safetymonitkwkworlog),
    "alarmreckwkword": mymeta(mc_alarmreckwkword),
    "robotlocation": mymeta(mc_robotlocation),
    "robotstatus": mymeta(mc_robotstatus),
    "robottkwkwask": mymeta(mc_robottkwkwask),
    "productionlkwkwineconfig": mymeta(mc_productionlkwkwineconfig),
    "permkwkwissionmanagement": mymeta(mc_permkwkwissionmanagement),
    "userinfo": mymeta(mc_userinfo),
    "roleinfo": mymeta(mc_roleinfo),
    "userrolerelation": mymeta(mc_userrolerelation),
    "robotfault": mymeta(mc_robotfault),
    "makwkwintenancereckwkword": mymeta(mc_makwkwintenancereckwkword),
    "robotmokwkwdel": mymeta(mc_robotmokwkwdel),
    "senskwkworinfo": mymeta(mc_senskwkworinfo),
    "senskwkwordata": mymeta(mc_senskwkwordata),
    "camerainfo": mymeta(mc_camerainfo),
    "videoreckwkword": mymeta(mc_videoreckwkword),
    "robotoperationlog": mymeta(mc_robotoperationlog),
    "productionlkwkwineefficiency": mymeta(mc_productionlkwkwineefficiency),
    "robotfirmwareupdate": mymeta(mc_robotfirmwareupdate),
    "robotfirmwareversion": mymeta(mc_robotfirmwareversion),
    "productionlkwkwinesafetyrule": mymeta(mc_productionlkwkwinesafetyrule),
    "robotsafetyconfig": mymeta(mc_robotsafetyconfig),
    "robotinspectionplan": mymeta(mc_robotinspectionplan),
    "inspectionresult": mymeta(mc_inspectionresult),
    "robotmakwkwintenancecycle": mymeta(mc_robotmakwkwintenancecycle),
    "productionlkwkwinedowntimereckwkword": mymeta(
        mc_productionlkwkwinedowntimereckwkword
    ),
    "robotpermkwkwissionassignment": mymeta(mc_robotpermkwkwissionassignment),
    "supermanager": mymeta(mc_supermanager),
}

# 所有用户表

all_tables_user = {
    "userinfo": mymeta(mc_userinfo),
    "supermanager": mymeta(mc_supermanager),
}
gl = {
    "robotinfo": mc_robotinfo,
    "productionlkwkwineinfo": mc_productionlkwkwineinfo,
    "safetymonitkwkworlog": mc_safetymonitkwkworlog,
    "alarmreckwkword": mc_alarmreckwkword,
    "robotlocation": mc_robotlocation,
    "robotstatus": mc_robotstatus,
    "robottkwkwask": mc_robottkwkwask,
    "productionlkwkwineconfig": mc_productionlkwkwineconfig,
    "permkwkwissionmanagement": mc_permkwkwissionmanagement,
    "userinfo": mc_userinfo,
    "roleinfo": mc_roleinfo,
    "userrolerelation": mc_userrolerelation,
    "robotfault": mc_robotfault,
    "makwkwintenancereckwkword": mc_makwkwintenancereckwkword,
    "robotmokwkwdel": mc_robotmokwkwdel,
    "senskwkworinfo": mc_senskwkworinfo,
    "senskwkwordata": mc_senskwkwordata,
    "camerainfo": mc_camerainfo,
    "videoreckwkword": mc_videoreckwkword,
    "robotoperationlog": mc_robotoperationlog,
    "productionlkwkwineefficiency": mc_productionlkwkwineefficiency,
    "robotfirmwareupdate": mc_robotfirmwareupdate,
    "robotfirmwareversion": mc_robotfirmwareversion,
    "productionlkwkwinesafetyrule": mc_productionlkwkwinesafetyrule,
    "robotsafetyconfig": mc_robotsafetyconfig,
    "robotinspectionplan": mc_robotinspectionplan,
    "inspectionresult": mc_inspectionresult,
    "robotmakwkwintenancecycle": mc_robotmakwkwintenancecycle,
    "productionlkwkwinedowntimereckwkword": mc_productionlkwkwinedowntimereckwkword,
    "robotpermkwkwissionassignment": mc_robotpermkwkwissionassignment,
    "supermanager": mc_supermanager,
}

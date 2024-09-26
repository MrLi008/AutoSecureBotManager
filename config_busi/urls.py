from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_busi_view_index"),
    # 如果用到预测算法,图像识别等单页面展示效果的算法去掉下方注释
    path("auto_detect", views.auto_detect, name="config_busi_view_auto_detect"),
    path("robotinfo", views.view_robotinfo, name="config_busi_view_robotinfo"),
    path(
        "productionlkwkwineinfo",
        views.view_productionlkwkwineinfo,
        name="config_busi_view_productionlkwkwineinfo",
    ),
    path(
        "safetymonitkwkworlog",
        views.view_safetymonitkwkworlog,
        name="config_busi_view_safetymonitkwkworlog",
    ),
    path(
        "alarmreckwkword",
        views.view_alarmreckwkword,
        name="config_busi_view_alarmreckwkword",
    ),
    path(
        "robotlocation", views.view_robotlocation, name="config_busi_view_robotlocation"
    ),
    path("robotstatus", views.view_robotstatus, name="config_busi_view_robotstatus"),
    path(
        "robottkwkwask", views.view_robottkwkwask, name="config_busi_view_robottkwkwask"
    ),
    path(
        "productionlkwkwineconfig",
        views.view_productionlkwkwineconfig,
        name="config_busi_view_productionlkwkwineconfig",
    ),
    path(
        "permkwkwissionmanagement",
        views.view_permkwkwissionmanagement,
        name="config_busi_view_permkwkwissionmanagement",
    ),
    path("userinfo", views.view_userinfo, name="config_busi_view_userinfo"),
    path("roleinfo", views.view_roleinfo, name="config_busi_view_roleinfo"),
    path(
        "userrolerelation",
        views.view_userrolerelation,
        name="config_busi_view_userrolerelation",
    ),
    path("robotfault", views.view_robotfault, name="config_busi_view_robotfault"),
    path(
        "makwkwintenancereckwkword",
        views.view_makwkwintenancereckwkword,
        name="config_busi_view_makwkwintenancereckwkword",
    ),
    path(
        "robotmokwkwdel",
        views.view_robotmokwkwdel,
        name="config_busi_view_robotmokwkwdel",
    ),
    path(
        "senskwkworinfo",
        views.view_senskwkworinfo,
        name="config_busi_view_senskwkworinfo",
    ),
    path(
        "senskwkwordata",
        views.view_senskwkwordata,
        name="config_busi_view_senskwkwordata",
    ),
    path("camerainfo", views.view_camerainfo, name="config_busi_view_camerainfo"),
    path(
        "videoreckwkword",
        views.view_videoreckwkword,
        name="config_busi_view_videoreckwkword",
    ),
    path(
        "robotoperationlog",
        views.view_robotoperationlog,
        name="config_busi_view_robotoperationlog",
    ),
    path(
        "productionlkwkwineefficiency",
        views.view_productionlkwkwineefficiency,
        name="config_busi_view_productionlkwkwineefficiency",
    ),
    path(
        "robotfirmwareupdate",
        views.view_robotfirmwareupdate,
        name="config_busi_view_robotfirmwareupdate",
    ),
    path(
        "robotfirmwareversion",
        views.view_robotfirmwareversion,
        name="config_busi_view_robotfirmwareversion",
    ),
    path(
        "productionlkwkwinesafetyrule",
        views.view_productionlkwkwinesafetyrule,
        name="config_busi_view_productionlkwkwinesafetyrule",
    ),
    path(
        "robotsafetyconfig",
        views.view_robotsafetyconfig,
        name="config_busi_view_robotsafetyconfig",
    ),
    path(
        "robotinspectionplan",
        views.view_robotinspectionplan,
        name="config_busi_view_robotinspectionplan",
    ),
    path(
        "inspectionresult",
        views.view_inspectionresult,
        name="config_busi_view_inspectionresult",
    ),
    path(
        "robotmakwkwintenancecycle",
        views.view_robotmakwkwintenancecycle,
        name="config_busi_view_robotmakwkwintenancecycle",
    ),
    path(
        "productionlkwkwinedowntimereckwkword",
        views.view_productionlkwkwinedowntimereckwkword,
        name="config_busi_view_productionlkwkwinedowntimereckwkword",
    ),
    path(
        "robotpermkwkwissionassignment",
        views.view_robotpermkwkwissionassignment,
        name="config_busi_view_robotpermkwkwissionassignment",
    ),
    path("supermanager", views.view_supermanager, name="config_busi_view_supermanager"),
]

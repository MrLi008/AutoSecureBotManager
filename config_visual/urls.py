from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_visual_view_index"),
    path("bi", views.bi, name="config_visual_view_bi"),
    path("bi_level_2", views.bi_level_2, name="config_visual_view_bi_level_2"),
    path("bi_new", views.bi_new, name="config_visual_view_bi_new"),
    path("bi_v1", views.bi, name="config_visual_view_bi_v1"),
    path("bi_v2", views.bi, name="config_visual_view_bi_v2"),
    path("bi_v3", views.bi, name="config_visual_view_bi_v3"),
    path("bi_v4", views.bi, name="config_visual_view_bi_v4"),
    path("bi_v5", views.bi, name="config_visual_view_bi_v5"),
    #
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotinfo",
        views.view_robotinfo,
        name="bi_tprobotinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpproductionlkwkwineinfo",
        views.view_productionlkwkwineinfo,
        name="bi_tpproductionlkwkwineinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsafetymonitkwkworlog",
        views.view_safetymonitkwkworlog,
        name="bi_tpsafetymonitkwkworlog",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpalarmreckwkword",
        views.view_alarmreckwkword,
        name="bi_tpalarmreckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotlocation",
        views.view_robotlocation,
        name="bi_tprobotlocation",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotstatus",
        views.view_robotstatus,
        name="bi_tprobotstatus",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobottkwkwask",
        views.view_robottkwkwask,
        name="bi_tprobottkwkwask",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpproductionlkwkwineconfig",
        views.view_productionlkwkwineconfig,
        name="bi_tpproductionlkwkwineconfig",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tppermkwkwissionmanagement",
        views.view_permkwkwissionmanagement,
        name="bi_tppermkwkwissionmanagement",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpuserinfo",
        views.view_userinfo,
        name="bi_tpuserinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tproleinfo",
        views.view_roleinfo,
        name="bi_tproleinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpuserrolerelation",
        views.view_userrolerelation,
        name="bi_tpuserrolerelation",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotfault",
        views.view_robotfault,
        name="bi_tprobotfault",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmakwkwintenancereckwkword",
        views.view_makwkwintenancereckwkword,
        name="bi_tpmakwkwintenancereckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotmokwkwdel",
        views.view_robotmokwkwdel,
        name="bi_tprobotmokwkwdel",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsenskwkworinfo",
        views.view_senskwkworinfo,
        name="bi_tpsenskwkworinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsenskwkwordata",
        views.view_senskwkwordata,
        name="bi_tpsenskwkwordata",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpcamerainfo",
        views.view_camerainfo,
        name="bi_tpcamerainfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoreckwkword",
        views.view_videoreckwkword,
        name="bi_tpvideoreckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotoperationlog",
        views.view_robotoperationlog,
        name="bi_tprobotoperationlog",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpproductionlkwkwineefficiency",
        views.view_productionlkwkwineefficiency,
        name="bi_tpproductionlkwkwineefficiency",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotfirmwareupdate",
        views.view_robotfirmwareupdate,
        name="bi_tprobotfirmwareupdate",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotfirmwareversion",
        views.view_robotfirmwareversion,
        name="bi_tprobotfirmwareversion",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpproductionlkwkwinesafetyrule",
        views.view_productionlkwkwinesafetyrule,
        name="bi_tpproductionlkwkwinesafetyrule",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotsafetyconfig",
        views.view_robotsafetyconfig,
        name="bi_tprobotsafetyconfig",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotinspectionplan",
        views.view_robotinspectionplan,
        name="bi_tprobotinspectionplan",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpinspectionresult",
        views.view_inspectionresult,
        name="bi_tpinspectionresult",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotmakwkwintenancecycle",
        views.view_robotmakwkwintenancecycle,
        name="bi_tprobotmakwkwintenancecycle",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpproductionlkwkwinedowntimereckwkword",
        views.view_productionlkwkwinedowntimereckwkword,
        name="bi_tpproductionlkwkwinedowntimereckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tprobotpermkwkwissionassignment",
        views.view_robotpermkwkwissionassignment,
        name="bi_tprobotpermkwkwissionassignment",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsupermanager",
        views.view_supermanager,
        name="bi_tpsupermanager",
    ),
]

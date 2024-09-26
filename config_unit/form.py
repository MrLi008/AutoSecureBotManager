from django import forms
from captcha.fields import CaptchaField

from appcenter.form import *

all_tables_form = {
    "robotinfo": mc_robotinfo_form,
    "productionlkwkwineinfo": mc_productionlkwkwineinfo_form,
    "safetymonitkwkworlog": mc_safetymonitkwkworlog_form,
    "alarmreckwkword": mc_alarmreckwkword_form,
    "robotlocation": mc_robotlocation_form,
    "robotstatus": mc_robotstatus_form,
    "robottkwkwask": mc_robottkwkwask_form,
    "productionlkwkwineconfig": mc_productionlkwkwineconfig_form,
    "permkwkwissionmanagement": mc_permkwkwissionmanagement_form,
    "userinfo": mc_userinfo_form,
    "roleinfo": mc_roleinfo_form,
    "userrolerelation": mc_userrolerelation_form,
    "robotfault": mc_robotfault_form,
    "makwkwintenancereckwkword": mc_makwkwintenancereckwkword_form,
    "robotmokwkwdel": mc_robotmokwkwdel_form,
    "senskwkworinfo": mc_senskwkworinfo_form,
    "senskwkwordata": mc_senskwkwordata_form,
    "camerainfo": mc_camerainfo_form,
    "videoreckwkword": mc_videoreckwkword_form,
    "robotoperationlog": mc_robotoperationlog_form,
    "productionlkwkwineefficiency": mc_productionlkwkwineefficiency_form,
    "robotfirmwareupdate": mc_robotfirmwareupdate_form,
    "robotfirmwareversion": mc_robotfirmwareversion_form,
    "productionlkwkwinesafetyrule": mc_productionlkwkwinesafetyrule_form,
    "robotsafetyconfig": mc_robotsafetyconfig_form,
    "robotinspectionplan": mc_robotinspectionplan_form,
    "inspectionresult": mc_inspectionresult_form,
    "robotmakwkwintenancecycle": mc_robotmakwkwintenancecycle_form,
    "productionlkwkwinedowntimereckwkword": mc_productionlkwkwinedowntimereckwkword_form,
    "robotpermkwkwissionassignment": mc_robotpermkwkwissionassignment_form,
    "supermanager": mc_supermanager_form,
}

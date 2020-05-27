from django.utils.translation import ugettext as _
from xadmin.layout import Fieldset, Main, Side, Row

MbrLayout = \
    (
        Main(
            Fieldset(_('会员信息'),
                     Row('mbse_user'),
                     'mbse_status',
                     ),
            Fieldset(_('个人信息'),
                     Row('mbse_name','mbr_gender','mbr_birth'),
                     Row('mbr_political','mbr_folk','mbr_title'),
                     Row('mbr_id_num',),
                     Row('mbr_graduate','mbr_graduate_time'),
                     Row('mbr_training_ins','mbr_training_date'),
                     'mbr_job',
                     Row('mbr_loc','mbr_zip'),
                     Row('mbr_email','mbr_phone'),
                     Row('mbr_cert','mbr_cert_date','mbr_cert_code'),
                     'mbr_achievement',
                     'mbse_judge',
                     Row('mbse_code','mbse_exp'),
                     ),
        ),
        Side(
            Fieldset(_('会员照片'),
                     'mbr_avatar'
                     )
        )
    )

IncLayout = \
    (
        Main(
            Fieldset(_('企业信息'),
                     Row('mbse_user'),
                     'mbse_status',

                     ),
            Fieldset(_('企业信息'),
                     'mbse_name',
                     'inc_loc',
                     'inc_code',
                     ),
            Fieldset(_('联系方式'),
                     'inc_phone',
                     Row('inc_fax','inc_email'),
                     'inc_site',
                     ),
            Fieldset(_('其他信息'),
                     Row('inc_charge','inc_charge_code'),
                     Row('inc_corporate','inc_corp_phone'),
                     Row('inc_director','inc_director_phone'),
                     'inc_opinion',
                     'inc_info'
                     ),
            Fieldset(_('审批意见'),
                     'mbse_judge',
                     'mbse_code',
                     'mbse_exp',
                     )
        ),
    )
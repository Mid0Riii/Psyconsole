from django.utils.translation import ugettext as _
from xadmin.layout import Fieldset, Main, Side, Row

MbrLayout = \
    (
        Main(
            Fieldset(_('会员信息'),
                     Row('mbse_type','mbse_user'),
                     'mbse_status',
                     ),
            Fieldset(_('个人信息'),
                     Row('mbr_name','mbr_gender','mbr_birth'),
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
    )

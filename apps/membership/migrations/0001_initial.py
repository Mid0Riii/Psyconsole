# Generated by Django 2.2.5 on 2020-05-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MbrCommon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbse_status', models.CharField(choices=[('0', '已注册，未提交申请'), ('1', '申请审核中'), ('2', '申请驳回，请检查申请信息'), ('3', '审核通过，等待缴费'), ('4', '缴费校验中'), ('5', '缴费校验不通过，请重新确认'), ('6', '已成为正式会员')], default='0', max_length=128, verbose_name='状态')),
                ('mbse_judge', models.TextField(blank=True, null=True, verbose_name='协会审批意见')),
                ('mbse_code', models.CharField(blank=True, max_length=128, null=True, verbose_name='会员编号')),
                ('mbse_exp', models.DateField(blank=True, null=True, verbose_name='有效期')),
                ('mbse_name', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='姓名')),
                ('mbr_gender', models.CharField(blank=True, max_length=128, null=True, verbose_name='性别')),
                ('mbr_birth', models.CharField(blank=True, max_length=128, null=True, verbose_name='出生年月')),
                ('mbr_political', models.CharField(blank=True, max_length=128, null=True, verbose_name='政治面貌')),
                ('mbr_folk', models.CharField(blank=True, max_length=128, null=True, verbose_name='民族')),
                ('mbr_title', models.CharField(blank=True, max_length=128, null=True, verbose_name='技术职称')),
                ('mbr_id_num', models.CharField(blank=True, max_length=128, null=True, verbose_name='身份证号')),
                ('mbr_graduate', models.CharField(blank=True, max_length=128, null=True, verbose_name='毕业院校及专业')),
                ('mbr_graduate_time', models.CharField(blank=True, max_length=128, null=True, verbose_name='毕业时间')),
                ('mbr_training_ins', models.CharField(blank=True, max_length=128, null=True, verbose_name='资格证培训机构')),
                ('mbr_training_date', models.CharField(blank=True, max_length=128, null=True, verbose_name='培训时间')),
                ('mbr_job', models.CharField(blank=True, max_length=128, null=True, verbose_name='工作单位及职务')),
                ('mbr_loc', models.CharField(blank=True, max_length=128, null=True, verbose_name='通讯地址')),
                ('mbr_zip', models.CharField(blank=True, max_length=128, null=True, verbose_name='邮编')),
                ('mbr_email', models.CharField(blank=True, max_length=128, null=True, verbose_name='电子邮件')),
                ('mbr_phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='手机')),
                ('mbr_cert', models.CharField(blank=True, max_length=128, null=True, verbose_name='心理咨询师级别')),
                ('mbr_cert_date', models.CharField(blank=True, max_length=128, null=True, verbose_name='获证年份')),
                ('mbr_cert_code', models.CharField(blank=True, max_length=128, null=True, verbose_name='证书编号')),
                ('mbr_achievement', models.TextField(blank=True, null=True, verbose_name='近五年承担的科研课题；著作、学术论文')),
            ],
            options={
                'verbose_name': '成员',
                'verbose_name_plural': '成员',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MbrInc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbse_status', models.CharField(choices=[('0', '已注册，未提交申请'), ('1', '申请审核中'), ('2', '申请驳回，请检查申请信息'), ('3', '审核通过，等待缴费'), ('4', '缴费校验中'), ('5', '缴费校验不通过，请重新确认'), ('6', '已成为正式会员')], default='0', max_length=128, verbose_name='状态')),
                ('mbse_judge', models.TextField(blank=True, null=True, verbose_name='协会审批意见')),
                ('mbse_code', models.CharField(blank=True, max_length=128, null=True, verbose_name='会员编号')),
                ('mbse_exp', models.DateField(blank=True, null=True, verbose_name='有效期')),
                ('mbse_name', models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='姓名')),
                ('inc_loc', models.CharField(blank=True, max_length=128, null=True, verbose_name='所在地区及办公地址')),
                ('inc_code', models.CharField(blank=True, max_length=128, null=True, verbose_name='邮编')),
                ('inc_phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='电话')),
                ('inc_fax', models.CharField(blank=True, max_length=128, null=True, verbose_name='传真')),
                ('inc_email', models.CharField(blank=True, max_length=128, null=True, verbose_name='电子邮箱')),
                ('inc_site', models.CharField(blank=True, max_length=128, null=True, verbose_name='网址')),
                ('inc_charge', models.CharField(blank=True, max_length=128, null=True, verbose_name='主管机关')),
                ('inc_charge_code', models.CharField(blank=True, max_length=128, null=True, verbose_name='组织机构代码')),
                ('inc_corporate', models.CharField(blank=True, max_length=128, null=True, verbose_name='法人代表')),
                ('inc_corp_phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='法人代表联系方式')),
                ('inc_director', models.CharField(blank=True, max_length=128, null=True, verbose_name='推举理事')),
                ('inc_director_phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='理事手机')),
                ('inc_opinion', models.TextField(blank=True, null=True, verbose_name='审批理事单位负责人意见')),
                ('inc_info', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '理事单位会员',
                'verbose_name_plural': '理事单位会员',
            },
        ),
    ]

import unittest, logging, random,time
from test.test01 import ctcdbUtil

for i in range (100):
    print("开始批量新建账号......")
    account_name = "test%d@lanlingdai.net" % (i+1)

    add_sql = "INSERT INTO customer (type, mobile, password, email, full_name, gender, dob, nric_no, country_code, register_channel_code, register_channel_name, register_platform, invite_code, fullface_pic, contact_first_name, contact_first_relation, contact_first_phone, contact_second_name, contact_second_relation, contact_second_phone, google_secret, device_bind_status, blacklisted, locked, unlock_code, credit_score, credit_level, credited_at, created_at, updated_at) VALUES (300, '13800000000', '3e6c7d141e32189c917761138b026b74', '%s', NULL, NULL, NULL, NULL, NULL, '', '', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, '2018-04-03 10:46:45', '2018-05-16 09:57:11');" % account_name

    ctcdbUtil.execute(add_sql)
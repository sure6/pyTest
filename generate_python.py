#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : pyTest
# @File    : generate_python.py
# @Author  : lee sure
# @Descriptions :
# @Date    : 2023/5/24 16:01 
# @Software : PyCharm


with open('demo1.py','w') as f:
    for i in range(50):
        f.write("\ndef test_sign_in"+str(i)+"():\n" 
                "   response_test, status_code = reuqest_sparkling(url, headers, payload)\n"
                "   assert status_code == 200")



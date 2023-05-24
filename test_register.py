#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : python-test
# @File    : test_register.py
# @Author  : lee sure
# @Descriptions :
# @Date    : 2023/4/25 0:02 
# @Software : PyCharm

import pytest
from sparkling import reuqest_sparkling

url = "https://abbyshi622.wixsite.com/_api/iam/authentication/v1/register"
headers = {"Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,ko;q=0.5", "Connection": "keep-alive",
           "Content-Type": "application/json",
           "Cookie": "XSRF-TOKEN=1684561023|ziiDMrWFrAk4; hs=9046605; bSession=cb407643-0a56-42e8-85db-51d55c624bcd|3",
           "Host": "abbyshi622.wixsite.com", "Origin": "https://abbyshi622.wixsite.com",
           "Referer": "https://abbyshi622.wixsite.com/sparking-home/booking-calendar/oven-repairs?referral=service_list_widget",
           "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
           "accept": "application/json",
           "authorization": "7y_5Jf7wieyukFNHHToTGO7W0u6QVnlGtW0SJrwi2eg.eyJpbnN0YW5jZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4IiwiYXBwRGVmSWQiOiIyMmJlZjM0NS0zYzViLTRjMTgtYjc4Mi03NGQ0MDg1MTEyZmYiLCJtZXRhU2l0ZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4Iiwic2lnbkRhdGUiOiIyMDIzLTA1LTIwVDA1OjM4OjQyLjU1NVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6ImQyN2IwYThiLTc1MGQtNGI0Yy1iNWI0LWVmOTkyYmU1NzNiOCIsInNpdGVPd25lcklkIjoiODI2MmY1MDAtZDJmMi00MDMzLWE3YjUtNWVkMTVkZjJkMTI2In0",
           "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
           "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "x-wix-client-artifact-id": "thunderbolt",
           "x-wix-site-revision": "250"}
"""
null
@xxx.com
xx@xx.com
xxx.com 
相同邮箱不能
"""
payload1 = """
 {
    "identity": {
        "identifiers": [
            {
                "email": "arm7@qq.com"
            }
        ],
        "identityProfile": {
            "customFields": [],
            "phones": [],
            "emails": [
                "arm7@qq.com"
            ],
            "firstName": "arm7",
            "lastName": "lee",
            "privacyStatus": "PRIVATE"
        }
    },
    "inputs": {
        "password": "123456"
    },
    "captcha_tokens": []
}
    """

payload = """
    {"identity":{"identifiers": [{"email": "sure1235@qq.com"}],"identityProfile":{"customFields": [],"phones": [],"emails": ["sure1235@qq.com"],"firstName": "sure12","lastName": "aaa12","privacyStatus": "PRIVATE"}},
               "inputs": {"password": "123456"},"captcha_tokens": []}
    """


def test_register():
    response_test, status_code = reuqest_sparkling(url, headers, payload1)
    assert status_code == 200

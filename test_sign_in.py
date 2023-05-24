#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : python-test
# @File    : test_sign_in.py
# @Author  : lee sure
# @Descriptions :
# @Date    : 2023/4/25 0:16 
# @Software : PyCharm
import pytest

from sparkling import reuqest_sparkling

url = "https://abbyshi622.wixsite.com/_api/iam/authentication/v1/login"

headers = {
  'Host': 'abbyshi622.wixsite.com',
  'Connection': 'keep-alive',
  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'authorization': 'Ssf13fhzOrGcAVqCevfdBHo9ve_CHEIKp22qzcixAf4.eyJpbnN0YW5jZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4IiwiYXBwRGVmSWQiOiIyMmJlZjM0NS0zYzViLTRjMTgtYjc4Mi03NGQ0MDg1MTEyZmYiLCJtZXRhU2l0ZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4Iiwic2lnbkRhdGUiOiIyMDIzLTA1LTIxVDA4OjQ1OjM4LjU2N1oiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6ImQyN2IwYThiLTc1MGQtNGI0Yy1iNWI0LWVmOTkyYmU1NzNiOCIsInNpdGVPd25lcklkIjoiODI2MmY1MDAtZDJmMi00MDMzLWE3YjUtNWVkMTVkZjJkMTI2In0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
  'Content-Type': 'application/json',
  'accept': 'application/json',
  'x-wix-site-revision': '304',
  'x-wix-client-artifact-id': 'thunderbolt',
  'sec-ch-ua-platform': '"Windows"',
  'Origin': 'https://abbyshi622.wixsite.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://abbyshi622.wixsite.com/sparking-home/booking-calendar/oven-repairs?referral=service_list_widget',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,ko;q=0.5',
  'Cookie': 'XSRF-TOKEN=1684561023|ziiDMrWFrAk4; hs=-69254378; bSession=eed986dc-7898-4640-a6a3-da42ebeb5332|3; XSRF-TOKEN=1684648394|Eo0ETSkne-vk',
  'Content-Length': '89'
}

headers = {
  'Host': 'abbyshi622.wixsite.com',
  'Connection': 'keep-alive',
  'Content-Length': '90',
  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'authorization': 'tnmxW1St3zywPYRJtpPvKkoiFfosgJQimfJsAhBrhwk.eyJpbnN0YW5jZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4IiwiYXBwRGVmSWQiOiIyMmJlZjM0NS0zYzViLTRjMTgtYjc4Mi03NGQ0MDg1MTEyZmYiLCJtZXRhU2l0ZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4Iiwic2lnbkRhdGUiOiIyMDIzLTA1LTI0VDA1OjI1OjAwLjA3M1oiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6ImQyN2IwYThiLTc1MGQtNGI0Yy1iNWI0LWVmOTkyYmU1NzNiOCIsInNpdGVPd25lcklkIjoiODI2MmY1MDAtZDJmMi00MDMzLWE3YjUtNWVkMTVkZjJkMTI2In0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
  'Content-Type': 'application/json',
  'accept': 'applcation/json',
  'x-wix-site-revision': '337',
  'x-wix-client-artifact-id': 'thunderbolt',
  'sec-ch-ua-platform': '"Windows"',
  'Origin': 'https://abbyshi622.wixsite.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://abbyshi622.wixsite.com/sparking-home/booking-calendar/oven-repairs?referral=service_list_widget',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,ko;q=0.5',
  'Cookie': 'XSRF-TOKEN=1684561023|ziiDMrWFrAk4; hs=-69254378; bSession=53ce2dc4-c548-4b11-adee-54f2d9126581|1; fedops.logger.defaultOverrides=%7B%22paramsOverridesForApp%22%3A%7B%22enterprise-premium-features-widget.pages.index%22%3A%7B%22is_rollout%22%3Atrue%7D%7D%7D'
}


payload = """
{"identifier": {"email": "arm10@qq.com"}, "inputs": {"password": "123456"}, "captcha_tokens": []}
"""

payload1 = """
{"identifier": {"email": "sure123@qq.com"}, "inputs": {"password": "123456"}, "captcha_tokens": []}
"""

def test_sign_in():
    response_test, status_code = reuqest_sparkling(url, headers, payload)
    assert status_code == 200


def test_sign_in3():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in2():
    response_test, status_code = reuqest_sparkling(url, headers, payload1)
    assert status_code == 200



if __name__=="__main__":
    pytest.main("-v, test_1.py")
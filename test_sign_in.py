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


def test_sign_in0():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in1():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in2():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in3():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in4():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in5():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in6():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in7():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in8():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in9():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in10():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in11():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in12():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in13():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in14():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in15():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in16():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in17():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in18():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in19():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in20():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in21():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in22():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in23():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in24():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in25():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in26():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in27():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in28():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in29():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in30():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in31():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in32():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in33():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in34():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in35():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in36():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in37():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in38():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in39():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in40():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in41():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in42():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in43():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in44():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in45():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in46():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in47():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in48():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200


def test_sign_in49():
  response_test, status_code = reuqest_sparkling(url, headers, payload)
  assert status_code == 200



if __name__=="__main__":
    pytest.main("-v, test_sign_in.py")
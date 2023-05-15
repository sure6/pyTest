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
headers = {
  'accept': 'application/json',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
  'authorization': 'ijroIU_uDutS8_XLW5JHrJk9EqRFxur7LWvyXoAq0Xk.eyJpbnN0YW5jZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4IiwiYXBwRGVmSWQiOiIyMmJlZjM0NS0zYzViLTRjMTgtYjc4Mi03NGQ0MDg1MTEyZmYiLCJtZXRhU2l0ZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4Iiwic2lnbkRhdGUiOiIyMDIzLTA0LTI1VDA2OjQzOjQxLjEzNFoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjY5MTRiZmJkLTBhNGYtNGI4Ny05YjI1LTJkOWNlYWEwZjI0NSIsInNpdGVPd25lcklkIjoiODI2MmY1MDAtZDJmMi00MDMzLWE3YjUtNWVkMTVkZjJkMTI2In0',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'cookie': 'XSRF-TOKEN=1682326148|9rO3qoRIlc4P; hs=-862654646; fedops.logger.defaultOverrides=%7B%22paramsOverridesForApp%22%3A%7B%22sms-bm.pages.index%22%3A%7B%22is_rollout%22%3Atrue%7D%2C%22sms-bm.pages.number%22%3A%7B%22is_rollout%22%3Atrue%7D%2C%22sms-bm.pages.purchase%22%3A%7B%22is_rollout%22%3Atrue%7D%2C%22sms-bm-pages-index%22%3A%7B%22is_rollout%22%3Atrue%7D%2C%22sms-bm-pages-backoffice%22%3A%7B%22is_rollout%22%3Atrue%7D%2C%22sms-bm-pages-number%22%3A%7B%22is_rollout%22%3Atrue%7D%2C%22sms-bm-pages-purchase%22%3A%7B%22is_rollout%22%3Atrue%7D%7D%7D; bSession=c29483b6-0bb1-4e3a-a30e-2431b4c0e940|2',
  'origin': 'https://abbyshi622.wixsite.com',
  'pragma': 'no-cache',
  'referer': 'https://abbyshi622.wixsite.com/sparking-home',
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'x-wix-client-artifact-id': 'thunderbolt',
  'x-wix-site-revision': '52'
}
"""
null
@xxx.com
xx@xx.com
xxx.com 
相同邮箱不能
"""
payload1="""
    {"identity":{"identifiers": [{"email": ""}],"identityProfile":{"customFields": [],"phones": [],"emails": [""],"firstName": "sure12","lastName": "aaa12","privacyStatus": "PRIVATE"}},
               "inputs": {"password": "123456"},"captcha_tokens": []}
    """

payload="""
    {"identity":{"identifiers": [{"email": "sure1235@qq.com"}],"identityProfile":{"customFields": [],"phones": [],"emails": ["sure1235@qq.com"],"firstName": "sure12","lastName": "aaa12","privacyStatus": "PRIVATE"}},
               "inputs": {"password": "123456"},"captcha_tokens": []}
    """


def test_register():
    response_test, status_code= reuqest_sparkling(url, headers, payload)
    assert status_code == 200
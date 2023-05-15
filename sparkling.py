#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : sparkling.py
# @Project : python-test
# @Author  : lee sure
# @Descriptions :
# @Time    : 2023/4/24 22:38
# @Software : PyCharm

import requests



def reuqest_sparkling(url,headers,payload):

  response = requests.request("POST", url, headers=headers, data=payload)

  return (response.text,response.status_code)


if __name__=="__main__":
  url = "https://abbyshi622.wixsite.com/_api/iam/authentication/v1/login"
  # headers = {
  #   'accept': 'application/json',
  #   'accept-encoding': 'gzip, deflate, br',
  #   'accept-language': 'en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
  #   'authorization': 'iF29Y8izzMc80w_QTARxhIpJQ1k66gCLJ4BeQBob_S8.eyJpbnN0YW5jZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4IiwiYXBwRGVmSWQiOiIyMmJlZjM0NS0zYzViLTRjMTgtYjc4Mi03NGQ0MDg1MTEyZmYiLCJtZXRhU2l0ZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4Iiwic2lnbkRhdGUiOiIyMDIzLTA0LTI0VDEzOjA4OjMxLjA1MFoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjY5MTRiZmJkLTBhNGYtNGI4Ny05YjI1LTJkOWNlYWEwZjI0NSIsInNpdGVPd25lcklkIjoiODI2MmY1MDAtZDJmMi00MDMzLWE3YjUtNWVkMTVkZjJkMTI2In0',
  #   'cache-control': 'no-cache',
  #   'content-type': 'application/json',
  #   'cookie': 'XSRF-TOKEN=1682326148|9rO3qoRIlc4P; hs=1404836118; bSession=79a5bcca-347b-424c-85bd-9a1afdd31ef2|4',
  #   'origin': 'https://abbyshi622.wixsite.com',
  #   'pragma': 'no-cache',
  #   'referer': 'https://abbyshi622.wixsite.com/sparking-home',
  #   'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  #   'sec-ch-ua-mobile': '?0',
  #   'sec-ch-ua-platform': '"Windows"',
  #   'sec-fetch-dest': 'empty',
  #   'sec-fetch-mode': 'cors',
  #   'sec-fetch-site': 'same-origin',
  #   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  #   'x-wix-client-artifact-id': 'thunderbolt',
  #   'x-wix-site-revision': '52'
  # }
  headers = {
    'Connection': 'keep-alive',
    'Content-Length': '91',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'gt0X2fkPkFd-GbVrOgzLr0D54HQiD19KpsCPvjc9iN4.eyJpbnN0YW5jZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4IiwiYXBwRGVmSWQiOiIyMmJlZjM0NS0zYzViLTRjMTgtYjc4Mi03NGQ0MDg1MTEyZmYiLCJtZXRhU2l0ZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4Iiwic2lnbkRhdGUiOiIyMDIzLTA0LTI0VDExOjAxOjQyLjA3M1oiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjY5MTRiZmJkLTBhNGYtNGI4Ny05YjI1LTJkOWNlYWEwZjI0NSIsInNpdGVPd25lcklkIjoiODI2MmY1MDAtZDJmMi00MDMzLWE3YjUtNWVkMTVkZjJkMTI2In0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'accept': 'application/json',
    'x-wix-site-revision': '52',
    'x-wix-client-artifact-id': 'thunderbolt',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://abbyshi622.wixsite.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://abbyshi622.wixsite.com/sparking-home/account/my-orders',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cookie': 'XSRF-TOKEN=1682326148|9rO3qoRIlc4P; hs=-1237997847; bSession=95b18a0e-0b16-4d52-8aec-3750dd44df0e|3; fedops.logger.defaultOverrides=%7B%22paramsOverridesForApp%22%3A%7B%22social-blog%22%3A%7B%22is_rollout%22%3Atrue%7D%2C%22cashier-merchant-settings%22%3A%7B%22is_rollout%22%3Atrue%7D%7D%7D'
  }

  # payload="""
  #   {"identity":{"identifiers": [{"email": "sure123@qq.com"}],"identityProfile":{"customFields": [],"phones": [],"emails": ["sure123@qq.com"],"firstName": "sure1","lastName": "aaa1","privacyStatus": "PRIVATE"}},
  #              "inputs": {"password": "123456"},"captcha_tokens": []}
  #   """

  payload = """
  {"identifier": {"email": "sure12@qq.com"}, "inputs": {"password": "123456"}, "captcha_tokens": []}
  """
  print(reuqest_sparkling(url,headers,payload))
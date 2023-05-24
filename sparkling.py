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
  url = "https://abbyshi622.wixsite.com/_api/iam/authentication/v1/register"
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
  'Accept-Encoding':'gzip, deflate, br',
  'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,ko;q=0.5',
  'Connection':'keep-alive',
  'Content-Type': 'application/json',
  'Cookie': 'XSRF-TOKEN=1684561023|ziiDMrWFrAk4; hs=9046605; bSession=cb407643-0a56-42e8-85db-51d55c624bcd|3',
  'Host': 'abbyshi622.wixsite.com',
  'Origin': 'https://abbyshi622.wixsite.com',
  'Referer': 'https://abbyshi622.wixsite.com/sparking-home/booking-calendar/oven-repairs?referral=service_list_widget',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
  'accept': 'application/json',
  'authorization': '7y_5Jf7wieyukFNHHToTGO7W0u6QVnlGtW0SJrwi2eg.eyJpbnN0YW5jZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4IiwiYXBwRGVmSWQiOiIyMmJlZjM0NS0zYzViLTRjMTgtYjc4Mi03NGQ0MDg1MTEyZmYiLCJtZXRhU2l0ZUlkIjoiNjI0MDY5N2QtYjg3Yi00Nzk0LWJmNWEtNzg2MDMzMTI3MGI4Iiwic2lnbkRhdGUiOiIyMDIzLTA1LTIwVDA1OjM4OjQyLjU1NVoiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6ImQyN2IwYThiLTc1MGQtNGI0Yy1iNWI0LWVmOTkyYmU1NzNiOCIsInNpdGVPd25lcklkIjoiODI2MmY1MDAtZDJmMi00MDMzLWE3YjUtNWVkMTVkZjJkMTI2In0',
  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'x-wix-client-artifact-id': 'thunderbolt',
  'x-wix-site-revision': '250'
  }

  payload="""
    {
    "identity": {
        "identifiers": [
            {
                "email": "arm4@qq.com"
            }
        ],
        "identityProfile": {
            "customFields": [],
            "phones": [],
            "emails": [
                "arm4@qq.com"
            ],
            "firstName": "arm4",
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

  # payload = """
  # {"identifier": {"email": "sure12@qq.com"}, "inputs": {"password": "123456"}, "captcha_tokens": []}
  # """
  print(reuqest_sparkling(url, headers, payload))
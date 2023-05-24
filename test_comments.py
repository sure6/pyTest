
from sparkling import reuqest_sparkling
headers = {
  'Host': 'abbyshi622.wixsite.com',
  'Connection': 'keep-alive',
  'Accept': 'application/json, text/plain, */*',
  'commonConfig': '%7B%22brand%22%3A%22wix%22%2C%22BSI%22%3A%22cb407643-0a56-42e8-85db-51d55c624bcd%7C59%22%7D',
  'x-wix-brand': 'wix',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
  'authorization': 'wixcode-pub.c1e2acbd799ebea89f8ccac8c7872be6151026cc.eyJpbnN0YW5jZUlkIjoiMDIwYjQxZGUtYzEyNS00MjZiLTg4ZmQtZTRhMDcxZjNiYWZiIiwiaHRtbFNpdGVJZCI6ImNlYjZiYjkyLTlmNjMtNDJlZC1iOTUwLWM3ODk2ZTY5ZWM5ZSIsInVpZCI6IjcyYzVmYTZiLWE1ZjItNGQwMy04ZjIzLWM3ZGEyMDI0ZWJlMiIsInBlcm1pc3Npb25zIjpudWxsLCJpc1RlbXBsYXRlIjpmYWxzZSwic2lnbkRhdGUiOjE2ODQ1NjM1NTAzMjgsImFpZCI6ImQyN2IwYThiLTc1MGQtNGI0Yy1iNWI0LWVmOTkyYmU1NzNiOCIsImFwcERlZklkIjoiQ2xvdWRTaXRlRXh0ZW5zaW9uIiwiaXNBZG1pbiI6dHJ1ZSwibWV0YVNpdGVJZCI6IjYyNDA2OTdkLWI4N2ItNDc5NC1iZjVhLTc4NjAzMzEyNzBiOCIsImNhY2hlIjpudWxsLCJleHBpcmF0aW9uRGF0ZSI6IjIwMjMtMDUtMjBUMTA6MTk6MTAuMzI4WiIsInByZW1pdW1Bc3NldHMiOiJTaG93V2l4V2hpbGVMb2FkaW5nLEFkc0ZyZWUsSGFzRG9tYWluIiwidGVuYW50IjpudWxsLCJzaXRlT3duZXJJZCI6IjgyNjJmNTAwLWQyZjItNDAzMy1hN2I1LTVlZDE1ZGYyZDEyNiIsImluc3RhbmNlVHlwZSI6InB1YiIsInNpdGVNZW1iZXJJZCI6IjcyYzVmYTZiLWE1ZjItNGQwMy04ZjIzLWM3ZGEyMDI0ZWJlMiIsInBlcm1pc3Npb25TY29wZSI6bnVsbH0=',
  'X-Wix-Client-Artifact-Id': 'wix-thunderbolt',
  'Content-Type': 'application/json',
  'Origin': 'https://abbyshi622.wixsite.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://abbyshi622.wixsite.com/sparking-home/_partials/wix-thunderbolt/dist/clientWorker.2b57f96a.bundle.min.js',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,ko;q=0.5',
  'Cookie': 'XSRF-TOKEN=1684561023|ziiDMrWFrAk4; hs=9046605; bSession=cb407643-0a56-42e8-85db-51d55c624bcd|59; XSRF-TOKEN=1684648394|Eo0ETSkne-vk'
}

url = "https://abbyshi622.wixsite.com/_api/cloud-data/v1/wix-data/collections/save"

payload = """
{
    "collectionName": "Reviews-Tree",
    "item": {
        "reviewerName": "SURE",
        "professionalName": "LEE",
        "rating": 4,
        "comment": "GOOD12",
        "_id": "962be186-5fda-43f8-a214-e5de5065fe50"
    },
    "options": {
        "includeReferences": true
    },
    "segment": "LIVE",
    "appId": "c2f5e5c2-7818-44d8-b479-2c927b0a9960"
}
"""

def test_comments():
    response_test, status_code = reuqest_sparkling(url, headers, payload)
    assert status_code == 200
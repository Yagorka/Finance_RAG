import requests 
import json
token = input()

headers={
  "Authorization":"Bearer t1.9euelZqexpbMipfMko7Kko3KjJPPm-3rnpWazZGTzZCWisqbjsjMjp7Nj5vl8_d1ExRN-e9DIR5q_N3z9zVCEU3570MhHmr8zef1656VmsfInMbLx4uRic-SjpDOnJOb7_zF656VmsfInMbLx4uRic-SjpDOnJOb.dMdjT-Qjn2kHsr1Qc9w-xc8R_v_IPmW8tn2hsWpFoOGwQ15AiJaKiV_P2Im5lzwacxOtMaxiRzoLUuwHHAfXBg",
  "x-folder-id": "b1gusha7mjmhs05l6c84",
  "Content-Type": "application/json",
  "x-data-logging-enabled": "true"
}

res = requests.get('https://ocr.api.cloud.yandex.net/ocr/v1/getRecognition?operationId='+token, headers=headers)

"""
res = json.loads(res.text)
#cfr5bps49udcr8l03ojn
print(res)
"""
with open("res.txt", "w", encoding='utf-8') as text_file:
    text_file.write("["+res.text.replace('{"result":', ',{"result":')[1:]+"]")

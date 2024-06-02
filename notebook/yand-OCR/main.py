#pdf
import base64
import requests



#def get_pdf_list(company, statement):


with open("file.pdf", "rb") as pdf_file:
  encoded_pdf = base64.b64encode(pdf_file.read())



headers={
  "Authorization":"Bearer t1.9euelZqexpbMipfMko7Kko3KjJPPm-3rnpWazZGTzZCWisqbjsjMjp7Nj5vl8_d1ExRN-e9DIR5q_N3z9zVCEU3570MhHmr8zef1656VmsfInMbLx4uRic-SjpDOnJOb7_zF656VmsfInMbLx4uRic-SjpDOnJOb.dMdjT-Qjn2kHsr1Qc9w-xc8R_v_IPmW8tn2hsWpFoOGwQ15AiJaKiV_P2Im5lzwacxOtMaxiRzoLUuwHHAfXBg",
  "x-folder-id": "b1gusha7mjmhs05l6c84",
  "Content-Type": "application/json",
  "x-data-logging-enabled": "true"
}

obj = {
  "mimeType": "application/pdf",
  "languageCodes": ["*"],
  "model": "table",
  "content": encoded_pdf.decode("utf-8")
}

len(encoded_pdf.decode("utf-8"))

url = 'https://ocr.api.cloud.yandex.net/ocr/v1/recognizeTextAsync'

req = requests.post(url, json=obj, headers=headers)
print(req.text)


#
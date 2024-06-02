import json 
obj = json.loads(open("res.txt", encoding='utf-8').read())
format_line = []
res = ""

for page in range(len(obj)):
	print(obj[page]["result"]["textAnnotation"]["fullText"])
	"""
	blocks = obj[page]["result"]["textAnnotation"]["blocks"]
	for block in blocks:
		for line in block["lines"]:
			x = int(line["boundingBox"]["vertices"][0]['x'])
			y = int(line["boundingBox"]["vertices"][0]['y'])
			text = line["text"]

			print(text)
	"""
	



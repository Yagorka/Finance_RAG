import pymupdf 

# Open the pdf
"""

for page in doc:
    # For every page, draw a rectangle on coordinates (1,1)(100,100)
    page.draw_rect([1,1,100,100],  color = (0, 1, 0), width = 1)
# Save pdf
doc.save('res.pdf')
"""


import json 
obj = json.loads(open("res.txt", encoding='utf-8').read())

table = {}
res = ""


doc = pymupdf.open('./file5.pdf')
for page in range(len(obj)):
    blocks = obj[page]["result"]["textAnnotation"]["blocks"]
    
    width_obj = float(obj[page]["result"]["textAnnotation"]["width"])
    height_obj = float(obj[page]["result"]["textAnnotation"]["height"])
    print(width_obj, height_obj)

    width_pdf = float(doc[page].mediabox.width)
    height_pdf = float(doc[page].mediabox.height)
    scale = height_obj/height_pdf
    for block in blocks:
        for line in block["lines"]:
            x_start = int(line["boundingBox"]["vertices"][0]['x'])/scale
            y_start = int(line["boundingBox"]["vertices"][0]['y'])/scale
            x_end = int(line["boundingBox"]["vertices"][2]['x'])/scale
            y_end = int(line["boundingBox"]["vertices"][2]['y'])/scale
            #print( line["boundingBox"]["vertices"])
            text = line["text"]

            #print(x_start, y_start, x_end, y_end)
            doc[page].draw_rect([x_start, y_start, x_end, y_end],  color = (0, 1, 0), width = 1)
            """
            if table.get(x) == None:
                table[x] = {}

            table[x][y] = text
            #print(line["boundingBox"]['x'])
            """

doc.save('res.pdf')
#print(res)



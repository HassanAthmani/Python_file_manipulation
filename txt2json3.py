import re
string = open('/home/hassan/Downloads/Products.txt').read()
new_str= re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
open('Products2.txt','w+').write(new_str)

filepath='/home/hassan/Downloads/Products2.txt'
with open(filepath) as fp:
     line = fp.readline()    
     for x in fp: 
         f=open("testFinal_json.json","a+")
         f.write("{\"keywords\":""\""+x.strip()+"\",\n \"limit\": 5,\n \"print_urls\":true},\n")

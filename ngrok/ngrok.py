from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import re

html = urlopen("http://127.0.0.1:4040")
bsObj = BeautifulSoup(html,"html.parser")
"""print(bsObj.prettify())"""
a_tags = bsObj.findAll("script",{"type":"text/javascript"})
for a_tag in a_tags:
  if "window.common = JSON.parse" in a_tag.get_text():
    pos_start=a_tag.get_text().find("tcp:")
    pos_end=a_tag.get_text().find("Proto")
    message = a_tag.get_text()[pos_start:pos_end-5]
    
    f=open("/home/jun/compiled/ngrok/ngrok.txt","w")
    f.write(message)
    
    
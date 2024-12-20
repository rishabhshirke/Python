import re
text="sdsuh he6572jbkji woe99 0238r gfbdg"

x=re.search('\s',text)
print(x.start())

x=re.split(('\s'),text,1)
print(x)

txt = "The rain in Spain"
x = re.findall("\AThe", txt)
print(x)


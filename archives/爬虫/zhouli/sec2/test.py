import requests

# The link should be of the file directly
url = 'http://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2023-04-14/600848_20230414_UZM6.pdf'
file_extension = '.pdf'  # Example .wav
r = requests.get(url)

with open('x.pdf', 'wb') as f:
    # You will get the file in base64 as content
    f.write(r.content)

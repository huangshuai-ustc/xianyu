import tkinter as tk
from tkinter import filedialog, ttk
import base64
import json
import requests


# 打开文件对话框
def getfile():
    file_path = filedialog.askopenfilename()
    fpath.set(file_path)


def face_baidu():
    class BaiduPicIndentify:
        def __init__(self, img):
            self.AK = "3Pd8EGPvjoZZATAmIL3VFcW9"
            self.SK = "33TrVpW5QjDchk0NjXUQGxHGTU5TKlLO"
            self.img_src = img
            self.headers = {
                "Content-Type": "application/json; charset=UTF-8"
            }

        def get_accessToken(self):
            host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + self.AK + '&client_secret=' + self.SK
            response = requests.get(host, headers=self.headers)
            json_result = json.loads(response.text)
            return json_result['access_token']

        def img_to_BASE64(slef, path):
            with open(path, 'rb') as f:
                base64_data = base64.b64encode(f.read())
                return base64_data

        def detect_face(self):
            # 人脸检测与属性分析
            img_BASE64 = self.img_to_BASE64(self.img_src)
            request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
            post_data = {
                "image": img_BASE64,
                "image_type": "BASE64",
                "face_field": "gender,age,beauty,gender,race,expression",
                "face_type": "LIVE"
            }
            access_token = self.get_accessToken()
            request_url = request_url + "?access_token=" + access_token
            response = requests.post(url=request_url, data=post_data, headers=self.headers)
            json_result = json.loads(response.text)
            if json_result['error_msg'] != 'pic not has face':
                t1 = tk.Label(win, text=json_result['result']['face_num']).grid(row=4, column=1)
                t2 = tk.Label(win, text=json_result['result']['face_list'][0]['age']).grid(row=5, column=1)
                t3 = tk.Label(win, text=json_result['result']['face_list'][0]['beauty']).grid(row=6, column=1)
                t4 = tk.Label(win, text=json_result['result']['face_list'][0]['gender']['type']).grid(row=7, column=1)
                t5 = tk.Label(win, text=json_result['result']['face_list'][0]['race']['type']).grid(row=8, column=1)
                t6 = tk.Label(win, text=json_result['result']['face_list'][0]['expression']['type']).grid(row=9,
                                                                                                          column=1)

    if __name__ == '__main__':
        img_src = fpath.get()
        baiduDetect = BaiduPicIndentify(img_src)
        baiduDetect.detect_face()


win = tk.Tk()
win.title("颜值检测")
win.geometry("400x200")
fpath = tk.StringVar()

l = tk.Label(win, text='颜值检测系统-由百度AI提供', bg='brown', font='黑体,20,bold', fg='white')
l.grid(row=1, column=0)

ttk.Button(win, text='打开图片', command=getfile).grid(row=2, column=0)
ttk.Entry(win, textvariable=fpath).grid(row=2, column=1)

l1 = tk.Label(win, text='人脸数：')
l1.grid(row=4, column=0)
l2 = tk.Label(win, text='人物年龄：')
l2.grid(row=5, column=0)
l3 = tk.Label(win, text='人物颜值评分：')
l3.grid(row=6, column=0)
l4 = tk.Label(win, text='人物性别：')
l4.grid(row=7, column=0)
l5 = tk.Label(win, text='人物种族：')
l5.grid(row=8, column=0)
l6 = tk.Label(win, text='人物表情：')
l6.grid(row=9, column=0)

b = tk.Button(win, text="点我检测", width=15, height=2, command=face_baidu)
b.grid(row=10, column=0)

win.mainloop()

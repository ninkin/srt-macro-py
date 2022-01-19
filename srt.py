import getpass
import random
import time

from SRT import SRT


SRT_ID = ''
SRT_PASSWD = ''

if SRT_ID == '' or SRT_PASSWD == '':
    SRT_ID = input('SRT ID: ')
    SRT_PASSWD = getpass.getpass('SRT PASSWD: ')

srt = SRT(SRT_ID, SRT_PASSWD)

if not srt.login():
    print('check id & passwd')
    exit(0)

print('login success')

dep = input('출발역: ').strip()
arr = input('도착역: ').strip()
dep_date = input('출발일(20220101): ').strip()
dep_time = input('시간(103000): ').strip()


suc = False
cnt = 0
while not suc:
    trains = srt.search_train(dep, arr, dep_date, dep_time, available_only=False)
    print(trains[0])
    try:
        seat = srt.reserve(trains[0])
        suc = True
        print(seat)
        print('done')
    except Exception as e:
        sleep_time = random.uniform(0.1, 0.9)
        time.sleep(sleep_time)
        print(f'trial {cnt} {e}')
        cnt += 1

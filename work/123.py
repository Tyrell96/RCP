import datetime

dt_s_y = input('시작년도: ')
dt_s_m = input('시작월: ')
dt_s_d = input('시작일: ')
dt_e_y = input('종료년도: ')
dt_e_m = input('종료월: ')
dt_e_d = input('종료일: ')

dt_s = datetime.date(int(dt_s_y), int(dt_s_m), int(dt_s_d))
dt_e = datetime.date(int(dt_e_y), int(dt_e_m), int(dt_e_d))

def convert(dt):

    format = '%Y%m%d'

    str_dt = datetime.datetime.strftime(dt, format)

    return str_dt

def compare(dt2):

    a = dt2[0:4]
    b = dt2[::-1][0:4]

    if a == b:
        return True

while True:

    if compare(convert(dt_s)) == True:
        print(dt_s)

    dt_s = dt_s + datetime.timedelta(days=1)

    if dt_s == dt_e:
        break


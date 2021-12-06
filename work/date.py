from datetime import timedelta
import datetime
date = timedelta(days=1)
format = '%Y%m%d'
reverse = ""
x = "20211202" #시작날짜
O = "20400830" #끝나는날짜
firsttime = datetime.datetime.strptime(x, format)
lasttime = datetime.datetime.strptime(O, format)
front = x[0:4]
x = x[::-1]
reverse = x[0:4]
day = (lasttime - firsttime).days

for i in range(0,day):
    if front == reverse:
        print(firsttime.strftime(format))
    firsttime = firsttime + date
    checktime = datetime.date.strftime(firsttime, format)
    front = checktime[0:4]
    x = checktime[::-1]
    reverse = x[0:4]
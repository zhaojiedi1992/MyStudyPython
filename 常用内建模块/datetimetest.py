from datetime import datetime, timedelta
now = datetime.now()
print(now)

print(type(now))

print(now.timestamp())

#时间转为str
from datetime import datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

now +　timedelta(hours=10)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
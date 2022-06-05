import datetime
now = datetime.datetime.now() + datetime.timedelta(hours=9) #한국시간으로

print(now.year)
print(now.month)
print(now.day)
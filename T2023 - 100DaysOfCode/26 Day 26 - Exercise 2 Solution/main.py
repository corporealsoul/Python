import time

times = time.strftime('%H:%M:%S')
hourstr = time.strftime('%H')
hours = int(time.strftime('%H'))
minutes = time.strftime('%M')
seconds = time.strftime('%S')

print(times)
print(hours)
print(minutes)
print(seconds)

if (hours>=0 and hours<=12):
    print("Good Morning !!")
elif (hours>=12 and hours<=17):
    print("Good Afternoon !!")
if (hours>=17 and hours<=24):
    print("Good Night !!")

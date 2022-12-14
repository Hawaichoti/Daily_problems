from datetime import datetime

current_time = datetime.now().strftime('%H:%M:%S')
#print(current_time)
# t = time.asctime(time.localtime(time.time())) 
tarr = current_time.split(":")
hr = int(tarr[0])
# hr = 23
#print(hr)
if hr<12:
  print("good morning sir")
if hr>=12 and hr<16:
  print("good afternoon sir")
elif hr>=16 and hr<20:
  print("good evening sir")
else:
  print("good night sir")

import datetime
current_time = datetime.datetime.now()
print("time now :",current_time)
print('week day:',current_time.strftime("%a"))
print('day no of year:',current_time.strftime("%j"))
print("week no of year:",current_time.strftime('%W)'))
print(" year:",current_time.strftime('%Y)'))
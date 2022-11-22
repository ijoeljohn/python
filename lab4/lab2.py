from datetime import date,timedelta
dt = date.today()-timedelta(5)
print('current date:',date.today()) 
print('5 day before current date:',dt)
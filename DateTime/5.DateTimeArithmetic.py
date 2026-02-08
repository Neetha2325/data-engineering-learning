from datetime import datetime,timedelta
my_dob=datetime(1991,5,7)
your_dob=datetime(1990,8,21)
print(my_dob-your_dob)

duration=timedelta(days=2)
print(my_dob+duration)

duration=timedelta(hours=1,seconds=30)
print(my_dob-duration)




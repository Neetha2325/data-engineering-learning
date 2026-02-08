from datetime import date
dob=date(1980,3,12)
print(dob)

print("Today Date:",date.today())

print(dob.day,dob.month,dob.year)

print(dob.strftime("%A %d - %b %Y"))

print(dob.weekday())

if dob.weekday()>=5:
    print("Weekend")
else:
    print("Weekday")

dob_updated=dob.replace(month=11)
print(dob_updated)
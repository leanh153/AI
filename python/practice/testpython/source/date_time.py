from datetime import date

now = date.today()

print(now)

birthday = date(1994, 3, 15)

age = now - birthday
age = age.days / 360

print("AGE: ", age)

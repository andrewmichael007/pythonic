

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))


if hours > 40 :
    pay = hours * rate
    overtime = hours - 40.0 * (1.5 * rate)
    gross_pay = pay + overtime
    print(gross_pay)
    
else:
    pay = hours * rate
    print(pay)
    
    
    
    

hours = input("Enter hours: ")
rate = input("Enter rate: ")

if hours > "40":
    pay = (float(hours) * float(1.5)) * float(rate)
    print(pay)
else:
    pay = float(hours) * float (rate)
    print(pay)

    






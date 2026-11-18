#Angelina Del VIcario
#11/18/26
#CMP131
#Lab 10
#Problem 1

def numEmp():
    employees = int(input("Enter the number of employees in company:"))

    while employees < 1:
        print("Error employees must be at least one")
        employees = int(input("Enter the number of employees in company:"))
    return employees

def absent(numEmp):
    total_days = 0

    for i in range(1, numEmp + 1):
        days = int(input("Enter Number of days employee missed: "))

    while days < 0:
        print ("Error: Days missed cannot be negative")
        days = int(input("Enter Number of daysemployee missed: "))

        total_days += days

    return total_days

def calc_avdays(numEmp,total_days):
    return total_days / numEmp

def main():
    employees = numEmp()

    absent = absent(employees)

    average_ab = average_days(employees, absent)

    print("\n the anverage number of days absent is: ",average_ab)

    main()

print("Enter the number of days:")
num = int(input())

year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)

print("Total number of year(s),", year)
print("Total number of week(s),", week)
print("Total number of day(s),", days)
# Take marks as input from user
print("Enter Marks obtained in 4 subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

# Let's calculate the sum of marks 
sum = math+english+science+hindi
print("sum of maths, english, science and hindi:", sum)

# Let's calculate the percentage of marks
perc = (sum/400)*100
print("percentage of maths, english, science and hindi:", perc)


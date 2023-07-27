# #Basics

# print("hello world")
# name="kshitij"
# age=21
# print(name)
# print(age)
# is_Adult=True
# print(is_Adult)

# #Taking user input

# name=input("Enter yor name ")
# print(name)
# old_age=input("enter your age")
# new_age=int(old_age)+2
# print(new_age)

#Simple program

# first=input("enter 1 num")
# second=input("Enter second num")
# sum=int(first)+int(second)
# print(sum)


#Strings
# name="kshitij"
# print(name.upper())
# print(name.lower())
# print(name.find('s'))
# print(name.replace('kshitij','kumar'))
# print('k'in name)

# #Operators
# print(5+2)
# print(5-2)
# print(5*2)
# print(5/2) #can be float value 
# print(5//2) #gives only int value
# print(5**2)#power to
# print(3>2)
# print(3<2)
# print(3>=2)
# print(3<=2)
# print(3==2)
# print(3!=2)

#Logical operator
# print(2>3 or 2>1) #true
# print(3>2 and 2<1) #true
# print(not 2>3) #true


#If-else
# age=21
# if age>=18:
#     print("you are eligible")
#     print("you can vote")
#     print("thank you")
# elif age<18 and age>3:
#          print("you are a minor")
# else:
#     print("you are a child")

# #Calculator program
# first=input("enter 1st number")
# operator=input("enter operator(+,-,*,/,%): ")
# second=input("enter 2nd number")
# if operator == "+" :
#     print(int(first) + int(second))
# elif operator == "-" :
#     print(int(first) - int(second))
# elif operator == "*" :
#     print(int(first) * int(second))
# elif operator == "/" :
#     print(int(first) / int(second))
# elif operator == "%" :
#     print(int(first) % int(second))
# else:
#     print("Invalid")
 #while loop
# i = 1
# while i<=5:
#      print(i)
#      i=i+1

#for loop
# for i in range(5)
# print(i)

#List
# marks=[67,78,90]
# print(marks)
# #for specific item
# marks=[67,78,90]
# print(marks[0])
# print(marks[0:2])
#  for score in marks:
#      print(score)
# marks.append() // to add value at the
# marks.insert(0,89)//to add value at specific position
# marks=[67,78,90]
# i=0
# while i<len(marks):
#     print(marks[i])
#     i=i+1
# marks.clear()//to clear list

#Break
# students=["kshitij","kumar","ram","sita"]
# for student in students
#  if student=="ram":
#      break;
#  print(student)


#Continue
# students=["kshitij","kumar","ram","sita"]
# for student in students
#  if student=="ram":
#      continue;//list will print without ram
#  print(student)

#Tuples
# makrs=(89,98,98,78,67)
# marks.count(98)//gives count
# marks.index(98)//gives index

#Sets
# marks={89,89,90,87}
# print(marks)//prints only unique values

#Dictionary
# marks={"eng":89,"hindi":78}
# print(marks["eng"])
# marks["phy"]=90;//to add new value
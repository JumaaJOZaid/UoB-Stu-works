from datetime import datetime #I used the datetime module to get the current hour of the day.
studentID = input("Hello student,please enter your student ID: ") #all of these inputs are used to get the studet details.
fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")
mark1 = int(input("Please enter your marks for subject 1: "))
mark2 = int(input("Please enter your marks for subject 2: "))
mark3 = int(input("Please enter your marks for subject 3: "))
mark4 = int(input("Please enter your marks for subject 4: "))
try:
    hour1 = int(input("Please enter the hour of the day in 24 hour format: ")) #I used try so that there is no error if no value is entered
except ValueError:
    hour1 = ""
hour2 = datetime.now().hour #And from here it is written to get the hour.

if hour1 == "": #this is used to check if the time is entered or not.
    time = hour2
elif hour1 < 0 or hour1 > 24: #this is used to check if the time entered is valid or not.
    print("Invalid data entered, time will be taken as current time.")
    time = hour2
else:
    time = hour1

if time < 12: #this is used to check about the greeting based on the time entered.
    greeting = "Good Morning"
elif time < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"
print(greeting + " " + fname + " " + lname)

total = mark1 + mark2 + mark3 + mark4 #this is used to calculate the total marks.
average = total / 4
print("Your average is: " + str(average))

highest = mark1 #it is used to find the highest and the lowest and to compare between them.
lowest = mark1
if highest < mark2: #This is used to find the highest.
    highest = mark2 
if highest < mark3:
    highest = mark3
if highest < mark4:
    highest = mark4

if lowest > mark2: #This is used to find the lowest.
    lowest = mark2
if lowest > mark3:
    lowest = mark3
if lowest > mark4:
    lowest = mark4
print("Your highest mark is: " + str(highest) + " and your lowest mark is: " + str(lowest)) 

difference = highest - lowest #This is used to find the difference between the highest and the lowest.
print("The difference between your highest and lowest mark is: " + str(difference))

if average >= 60: #this is used to check if the student has passed or not.
    print("You passed")
else:
    print("You failed")

if average >= 80: # in here it check if the average is greater than or equal to 80 and 70
    print("Excellent.")
elif average >= 70:
    print("Well done,")
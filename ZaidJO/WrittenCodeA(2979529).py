#Student number: 2979529

from datetime import datetime #I used the datetime module to get the current hour of the day.
while True: #this is used to check if the student ID is valid or not.
    studentID = input("Hello student,please enter your student ID: ") #all of these inputs are used to get the studet details.
    if len(studentID) == 7 and studentID.isdigit():
        break
    print("Invalid student ID. Please enter a 7-digit number.")

while True: #this is used to check if the first name is valid or not.
    fname = input("Please enter your first name: ")
    if fname.isalpha():
        break
    print("Invalid first name. Please enter a valid name.")

while True: #this is used to check if the last name is valid or not.
    lname = input("Please enter your last name: ")
    if lname.isalpha():
        break
    print("Invalid last name. Please enter a valid name.")

while True: #this is used to check if the first mark entered is valid or not.
    mark1 = input("Please enter your 1st marks: ")
    if mark1.isdigit() and 0 <= int(mark1) <= 100:
        break
    print("Invalid mark entered. Please enter a number between 0 and 100.")
mark1 = int(mark1) #this is used to convert the mark entered into an integer.

while True: #this is used to check if the second mark entered is valid or not.
    mark2 = input("Please enter your 2nd marks: ")
    if mark2.isdigit() and 0 <= int(mark2) <= 100:
        break
    print("Invalid mark entered. Please enter a number between 0 and 100.")
mark2 = int(mark2) #this is used to convert the mark entered into an integer.

while True: #this is used to check if the third mark entered is valid or not.
    mark3 = input("Please enter your 3rd marks: ")
    if mark3.isdigit() and 0 <= int(mark3) <= 100:
        break
    print("Invalid mark entered. Please enter a number between 0 and 100.")
mark3 = int(mark3) #this is used to convert the mark entered into an integer.

while True: #this is used to check if the fourth mark entered is valid or not.
    mark4 = input("Please enter your 4th marks: ")
    if mark4.isdigit() and 0 <= int(mark4) <= 100:
        break
    print("Invalid mark entered. Please enter a number between 0 and 100.")
mark4 = int(mark4) #this is used to convert the mark entered into an integer.

hour2 = datetime.now().hour #From here it is written to get the hour.
if hour2 < 12: #this is used to check about the greeting based on the time.
    greeting = "Good Morning"
elif hour2 < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"
print(greeting + " " + fname + " " + lname)

total = mark1 + mark2 + mark3 + mark4 #this is used to calculate the total marks.
average = total / 4
print("Here is your average student: " + str(average))

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
    print("congratulations " + fname + " " + lname + "! You passed")
else:
    print("sorry " + fname + " " + lname + ". You failed")

if average >= 80: # in here it check if the average is greater than or equal to 80 and 70
    print("Excellent.")
elif average >= 70:
    print("Well done,")
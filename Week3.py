# #print statement
# print("Welcome to tutorial week 3")

# #variable
week = "Week"
# #week = 5 #this will cause an error at line 11
number = 3

#print with string
print("Welcome to tutorial", week , number) #3 arguments, convert automatically each argument
print("Welcome to tutorial"+ " " + week + " " + str(number)) #1 argument
print("Welcome to tutorial {} {}".format(week, number))
print(f"Welcome to tutorial {week} {number}")


# #input function
# # ageInput = input("How old are you: ")

# # print("Your age is", ageInput)
# # print("Your age is {}".format(ageInput))


# # is_receive_money = bool(input("Do you receive pocket money (true/false): "))
# # print(is_receive_money)

# # pockey_money = 5
# # pockey_money += int(input("How much do you receive each month: "))
# # print("Your balance is", pockey_money)


# #string manipulation
greeting = "Welcome to tutorial, week 4"
first_char = greeting[0]
last_char = greeting[-1]

print("the first character is", first_char)
print("the last character is", last_char)

length_greeting = len(greeting)
print("the length of my string is", length_greeting)

week_num = greeting[20:26] #index 20 to 25, because exclude 26
print("We are at ", week_num)

split_greeting = greeting.split()
print(split_greeting)

join_greeting = ("|").join(split_greeting)
print(join_greeting)


print(greeting.isalpha())
print(greeting.islower())  #lower()
print(greeting.isupper()) #upper()
print(greeting.isdigit())
print(split_greeting[4].isdigit())

# print(greeting.startswith("welcome"))
# print(greeting.endswith("welcome"))

print(greeting.upper())
print(greeting.lower())
print(greeting.title())
student_info_title = "Student information".center(25)
print(student_info_title, "something")
print("name".ljust(10), "id".rjust(10) )
print("joe".ljust(10), "12234".rjust(10))
print("john".ljust(10), "15634".rjust(10))

name = "name"
print(f"{name:<20} something")
print("%-20s something" %name)

s_i_t_lstrip = student_info_title.lstrip()
print(s_i_t_lstrip)
s_i_t_rstrip = student_info_title.rstrip()
print(s_i_t_rstrip, "something")
s_i_t_strip = student_info_title.strip()
print(s_i_t_strip, "something")


total = 123.4567
print("-"*20)
print("Round a number to 2 decimal numbers")
print("Total: $ " + str(round(total,2)))
print("Total: $",  round(total,2))
print("Total: $ %.2f" % total)
print("Total: $ {0:.2f}".format(total))
print(f"Total: $ {total:0,.2f}")

# print("-"*20)
# print(f"Total: $ {total:^15.2f}center") #center
# print(f"Total: $ {total:<15.2f}left") #left to right
# print(f"Total: $ {total:>15.2f}right") #right to left
# print("Total: $ %15.2fright" %total )  #for right to left
# print("Total: $ %-15.2fleft" %total ) #for left to right











print("####              ****Please use only whole numbers****             ####")
print("####    If you enter anything else you will get an error            ####")
print("####    I hope you enjoy this small demo of determining             ####")
print("####    someones eligibility to enter a site based on there age!    ####\n")



user_day = input("Please enter the day you were born [In Numbers]: ")
user_month = input("Please enter the month you were born [In Numbers]: ")
user_year = input("Please enter the year you were born [In Numbers]:")

min_agereq_day = int(16)
min_agereq_month = int(12)
min_agereq_year = int(2000)

iuser_day = int(user_day)
iuser_month = int(user_month)
iuser_year = int(user_year)


if iuser_day <= min_agereq_day and iuser_month <= min_agereq_month and iuser_year <= min_agereq_year:
    print("You are old enough to enter the site!")
else:
    print("You are not old enough to enter the site!\n")


print("Thanks for checking out my demo!")
print("Created by Garrett Johnson,2018")


## Conversion to integer from string variables.

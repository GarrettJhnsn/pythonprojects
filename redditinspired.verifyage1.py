print("####              ****Please use only whole numbers****             ####")
print("####    If you enter anything else you will get an error            ####")
print("####    I hope you enjoy this small demo of determining             ####")
print("####    someones eligibility to enter a site based on there age!    ####\n")

"""USER INPUT/NUMBERS ONLY/NO FLOAT"""

user_day = input("Please enter the day you were born [In Numbers}: ")
user_month = input("Please enter the month you were born [In Numbers]: ")
user_year = input("Please enter the year you were born [In Numbers]:")

"""CONVERSION FROM STRING TO INT/IF NOT CONVERSION IF STATEMENT FAILS"""

min_age_req_day = int(16)
min_age_req_month = int(12)
min_age_req_year = int(2000)

"""USER INPUT INT CONVERTED VARIABLES"""

i_user_day = int(user_day)
i_user_month = int(user_month)
i_user_year = int(user_year)

"""IF YOU MEET THE MIN REQ STATED IN MIN_AGE_REQ VALUE PRINTS WELCOME/IF NOT MEETING MIN REQ PRINTS ELSE"""

if i_user_day <= min_age_req_day and i_user_month <= min_age_req_month and i_user_year <= min_age_req_year:
    print("You are old enough to enter the site!")
else:
    print("You are not old enough to enter the site!")


"""THANK YOU"""

print("\n")
print("Thanks for checking out my demo!")
print("Created by Garrett Johnson,2018")


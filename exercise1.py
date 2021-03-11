# This small script is the answer to exercise 1
def age_calc(age):  # This function will calculate the age to the next tenth
    """Calculate the age to the next tenth."""
    new_age = int((age // 10) * 10 + 10)
    return new_age

user_name = input("Enter Your name, please: ")
user_age = float(input("Enter Your age, please: "))

next_tenth = age_calc(user_age)

print(user_name + ", in " + str(int(next_tenth - user_age)) + " years You will be " + str(next_tenth) + ".")
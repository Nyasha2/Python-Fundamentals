"""
CS 1 Lab 01: Pitfalls
Warmup Question 0
Write a Python function which takes a Caltech username as a string parameter and returns a valid email address in the format of <username>@caltech.edu. Hint: You can lowercase a string with the <str>.lower() method (e.g. 'ABC'.lower()).

*Remember that printing and returning is not the same thing!* This function should not
print anything.
"""

def username_to_email(username):
    name = username.lower()
    email = name + "@caltech.edu"
    return email


# 2. Uncomment this line to test your function
email1 = username_to_email('lhovik') # 'lhovik@caltech.edu' 
print(email1)
email2 = username_to_email('Lhovik') # 'lhovik@caltech.edu' 

username3 = 'EHovik'
email3 = username_to_email(username3)
print(f'{username3}\'s Caltech email is {email3}!')

email4 = username_to_email('MaDDie') # 'lhovik@caltech.edu' 



# 3. Add at least one more function call to test your function

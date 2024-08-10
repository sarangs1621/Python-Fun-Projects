import random
import string
def get_random_password_string(length):
   password_character=string.ascii_letters+string.digits+string.punctuation
   password=' '.join(random.choice(password_character) for i in range(length))
   print("Your Password is:",password)
get_random_password_string(int(input("enter how many characters:")))
   

import string
import random
#Letters upercase lowercase , numbers , character
s1 = list( string.ascii_lowercase )
s2 = list( string.ascii_uppercase)
s3 = list( string.digits )
s4 = list( string.punctuation )
# enter length of password
length = input("How many characters for the password? ")
while True:
    try:
        length = int( length )
        if length  < 6 :
            print( "You need at least 6 characters")
            length = input("Please enter the number again: ")
        else:
            break
    except:
        print("Please enter numbers only")
        length = input("Please enter the number again: ")
# letters  upper and lower 30% ; numbers 20% ; char 20% 
numbers_of_letters = round(0.3 * length ) 
numbers_of_char =  round(0.2 * length) 
# the variable of password
password = []
# store the password
for i in range( numbers_of_letters ):
    password.append( random.choice( s1 ))
    password.append( random.choice( s2 ) )
for i in range( numbers_of_char ):
    password.append( random.choice( s3 ))
    password.append( random.choice( s4 ))
# sure of length password
if length < len(password):
    password.pop( )
elif length > len(password):
    password.append( '_' )
# sure of numbers and letters and character are not sort
random.shuffle( password)
# return from list to string
password = ''.join( password )
print( password )
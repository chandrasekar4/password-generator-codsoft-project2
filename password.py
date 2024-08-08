import random
import string
length=int(input("Enter the desired length of the password: "))
#password generator
charactor=string.ascii_letters+string.digits+string.punctuation
password=''.join(random.choice(charactor) for i in range(length))
print("Generated Password:",password)
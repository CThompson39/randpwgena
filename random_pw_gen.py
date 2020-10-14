# Random Password Generator

import random
import string


lc = string.ascii_lowercase
uc = string.ascii_uppercase
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
rc = ['~', '!', '@', '#', '$', '%', '&', '?']
# Creating pieces of the string to be shuffled.

uppercaseLetter1 = random.choice(uc)
uppercaseLetter2 = random.choice(uc)
uppercaseLetter3 = random.choice(uc)
uppercaseLetter4 = random.choice(uc)
lowercaseLetter1 = random.choice(lc)
lowercaseLetter2 = random.choice(lc)
lowercaseLetter3 = random.choice(lc)
lowercaseLetter4 = random.choice(lc)
digit1 = random.choice(num)
digit2 = random.choice(num)
digit3 = random.choice(num)
digit4 = random.choice(num)
randomCharacter1 = random.choice(rc)
randomCharacter2 = random.choice(rc)

# Creating string of all previously defined items.

password = (uppercaseLetter4 + uppercaseLetter3 + uppercaseLetter2 + uppercaseLetter1 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + digit1 + digit2 + digit3 + digit4 + randomCharacter1 + randomCharacter2)

# Shuffle string to generate new password.

password = str(password)
p_list = list(password)
random.shuffle(p_list)
psw = ''.join(p_list)

# Output/Print the password.

print(psw)
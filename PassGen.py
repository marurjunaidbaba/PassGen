import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Hello! Good Day")
n_letters = int(input("Number of Letters: \n"))
n_numbers = int(input("Number of numbers: \n"))
n_symbols = int(input("Number of symbols: \n"))
P_list = []
for i in range(1,n_letters+1):
  char = random.choice(letters)
  P_list += char
for i in range(1,n_numbers+1):
  char = random.choice(numbers)
  P_list += char
for i in range(1,n_symbols+1):
  char = random.choice(symbols)
  P_list += char

random.shuffle(P_list)
password = ""
for char in P_list:
  password += char

print("Generated Password: ",password)

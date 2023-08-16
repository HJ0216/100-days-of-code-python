#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
import random

letter_list = [];
for i in range(0, nr_letters):
  random_num = random.randint(0, len(letters)-1);
  letter_list.append(letters[random_num]);

symbol_list = [];
for i in range(0, nr_symbols):
  random_num = random.randint(0, len(symbols)-1);
  symbol_list.append(symbols[random_num]);

number_list = [];
for i in range(0, nr_numbers):
  random_num = random.randint(0, len(numbers)-1);
  number_list.append(numbers[random_num]);

all = letter_list+symbol_list+number_list;

for s in all:
  print(s, end="");
print();

pwd = ""

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    pwd += random_char

for char in range(1, nr_symbols + 1):
    pwd += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    pwd += random.choice(numbers)

print(pwd)




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_list = []

while len(random_list) < len(all):
    all_len = len(all)
    random_num = random.randint(0, all_len - 1)
    if (random_list.count(random_num) == 0):
        random_list.append(random_num)

for i in random_list:
    print(all[i], end="")
print();


pwd_list = [];

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    pwd_list += random_char

for char in range(1, nr_symbols + 1):
    pwd_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    pwd_list += random.choice(numbers)

random.shuffle(pwd_list);

pwd2 = "";
for char in pwd_list:
  pwd2 += char;
  
print(pwd2);

# Import the random module here
import random;

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Sol-1
random_num = random.randint(0, len(names)-1);
print(names[random_num] + " is going to buy the meal today!")

# Sol-2
random_choice = random.choice(names);
print(random_choice + " is going to buy the meal today!")

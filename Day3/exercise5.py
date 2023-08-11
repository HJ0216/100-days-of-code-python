# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
true_occur = 0;
love_occur = 0;

true_occur += name1.lower().count("t");
true_occur += name1.lower().count("r");
true_occur += name1.lower().count("u");
true_occur += name1.lower().count("e");
true_occur += name2.lower().count("t");
true_occur += name2.lower().count("r");
true_occur += name2.lower().count("u");
true_occur += name2.lower().count("e");

love_occur += name1.lower().count("l");
love_occur += name1.lower().count("o");
love_occur += name1.lower().count("v");
love_occur += name1.lower().count("e");
love_occur += name2.lower().count("l");
love_occur += name2.lower().count("o");
love_occur += name2.lower().count("v");
love_occur += name2.lower().count("e");

total = 10 * true_occur + love_occur;
if(total<10 or total>90):
    print(f"Your score is {total}, you go together like coke and mentos.");
elif(total>=40 and total<=50):
    print(f"Your score is {total}, you are alright together.");
else:
    print(f"Your score is {total}.");

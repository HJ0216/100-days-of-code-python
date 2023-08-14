rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random;

image_list = [rock, paper, scissors];

name = input("What is your name?\n");
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"));
# if(choose == 0):
#   choose_ASCII = rock;
# elif(choose == 1):
#   choose_ASCII = paper;
# elif(choose == 2):
#   choose_ASCII = scissors;
# print(name + "\n" + choose_ASCII);

if(choose==0 or choose==1 or choose==2):
  print(name + "\n" + image_list[choose]);

  com = random.randint(0, 2);
  # if(com == 0):
  #   com_ASCII = rock;
  # elif(com == 1):
  #   com_ASCII = paper;
  # elif(com == 2):
  #   com_ASCII = scissors;
  
  # print("computer\n" + com_ASCII);
  
  print(f"computer\n{image_list[com]}");

  if(choose==com):
    result = "Draw";
  
  if(choose==0):
    if(com==1):
      result = "Computer win";
    elif(com==2):
      result = name + " win";
  elif(choose==1):
    if(com==0):
      result = name + " win";
    elif(com==2):
      result = "Computer win";
  elif(choose==2):
    if(com==0):
      result = "Computer win";
    elif(com==1):
      result = name + " win";
    
  print(result);
  
else:
  print("You entered the wrong number.");

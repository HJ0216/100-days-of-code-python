#Write your code below this row 👇
for num in range(1, 101):
    if(num%3==0):
        if(num%5==0):
            print("FizzBuzz");
        else:
            print("Fizz");
    elif(num%5==0):
        if(num%3==0):
            print("FizzBuzz");
        else:
            print("Buzz");
    else:
        print(num);


#Write your code below this row 👇
for num in range(1, 101):
    if(num%3==0 and num%5==0):
        print("FizzBuzz");
    elif(num%3==0):
        print("Fizz");
    elif(num%5==0):
        print("Buzz")
    else:
        print(num);


#Write your code below this row 👇
for num in range(1, 101):
    if(num%15!=0):
        if(num%3==0):
            print("Fizz");
        elif(num%5==0):
            print("Buzz");
        else:
            print(num);
    else:
        print("FizzBuzz");

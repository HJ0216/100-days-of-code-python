# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
heights = 0;
nums = 0;

for height in student_heights:
    heights += height;
    nums += 1;

avg = round(heights / nums, 0);
print(int(avg));


#Write your code below this row 👇
sum_height = sum(student_heights);
num_students = len(student_heights);
avg_height = round(sum_height/num_students);
print(avg_height);

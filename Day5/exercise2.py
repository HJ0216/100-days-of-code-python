# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
max_score = 0;
for score in student_scores:
    if max_score < score:
        max_score = score;

print(f"The highest score in the class is: {max_score}");


#Write your code below this row 👇
min_score = 100;
for score in student_scores:
  min_score = min_score if min_score<=score else score;

print(f"The lowest score in the class is: {min_score}");


#Write your code below this row 👇
print(max(student_scores));
print(min(student_scores));

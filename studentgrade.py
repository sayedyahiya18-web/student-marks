marks = [80,95,85,85,70]
avg = sum(marks)/5
if avg>85:
    grade = 'A'
elif avg>70 or avg<85:
    grade = 'B'
elif avg>55 or avg<70:
    grade = 'C'
elif avg>40 or avg<55:
    grade = 'D'
else:
    grade = 'Fail'

print("Marks :",marks)
print(f"The average is :{avg:.2f}")
print("Grade :",grade)
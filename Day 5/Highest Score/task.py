student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_scores = sum(student_scores)

sum = 0
max = max(student_scores)
min = min(student_scores)
new_min = student_scores[0]
new_max = student_scores[0]

for score in student_scores:
    sum += score

for mini in student_scores:
    if new_min > mini:
        new_min = mini
    if new_max < mini:
        new_max = mini

print(f"min = {new_min}")
print(new_max)


print(min)
print(max)
print(sum)
print(total_exam_scores)


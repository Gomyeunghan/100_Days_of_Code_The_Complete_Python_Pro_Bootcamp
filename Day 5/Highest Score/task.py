student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0


for next_score in student_scores:
    if(max_score < next_score):
        max_score = next_score

print(max_score)
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
# - 91 - 100점: 등급= "Outstanding"
#
# - 81 - 90점: 등급= "Exceeds Expectations"
#
# - 71 - 80점: 등급= "Acceptable"
#
# - 70점 이하: 등급= "Fail"

def grades (scores):
    if(scores > 90):
        return "Outstanding"
    if(scores > 80 and scores <= 90):
        return "Exceeds Expectations"
    if(scores > 70 and scores <= 80):
        return "Acceptable"
    if(scores < 70):
        return "Fail"



student_grades = {}

for name in student_scores:
    student_grades[name]= grades(student_scores[name])
v
print(student_grades)
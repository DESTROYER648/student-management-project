import math

import random


raw_Course_Codes = ("CHE201", "CHE203", "CHE201", "MAT201", "CHE203",)

Set_of_Raw_Course_Codes = set(raw_Course_Codes)

Sorted_List = sorted( Set_of_Raw_Course_Codes)



students = {
    "Idris": {"scores": {"CHE201": 85, "CHE203": 90, "MAT201": 78}},
    "Alex": {"scores": {"CHE201": 65, "CHE203": 72, "MAT201": 88}}
}



def calculate_stats(scores_dict):
    for name , data in scores_dict.items():
        scores = data["scores"]
        score_Value = scores.values()
        
        total = sum(score_Value)
        
        Length = len(score_Value)


        Average_Score = total / Length
       
        highest_score= max(scores.values())
        lowest_score = min(scores.values())
    return round(Average_Score, 2), highest_score, lowest_score




def random_bonus(student_disc):
    for name, data in student_disc.items():
        scores = data["scores"]
        courses = list(scores.keys())

        bonus_course = random.choice(courses)
        num = random.randint(1, 5)

        scores[bonus_course] += num

        # Clear, formatted feedback instead of raw print(scores)
        print(f" congrats Added +{num} bonus points to {name}'s {bonus_course} score!")
        


def index():
    print("\n -- Available Courses ---")
    for i,j  in enumerate(Sorted_List  , 1) :
        print(i, j)



index()

print()


random_bonus(students)
for Student_names,student_data in students.items():
    scores = student_data["scores"]
    average, highest, low = calculate_stats(students)

    print(f"\nSTUDENT: {Student_names.upper()}")
    for course,score in scores.items() :
        print(f"{course}: {score}")
    print(f"Average: {average}")
    print(f"highest: {highest}")
    print(f"lowest: {low}")
#Student become teacher starts
# student first
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

# student secomd
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

# student third
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


# Add your function below!
# function for calculating average
def average(numbers):
    total = sum(numbers)
    total = float(total) / float(len(numbers))
    return total


# function for calculating the students's average
def get_average(student):
    homework = average(student["homework"]) * 0.1
    quizzes = average(student["quizzes"]) * 0.3
    tests = average(student["tests"]) * 0.6

    avg = homework + quizzes + tests
    return avg

    # grading function


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

students=[lloyd,alice,tyler]
print get_letter_grade(get_average(lloyd))
print get_letter_grade(get_average(alice))
print get_letter_grade(get_average(tyler))


# class average function
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)


print "the average of class is %f"%(get_class_average(students))
print "the grade for class is %s" % (get_letter_grade(get_class_average(students)))
# Student become teacher ends
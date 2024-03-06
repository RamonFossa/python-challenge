import math

grades = [9, 8.5, 0.5, 10, 1, 4, 5, 6, 6.5, 3]

def calculate_average(sum, grades_length):
    return (sum / grades_length)

def calcuate_standard_deviation(sum, grades_length, grade, average):
    return math.sqrt((1/(grades_length-1)) * (sum) * ((grade - average) ** 2))

sum = 0
grades_length = len(grades)

for mGrade in grades: sum += mGrade

average = calculate_average(sum, grades_length)

standard_deviation_list = []

for mGrade in grades: standard_deviation_list.append(calcuate_standard_deviation(sum, grades_length, mGrade, average))

print('AVERAGE:')
print(average)
print('STANDART DEVIATION:')
print(standard_deviation_list)
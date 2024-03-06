import math

grades = [9, 8.5, 0.5, 10, 1, 4, 5, 6, 6.5, 3]

def calculate_average(sum, grades_length):
    return (sum / grades_length)

def calculate_standard_deviation(grades_length, standard_deviation_sum):
    return math.sqrt((1/(grades_length-1)) * standard_deviation_sum)

def calculate_standard_deviation_element(grade, average):
    return (grade - average) ** 2

sum = 0
grades_length = len(grades)

for mGrade in grades: sum += mGrade

average = calculate_average(sum, grades_length)

standard_deviation_sum = 0

for mGrade in grades: standard_deviation_sum += calculate_standard_deviation_element(mGrade, average)


standard_deviation = calculate_standard_deviation(grades_length, standard_deviation_sum)

print('AVERAGE:')
print(average)
print('STANDARD DEVIATION:')
print(standard_deviation)
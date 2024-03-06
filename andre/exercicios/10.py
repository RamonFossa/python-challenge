import math

def calcula_desvio_media(grades_list):
  total_grades = len(grades_list)
  sum = 0
  for grade in grades_list:
    sum += grade
  media = sum / total_grades
  values_minus_media = []
  for grade in grades_list:
    values_minus_media.append((grade - media) * (grade - media))
  sum_values = 0
  for value in values_minus_media:
    sum_values += value
  values__dived = sum_values / (total_grades - 1)
  desvio_padrao = math.sqrt(values__dived)

  return print(media, desvio_padrao)


    

grades = [9, 8.5, 0.5, 10, 1, 4, 5, 6, 6.5, 3]
calcula_desvio_media(grades)

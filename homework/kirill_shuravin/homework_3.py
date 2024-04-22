person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(person)


result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

result_1_final = int(result_1[result_1.index(':') + 2:]) + 10
result_2_final = int(result_2[result_2.index(':') + 2:]) + 10
result_3_final = int(result_3[result_3.index(':') + 2:]) + 10
print(result_1_final, result_2_final, result_3_final)


students = ['Ivanov', 'Petrov', 'Sidorov']
students_str = ', '.join(students)
subjects = ['math', 'biology', 'geography']
subjects_str = ', '.join(subjects)

my_text = f'Students {students_str} study these subjects: {subjects_str}'
print(my_text)

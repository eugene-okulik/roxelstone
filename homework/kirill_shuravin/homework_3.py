#1 Задача
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name = person[0]
last_name = person[1]
city = person[2]
phone = person[3]
country = person[4]


person_result = f"{name}, {last_name}, {city}, {phone}, {country}"
print(person_result)

#2 Задача
program_results = 'результат операции: 42 результат операции: 514 результат работы программы: 9'

results_string = program_results.split()

#Первый результат
first_result = program_results[20:22]

release_first_result = int(first_result) + 10

final_first_result = (release_first_result)
print(final_first_result)

#Второй результат
second_result = program_results[43:46]

release_second_result = int(second_result) + 10

final_second_result = (release_second_result)
print(final_second_result)

#Третий результат
third_result = program_results[-1:]

release_third_result = int(third_result) + 10

final_third_result = (release_third_result)
print(final_third_result)

#Задача 3
students = ['Ivanov', 'Petrov', 'Sidorov']
students_str = ', '.join(students)
print(students_str)
subjects = ['math', 'biology', 'geography']
subjects_str = ', '.join(subjects)

my_text = f'Students {students_str} study these subjects: {subjects_str}'
print(my_text)



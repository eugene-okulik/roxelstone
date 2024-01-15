my_dict = {'tuple': '', 'list': '', 'dict': '', 'set': ''}
my_dict['tuple'] = (12, 'massive', False, None, '34')
# print(my_dict['tuple'][ - 1]) ## Для Проверок!

my_dict['list'] = ['Donut', 'Soup', 'Car', 'Bread', 'Tomatoes']
my_dict['list'].append('Watermelon')
my_dict['list'].pop(1)
# print(my_dict['list']) ## Для Проверок!

my_dict['dict'] = {'time': '22', 'size': 'XS', 'trueOrNot': False, 'yesOrNot': None, 'age': '22'}
my_dict['dict'][('i am a tuple',)] = 'Inoske'
my_dict['dict'].pop('time')
# print(my_dict['dict']) ## Для Проверок!

my_dict['set'] = {'1', '2', False, 'Mom', 'Pudge', 2}
my_dict['set'].add('3')
my_dict['set'].remove('1')
# print(my_dict['set']) ## Для Проверок!


print(my_dict)

# Проверка типов
# print(type(my_dict)['tuple'])
# print(type(my_dict)['list'])
# print(type(my_dict)['dict'])
# print(type(my_dict)['set'])

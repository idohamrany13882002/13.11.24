# grades: dict[str, int] = {'moshe': 89, 'danny': 94, 'zeev': 55, 'maya': 75}
# print(grades['maya'])

personal: dict[str, object] = {'f_name': 'ido', 'l_name': 'hamrany', 'age': 22, 'smoker?': True,
                               'siblings': {'hagai': 26, 'mor': 21, 'tohar': 18},
                               'adress': {'city': ' rosh haayin', 'street': 'canfei nesharim', 'number': 6,
                                          'zip': 111111}}

print(personal.get('age'))
personal['smoker'] = False
personal.pop('l_name')

d1: dict[str, object] = {'a': '@', 'e': 3, 'i': '!', 'o': 0, 's': '$'}

for char in 'password':
    print(d1.get(char,char), end ='')
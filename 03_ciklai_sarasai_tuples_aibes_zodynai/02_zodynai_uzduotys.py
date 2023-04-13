"""
Pirma užduotis
Sukurkite žodyną su bent trimis augintinių vardais ir jų amžiumi.
Atspausdinkite visą žodyną.
"""
# augintiniai = {'coco': 10, 'meri': 2, 'beru': 99}
# print(augintiniai)

"""
Antra užduotis
Atspausdinkite kurio nors augintinio amžių.
"""
# augintiniai = {'coco': 10, 'meri': 2, 'beru': 99}
# print(augintiniai['coco'])

"""
Trečia užduotis
Pridėkite naują augintinį.
"""
# augintiniai = {'coco': 10, 'meri': 2, 'beru': 99}
# augintiniai['tiki'] = 3
# print(augintiniai)

"""
Ketvirta užduotis
Pakeiskite kurio nors augintinio amžių.
"""
# augintiniai = {'coco': 10, 'meri': 2, 'beru': 99}
# augintiniai['coco'] = 55
# print(augintiniai)

"""
Penkta užduotis
Ištrinkite kurį nors augintinį.
Atspausdinkite visą žodyną.
"""
# augintiniai = {'coco': 10, 'meri': 2, 'beru': 99}
# del augintiniai['coco']
# print(augintiniai)

"""
Šešta užduotis
Atspausdinkite visų augintinių vardus. 1+
Atspausdinkite visų augintinių amžius. 2+
Atspausdinkite visų augintinių vardų ir amžių sąrašą. 3+
Atspausdinkite konkretaus augintinio amžių pagal jo vardą. 4+
Pabandykite papildomai panaudoti kitus metodus. 5+
"""
augintiniai = {'coco': 10, 'meri': 2, 'beru': 99}

dict_keys = augintiniai.keys() # 1
print('1 uzd: ', dict_keys)

dict_values = augintiniai.values() # 2
print('2 uzd: ', dict_values)

dict_to_list = list(augintiniai.items()) #3
print('3 uzd: ', dict_to_list)

value_by_key = augintiniai['coco'] # 4
print('1 uzd: ', value_by_key)

get_method1 = augintiniai.get('karve') # 5a
get_method2 = augintiniai.get('beru') # 5b
augintiniai.clear() # 5c
print('5a uzd: ', get_method1)
print('5b uzd: ', get_method2)
print('5c uzd: ', augintiniai)

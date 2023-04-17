'''
Pirma užduotis
Sukurkite funkciją, kuri priima sąrašą ir grąžina naują sąrašą atvirkščia tvarka.
'''

# def funkcija_reverse(sarasas):
#     sarasas.reverse()  # butina pirmiausia ivykdyti procedura,
#     return sarasas  # o tik paskiau isvesti duomenis!

# some_list = [1, 2, 3]

# print(funkcija_reverse(some_list))


'''
Antra užduotis
Sukurkite funkciją, kuri apskaičiuoja trikampio plotą pagal kraštinių ilgius ir grąžina jį.
'''

# def triangle_area(a, b, c):
#     # calculate the semi-perimeter of the triangle
#     s = (a + b + c) / 2
#     # calculate the area using Heron's formula
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     return area

# # example usage
# a = 5
# b = 6
# c = 7
# area = triangle_area(a, b, c)
# print("The area of the triangle with sides {}, {}, and {} is {}".format(a, b, c, area))


'''
Trečia užduotis
Sukurkite funkciją, kuri iš sąrašo išrenka žodžius, kurie yra nurodyto ilgio ir grąžina sąrašą su tais žodžiais.
'''

# initial_list = ['vienas', 'du', 'trys', 'keturi', 'penki']
# returned_list = []

# def list_element_meter(some_list, word_len):
#     for some_word in some_list:
#         if len(some_word) == word_len:
#             returned_list.append(some_word)
#     return returned_list
    
# print(list_element_meter(initial_list, 6))



'''
Ketvirta užduotis
Sukurkite funkciją, kuri iš sąrašo išrenka didžiausią skaičių ir grąžina jį.
'''

# initial_list = [1, 2, 3, 4, 5]

# def big_number(some_list):
#     biggest_number = max(some_list)
#     return biggest_number

# print(big_number(initial_list))


'''
Penkta užduotis
Sukurti funkciją, kuri iš žodžių sąrašo išrenka žodžius, kurie prasideda nurodyta raide ir grąžina sąrašą su tais žodžiais.
'''

# initial_list = ['vienas', 'du', 'trys', 'keturi', 'penki', 'sesi', 'septyni']
# returned_list = []

# def list_element_meter(some_list, some_letter):
#     for some_word in some_list:
#         if some_word[0][0] == some_letter:
#             returned_list.append(some_word)
#     return returned_list

# print(list_element_meter(initial_list, 's'))


'''
Šešta užduotis
Sukurkite funkciją, kuri iš eilutės išrenka visus žodžius, kurių ilgis yra lyginis, ir grąžina sąrašą su tais žodžiais.
'''

# initial_list = ['vienas', 'du', 'trys', 'keturi', 'penki', 'sesi', 'septyni']
# returned_list = []

# def even_word_len(some_list):
#     for some_word in some_list:
#         if len(some_word) % 2 == 0:
#             returned_list.append(some_word)
#     return returned_list

# print(even_word_len(initial_list))

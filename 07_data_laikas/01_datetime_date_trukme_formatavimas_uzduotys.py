'''
Pirma užduotis
Parašykite programą, kuri pateiktų dabartinį laiką, bet tik minutes ir sekundes.
'''
# import datetime

# now = datetime.datetime.now().time()

# time_string = now.strftime('%H:%M:%S')

# print(time_string)


'''
Antra užduotis
Sukurkite funkciją, kuri priimtų gimimo datą kaip stringą (formatu "%Y-%m-%d") ir grąžintų, kiek dienų liko iki jūsų gimtadienio šiais metais
'''
# from datetime import datetime
# from datetime import date

# # dabar = date.today()
# # print("Dabar:", dabar)

# def kiek_liko(gimimo_data):
#     format_string = "%Y-%m-%d"
#     date_object = datetime.strptime(gimimo_data, format_string)
#     date1 = datetime.now()
#     date2 = date_object
#     # return  date1, date2
#     return  date1 - date2

# print(kiek_liko("1991-08-28"))

# import datetime

# def days_until_birthday(birthday_str):
#     # Convert the string to a date object
#     birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()
#     # Get today's date
#     today = datetime.date.today()
#     # Get the month and day of the birthday
#     bday_month = birthday.month
#     bday_day = birthday.day
#     # Get the year of the next birthday
#     next_bday_year = today.year
#     if (bday_month, bday_day) < (today.month, today.day):
#         next_bday_year += 1
#     next_birthday = datetime.date(next_bday_year, bday_month, bday_day)
#     # Calculate the number of days until the next birthday
#     days_until = (next_birthday - today).days
#     return days_until

# print(days_until_birthday('1991-08-28'))


'''
Trečia užduotis
Parašykite programą, kuri priimtų datą ir laiką stringo formatu (pavyzdžiui, "2023-05-21 15:30"), pridėtų prie to 48 valandas ir grąžintų naują datą ir laiką stringo formatu.
'''
# from datetime import timedelta
# from datetime import datetime

# def plius_dvi_paros(data_laikas):
#     format_string = "%Y-%m-%d %H:%M"
#     date_string = datetime.strptime(data_laikas, format_string)
#     return date_string - timedelta(hours=48)

#     # uz_penkiu_min = datetime.now() + timedelta(minutes=5)

# print(plius_dvi_paros("2023-05-21 15:30"))


'''
Ketvirta užduotis
Parašykite programą, kuri priimtų du laikotarpius kaip timestamp'us ir grąžintų laikotarpių skirtumą dienomis.
'''
# from datetime import datetime
# import time

# def laikotarpiu_skirtumas(laikotarpis1, laikotarpis2):
#      # Convert the string to a date object
#     dt_obj1 = datetime.strptime(laikotarpis1, "%Y-%m-%d").date()
#     dt_obj2 = datetime.strptime(laikotarpis2, "%Y-%m-%d").date()

#     timestamp1 = time.mktime(dt_obj1.timetuple())
#     timestamp2 = time.mktime(dt_obj2.timetuple())
#     return (timestamp1 - timestamp2) / 86400

# skirtumas = laikotarpiu_skirtumas("2000-8-8", "1991-8-8")
# print(skirtumas)


'''
💡 Penkta užduotis
Sukurkite funkciją, kuri priimtų datą kaip stringą (pavyzdžiui, "2023-06-01") ir grąžintų, kokia savaitės diena yra ta data (pavyzdžiui, "Pirmadienis", "Antradienis" ir tt.).
'''
from datetime import datetime
from datetime import timedelta

def laikotarpiu_skirtumas(datos_str):
     # Convert the string to a date object
    dt_obj1 = datetime.strptime(datos_str, "%Y-%m-%d").date()

    return dt_obj1.strftime("%A")

data_inputas = laikotarpiu_skirtumas("2000-8-8")
print(data_inputas)
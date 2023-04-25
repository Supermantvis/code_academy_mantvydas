import os.path

def json_i_saldytuva():
    # paleidus programą, jeigu randamas šaldytuvo json failas, jį nuskaityti ir užpildyti šaldytuvą jo turiniu
    pass


path = '04_funkcijos/testfile.json'

check_file = os.path.isfile(path)

print(check_file)

# output

# True
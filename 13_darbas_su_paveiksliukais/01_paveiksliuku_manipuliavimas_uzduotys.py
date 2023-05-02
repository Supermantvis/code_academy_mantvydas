'''
Paimkite nuotrauką, ją apkarpyti ir sumažinti taip, kad liktų graži maža kvadratinė ikonėlė 128x128.
Padarykite savo anksčiau sukurtą ikonėlę juodai baltą.
Ant savo portreto dešinėje viršuje uždėkite permatomą png logotipą kompanijos, kuri Jums patinka.
'''
from PIL import Image

background_img = Image.open("./13_darbas_su_paveiksliukais/dog_running.jpg")
foreground_img = Image.open("./13_darbas_su_paveiksliukais/logo.png")

modified_b_img1 = background_img.copy()
modified_f_img1 = foreground_img.copy()

new_logo_size = (modified_f_img1.size[0]//4, modified_f_img1.size[1]//4)
resized_logo = modified_f_img1.resize(new_logo_size)
bnw_logo = resized_logo.convert('L')

print(f"Background image:{modified_b_img1.size}")
print(f"Foreground image:{bnw_logo.size}")

position = ((modified_b_img1.size[0] - bnw_logo.size[0]), 5)  # same as: position = ((620 - 128), 5)

modified_b_img1.paste(bnw_logo, position, bnw_logo)
modified_b_img1.show()
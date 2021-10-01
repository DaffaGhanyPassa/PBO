class suku:
    def intro(self):
        print("indonesia mempunyai berbagai macam suku")

    def daerah(self):
        print("suku suku tersebut menetap diberbagai daerah")

class sunda(suku):
    def daerah(self):
        print("Orang Sunda, secara tradisional tinggal di provinsi Jawa Barat , Banten , Jakarta , dan bagian barat Jawa Tengah.")

class jawa(suku):
    def daerah(self):
        print("Orang Jawa, secara tradisional tinggal di provinsi Jawa Tengah, DIY, dan Jawa Timur.")

class lampung(suku):
    def daerah(self):
        print("Orang Lampung, secara tradisional tinggal di provinsi Lampung")

class Betawi(suku):
    def daerah(self):
        print("Suku Betawi adalah salah satu suku yang berada di kawasan DKI Jakarta")

class Madura(suku):
    def daerah(self):
        print("Suku Madura dikenal sebagai macam-macam suku di Indonesia yang menghuni kawasan Jawa Timur")

class Dayak(suku):
    def daerah(self):
        print("Suku Dayak dikenal sebagai suku bangsa yang berasal dari pedalaman pulau Kalimantan secara keseluruhan")

obj_suku = suku()
obj_sunda = sunda()
obj_jawa = jawa()
obj_lampung = lampung()
obj_Betawi = Betawi()
obj_Madura = Madura()
obj_Dayak = Dayak()

obj_suku.intro()
obj_suku.daerah()

print("\n")

obj_sunda.intro()
obj_sunda.daerah()

print("\n")

obj_jawa.intro()
obj_jawa.daerah()

print("\n")

obj_lampung.intro()
obj_lampung.daerah()

print("\n")

obj_Betawi.intro()
obj_Betawi.daerah()

print("\n")

obj_Madura.intro()
obj_Madura.daerah()

print("\n")

obj_Dayak.intro()
obj_Dayak.daerah()
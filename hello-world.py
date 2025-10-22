# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 18:47:34 2025

@author: User
"""

#print ("hello world!")
#print(6+9)

#xabar = "Assalomu alaykum"
#print(xabar)
#class ="6"
#print (class)

#radius=5     
#pi = 3.14159
#aylana_yuzi = pi * radius**2
#print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

#ism = 'Ahad'
#familiya = 'Qayum'
#print(ism +' '+ familiya)

#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor"
#viloyat="Samarqand"
#print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
     # tuman + " tumani, " + viloyat + " viloyati")
     
#print("Iltimos, quyidagi ma'lumotlarni kiriting:")
#kocha = input("Ko'changiz: ")
#mahalla = input("Mahallangiz: ")
#tuman = input("Tumaningiz: ")
#viloyat = input("Viloyatingiz: ")
#rint(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
 #     tuman + " tumani, " + viloyat + " viloyati")   
    
#manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
#print(manzil.upper())
#print(manzil.lower())
#print(manzil.title())
#print(manzil.capitalize())

#stalganson= int(input('istalgan sonni kiriting\n>>>'))
#rint(istalganson,  "ning kvadrati", istalganson**2 )
#rint(istalganson,  "ning kubi",  istalganson**3 )

#osh=int(input("Tug'ilgan yilingiz qachon?\n>>>"))
#rint("siz", 2025-yosh,"yosh ekansiz")
#006

#ismlar=['Umar',' Salohiddin',' Abdulloh']
#print("salom", ismlar[0], "bugun choyxona bormi?")
#print(ismlar[1],' choyxonaga boramizmi?')

#davlatlar=[ 'Ozbekiston', 'Turkiya', 'Niderlandiya','Iordaniya' ]
#print(sorted(davlatlar))
#print(len(davlatlar))
#print(sorted(davlatlar, reverse=True))
#davlatlar.reverse()
#print(davlatlar)
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)
#juftsonlar = list(range(120,1200,2))
#print(sum(juftsonlar))
#print(max(juftsonlar)-min(juftsonlar))
# print(len(juftsonlar))
# print(juftsonlar[:20])
# #print(juftsonlar[-20:])
# print(juftsonlar[230:250])

# taomlar = ['osh','somsa','norin','manti','dolma']
# print(taomlar)
# nonushta= taomlar[:]
# nonushta.remove('norin')
# nonushta.remove('manti')
# nonushta.remove('osh')
# nonushta.append('non va qaymoq')
# nonushta.append('avacado')
# print(nonushta)
# print(nonushta[2])
# nonushta=tuple(nonushta)
# nonushta[2]="quymoq"
# nonushta=(list)

# ismlar=['Ammor', 'Umar', 'Yosir' , 'Habbob', 'Hattot','Samul']
# for ism in ismlar:
#     print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")
# print(f"Kod {len(ismlar)} marta takrorlandi")

# kitoblar = []
# print("5 ta sevimli kitobingiz qaysilar?")
# for kitob in range(5):
#     kitoblar.append(input(f"{kitob+1}-kitob:"))
# print(kitoblar)  

# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(f'siz {ismlar} bilan suhbat qilibsiz)  

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# # for car in cars:
# #  if car == "gm":
# #     print(car.upper())
# #  else:
# #     print(car.title())
# for car in cars:
#    if car != "gm":
#     print(car.title())
#    else:
#     print(car.upper())
    
# son = float(input("Istalgan son kiriting:>>>\n"))
# print("Son manfiy") if son<0 else print("Son musbat")

# login = input("Login kiriting:>>>\n ")
# if login.lower() == 'mehriniso':
#   print("Xush kelibsiz Mehriniso, foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
# print(f"Xush kelibsiz {login.title()}!")

# dadam ={"ism":"Umidjon", "t_y":1978 , "t_j": "Guliston"}
# onam ={"ism":"Obida","t_y":1984 ,"t_j":"Guliston"}
# ukam ={"ism":"Kamoliddin", "t_y":2011 ,"t_j":"Guliston"}
 
# print(f'Dadamning ismi {dadam ["ism"]} {dadam["t_y"]} -yilda,\
#       {dadam["t_j"] }da tavallud topgan')
# print(f'Onamning ismi {onam ["ism"]} {onam["t_y"]} -yilda,\
#       {onam["t_j"] }da tavallud topgan')      
# print(f'Ukamning ismi {ukam ["ism"]} {ukam["t_y"]} -yilda,\
#       {ukam["t_j"] }da tavallud topgan')

# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# # print(python_izohli_lugati['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")

# 1-TOPSHIRIQ: Python izohli lug'ati

# print("--- PYTHON IZOHLI LUG'ATI ---")
# python_izohli_lugat = {
#     "list": "Ro'yxat. Elementlarni tartiblangan holda saqlaydi.",
#     "dict": "Lug'at. Kalit-qiymat juftliklarini saqlaydi.",
#     "tuple": "Opinchoq. O'zgarmas ro'yxat.",
#     "set": "To'plam. Takrorlanmas elementlardan iborat.",
#     "string": "Matn turi. Harflar ketma-ketligi.",
#     "integer": "Butun son turi.",
#     "float": "O'nli son turi.",
#     "print": "Konsolga ma'lumot chiqarish funksiyasi.",
#     "input": "Foydalanuvchidan ma'lumot olish funksiyasi.",
#     "for": "Takrorlash sikli. Ro'yxat yoki boshqa ketma-ketlik elementlari bo'ylab yuradi.",
#     "if": "Shartli operator. Agar ma'lum bir shart bajarilsa, kod blokini ishga tushiradi."
# }

# # Kalitlarni alifbo ketma-ketligida olib, konsolga chiroyli chiqarish
# print("\nKalitlar va ularning izohlari (alifbo ketma-ketligida):")
# # Lug'at kalitlarini tartiblab olish
# sorted_keys = sorted(python_izohli_lugat.keys())

# for kalit in sorted_keys:
#     print(f"- {kalit.title()}: {python_izohli_lugat[kalit]}")


# 2-TOPSHIRIQ: Davlatlar va poytaxtlari lug'ati

# print("\n--- DAVLATLAR VA POYTAXLAR ---")
# davlatlar_poytaxtlar = {
#     "O‘zbekiston": "Toshkent",
#     "Qozog‘iston": "Ostona",
#     "Rossiya": "Moskva",
#     "Qirg‘iziston": "Bishkek",
#     "Tojikiston": "Dushanba",
#     "Turkiya": "Anqara",
#     "Germaniya": "Berlin",
#     "Fransiya": "Parij",
#     "Buyuk Britaniya": "London",
#     "Italiya": "Rim"
# }

# # Davlatlarni alifbo ketma-ketligida chiqarish
# print("\nDavlatlar (alifbo ketma-ketligida):")
# sorted_davlatlar = sorted(davlatlar_poytaxtlar.keys())
# for davlat in sorted_davlatlar:
#     print(f"- {davlat}")

# # Poytaxtlarni alifbo ketma-ketligida chiqarish
# print("\nPoytaxtlar (alifbo ketma-ketligida):")
# sorted_poytaxtlar = sorted(davlatlar_poytaxtlar.values())
# for poytaxt in sorted_poytaxtlar:
#     print(f"- {poytaxt}")

# 3-TOPSHIRIQ: Foydalanuvchidan davlatni so'rash va poytaxtini chiqarish

# print("\n--- POYTAXTNI ANIQLASH ---")
# davlat_nomi = input("Istalgan davlat nomini kiriting: ")

# # Lug'atdan davlatni qidirish
# # .get() metodi kalit mavjud bo'lsa, qiymatini, mavjud bo'lmasa None qaytaradi.
# # Agar None bo'lsa, ikkinchi argumentdagi xabar ko'rsatiladi.
# poytaxt = davlatlar_poytaxtlar.get(davlat_nomi, "Bizda bunday ma'lumot yo'q")

# print(f"{davlat_nomi}: {poytaxt}")


# 4-TOPSHIRIQ: Restoran menusi

# print("\n--- RESTORAN MENYUSI ---")
# restoran_menyu = {
#     "Osh": 55000,
#     "Lag'mon": 45000,
#     "Shashlik (mol go'shti)": 60000,
#     "Shashlik (tovuq go'shti)": 50000,
#     "Manti": 30000,
#     "Somsa": 15000,
#     "Salat Olivier": 35000,
#     "Salat Grecheskiy": 40000,
#     "Chuchvara": 40000,
#     "Kompot": 10000,
#     "Choy": 5000
# }

# print("Menyu:")
# # Menuni ham alifbo ketma-ketligida chiqarish yaxshi
# sorted_taomlar = sorted(restoran_menyu.keys())
# for taom in sorted_taomlar:
#     narh = restoran_menyu[taom]
#     print(f"- {taom}: {narh} so'm")

# print("\nBuyurtma bering:")
# buyurtmalar = []
# umumiy_narh = 0

# for i in range(3):
#     ovqat = input(f"{i+1}-ovqat nomini kiriting: ")
#     # Buyurtmani lug'atda qidirish
#     if ovqat in restoran_menyu:
#         narh = restoran_menyu[ovqat]
#         buyurtmalar.append(ovqat)
#         umumiy_narh += narh
#         print(f"✅ '{ovqat}' qo'shildi. Narxi: {narh} so'm.")
#     else:
#         print(f"❌ Afsuski, '{ovqat}' nomli taom bizning menyuda yo'q.")

# print("\n--- BUYURTMANGIZ ---")
# if buyurtmalar:
#     print("Siz buyurtma qilgan taomlar:")
#     for buyurtma_taom in buyurtmalar:
#         print(f"- {buyurtma_taom} ({restoran_menyu[buyurtma_taom]} so'm)")
#     print(f"\nUmumiy summa: {umumiy_narh} so'm")
# else:
#     print("Siz hech qanday taom buyurtma qilmadingiz.")

# 1-TOPSHIRIQ: Adabiyot olamidagi 4 mashxur shaxs

# print("--- ADABIYOT OLAMIDAGI MASHXUR SHAXSLAR ---")

# shaxslar_malumotlari = [
#     {
#         "ism": "William Shakespeare",
#         "soha": "Adabiyot (Dramaturg)",
#         "mashxur_asarlar": ["Hamlet", "Romeo and Juliet", "Othello", "Macbeth", "King Lear"]
#     },
#     {
#         "ism": "Albert Einstein",
#         "soha": "Ilm-fan (Fizik)",
#         "mashxur_asarlar": ["Zurriyatga nisbatan umumiy nisbiylik nazariyasi", "Fotoelektrik effekt qonunlari", "Bronun harakatining molekulyar-kinetik nazariyasiga asos soldi"]
#     },
#     {
#         "ism": "Leonardo da Vinci",
#         "soha": "San'at (Rassom, ixtirochi)",
#         "mashxur_asarlar": ["Mona Lisa", "The Last Supper", "Vitruvian Man"]
#     },
#     {
#         "ism": "Tim Berners-Lee",
#         "soha": "Internet (Dasturchi, ixtirochi)",
#         "mashxur_asarlar": ["World Wide Web (WWW) asoschisi", "HTML", "URL", "HTTP protokoli"]
#     }
# ]

# # Har bir shaxs haqidagi ma'lumotni konsolga chiqarish
# print("\nHar bir shaxs haqidagi ma'lumotlar:")
# for shaxs in shaxslar_malumotlari:
#     print(f"\nIsm: {shaxs['ism']}")
#     print(f"Soha: {shaxs['soha']}")
#     print("Mashxur asarlari:")
#     # Muallifning ismini va asarlarini chiqarish
#     for asar in shaxs["mashxur_asarlar"]:
#         print(f"- {asar}")

# 2-TOPSHIRIQ: Oila a'zolari/do'stlar sevimli kino-seriallari

# print("\n--- SEVIMLI KINOLAR ---")
# do_stlar_kinolari = {}

# for i in range(3):
#     ism = input(f"{i+1}-do'stingiz ismini kiriting: ")
#     sevimli_kinolar = []
#     print(f"{ism}ning 3 ta sevimli kino/seriali nomini kiriting:")
#     for j in range(3):
#         kino = input(f"- {j+1}-kino/serial: ")
#         sevimli_kinolar.append(kino)
#     do_stlar_kinolari[ism] = sevimli_kinolar

# print("\nDo'stlaringizning sevimli kinolari:")
# for do_st_ism, kinolar_rohati in do_stlar_kinolari.items():
#     print(f"\n{do_st_ism.title()}ning sevimli kinolari:")
#     for kino in kinolar_rohati:
#         print(f"- {kino}")

# # 3-TOPSHIRIQ: Davlatlar haqida ma'lumotlar (NESTED DICTIONARIES)

# print("\n--- DAVLATLAR HAQIDA MA'LUMOTLAR ---")
# davlatlar_malumotlari = {
#     "O'zbekiston": {
#         "poytaxt": "Toshkent",
#         "aholi_soni": "36 million",
#         "til": "O'zbek tili",
#         "valyuta": "So'm"
#     },
#     "Qozog'iston": {
#         "poytaxt": "Ostona",
#         "aholi_soni": "19 million",
#         "til": "Qozoq tili",
#         "valyuta": "Tenge"
#     },
#     "Rossiya": {
#         "poytaxt": "Moskva",
#         "aholi_soni": "146 million",
#         "til": "Rus tili",
#         "valyuta": "Ruble"
#     },
#     "Germaniya": {
#         "poytaxt": "Berlin",
#         "aholi_soni": "84 million",
#         "til": "Nemis tili",
#         "valyuta": "Yevro"
#     }
# }

# # Foydalanuvchidan davlatni so'rash
# soralgan_davlat = input("Qaysi davlat haqida ma'lumot olmoqchisiz? ")

# # Davlatni lug'atdan qidirish va ma'lumotni chiqarish
# davlat_malumot = davlatlar_malumotlari.get(soralgan_davlat) # Agar topilmasa, None qaytaradi

# if davlat_malumot:
#     print(f"\n--- {soralgan_davlat} HAQIDA MA'LUMOT ---")
#     for kalit, qiymat in davlat_malumot.items():
#         print(f"{kalit.capitalize()}: {qiymat}")
# else:
#     print(f"Bizda '{soralgan_davlat}' haqida ma'lumot yo'q.")

# print("--- SEVIMLI KITOB NOMLARINI KIRITING (to'xtatish uchun 'stop' yozing) ---")
# sevimli_kitoblar = []

# while True:
#     kitob_nomi = input("Kitob nomini kiriting: ")
#     if kitob_nomi.lower() == "stop": # Foydalanuvchi 'stop' yozsa (katta-kichik harf farq qilmaydi)
#         break # Tsiklni to'xtatadi
#     else:
#         sevimli_kitoblar.append(kitob_nomi)

# print("\nSiz kiritgan sevmli kitoblar:")
# if sevimli_kitoblar:
#     for kitob in sevimli_kitoblar:
#         print(f"- {kitob}")
# else:
#     print("Siz hech qanday kitob kiritmadingiz.")

# print("\n--- MUZEY CHIPTA NARHI HISOBSI ---")

# while True:
#     yosh_input = input("Yoshingizni kiriting (chiqish uchun 'exit' yoki 'quit' yozing): ")

#     # Dasturni to'xtatish shartlari
#     if yosh_input.lower() == "exit" or yosh_input.lower() == "quit":
#         print("Dastur tugatildi.")
#         break # Tsikldan chiqish

#     # Yoshni butun songa aylantirishga urinish
#     try:
#         yosh = int(yosh_input)
#     except ValueError:
#         print("Noto'g'ri yosh kiritildi. Iltimos, raqam bilan yoki 'exit'/'quit' yozing.")
#         continue # Keyingi tsikl aylanishiga o'tish

#     # Chipta narhini aniqlash
#     if yosh < 7:
#         narh = "2000 so'm"
#     elif 7 <= yosh <= 18: # 7 dan katta va 18 gacha
#         narh = "3000 so'm"
#     elif 18 <= yosh < 65: # 18 dan katta va 65 gacha
#         narh = "10000 so'm"
#     else: # 65 dan katta
#         narh = "Bepul"

#     print(f"Siz uchun chipta narhi: {narh}")

# buyurtma=[]
# while True:
#     mahsulot=input("Mahsulot buyurtma qiling:")
#     buyurtma.append(mahsulot)
#     javob=input("Yana mahsulot qo'shasizmi(ha/yo'q)?")
#     if javob!='ha':
#         break

# print(f"buyurtma qabul qilindi. Siz buyurtma bergan mahasulotlar:{buyurtma}")    
    
# import datetime

# def tugilgan_yilini_hisobla():
#     """
#     Foydalanuvchidan ismini va yoshini so'rab, tug'ilgan yilini hisoblaydi va chiqaradi.
#     """
#     ism = input("Ismingizni kiriting: ")
    
#     while True: # Yoshni to'g'ri kiritish uchun tsikl
#         yosh_str = input(f"{ism}, yoshingizni kiriting: ")
#         try:
#             yosh = int(yosh_str) # Yoshni butun songa aylantirish
#             if yosh >= 0: # Yosh manfiy bo'lmasligi kerak
#                 break # Agar yosh to'g'ri kiritilsa, tsikldan chiq
#             else:
#                 print("Yosh manfiy bo'lishi mumkin emas. Iltimos, to'g'ri yosh kiriting.")
#         except ValueError:
#             print("Noto'g'ri format. Iltimos, yoshingizni raqamlar bilan kiriting.")

#     # Joriy yilni aniqlash
#     joriy_yil = datetime.datetime.now().year
    
#     # Tug'ilgan yilni hisoblash
#     tugilgan_yil = joriy_yil - yosh
    
#     print(f"\nXush kelibsiz, {ism}!")
#     print(f"Siz {tugilgan_yil} yilda tug'ilgansiz.")

# # Funksiyani chaqirish
# tugilgan_yilini_hisobla()

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
    
#     print(salom_ber.__doc__)

# 
# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)



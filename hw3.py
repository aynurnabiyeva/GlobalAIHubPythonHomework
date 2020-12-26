"""
Aynur Nebioğlu
nabiyevaa20@gmail.com
Homework-3

"""

import random
 
isim = input("Kullanıcı Adınızı Girin: ")
print("WELCOME", isim)
 
kelimeler = ['bilgisayar', 'sınav', 'aşk', 'sudoku', 
         'python', 'fare', 'saksı', 'konferans', 
         'akıl', 'ıslık', 'sakız'] 

kelime = random.choice(kelimeler)
print("Harf tahmini")
 
tahminler = ''
cevir = 10
 
while cevir > 0:
     
    failed = 0
     
    for char in kelime: 
         
      if char in tahminler: 
            print(char)
             
    else: 
            print("_")
             
    failed += 1
             
    if failed == 0:
    
        print("KAZANDINIZ!!!") 
        print("KELİME: ", kelime) 
        break
     
    tahmin= input("Bir harf tahmin ediniz: ")
      
    tahminler += tahmin 
    if tahmin not in kelime:
         
        cevir -= 1 
        print("YANLIŞ!!!")
        print("Kalan tahmin sayısı: ", + cevir,)
         
    if cevir == 0:
         print("KAYBETTİNİZ!")
"""
Aynur Nebioğlu
nabiyevaa20@gmail.com
Final Project

"""

count = 0
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
girilen_ad = input("Girilen Ad: ")
girilen_soyad = input("Girilen Soyad: ")

while count < 3:

     if girilen_ad == ad and girilen_soyad == soyad:
        print("WELCOME",girilen_ad,girilen_soyad)
     else:
          for i in range(2):
               count += 1
               print("Please try again later")
               girilen_ad = input("Girilen Ad: ")
               girilen_soyad = input("Girilen Soyad: ")
          break

     dersler = ["OOP", "Computer Architecture", "Data Structures","Numerical Analysis", "Operating Systems"]
     dersler_input = input("\nAlmak isyediğiniz dersleri seçiniz: ")
     ders_list = list(dersler_input.split(","))

     if len(ders_list) >= 3 and len(ders_list) <= 5:
     
          for i in ders_list:
               if i not in dersler:
                    print(f"Sistemde {i} isimli ders bulunmamaktadır!")
               
          ders = input("Aldığınız notu görmek için ilgili dersi girin: ")
          if ders in ders_list:
               notlar = {"Midterm":0,"Final":0,"Project":0}
               midterm = int(input("\nMidterm(arasınav) notunuzu giriniz: "))
               notlar["Midterm"] = midterm
               final = int(input("Final notunuzu giriniz: "))
               notlar["Final"] = final
               project = int(input("Project(proje) notunuzu giriniz: "))
               notlar["Project"] = project
               sonuc_not = midterm * 0.3 + final * 0.5 + project * 0.2

               if sonuc_not >= 90:
                    print("\n{} notunuz AA, geçtiniz".format(ders))
               elif sonuc_not >= 70 and sonuc_not < 90:
                    print("\n{} notunuz BB, geçtiniz".format(ders))
               elif sonuc_not >= 50 and sonuc_not < 70:
                    print("\n{} notunuz CC, geçtiniz".format(ders))
               elif sonuc_not >= 30 and sonuc_not < 50:
                    print("\n{} notunuz DD, geçtiniz".format(ders))
               else:
                    print("\n{} notunuz FF, kaldınız".format(ders))
          
          elif ders not in ders_list and ders in dersler:
               print(f"\n {ders} alamazsınız!")
          else:
               print(f"\nÖğrenci yönetim sisteminde {ders} isimli ders bulunmamaktadır")  
     else:
          print("\nEn az 3 ve en fazla 5 ders almalısınız.Sınıfta kaldınız!")
     break




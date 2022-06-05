def alternatifMalzemeOner():
  from matplotlib import pyplot as plt
  malzemeListesi=" " #while döngüsünde kullanılacak string boş olarak ilklendirilir
  #kullanıcının girdiği malzemeleri stringe atar ve kullanıcı enter tuşuna basınca döngüden çıkar
  while True:
   malzeme=input("Malzemeyi giriniz: ")
   malzemeListesi+=" "
   malzeme=malzeme.upper()
   malzemeListesi+=malzeme
   if not malzeme:
     break
  #malzemeListesindeki tüm kelimeleri teker teker kontrol edip gerekli önerileri yapar
  for i in malzemeListesi.split():
      if i=="ŞEKER":
          # ekrana öneri besinler bastırılır
          print("*Şeker yerine esmer şeker / bal / muz / tarçın / vanilya ya da hurma kullanabilirsiniz.")
          #bar grafiğindeki sütunların sırasıyla x ekseni değeri,y ekseni değeri,renk bilgisi verilir
          plt.bar(["şeker"], [387], color="#B21230", label="en yüksek:şeker")
          plt.bar(["esmer şeker"], [377], color="#D99197")
          plt.bar(["bal"], [304], color="#CDEBFF")
          plt.bar(["muz"], [89], color="#4FB99F", label="en düşük:muz")
          plt.bar(["tarçın"], [261], color="#6EB2C4")
          plt.bar(["vanilya"], [288], color="#D4FFE3")
          plt.bar(["hurma"], [282],color="#D5ADA6")
          plt.legend()#label etiketiyle verilen bilgileri grafiğin üstüne bastırır
          plt.xlabel('Besinler')#x eksenine isim verilir
          plt.ylabel('Kalori(cal)') #y eksenine isim verilir
          plt.title('Şeker ve türevleri karşılaştırma')# grafiğe isim verilir
          plt.show()#grafik ekrana bastırılır

      elif i == "UN":
          print("*Beyaz un yerine yulaf unu / kepekli un / tam buğday unu ya da çavdar unu kullanabilirsiniz.")
          plt.bar(["beyaz un"], [364], color="#B21230", label="en yüksek:beyaz un")
          plt.bar(["yulaf"], [357], color="#D99197")
          plt.bar(["çavdar"], [322], color="#4FB99F", label="en düşük:çavdar unu")
          plt.bar(["tam buğday"], [329], color="#CDEBFF")
          plt.bar(["kepek"], [340], color="#6EB2C4")
          plt.legend()
          plt.xlabel('Besinler')
          plt.ylabel('Kalori(cal)')
          plt.title('Un ve türevleri karşılaştırma')
          plt.show()

      elif i == "SIVIYAĞ":
          print("*Sıvıyağ yerine zeytinyağı ya da tereyağı kullanabilirsiniz.")
          plt.bar(["sıvıyağ"], [844], color="#B21230", label="en yüksek:sıvıyağ")
          plt.bar(["zeytinyağı"], [830], color="#CDEBFF")
          plt.bar(["tereyağ"], [717], color="#4FB99F", label="en düşük:tereyağı")
          plt.legend()
          plt.xlabel('Besinler')
          plt.ylabel('Kalori(cal)')
          plt.title('Yağ ve türevleri karşılaştırma')
          plt.show()

      elif i == "TUZ":
          print("*Sofra tuzu yerine himalaya tuzu / sofra tuzu / kaya tuzu kullanabilirsiniz.")

      elif i == "TAVUK":
          print("*Tavuk yerine hindi / kaz ya da ördek kullanabilirsiniz.")
          plt.bar(["tavuk"], [215], color="#B21230", label="en yüksek:tavuk")
          plt.bar(["ördek"], [132], color="#D99197")
          plt.bar(["kaz"], [161], color="#CDEBFF")
          plt.bar(["hindi"], [119], color="#4FB99F", label="en düşük:hindi")
          plt.legend()
          plt.xlabel('Besinler')
          plt.ylabel('Kalori(cal)')
          plt.title('Tavuk ve türevleri karşılaştırma')
          plt.show()

      elif i == "SÜT":
          print("*Süt yerine light süt / laktozsuz süt / keçi sütü ya da badem sütü kullanabilirsiniz.")
          plt.bar(["beyaz süt"], [62], color="#B21230", label="en yüksek:beyaz süt")
          plt.bar(["light süt"], [34], color="#D99197")
          plt.bar(["laktozsuz süt"], [44], color="#CDEBFF")
          plt.bar(["keçi sütü"], [57], color="#6EB2C4")
          plt.bar(["badem sütü"], [22], color="#4FB99F", label="en düşük:badem sütü")
          plt.legend()
          plt.xlabel('Besinler')
          plt.ylabel('Kalori(cal)')
          plt.title('Süt ve türevleri karşılaştırma')
          plt.show()
      elif i == "DANA":
          print("*Dana eti yerine koyun eti ya da keçi eti kullanabilirsiniz." )
          plt.bar(["Dana eti"], [229], color="#B21230", label="en yüksek:dana eti")
          plt.bar(["Koyun eti"], [220], color="#CDEBFF")
          plt.bar(["Keçi eti"], [109], color="#4FB99F", label="en düşük:keçi eti")
          plt.legend()
          plt.xlabel('Besinler')
          plt.ylabel('Kalori(cal)')
          plt.title('Et ve türevleri karşılaştırma')
          plt.show()

alternatifMalzemeOner()#fonksiyon çağırımı

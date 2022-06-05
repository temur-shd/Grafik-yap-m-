"""pasta grafiklerini ekrana bastıran kod parçası"""
#gerekli kütüphaneler projeye eklendi
import matplotlib.pyplot as plt
import pandas as pd
#besin_degerleri.csv dosyası DataFrame olarak okunur
besin=pd.read_csv('besin_degerleri.csv',names=['besin','protein','karbonhidrat','yag','kalori'])
#for döngüsünde kullanılacak ve indeks bilgisini tutan count değişkeni ilklendirildi
count=0
#besin dosyası içinde gezinerek pasta grafiklerini ekrana basar
for i in besin.besin:
    #dilimlerin yüzdeliklerinin hesaplanması için dosyadan değerleri okutuldu.
    dilimler = [besin.protein.iloc[count],besin.karbonhidrat.iloc[count],besin.yag.iloc[count],besin.kalori.iloc[count]]
    count += 1 #indeks değerini 1 artırdır
    besin_degerleri = ['karbonhidrat', 'protein', 'yag', 'kalori']#dilimlerin isimleri verildi
    renkler = ['g', 'c', 'y', 'r']#dilim renkleri seçildi
    plt.pie(dilimler,
            labels=besin_degerleri,
            colors=renkler,
            startangle=90,
            shadow=True,
            explode=(0, 0.1, 0, 0),
            autopct='%1.1f%%')

    plt.title(i)#grafiğin adı verildi
    plt.show()#grafik ekrana bastırıldı


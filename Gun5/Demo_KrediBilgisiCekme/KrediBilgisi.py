#paketleri import ettik.
import numpy as np
import pandas as pd

#urli okuyalım
df = pd.read_html("https://www.bddk.org.tr/BultenHaftalik/"
                 ,decimal=","
                 ,converters={
                                "TP":lambda tp: tp.replace(".","").replace(",","."),
                                "YP":lambda tp: tp.replace(".","").replace(",",".")
                 })


#3. sıradaki html tabloyu aldık.
dff = df[3].copy()

#re kütüphanesi ile kolondan geçerli tarihi aldık.
import re
tarih = re.findall(r"\d{1,2}\s\w+\s\d{4}",dff.columns[1])[0]

#belirlediğimiz kolonarı seçiyoruz.
dff = dff.iloc[:,1:4].copy()

#kolon adlarını düzenledik.
dff.columns = ["Krediler","TP","YP"]

#veri tipleri değiştirdik.
dff = dff.astype({
            "TP":np.float64,
            "YP":np.float64
})


#excele tarihle aynı isimde bir sayfaya sonuçları basıyoruz.
dff.to_excel("Krediler.xlsx",sheet_name=tarih,index=False)
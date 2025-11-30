Specification Heading
=====================
Created by pc on 9.04.2025

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

     
Search > Kategoriler tabına basılır, Arama alanına basılır, açıldığının kontrolü. Çarpıya basılır, kapandığının kontrolü.
-----
tags:Android_Kategoriler_AramaAlani_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Anasayfa_Search_Input_Areaa"
* Elementine tıkla "Anasayfa_Search_Close_Button"
//Kategoriler > Kategoriler tabına basılır, Kategoriler ve Markalar sekmelerinin olduğu sayfanın açıldığının kontrolü
* Element var mı kontrol et "Close_Scenario_Control_Makyaj"
* Element var mı kontrol et "Close_Scenario_Control_Kategoriler_Tab_Menu"

Kategoriler > Kategoriler başlığına basılır(Makyaj), sağ tarafta alt başlıkların açıldığının kontrolü
-----
tags:Android_Kategoriler_Makyaj_Alt_Baslik_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Makyaj_List_Button"
* Element var mı kontrol et "Kategoriler_Makyaj_Alt_List_Control1"
* Element var mı kontrol et "Kategoriler_Makyaj_Alt_List_Control2"

Kategoriler > Alt Kategori başlıkları aşağı/yukarı kaydırılmasının kontrolü.
-------
tags:Android_Kategoriler_AltBasliklar_Slide_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
//* "840","2063" coordinatından "838","692" coordinatına "1" kere swipe et
* "1" kere aşağıya kaydır
* "1" saniye bekle
* Element var mı kontrol et "Kategoriler_Makyaj_Alt_List_Control3"

Kategoriler > Alt Kategori başlığına basılır(Dudak Makyajı), Alt başlıkların(Ruj) aşağıya doğru açıldığının kontrolü
------
tags:Android_Kategoriler_AltBasliklar_DudakMakyaji_Ruj_Liste_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Alt_List_Dudak_Makyaji_Button"
* Element var mı kontrol et "Kategoriler_Alt_List_Dudak_Makyaji_Alt_Baslık_LikitRuj_Control"
//Kategoriler > Açık olan Alt Kategori başlığına basılır(Dudak Makyajı), Alt başlıkların(Ruj) kapandığının kontrolü
* Elementine tıkla "Kategoriler_Alt_List_Dudak_Makyaji_Button"
* "Kategoriler_Alt_List_Dudak_Makyaji_Alt_Baslık_LikitRuj_Control" li element sayfada görünüyorsa hata ver

Kategoriler > Alt başlığa(Ruj) basılır, ürünlerin listelendiğinin kontrolü
-----
tags:Android_Kategoriler_AltBasliklar_Liste_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Alt_List_Dudak_Makyaji_Button"
* Elementine tıkla "Kategoriler_Alt_List_Ruj_button"
* Element var mı kontrol et "Kategoriler_Alt_List_Ruj_Page_Control"
* Element var mı kontrol et "Kategoriler_Alt_List_Ruj_Product_Control"

Kategoriler > Alt başlığa(Ruj) altında Tüm ürünleri göster seçeneğine basılır, ürünlerin listelendiğinin kontrolü
-----
tags:Android_Kategoriler_AltBasliklar_Ruj_Tum_Urunleri_Goster

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Alt_List_Dudak_Makyaji_Button"
* Elementine tıkla "Kategoriler_Alt_List_Tum_Urunleri_Goster"
* Element var mı kontrol et "Kategoriler_Alt_List_Ruj_Product_Control"

Kategoriler > Alt Kategori başlığı(Dudak Makyajı) açıkken, başka alt kategori başlığına(Göz makyajı) seçeneğine basılır, açık olan başlığın kapandığı, yeni seçilen başlığın açıldığının kontrolü
-----
tags:Android_Kategoriler_AltBasliklar_Liste_Gezinme_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Alt_List_Dudak_Makyaji_Button"
* Element var mı kontrol et "Kategoriler_Alt_List_Dudak_Makyaji_Alt_Baslık_LikitRuj_Control"
* Elementine tıkla "Kategoriler_Alt_List_Goz_Makyajı_Button"
* "Kategoriler_Alt_List_Dudak_Makyaji_Alt_Baslık_LikitRuj_Control" li element sayfada görünüyorsa hata ver
* Element var mı kontrol et "Kategoriler_Alt_List_Goz_Makyajı_Alt_List_Maskara_Control"

Kategoriler > Alt Kategori başlığına(Makyaj fırçaları) basılır, ürünlerin listelendiğinin kontrolü
---
tags:Android_Kategoriler_AltBasliklar_MakyajFircalari_Liste_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Alt_List_Makyaj_Fırcaları_Button"
* Element var mı kontrol et "Kategoriler_Alt_List_Makyaj_Fırcaları_Page_Control"
* Element var mı kontrol et "Kategoriler_Alt_List_Makyaj_Fırcaları_Product_Control"


Detay > Search > Arama alanına basılır, açıldığının kontrolü. Çarpıya basılır, kapandığının kontrolü.
-----
tags:Android_Kategoriler_SearchAlani_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir

Markalar > Kategoriler tabına basılır, Kategoriler ve Markalar sekmelerinin olduğu sayfanın açıldığının kontrolü
-----
tags:Android_Kategoriler_Markalar_KategoriMarka_Sekme_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Element var mı kontrol et "Kategoriler_Menu_Tab_Control"
* Element var mı kontrol et "Kategoriler_Menu_Tab_Control_Markalar"

Markalar > Markalar sekmesine basılır, sekmenin açıldığının kontrolü
-------
tags:Android_Kategoriler_Markalar_Sekme_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Menu_Tab_Control_Markalar"
* Element var mı kontrol et "Kategoriler_Menu_Markalar_Sadece_Gratis_Control"
* Element var mı kontrol et "Kategoriler_Marka_Activex_Button"

Markalar > Sadece gratis'te altında markaya basılır, ürünlerin listelendiğinin kontrolü
-----
tags:Android_Kategoriler_Markalar_SadeceGratis_UrunListe_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Menu_Tab_Control_Markalar"
* Elementine tıkla "Kategoriler_Marka_Activex_Button"
* Element var mı kontrol et "Kategoriler_Marka_Activex_Button"

Markalar > Sadece gratis'te altında daha fazla göster seçeneğine basılır, diğer markaların geldiğinin kontrolü - sor
-----
tags:Android_Kategoriler_Markalar_SadeceGratis_DahaFazlaGoster_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Menu_Tab_Control_Markalar"
* Elementine tıkla "Kategoriler_Marka_Daha_Fazla_Goster_Button"
* Element var mı kontrol et "Kategoriler_Marka_Daha_Fazla_Goster_Button_Marka_Control"
 Orta düzeyde "5" swipe yap
* Elementine tıkla "Kategoriler_Marka_Daha_Az_Goster_Button"
 "2" kere yukarı doğru kaydır
//* "838","765" coordinatından "842","2275" coordinatına "1" kere swipe et
* Element var mı kontrol et "Kategoriler_Marka_Daha_Fazla_Goster_Button"

Markalar > Sayfa aşağı/tukarı kaydırılır, markaya tıklanır, ürünlerin listelendiğinin kontrolü
------
tags:Android_Kategoriler_Markalar_KaydirmaUrunListe_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Menu_Tab_Control_Markalar"
//* "540","1900" coordinatından "540","600" coordinatına "1" kere swipe et
//* "540","600" coordinatından "540","1900" coordinatına "1" kere swipe et
* "Kategoriler_Marka_Activex_Button" li elementi bulana kadar swipe et
* "2" saniye bekle
* Elementine tıkla "Kategoriler_Marka_Activex_Button"
* Element var mı kontrol et "Kategoriler_Marka_Activex_Urun_Control"

Markalar > Sayfa aşağı/tukarı kaydırılır, harfe tıklanır, harf sırasına gittiğinin kontrolü
-----
tags:Android_Kategoriler_Markalar_HarfSirasi_Kaydirma_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Elementine tıkla "Anasayfa_Kategoriler_Tab_Menu_Button"
* Elementine tıkla "Kategoriler_Menu_Tab_Control_Markalar"
* "3" kere aşağıya kaydır
* Elementine tıkla "Kategoriler_Marka_Harf_List_Button"
//hata

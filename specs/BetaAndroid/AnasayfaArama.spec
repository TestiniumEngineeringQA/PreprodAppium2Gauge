# Specification Heading
Created by pc on 26.03.2025

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

## Anasayfa > Search Textbox placeholder kontrolü => "Gratis'te Ara"

tags: Android_AnasayfaArama_Search_Gratiste_Ara

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Element var mı kontrol et "Anasayfa_Gratiste_Ara_Search_Box"

## Anasayfa > Search Textbox Barkod_Okuyucu_Sayfa_Kontrol

tags: Android_AnasayfaArama_Search_Barkod

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Element var mı kontrol et "Anasayfa_Gratiste_Ara_Search_Box"
* Elementine tıkla "Barkod_Okuyucu_Pic_Video_İzin"
* "locationPermissionBtnAnd" li element varsa tıkla yoksa devam et
* Element var mı kontrol et "Barkod_Okuyucu_Sayfa_Kontrol"

## Anasayfa > Kullanıcı login ise text kontrolü => "Merhaba, Yusuf"

tags: Android_AnasayfaArama_Kullanici_Login_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır 2
* Element var mı kontrol et "KUllanıcı_Gırısı_Kullanıcı_Username_Control"
* Element var mı kontrol et "KUllanıcı_Gırısı_Merhaba_Control"

## Anasayfa > İlk slider altındaki aktif slider sayfa kontrolü

tags: Android_AnasayfaArama_Ilk_Slider_Altindaki_Slider_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Element var mı kontrol et "Anasayfa_Gratiste_Ara_Search_Box"
* "750","827" coordinatından "150","827" coordinatına "1" kere swipe et
* Element var mı kontrol et "Anasayfa_Ilk_Slider_Ikıncı_Banner_Control"
//* Elementine tıkla "Anasayfa_First_Slider_SecondChoice"
* "2" saniye bekle
//* Element var mı kontrol et "First_Pro_Control_Tab"

## Ürün Kategorileri > Slider kontrolü

tags: Android_AnasayfaArama_Urun_Kategori_Slider_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
 "886","1345" coordinatından "104","1345" coordinatına "2" kere swipe et
* "Kategori_Slider_Sac_Bakim_Banner_Control" li elementi bulana kadar swipe et
 "2" kere aşağıya kaydır
* "Kategori_Slider_Sac_Bakim_Banner_Control" elementinin hizasından sağdan sola "2" kere kaydır 2
* Element var mı kontrol et "Kategori_Slider_Anne_Bebek_Banner_Control"

## Ürün Kategorileri > Kategoriye tıklandığında ilgili ürünlerin listelenmesi

tags: Android_AnasayfaArama_Kategori_Urun_Listelenmesi_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* "Kategori_Cilt_Bakım_Banner_Button" li elementi bulana kadar swipe et
* Elementine tıkla "Kategori_Cilt_Bakım_Banner_Button"
* Element var mı kontrol et "Kategori_Cilt_Bakım_Banner_Button"
//* Elementine tıkla "Kategori_Cilt_Bakım_Show_All_Button"
* Element var mı kontrol et "Kategori_Cilt_Urun_Card_Control"

## Kampayalar > "Tüm Kampanyalar", "Süper İndirimler", "Fiyatları Tek Ürünler" tablarının kontrolü

tags: Android_AnasayfaArama_Kampanya_Tab_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
 "240","1628" coordinatından "280","718" coordinatına "3" kere swipe et
 "2" kere aşağıya kaydır
* "Kategori_Tab_Tum_Kampanyalar_Control" li elementi bulana kadar swipe et
* Element var mı kontrol et "Kategori_Tab_Tum_Kampanyalar_Control"
* "Kategori_Tab_Anne_Bebek_Tab_Control" elementinin hizasından sağdan sola "2" kere kaydır 2
* Element var mı kontrol et "Kategori_Tab_Yeni_Gelenler_Control"

## Kampanyalar > Slider Kontrolü

tags: Android_AnasayfaArama_Kampanya_Slider_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* "2" kere aşağıya kaydır
 "240","1628" coordinatından "280","718" coordinatına "3" kere swipe et
* Element var mı kontrol et "Kategori_Tab_Tum_Kampanyalar_Control"
* Element var mı kontrol et "Kategori_Tab_Anne_Bebek_Tab_Control"
* "Kategori_Tab_Anne_Bebek_Tab_Control" elementinin hizasından sağdan sola "3" kere kaydır 2
* Element var mı kontrol et "Kategori_Tab_Yeni_Gelenler_Control"
* Elementine tıkla "Kategori_Tab_Yeni_Gelenler_Control"
* Element var mı kontrol et "Kategori_Tab_Yeni_Gelenler_Aktif_Slider_Control"

## Kampanyalar > Slider altındaki aktif slider sayfa kontrolü

tags: Android_AnasayfaArama_Kampanya_SliderAltindaki_AktifSlider_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
 "2" kere aşağıya kaydır
* "Kategori_Tab_Tum_Kampanyalar_Control" li elementi bulana kadar swipe et
 "240","1628" coordinatından "280","718" coordinatına "4" kere swipe et
* Element var mı kontrol et "Kategori_Tab_Tum_Kampanyalar_Control"
* Element var mı kontrol et "Kategori_Tab_Anne_Bebek_Tab_Control"
* Elementine tıkla "Kategori_Tab_Anne_Bebek_Tab_Control"
* "Kategori_Tab_Anne_Bebek_Tab_Control" elementinin hizasından sağdan sola "1" kere kaydır 2
* Elementine tıkla "Kategori_Tab_Super_Indirimler_Tab"
//* "1" kere aşağıya kaydır
* "Kategori_Tab_Super_Indırımler_Aktif_Slider_Control" li elementleri "text" attribute bul ve ekrana yazdır
//* Element var mı kontrol et "Kategori_Tab_Super_Indırımler_Aktif_Slider_Control"

## Sadece Gratis'te > Sadece Gratis'te bulunan markaların listelenmesi kontrolü

tags: Android_AnasayfaArama_SadeceGratiste_MarkaListe_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* "Kategoriler_Marka_Activex_Button" li elementi bulana kadar swipe et
 "240","1628" coordinatından "280","718" coordinatına "5" kere swipe et
* Element var mı kontrol et "Kategoriler_Marka_Activex_Button"


## Sadece Gratis'te > Slider kontrolü

tags: Android_AnasayfaArama_SadeceGratiste_Slider_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
 "240","1628" coordinatından "280","718" coordinatına "5" kere swipe et
* "Kategoriler_Marka_Activex_Button" li elementi bulana kadar swipe et
* Element var mı kontrol et "Kategoriler_Marka_Activex_Button"
* "Sadece_Gratiste_Marka_Slider_Item" elementinin hizasından sağdan sola "2" kere kaydır 2
* "Sadece_Gratiste_Marka_Benri_Control" li element sayfada görünüyorsa hata ver
//* Elementine tıkla "Sadece_Gratiste_Marka_Slider_Item_Wednwild"
//* Element var mı kontrol et "Sadece_Gratiste_Marka_Slider_Item_Wednwild_Liste_Control"

## Gratis Beauty Banner > Gratis Beauty Banner alanı kontrolü

tags: Android_AnasayfaArama_GratisBeautyBanner_Banner_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* "240","1628" coordinatından "280","718" coordinatına "8" kere swipe et
* Element var mı kontrol et "Beauty_Banner_Text_Control"

## Gratis Beauty Banner > "Randevu Al" butonu kontorlü

tags: Android_AnasayfaArama_GratisBeautyBanner_RandevuAl_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
 "240","1628" coordinatından "280","718" coordinatına "8" kere swipe et
* "Beauty_Banner_Text_Control" li elementi bulana kadar swipe et
* Element var mı kontrol et "Beauty_Banner_Text_Control"
* Elementine tıkla "Beauty_Banner_Randevu_Al_Button"
* "Cookie_Accept" li element varsa tıkla
//cookie
* Element var mı kontrol et "Beauty_Banner_Randevu_Al_Liste_Sepet_Control"
* "2" saniye bekle
* Elementine tıkla "Beauty_Banner_Randevu_Al_Page_Randevu_Al_Buton"
//* Elementine tıkla "Beauty_Banner_Randevu_Al_Page_Kategori_Sec"
//* Elementine tıkla "Beauty_Banner_Randevu_Al_Page_Rez_Ekle_Buton"
//* Element var mı kontrol et "Beauty_Banner_Randevu_Al_Page_Rez_Ekle_Basarılı_Mesaj"
//lokasyon, zaman



## Arama > Arama sonuçlarının "ÖNERİLEN ARAMALAR" title altında gösterilmesi

tags: Android_AnasayfaArama_AramaSonuclari_OnerilenAramalarAlti_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir

## Arama > Arama sonuçlarının "ÖNERİLEN Markalar" title altında gösterilmesi

tags: Android_AnasayfaArama_AramaSonuclari_OnerilenMarkalarAlti_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir

## Arama > Arama sonuçlarının "ÖNERİLEN KAtegoriler" title altında gösterilmesi

tags: Android_AnasayfaArama_AramaSonuclari_OnerilenKategorilerAlti_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir

## Arama > Ürün isminin yazılıp aranması, sonuçların listelenmesi ve sonuca tıklanıp ürünleri görme

tags: Android_AnasayfaArama_AramaSonuclari_UrunIsmiListeleme_UrunGorme

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Sayfada "fön suyu" arama yapılır
//* Android Enter tıkla
//* Element var mı kontrol et "Search_Page_First_Product_Control"
* Elementine tıkla "Search_Page_First_Product_Control"
* Element var mı kontrol et "Product_Page_Product_Name_Pastel_Control"
* "Product_Page_Product_Name_Morfose_Control" li elementleri bul ve ekrana yazdır

## Arama > Marka isminin yazılıp aranması, sonuçların listelenmesi ve sonuca tıklanıp ürünleri görme

tags: Android_AnasayfaArama_AramaSonuclari_MarkaIsmiListeleme_UrunGorme

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir

* Arama alanından "makyaj" isimli ürün aratılır

* Element var mı kontrol et "Search_Page_First_Product_Control"
* Elementine tıkla "Search_Page_First_Product_Control"
* "Product_Detail_Brand_Name" li elementleri bul ve ekrana yazdır
* Element var mı kontrol et "Product_Detail_Brand_Name"

## Arama > Kategori isminin yazılıp aranması, sonuçların listelenmesi ve sonuca tıklanıp ürünleri görme

tags: Android_AnasayfaArama_AramaSonuclari_KategoriIsmiListeleme_UrunGorme

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Arama alanından "makyaj" isimli ürün aratılır
* Element var mı kontrol et "Search_Page_First_Product_Control"
* Elementine tıkla "Search_Page_First_Product_Control"
* Element var mı kontrol et "Product_Detail_Brand_Name"

## Arama > Arama sonucu bulunamadığında sonuç bulunamadı hata mesajı kontrolü

tags: Android_AnasayfaArama_AramaSonuclari_SonucBulunamadi_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Arama alanından "xasdc" isimli ürün aratılır
* Element var mı kontrol et "SearchPage_Aranan_Urun_Bulunmamıstır_Text_Control"

## Arama sonucu > Aranan kelimenin sonuç sayfasında yazması ve altında kaç ürün bulunduğun yazması => "Yüz" "687 Ürün"

tags: Android_AnasayfaArama_AramaSonuclari_Urun_Aratma_KacAdet_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Arama alanından "gilette" isimli ürün aratılır
* "Searched_Item_Name_Control" elementinin "text" attiribute değerinin  "\"gilette\"" text degerine sahip oldugu kontrol edilir
* Element var mı kontrol et "Searched_Item_Gilette_Sayı_Control"

## Arama sonucu > "Sırala" ve "Filtrele" butonlarının kontrolü

tags: Android_AnasayfaArama_AramaSonuclari_SiralaFiltrele_Kontrol

* Beta uygulamasi baslatilir.
//sırala filtrele element yapısı
* Notification location izinleri verilir
* Arama alanından "gilette" isimli ürün aratılır
* Elementine tıkla "Search_Sırala_Button"

## Arama sonucu > Ürünlerin listelenmesi, favorilere eklenmesi, sepete eklenmesi, stokta yoksa "GELİNCE HABER VER" butonu kontrolü

tags: Android_AnasayfaArama_UrunListele_FavEkle_SepeteEkle_Stok_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Arama alanından "gilette" isimli ürün aratılır
* Elementine tıkla "Urun_Listesi_Ilk_Urun_Fav_Ekle_Button"
* Elementine tıkla "Urun_Listesi_Urun_Fav_Listeye_Ekle_Button"
* "2" saniye bekle
* Elementine tıkla "Urunler_Page_Urun_Ilk_Ekle_Buton"
* Elementine tıkla "Sepet_Bottom_Bar_Menu"
* Element var mı kontrol et "Sepet_Page_Checkbox_Control"
* Favorilerime gidilir ve ürün favorilerden kaldırılır
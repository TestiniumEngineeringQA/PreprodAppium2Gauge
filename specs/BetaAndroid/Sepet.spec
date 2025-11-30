# Specification Heading
Created by pc on 9.04.2025

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

## Sepet > Sepete ürün ekleme

tags: Android_Sepet_Urun_Ekleme

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
//* Elementine tıkla "Kasa_Arkası_Urunler_Alısveris_Tamamla_2"
* "5" saniye bekle

## Sepet > Sepet boşsa empty state kontrolü => "Sepetinizde Ürün Bulunmuyor" => "ALIŞVERİŞE BAŞLA" butonu

tags: Android_Sepet_BosSepet_AlisveriseBasla

* Notification location izinleri verilir
* Android giriş yapılır
* Elementine tıkla "HomePage_Sepet_Tab_Menu_Button"
* Element var mı kontrol et "Sepet_Urun_Yok_Text_Control"
* Elementine tıkla "Sepet_Bos_Alısverise_Basla_Buton"
* "Email_Dogrulama" li element varsa tıkla
* Element var mı kontrol et "Home_Page_UserName_Control"


## Sepet > Sepete eklenen ürün fotoğrafı, açıklaması ve kaç adet olduğu bottom sheet'te olması

tags: Android_Sepet_UrunFotosu_Aciklamasi_Adet_Kontrol

* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
//* Element var mı kontrol et "Sepet_Bottom_Sheet_ImageView_Control"
//* "Sepet_Bottom_Sheet_Acıklama_Control" li elementleri "text" attribute bul ve ekrana yazdır

## Sepet > Sepete ürün eklendikten sonra bottom sheet'te "SEPETE GİT" ve "ALIŞVERİŞE DEVAM ET" butonlarının olması ve butonların aksiyon kontrolü

tags: Android_Sepet_AlisveriseDevam_Sepetegit_Button_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir

## Sepet > Sepete ürün eklendikten sonra tabbardaki sepet  iconunun üzerinde sepetteki ürün adetinin yazması

tags: Android_Sepet_UrunEklenir_TabBar_SepetteUrunAdeti_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Element var mı kontrol et "Sepet_Bottom_Sheet_Eklenen_Urun_Adeti_Control"

## Sepet > "Sepetiniz" alanı altında sepette toplam kaç adet ürün yazılan text olması => "2 Ürün"

tags: Android_Sepet_Sepetiniz_ToplamUrunAdeti_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* "Kasa_Arkası_Urunler_Popup_Close" li element varsa tıkla
* "5" saniye bekle
/* Elementine tıkla "Kasa_Arkası_Urunler_Agız_Dis_Kategori"
/* Elementine tıkla "Kasa_Arkası_Urunler_Agız_Tab_Ilk_Urun_Ekle"
/* Elementine tıkla "Kasa_Arkası_Urunler_Alısveris_Tamamla_2"
/* "Sepet_Eklenen_Urun_Adeti_Control" elementinin "text" attiribute değerinin  "2 Ürün" text degerine sahip oldugu kontrol edilir

## Sepet > Sepetteki ürünlerin fotoğraf, ürün ismi, kampanya badge'i, Gratis Kart ve Normal fiyat alanlarının olması

tags: Android_Sepet_UrunFoto_UrunIsmi_KampanyaBadge_GratisKart_FiyatAlani_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Element var mı kontrol et "Sepet_Urun_Fotosu_Control"
//* Element var mı kontrol et "Sepet_Urun_Text_Control"
* Element var mı kontrol et "Sepet_Gratis_Kart_Control"
* Element var mı kontrol et "Sepet_Promosyon_Kodu_Alanı_Control"

## Sepet > Sepette ürün adet arttırma, azaltma, silme => Ürün adeti 1 ise adet azalttığımız "-" butonu silme iconu olmalı

tags: Android_Sepet_UrunArttirma_Azaltma_Silme_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Elementine tıkla "Sepet_Urun_Arttırma_Butonu"
* Element var mı kontrol et "Sepet_Urun_Arttırma_2adet_Control"
* Elementine tıkla "Sepet_Urun_Azaltma_Butonu"
* Element var mı kontrol et "Sepet_Urun_Azaltma_Adet1_Control"
* Elementine tıkla "Sepet_Urun_Azaltma_Butonu"
* Elementine tıkla "Sepet_Urun_Bosaltma_Popup_Sil_Button"
* Element var mı kontrol et "Sepet_Urun_Empty_Trash_Control"

## Sepet > "TÜMÜNÜ SİL" butonuna tıklandığında popup açılması => "Sepetenizdeki tüm ürünler silinecektir" "Vazgeç" "Tamam" => "Tamam" butonu tıklandığında sepetteki tüm ürünlerin silinmesi

tags: Android_Sepet_TumunuSil_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Elementine tıkla "Sepet_Ikıncı_Urun_Ekleme_Button"
* Elementine tıkla "Sepet_Bottom_Bar_Menu"
* "Kasa_Arkası_Urunler_Popup_Close" li element varsa tıkla
* Elementine tıkla "Sepet_Tumunu_Sil_Button"
* Element var mı kontrol et "Sepet_Tumunu_Vazgec_Popup_Button"
* Elementine tıkla "Sepet_Tumunu_Sil_Popup_Button"
* Element var mı kontrol et "Sepet_Urun_Empty_Trash_Control"

## Sepet > Silme iconuna basıldığında popup açılması => "Sepetinizden ürün silinecektir." "Sil ve Favorilere Ekle" "Tamam" ve kapatma iconu => "Tamam" butonuna tıklandığında ürünün sepetten silinmesi

tags: Android_Sepet_UrunSil_Sonrasi_SilFavorilereEkle_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir

## Sepet > Silme iconuna basıldığında popup açılması => Favori listesine ekli ürün silme, Ürün sepetinizden silinecektir, tamam ile silinmesi, çarpı ile kapatılması.

tags: Android_Sepet_FavlistesineEkli_UrunSilme_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Elementine tıkla "Urun_Listesi_Urun_Fav_Button"
* Elementine tıkla "Urun_Listesi_Urun_Fav_Listeye_Ekle_Button"
* Sepet alanına gidilir
* Elementine tıkla "Sepet_Urun_Trash_Button"
* Elementine tıkla "Sepet_Urun_Bosaltma_Popup_Sil_Button"
* Element var mı kontrol et "Sepet_Urun_Empty_Trash_Control"
* Elementine tıkla "Profile_Tab_MainMenu_Button"
* Elementine tıkla "Profile_Favorilerim_Menu_Button"
* Ürün favorilerden silinir

## Sepet > Ürünlerin solunda checkbox olması ve checkboxların select ve unselect durumlarına gelmesi => Seçili ürünler ile siparişe devam edilmesi

tags: Android_Sepet_CheckBox_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Elementine tıkla "Sepet_Ikıncı_Urun_Ekleme_Button"
* Sepet alanına gidilir
//* İlk ürün sepete eklenir
* Elementine tıkla "Sepet_Alısverisi_Tamamla_Button"
* Element var mı kontrol et "Siparisi_Tamamla_Teslimat_Secenekler_Text_Kontrol"

## Sepet > Ürün listesinin altında "Promosyon Kodu Ekle" alanlarının olması

tags: Android_Sepet_PromosyonKodu_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Elementine tıkla "Sepet_PromosyonKodu_Alanı"
* "14500004279" textini "Sepet_PromosyonKodu_TextGırıs_Alanı" elemente yaz
* Elementine tıkla "Sepet_PromosyonKodu_Uygula_Button"

## Sepet > Ürün listesinin altında "Hediye Kartım Var"

tags: Android_Sepet_HediyeKart_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Elementine tıkla "Sepet_HediyeKart_Alanı"
* Elementine tıkla "Sepet_HediyeKart_Text_Alanı"
* "1234567854438474" textini "Sepet_HediyeKart_Text_Alanı" elemente yaz
* Elementine tıkla "Sepet_PromosyonKodu_Uygula_Button"

## Sepet > Ürün listesinin altında Gratis Kart alanlarının olması

tags: Android_Sepet_GratisKart_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "makyaj" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Elementine tıkla "Sepet_GratisPuan_Alanı"
* Elementine tıkla "Sepet_GratisPuan_Kullan_Butonu"

## Sepet > Ürün listesinin altında "Kasa Arkası Ürünler" alanlarının olması

tags: Android_Sepet_KasaArkasi_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
//* Elementine tıkla "Kasa_Arkası_Urunler_Add_Button"
* Elementine tıkla "Kasa_Arkası_Urunler_Alısveris_Tamamla_2"

* Element var mı kontrol et "Siparisi_Tamamla_Teslimat_Secenekler_Text_Kontrol"
* Element var mı kontrol et "Teslimat_Magazadan_Teslim_Alacağım_Kontrol"
* Element var mı kontrol et "Teslimat_Adrese_Teslim_Text_Kontrol"
* Elementine tıkla "Teslimat_İl_Seciniz_Dropdown"
* Elementine tıkla "Teslimat_İl_Secim"
* Elementine tıkla "Teslimat_İlce_Secim"
//* Elementine tıkla "Teslimat_Magaza_Calısma_Saatleri"
//* Element var mı kontrol et "Teslimat_Magaza_Calısma_Saatleri_Kontrol"
* Elementine tıkla "Teslimat_Magaza_Konum_Gor_Button"
* Element var mı kontrol et "Teslimat_Magaza_Konum_Kontrol_Area"
* Android Geri tıkla
* Android Geri tıkla
* Elementine tıkla "Teslimat_Magaza_Secim_Button"
* Elementine tıkla "Teslimat_Magazdan_TeslimAlacakKısı_Edit_Button"
* Elementine tıkla "Teslimat_Magazdan_TeslimAlacakKısı_Kaydet_Button"
* Element var mı kontrol et "Teslimat_Magazdan_TeslimAlacakKısı_AdZorunluText"
* Element var mı kontrol et "Teslimat_Magazdan_TeslimAlacakKısı_SoyadZorunluText"
* Element var mı kontrol et "Teslimat_Magazdan_TeslimAlacakKısı_TelefonZorunluText"
* "TestAd" textini "Teslimat_Magazdan_TeslimAlacakKısı_Ad_Edit" elemente yaz
* "TestSoyad" textini "Teslimat_Magazdan_TeslimAlacakKısı_Soyad_Edit" elemente yaz
* "995555502" textini "Teslimat_Magazdan_TeslimAlacakKısı_Telefon_Edit" elemente yaz
* Elementine tıkla "Teslimat_Magazdan_TeslimAlacakKısı_Kaydet_Button"
//* "Teslimat_Magazdan_TeslimAlacakKısı_Edit_Text_Kontrol" elementinin "text" attiribute değerinin  "test test, (599) 555 55 02" text degerine sahip oldugu kontrol edilir
//* Element var mı kontrol et "Teslimat_Magazdan_Teslim_Fatura_Kontrol"
//* Elementine tıkla "Teslimat_Magazdan_Teslim_Fatura_Edit_Button"
//* Elementine tıkla "Teslimat_Magazdan_Teslim_Fatura_Kontrol"
//* Elementine tıkla "Teslimat_Magazdan_Teslim_Fatura_Yeni_Ekle_Button"
//
//* Elementine tıkla "Teslimat_Magazdan_Teslim_Fatura_Adresimi_Kaydet_Button"

## Sepet > Ürün listesinin altında "Personel İndirimi" alanlarının olması

tags: Android_Sepet_PersonelIndirimi_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Elementine tıkla "Sepet_Personel_Indırımı_Alanı"
* Elementine tıkla "Sepet_Personel_Indırımı_Kullan_Button"
* Element var mı kontrol et "Sepet_Personel_Indrımı_Kullanmaktan_Vazgec_Button_Kontrol"

//teslimat

## Teslimat > "TESLİMAT SEÇENEKLERİ" checkbox kontrolü => "Mağazadan Teslim Alacağım (ÜCRETSİZ)" "Kargo (Adrese Teslim)"

tags: Android_Sepet_Teslimat_Secenekleri_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Element var mı kontrol et "Sepet_Page_Checkbox_Control"
* Elementine tıkla "Sepet_Alısverisi_Tamamla_Button"
* Element var mı kontrol et "Siparisi_Tamamla_Teslimat_Secenekler_Text_Kontrol"
* Element var mı kontrol et "Teslimat_Magazadan_Teslim_Alacağım_Kontrol"
* Element var mı kontrol et "Teslimat_Adrese_Teslim_Text_Kontrol"

## Teslimat > Mağazadan Teslim Alacağım

tags: Android_Sepet_Teslimat_Secenekleri_Magazadan_Teslimat_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Element var mı kontrol et "Sepet_Page_Checkbox_Control"
* Alışverişi tamamla butonu ile devam edilir
* Teslimat sayfasında genel kontroller sağlanır
* Mağazadan teslim il ilçe mağaza seçimi yapılır
 Mağazadan teslim alacak kişi bilgileri girilir
* Mağazadan teslim fatura işlemleri yapılır
* Mağazadan teslim Checkbox işaretlenir ödeme adımına geçilir


## Kargo (Adrese Teslim)

tags: Android_Sepet_Teslimat_Adrese_Teslim

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Alışverişi tamamla butonu ile devam edilir
* Teslimat sayfasında genel kontroller sağlanır
* Adrese teslim seçimi ile ilerlenir
* Adrese teslim ödeme adımına geçilir

## Sepet > Tabbar üstünde sepet tutarının ve sepette seçilen ürün adetinin yazdığı Action Bar olması => "2 Ürün Seçildi" "6667,50TL" => İndirim durumunda => "2 Ürün Seçildi" "6667,50TL" "200,00TL"

tags: Android_Sepet_Tutar_Adet_ActionBar_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir

## Sepet > Action Barda sepet tutarı alanına tıklandığında sepet tutarlarının detaylarının gözüktüğü bottom sheet açılması

tags: Android_Sepet_Tutar_Alani_Tiklanir_Sepet_Tutar_Detay_BottomSheet_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Sepette fiyata tıklayınca açılan sheet kontrol edilir


## Sepet > Tutar Detay > "Ürünler" "Teslimat Ücreti => 300 TL ve üzeri alışverişlerinize ücretsiz teslimat" "Hediye Kart İndirimi" "Gratis Puan İndirimi" "Promosyon Kodu İndirimi" "Toplam" alanlarının kontrolü

tags: Android_Sepet_Ekrani_Genel_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Sepet sayfasında genel kontroller sağlanır

## Sepet > Taksit bilgilendirme text kontrolü => "Sepetinizdeki (X, Y, Z) ürün/ürünlere taksit uygulanamamaktadır."

tags: Android_Sepet_Taksit_Kontrol

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir

## Sepet > "ALIŞVERİŞİ TAMAMLA" butonuna tıklandığında "Teslimat" sayfasına yönlendirme

tags: Android_Sepet_AlisverisTamamla_Teslimat_Yonlenme

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır
* Sayfada "fön suyu" arama yapılır
* İlk ürün sepete eklenir
* Sepet alanına gidilir
* Alışverişi tamamla butonu ile devam edilir
* Teslimat sayfasında genel kontroller sağlanır
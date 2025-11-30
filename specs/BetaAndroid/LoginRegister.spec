Login Register
=====================
Created by testinium on 17.12.2024

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.




Beta Android Login
----------------
tags:Android_RegisterLogin_Login

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android giriş yapılır


Beta Android Üye ol register yönlenme
----------------
tags:Android_RegisterLogin_Uye_Ol_Register_Yonlenme


* Beta uygulamasi baslatilir.
//Login > "ÜYE Ol" butonun tıklandıktan register sayfasına yönlendirme
//ayrı
* Notification location izinleri verilir
///Anasayfa
* Element var mı kontrol et "HomePage_Uye_Olun_Button"
* Elementine tıkla "HomePage_Uye_Olun_Button"
* Element var mı kontrol et "Uye_Gırısı_Telefon_Numarası_Text"
* "995555502" textini "Uye_Gırısı_Telefon_Numarası_Text" elemente yaz
* Elementine tıkla "Uye_Gırısı_Gırıs_Yap_Button"
* "141414" textini "Register_Telefon_Numarası_Text_Area" elemente yaz
//* Element var mı kontrol et "Login_Olmadan_Sepete_Ekle_Sonrası_Control"

Beta Android Sepete ürün ekleyerek login olma
----------------
tags:Android_RegisterLogin_Sepete_Urun_Ekle_Login


* Beta uygulamasi baslatilir.
//Login > "ÜYE Ol" butonun tıklandıktan register sayfasına yönlendirme
//ayrı
* Notification location izinleri verilir
///Anasayfa
* Elementine tıkla "Makyaj_Kat_Button"
* Elementine tıkla "İlk_Ürün_Sepete_Ekle_Button"
* "995555502" textini "Uye_Gırısı_Telefon_Numarası_Text" elemente yaz
* Elementine tıkla "Uye_Gırısı_Gırıs_Yap_Button"
* "141414" textini "Register_Telefon_Numarası_Text_Area" elemente yaz





Beta Android  Login Favorilere ürün ekleyerek login olma
----------------
tags:Android_RegisterLogin_Urun_Fav_Login


* Beta uygulamasi baslatilir.
//Login > "ÜYE Ol" butonun tıklandıktan register sayfasına yönlendirme
//ayrı
* Notification location izinleri verilir

///Anasayfa
* Elementine tıkla "Makyaj_Kat_Button"
* Elementine tıkla "Login_Olmadan_İlk_Urun_Fax_Button"
* "995555502" textini "Uye_Gırısı_Telefon_Numarası_Text" elemente yaz
* Elementine tıkla "Uye_Gırısı_Gırıs_Yap_Button"
* "141414" textini "Register_Telefon_Numarası_Text_Area" elemente yaz
* Element var mı kontrol et "Login_Olmadan_İlk_Urun_Fav_Sonrası_Control"

Beta Android Login  Numaranın son 7 hanesi aynı olamaz kontrolü
----------------
tags:Android_RegisterLogin_Login_Numara_Son_7_Kontrol

//Login > "ÜYE Ol" butonun tıklandıktan register sayfasına yönlendirme
//ayrı
* Beta uygulamasi baslatilir.
* Notification location izinleri verilir

///Anasayfa
* Elementine tıkla "Anasayfa_Giris_Yapın_Button"
* "995555555" textini "Uye_Gırısı_Telefon_Numarası_Text" elemente yaz
* Elementine tıkla "Uye_Gırısı_Gırıs_Yap_Button"
* "1" saniye bekle
* Element var mı kontrol et "Son_7_Hane_Text_Kontrol"





//REGISTER//

Gratis Beta Register
-----------------
tags:GratisBeta_Register

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
///Anasayfa
Register > "Giriş Yap" veya "Üye Ol" butonu ile "Cep No. Doğrulama" ekranına geçme
* Elementine tıkla "HomePage_Uye_Olun_Button"
//* Element var mı kontrol et "HomePage_Uye_Olun_Button"
//* Element var mı kontrol et "Uye_Gırısı_Gırıs_Yap_Telefon_Zorunlu_Text"

//Register > "Cep No. Doğrulama" ekranında doğrulama yapıldıktan kullanıcı yoksa register ekranına geçmeli
* "995555505" textini "Uye_Gırısı_Telefon_Numarası_Text" elemente yaz
* Elementine tıkla "Uye_Gırısı_Gırıs_Yap_Button"
* "141414" textini "Register_Telefon_Numarası_Text_Area" elemente yaz
* Element var mı kontrol et "Register_Form_Username_Control"
//Register > Required alanların kontrolü

//kaydırma
* "2" kere aşağıya kaydır
* Elementine tıkla "Register_Forum_Uyeligi_Olustur_Button"

//Register > "Adınız", "Soyadınız", "E-Posta Adresiniz" alanlarının format kontrolü
//kabul kriteri bilgisi al

Register > Adınız hata mesajı kontorlü  => "Ad bilgisi zorunludur."
* Element var mı kontrol et "Register_Forum_Ad_Zorunlu_Text"
Register > Soyadınız hata mesajı kontorlü  => "Soyadı bilgisi zorunludur."
* Element var mı kontrol et "Register_Forum_Soyad_Zorunlu_Text"
Register > E-Posta Adresiniz hata mesajı kontorlü  => "E-Posta adresi zorunludur."
* Element var mı kontrol et "Register_Forum_Eposta_Zorunlu_Text"
Register > Doğum Tarihiniz hata mesajı kontorlü  => "Doğum Tarihi zorunludur."
* Element var mı kontrol et "Register_Forum_Dogum_Tarihi_Zorunlu_Text"
* Android Geri tıkla
* "1" kere aşağıya kaydır
* Element var mı kontrol et "Register_Forum_Dogum_Sifre_Zorunlu_Text"

Register > Cinsiyet alanı required kontrolü => İlgili alanlar kırmızı renk olmalı
/bilgi al

Register > Şifre alanı hata mesajı kontorlü  => "Şifreniz en az bir büyük harf, bir küçük harf, bir rakamlardan oluşmaldır."
/info

Register > Şifre alanı regex kontorlü  => Şifre girildikçe ilgili alanlarda tik işaretlenmesi
/info

Register > Şifre uyuşmama hata mesajı kontrolü  => "Girmiş olduğunuz şifreler uyuşmamaktadır."
/kaydırma
* "Candem.61" textini "Register_Forum_Password1_Text_Area" elemente yaz

* "Candem.62" textini "Register_Forum_Password2_Text_Area" elemente yaz
* "2" kere aşağıya kaydır
* Elementine tıkla "Register_Forum_Uyeligi_Olustur_Button"
* Element var mı kontrol et "Register_Forum_Password_Doesnt_Match_Text_Control"

Register > Şifreyi göster/gizle icon kontrolü
* "1" kere yukarı doğru kaydır
* Elementine tıkla "Register_Forum_Show_Password_Button"
* Element var mı kontrol et "Register_Forum_Show_Password_Control_Text"

//Register > Aydınlatma metni required kontrolü => "Aydınlatma Metni'ni okudum ve onaylıyorum" metni kırmızı olmalı.  (element düzeltimi istenecek )
//kırmızı kontrol elemnt?
* Element var mı kontrol et "Register_Forum_Aydınlatma_Metni_Control"

//Register > Kayıtlı E-mail kontorlü => "Bu E-Posta adresi daha önce kayıt olmuş."
//todo

//Register > Register ekranına OTP doğrulaması ile gelindiğinde "Telefon Numaranız" alanı değiştirilemez olmalı
//* "Register_Forum_Telefon_Degistirelemez_Enabled_Control" elementinin "enabled" attiribute değerinin  "false" text degerine sahip oldugu kontrol edilir

//
//* Beta uygulamasi baslatilir.
//* Elementine tıkla "popupOkayButton"
//* Elementine tıkla "Notification_Allow_Button"
//* Elementine tıkla "locationPermissionBtn"
//* Elementine tıkla "Location_Permission_Only_App_Using"
/////Anasayfa
//Register > "Giriş Yap" veya "Üye Ol" butonu ile "Cep No. Doğrulama" ekranına geçme
//* Elementine tıkla "HomePage_Uye_Olun_Button"
//* Element var mı kontrol et "HomePage_Uye_Olun_Button"
////* Element var mı kontrol et "Uye_Gırısı_Gırıs_Yap_Telefon_Zorunlu_Text"
//
////Register > "Cep No. Doğrulama" ekranında doğrulama yapıldıktan kullanıcı yoksa register ekranına geçmeli
//* "995555505" textini "Register_Telefon_Numarası_Text_Area" elemente yaz
//* Elementine tıkla "Uye_Gırısı_Gırıs_Yap_Button"
//* "141414" textini "Register_Telefon_Numarası_Text_Area" elemente yaz
//
//* Element var mı kontrol et "Register_Form_Username_Control"
////Register > Required alanların kontrolü
//
////kaydırma
////* Elementine tıkla "Register_Forum_Uyeligi_Olustur_Button"





Gratis Beta Register Ana Senaryo
-----------------
tags:Android_RegisterLogin_Register_Ana_Senaryo


* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Element var mı kontrol et "HomePage_Uye_Olun_Button"
* Elementine tıkla "HomePage_Uye_Olun_Button"
* "995555505" textini "Uye_Gırısı_Telefon_Numarası_Text" elemente yaz
* Elementine tıkla "Uye_Gırısı_Gırıs_Yap_Button"
* "1" saniye bekle

* "141414" textini "Register_Telefon_Numarası_Text_Area" elemente yaz

//* Element var mı kontrol et "Register_Form_Username_Control"
//Register > Required alanların kontrolü
* "DenemeAd" textini "Register_Forum_Adınız_Alanı_Text" elemente yaz
* "DenemeSoyad" textini "Register_Forum_Soyad_Alanı_Text" elemente yaz
* "denemetest@gmail.com" textini "Register_Forum_Eposta_Alanı_Text" elemente yaz
* "denemetest@gmail.com" textini "Register_Forum_Eposta_Tekrari_Alanı_Text" elemente yaz
* "13041996" textini "Register_Forum_Dogum_Tarihi_Alanı_Text" elemente yaz
* "1" kere aşağıya kaydır
* "Testtest.61" textini "Register_Forum_Password1_Text_Area" elemente yaz
* "1" kere aşağıya kaydır
* "Testtest.61" textini "Register_Forum_Password2_Text_Area" elemente yaz
* Elementine tıkla "Register_Forum_Aydınlatma_Metni_CheckBox"
* Elementine tıkla "Register_Forum_Cep_Telefonu_Sms_Onay_CheckBox"
* Elementine tıkla "Register_Forum_Eposta_Bilgilendirme_Onay_CheckBox"
* Elementine tıkla "Register_Forum_Callbox_Onay_CheckBox"
* "1" kere aşağıya kaydır

//kaydırma
* Elementine tıkla "Register_Forum_Uyeligi_Olustur_Button"
//* Element var mı kontrol et "Register_Sonrası_İsim_Control"

//Register > Üye oldup succes mesajı aldıktan sonra en altta "ALIŞVERİŞE BAŞLAYIN" butonu kontrolü


Gratis Beta Delete Account
-----------------
tags:Android_Delete_Account

* Beta uygulamasi baslatilir.
* Notification location izinleri verilir
* Android 05 numarali hesapla giris yapilir
* Ana menüden profil sekmesine gidilir
* Android Hesabim ve ayarlarim menüsüne tiklanir
* Android Üyelik Bilgilerim menüsüne tiklanir
* Android Üyelikten ayrıl butonuna tiklanir
* Hesabı silmek istendiğine dair uyari mesajları görüntülenir ve sil butonuna tiklanir
* Hesabın silindiğine dair uyarı mesajı görüntülenir
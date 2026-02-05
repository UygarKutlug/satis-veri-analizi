# Satış Verileri Analizi – Python ile Temel Veri Analizi


Bu proje, bir satış veri seti üzerinde **temel veri analizi ve iş içgörüsü çıkarımı**
yapmak amacıyla geliştirilmiştir.  
Python ve **pandas** kütüphanesi kullanılarak satış performansı analiz edilmiştir.

---

## 🎯 Proje Amacı

Bu projenin amacı:

- Satış verilerini analiz etmek  
- Toplam ciroyu hesaplamak  
- Kategori bazlı gelir dağılımını incelemek  
- En çok satan ürünleri belirlemek  
- Python ile veri analizi sürecini temiz ve anlaşılır bir yapı ile göstermek  

Bu çalışma, veri analizi alanında **portföy amaçlı** hazırlanmıştır.

---

## 📂 Veri Seti Bilgisi

Kullanılan veri seti aşağıdaki alanlardan oluşmaktadır:

- `order_id` → Sipariş numarası  
- `date` → Sipariş tarihi  
- `product` → Ürün adı  
- `category` → Ürün kategorisi  
- `quantity` → Satılan adet  
- `unit_price` → Birim fiyat  

Veriler CSV formatındadır ve pandas ile işlenmektedir.

---

## 🧰 Kullanılan Teknolojiler

- Python  
- Pandas  

---

## 📁 Proje Yapısı

satis_veri_analizi/
│
├── data/
│ └── sales.csv # Satış verileri
│
├── analysis.py # Veri analiz fonksiyonları
├── main.py # Programın çalıştırıldığı ana dosya
│
├── requirements.txt # Gerekli kütüphaneler
└── README.md # Proje açıklaması


---

## ⚙️ Proje Nasıl Çalışır?

1. Satış verileri CSV dosyasından yüklenir  
2. Her sipariş için toplam tutar hesaplanır (`quantity × unit_price`)  
3. Toplam ciro bulunur  
4. Kategori bazlı ciro analizi yapılır  
5. En çok satan ürünler belirlenir  

Sonuçlar terminal ekranında görüntülenir.

---

## ▶️ Projeyi Çalıştırma

1. Depoyu klonlayın:
```bash
git clone https://github.com/kullanici-adi/satis_veri_analizi.git
Proje klasörüne girin:

cd satis_veri_analizi
Gerekli kütüphaneleri kurun:

pip install -r requirements.txt
Programı çalıştırın:

python main.py
📈 Üretilen Çıktılar
Toplam ciro

Kategori bazlı ciro dağılımı

En çok satan ürünler

🚀 Geliştirme Fikirleri
Grafiklerle veri görselleştirme

Tarih bazlı satış trendleri

Sonuçları Excel veya CSV olarak dışa aktarma

Veri doğrulama kontrolleri ekleme
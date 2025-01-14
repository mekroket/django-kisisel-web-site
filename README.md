# Kişisel Web Sitesi

Bu proje, Django ve SQLite kullanarak geliştirilen bir kişisel web sitesidir. Proje, HTML, CSS ve JavaScript kullanılarak yapılmıştır. Bu site, kişisel bilgilerinizi, portföyünüzü ve iletişim bilgilerinizi sergilemek amacıyla tasarlanmıştır.

## Proje Genel Bakış

- **Backend:** Django
- **Veritabanı:** SQLite
- **Frontend:** HTML, CSS, JavaScript

## Özellikler

- Kullanıcı Kaydı ve Girişi
- Blog Yazıları Yayınlama
- Portföy Projelerini Gösterme
- İletişim Formu

## Kurulum

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

1. **Depoyu klonlayın:**
    ```bash
    git clone https://github.com/kullaniciadi/kisisel-web-sitesi.git
    cd kisisel-web-sitesi
    ```

2. **Sanal ortam oluşturun ve etkinleştirin:**
    ```bash
    python -m venv env
    source env/bin/activate  # Windows için: .\env\Scripts\activate
    ```

3. **Gerekli paketleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Veritabanını oluşturun:**
    ```bash
    python manage.py migrate
    ```

5. **Geliştirme sunucusunu başlatın:**
    ```bash
    python manage.py runserver
    ```

6. **Web sitesine gidin:**
    Tarayıcınızda `http://127.0.0.1:8000/` adresine gidin.

## Kullanım

- **Blog Yazısı Yayınlama:** Yönetici paneline giriş yaparak yeni blog yazıları ekleyebilirsiniz.
- **Portföy Projeleri:** Proje detaylarını portföy bölümüne ekleyebilirsiniz.
- **İletişim Formu:** Ziyaretçiler iletişim formunu kullanarak sizinle iletişime geçebilirler.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.

## Yazar

Oğuz Kaan Ekin - Akdeniz Üniversitesi - Öğrenci No: 20211129075


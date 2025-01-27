# Port Scanner Program

Bu program, Python kullanarak bir ağdaki açık portları taramak için tasarlanmış bir port tarayıcıdır. Program, kullanıcıdan alınan hedef IP adresi veya hostname üzerinde belirtilen port aralığını tarar ve açık portları listeler. Çıktılar, renklendirilmiş bir şekilde terminalde gösterilir.

## Özellikler
- Hedef IP adresindeki açık portları tespit etme
- Renkli ve okunabilir terminal çıktıları
- Tarama süresini hesaplama ve gösterme
- Terminal üzerinden argümanlarla hedef belirleme

## Gereksinimler

Bu program aşağıdaki Python kütüphanelerini gerektirir:
- `socket`
- `datetime`
- `termcolor`
- `sys`

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:
```bash
pip install termcolor
```

## Kullanım

Programın çalıştırılması için terminal üzerinden hedef IP adresini belirtmeniz gerekir. Program tam port aralığını (0-65535) varsayılan olarak tarar.

### Çalıştırma Komutu
```bash
python port_scanner.py <Hedef_IP>
```

### Örnek Kullanım
Hedef IP adresi olarak `192.168.1.1` üzerinde tarama yapmak için aşağıdaki komut kullanılabilir:
```bash
python port_scanner.py 192.168.1.1
```

### Çıktı Formatı
Programın terminal çıktısı renklendirilmiştir ve şu formatta bilgi sağlar:
- **INFO (Yeşil)**: Bilgilendirme mesajları
- **ERROR (Kırmızı)**: Hata mesajları
- **WARNING (Sarı)**: Uyarı mesajları
- **OPEN (Kalın Yeşil)**: Açık port bilgisi

Örnek çıktı:
```
[19.00.12] [INFO] Scanning target: 192.168.1.1
[19.00.12] [INFO] Scanning ports from 0 to 65535
[19.00.13] [OPEN] 22
[19.00.14] [OPEN] 80
[19.01.12] [INFO] Scanning completed in 0:01:00
```

## Kod Özeti

### Fonksiyonlar
- `get_time()`: Mevcut saat ve dakikayı renklendirilmiş bir şekilde döndürür.
- `port_scanner(target, start_port, end_port)`: Belirtilen hedefteki port aralığını tarar ve açık portları listeler.

### Hata Yönetimi
- **`KeyboardInterrupt`**: Tarama sırasında kullanıcı tarafından iptal edilirse bir "Bye" mesajı görüntüler.
- **`socket.gaierror`**: Hedef hostname çözülemezse bir hata mesajı görüntüler.
- **`socket.error`**: Hedefe bağlantı sağlanamazsa bir hata mesajı görüntüler.

## Uyarılar
- Bu program yalnızca yasal ve izin verilen amaçlar için kullanılmalıdır. İzin alınmadan yapılan port taramaları yasal sorunlara yol açabilir.
- Taramalar, ağ üzerindeki performansı etkileyebilir. Kullanırken dikkatli olun.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.


# BOT untuk rekap data santri pulang & sakit

## cara penggunaan
1. Wali kamar harus mengirim dengan format sebagai berikut
```
kamar7
pulang
1. adn (keterangan)
sakit
1. ada (keterangan)
```
- untuk keterangan sifat nya optional(boleh ada/boleh tidak ada)
- `kamar7` diganti sesuai kamar, untuk Asrama Tahfidz format nya tahfidz


## penginstallan
### POSTGRESQL
TABLE
```
create table santri_putra(
id VARCHAR UNIQUE,
nama VARCHAR,                             kelas_up integer,                         jenjang_up VARCHAR,                       kelas_diniyah VARCHAR,                    jenjang_diniyah VARCHAR,                  nama_wali_laki VARCHAR,                   nama_wali_perempuan VARCHAR,
kontak_wali integer,                      status_pondok VARCHAR);
```


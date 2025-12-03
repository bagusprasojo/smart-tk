# Smart TK Web Platform

Implementasi SRS `SRS.docx` berupa aplikasi Django untuk website TK dengan modul publik dan internal (admin, guru, orang tua).

## Fitur

- Landing page publik dan daftar artikel.
- Role-based access (Admin, Guru, Orang Tua) memakai custom user.
- Manajemen pengguna internal (admin-only).
- Manajemen siswa (data profil, relasi orang tua/guru).
- Mutabaah harian: input, edit, detail, filter, unduh PDF via WeasyPrint.
- Artikel internal (CRUD) dengan status draft/published + tampilan publik.

## Persiapan

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Setelah login sebagai admin:

1. Tambah pengguna (guru/orang tua) melalui menu Kelola Pengguna.
2. Tambah data siswa dan hubungkan dengan akun orang tua jika tersedia.
3. Guru bisa masuk untuk menginput mutabaah dan mengunduh laporan PDF.
4. Artikel bisa dibuat melalui menu Kelola Artikel lalu publish agar muncul di landing page/publik.

## Catatan

- Default database: SQLite (`db.sqlite3`). Ganti via `smarttk/settings.py` untuk produksi.
- PDF generator menggunakan WeasyPrint; pada Windows membutuhkan Microsoft Visual C++ runtime. Paket `pydyf==0.8.0` sudah dipin supaya API WeasyPrint terbaru tetap kompatibel di lingkungan ini.
- Folder media untuk unggahan foto siswa/artikel disediakan (`MEDIA_ROOT`). Pastikan membuat folder tersebut saat deploy.
"# smart-tk" 

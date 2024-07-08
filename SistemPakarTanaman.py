import tkinter as tk
from tkinter import messagebox

class SistemPakarTanaman:
    def __init__(self):
        self.kondisi = {}

    def tambah_kondisi(self, faktor, nilai):
        self.kondisi[faktor] = nilai

    def rekomendasi_tanaman(self):
        tanah = self.kondisi.get('jenis_tanah')
        curah_hujan = self.kondisi.get('curah_hujan')
        suhu = self.kondisi.get('suhu')

        if tanah == 'pasir' and curah_hujan == 'rendah' and suhu == 'tinggi':
            return 'Kaktus'
        elif tanah == 'lempung' and curah_hujan == 'sedang' and suhu == 'sedang':
            return 'Padi'
        elif tanah == 'gembur' and curah_hujan == 'tinggi' and suhu == 'rendah':
            return 'Strawberry'
        elif tanah == 'gembur' and curah_hujan == 'sedang' and suhu == 'tinggi':
            return 'Tomat'
        elif tanah == 'pasir' and curah_hujan == 'tinggi' and suhu == 'rendah':
            return 'Anggur'
        else:
            return 'Tanaman tidak diketahui'

class AplikasiSistemPakar(tk.Tk):
    def __init__(self, sistem_pakar):
        super().__init__()
        self.sistem_pakar = sistem_pakar
        self.title("Sistem Pakar Rekomendasi Tanaman")
        self.geometry("400x300")

        self.label_jenis_tanah = tk.Label(self, text="Masukkan jenis tanah (pasir/lempung/gembur):")
        self.label_jenis_tanah.pack()
        self.entry_jenis_tanah = tk.Entry(self)
        self.entry_jenis_tanah.pack()

        self.label_curah_hujan = tk.Label(self, text="Masukkan curah hujan (rendah/sedang/tinggi):")
        self.label_curah_hujan.pack()
        self.entry_curah_hujan = tk.Entry(self)
        self.entry_curah_hujan.pack()

        self.label_suhu = tk.Label(self, text="Masukkan suhu (rendah/sedang/tinggi):")
        self.label_suhu.pack()
        self.entry_suhu = tk.Entry(self)
        self.entry_suhu.pack()

        self.button_submit = tk.Button(self, text="Dapatkan Rekomendasi", command=self.dapatkan_rekomendasi)
        self.button_submit.pack()

    def dapatkan_rekomendasi(self):
        jenis_tanah = self.entry_jenis_tanah.get().lower()
        curah_hujan = self.entry_curah_hujan.get().lower()
        suhu = self.entry_suhu.get().lower()

        if jenis_tanah not in ['pasir', 'lempung', 'gembur']:
            messagebox.showerror("Error", "Jenis tanah tidak valid!")
            return
        if curah_hujan not in ['rendah', 'sedang', 'tinggi']:
            messagebox.showerror("Error", "Curah hujan tidak valid!")
            return
        if suhu not in ['rendah', 'sedang', 'tinggi']:
            messagebox.showerror("Error", "Suhu tidak valid!")
            return

        self.sistem_pakar.tambah_kondisi('jenis_tanah', jenis_tanah)
        self.sistem_pakar.tambah_kondisi('curah_hujan', curah_hujan)
        self.sistem_pakar.tambah_kondisi('suhu', suhu)

        hasil = self.sistem_pakar.rekomendasi_tanaman()
        messagebox.showinfo("Rekomendasi Tanaman", f"Rekomendasi tanaman: {hasil}")

if __name__ == "__main__":
    sistem_pakar = SistemPakarTanaman()
    aplikasi = AplikasiSistemPakar(sistem_pakar)
    aplikasi.mainloop()

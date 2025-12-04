class DaftarNilai:
    def __init__(self):
        self.data_mahasiswa = []
    
    def tambah(self):
        """Method untuk menambah data mahasiswa"""
        print("\n=== Tambah Data Mahasiswa ===")
        nama = input("Masukkan nama: ")
        nilai = float(input("Masukkan nilai: "))
        
        self.data_mahasiswa.append({
            'nama': nama,
            'nilai': nilai
        })
        print(f"Data {nama} berhasil ditambahkan!")
    
    def tampilkan(self):
        """Method untuk menampilkan data mahasiswa"""
        print("\n=== Daftar Nilai Mahasiswa ===")
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
            return
        
        print(f"{'No':<5}{'Nama':<20}{'Nilai':<10}")
        print("-" * 35)
        for i, mhs in enumerate(self.data_mahasiswa, 1):
            print(f"{i:<5}{mhs['nama']:<20}{mhs['nilai']:<10}")
    
    def hapus(self, nama):
        """Method untuk menghapus data berdasarkan nama"""
        for mhs in self.data_mahasiswa:
            if mhs['nama'].lower() == nama.lower():
                self.data_mahasiswa.remove(mhs)
                print(f"\nData {nama} berhasil dihapus!")
                return
        print(f"\nData dengan nama {nama} tidak ditemukan.")
    
    def ubah(self, nama):
        """Method untuk mengubah data berdasarkan nama"""
        for mhs in self.data_mahasiswa:
            if mhs['nama'].lower() == nama.lower():
                print(f"\n=== Ubah Data {nama} ===")
                nama_baru = input("Masukkan nama baru: ")
                nilai_baru = float(input("Masukkan nilai baru: "))
                
                mhs['nama'] = nama_baru
                mhs['nilai'] = nilai_baru
                print(f"Data berhasil diubah!")
                return
        print(f"\nData dengan nama {nama} tidak ditemukan.")


def main():
    daftar = DaftarNilai()
    
    while True:
        print("\n" + "="*40)
        print("PROGRAM DAFTAR NILAI MAHASISWA")
        print("="*40)
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        print("="*40)
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            daftar.tambah()
        elif pilihan == '2':
            daftar.tampilkan()
        elif pilihan == '3':
            nama = input("\nMasukkan nama yang akan dihapus: ")
            daftar.hapus(nama)
        elif pilihan == '4':
            nama = input("\nMasukkan nama yang akan diubah: ")
            daftar.ubah(nama)
        elif pilihan == '5':
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid!")


if __name__ == "__main__":
    main()

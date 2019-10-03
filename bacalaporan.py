class BacaLaporan:

    def __init__(self):
        self.usersession = ''

    

    def identifikasiUser(self):
        #1. ambil nip user dari session
        #2. Set self.userssion = nip user dari session 
    
    def tampilHalamanUtamaBaca(self):
        #1. Panggil method identifikasiUser() untuk mengetahui siapa user 
        #2. buka koneksi ke database 
        #3. Baca database untuk mengetahui laporan apa saja yang berhak dibaca oleh user
        #4. Kembalikan hasil langkah nomor 3 ke UI dalam bentuk json 

    def mintaFileLaporan(self, kode_laporan, nama_file):
        #1. Panggil method identifikasiUser untuk mengetahui siapa user
        #2. buka koneksi database 
        #3. Periksa apakah user berhak baca kode_laporan 
        #4. Jika user berhak maka transfer (kirim) file yang diminta ke UI
        #5. Jika tidak berhak, tidak perlu kembalikan apa2 ke UI (kembalikan kosong)


class ListenerBacaLaporan:

    def __init__(self):

    def listenScheduleBaru(self, record_schedule_baru):
        #1. untuk setiap record schedule baru yang masuk, ambil data kode laporan, NIP PIC & penerima
        #2. Buka koneksi ke database 
        #3. Masukkan NIP PIC, kode laporan satu per satu record kedalam tabel 

    def listenUpdateSchedule(self):
        #1. untuk setiap record update schedule yang masuk, ambil data kode laporan, NIP PIC & penerima 
        #2. Buka koneksi ke database 
        #3. Cari semua PIC dan penerima untuk kode laporan yang diterima. 
        #4. Jika PIC tidak ada di database, tetapi ada di update record, tambahkan PIC 
        #5. Jika PIC ada di database, tetapi tidak ada di update record, hapus PIC 

    def listenHasilProsesLaporan(self):
        #1. Untuk setiap hasil proses laporan, ambil kode laporan, nama file, dan tanggal proses
        #2. Buka koneksi ke database 
        #3. Cari di database apakah ada kode laporan
        #4. Jika kode laporan belum ada, insert kode laporan, nama file dan tanggal proses 
        #5. Jika kode laporan ada, update kode laporan tersebut dengan nama file dan tanggal proses yang baru 
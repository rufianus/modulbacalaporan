from flask import Flask 

app = Flask(__name__)

@app.route('/halamanbacalaporan')
def halamanBacaLaporan(identitas):
    #1 baca identitas user 
    #2 akses class untuk menampilkan menu laporan 
    #3 kembalikan menu laporan ke layar

@app.route('/membaca')
def membacaLaporan(nama_file_laporan):
    #1 akses class untuk mencari laporan dalam folder 
    #2 kembalikan file yang diminta kepada request 

@app.route('/listenschedulebaru')
def scheduleBaru(record_schedule):
    #1 terima record schedule baru 
    #2 akses class untuk insert record tersebut kedalam tabel pic schedule


@app.route('/listenupdatetabelschedule')
def updatePICSchedule(record_schedule):
    #1 terima record update schedule
    #2 Akses ke class untuk update schedule 

@app.route('/listenproseslaporan')
def hasilProsesLaporan(record_proses_laporan):
    #1 terima record hasil proses laporan 
    #2 akses ke class untuk update hasil proses laporan 
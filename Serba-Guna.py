#!/bin/python
#coding=utf-8

# import module
import os,sys,time,requests
from time import sleep

blue='\33[34;1m'
green='\33[32;1m'
purple='\33[35;1m'
cyan='\33[36;1m'
red='\33[31;1m'
white='\33[37;1m'
yellow='\33[33;1m'
Toska='033[96;1m'


# Clear Text
def bersih():
	os.system("clear")



# Mengetik Otomatis
def mengetik(z):
    for e in z + "\n":
	sys.stdout.write(e)
  	sys.stdout.flush()
	time.sleep(0.10)

#memgetik cepat
def speed(z):
    for e in z + "\n":
 	sys.stdout.write(e)
 	sys.stdout.flush()
 	time.sleep(0.005)

#def run
def run_indo():
        m = ["|","/","-","\\"]
        for b in range(2):
                for t in m:
                        sys.stdout.write("  \r\033[37m[!] \033[33mMenghubungkan ke server \033[34m"+t)
                        sys.stdout.flush()
                        time.sleep(1)
#menu

def menu1():
 time.sleep(1.5)
 bersih()
 speed("""   \x1b[1;95m _____            __                   ______         __                __           
   /     |          /  |                 /      \       /  |              /  |          
   $$$$$ |  ______  $$/  _______        /$$$$$$  |  ____$$ | _____  ____  $$/  _______  
      $$ | /      \ /  |/       \       $$ |__$$ | /    $$ |/     \/    \ /  |/       \ 
 __   $$ |/$$$$$$  |$$ |$$$$$$$  |      $$    $$ |/$$$$$$$ |$$$$$$ $$$$  |$$ |$$$$$$$  |
/  |  $$ |$$ |  $$ |$$ |$$ |  $$ |      $$$$$$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |$$ |  $$ |
$$ \__$$ |$$ \__$$ |$$ |$$ |  $$ |      $$ |  $$ |$$ \__$$ |$$ | $$ | $$ |$$ |$$ |  $$ |
$$    $$/ $$    $$/ $$ |$$ |  $$ |      $$ |  $$ |$$    $$ |$$ | $$ | $$ |$$ |$$ |  $$ |
 $$$$$$/   $$$$$$/  $$/ $$/   $$/       $$/   $$/  $$$$$$$/ $$/  $$/  $$/ $$/ $$/   $$/ """)
 time.sleep(1.2)
 print ""
 print "\033[1;32m[ \033[1;35m> \033[1;32m]\033[1;35m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;32m[ \033[1;35m< \033[1;32m]"
 print "\033[1;32m[\033[1;35m===\033[1;32m]"
 print "\033[1;32m[ \033[1;35m• \033[1;32m] \033[1;33mAuthor   \033[1;31m: \033[1;37mRichesee"
 print "\033[1;32m[ \033[1;35m• \033[1;32m] \033[1;33mGithub   \033[1;31m: \033[1;37mhttps://github.com/Richesee"
 print "\033[1;32m[ \033[1;35m• \033[1;32m] \033[1;33mTeam     \033[1;31m: \033[1;37mUser Termux Newbie <Newbie To Mastah>"
 print "\033[1;32m[ \033[1;35m• \033[1;32m] \033[1;33mNote     \033[1;31m: \033[1;37mShortcut Code No Enc <Free Recode>"
 print "\033[1;32m[\033[1;35m===\033[1;32m]"
 print "\033[1;32m[ \033[1;35m> \033[1;32m]\033[1;35m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;32m[ \033[1;35m< \033[1;32m]"
 mengetik("                 \033[1;35m[\033[1;37m \033[45;1mCreated Code By Richesee ID\033[40;1m \033[1;35m]")
 time.sleep(1.5)
 print """
\033[1;35m ╔════════════════════╗  ╔════════════════════╗
 ╠═▶   \033[1;33mJOIN ADMIN           Vierws (99K+)
 \033[1;35m╚════════════════════╝  ╚════════════════════╝
 """
 time.sleep(2.5)
 mengetik(" \033[1;35m╠═▶\033[33;1mDiwajibkan Join Akun Admin Terlebih Dahulu")

 speed("""
 \033[1;35m╔══════════════════════════════╗
 ╠═▶ \033[1;33m1 Join Facebook Admin
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m2 Join Discord Admin
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m3 Join Grup WhatsApp UTN
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m4 Join Grup Facebook UTN
 \033[1;35m╚══════════════════════════════╝

  \033[1;91m════════════════════════════════════════

 \033[1;35m╔══════════════════════════════╗
 ╠═▶ \033[1;33m5 INSTALL BAHAN
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m6 EXIT LOGOUT
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m0 OPEN TOOLS
 \033[1;35m╚══════════════════════════════╝
 """)
 pil = raw_input(""" \033[1;33m╠═▶\033[1;35mPilih Sesuai Nomor : \033[1;33m""")
 run_indo()
#database Admin

 if pil =="1":
        time.sleep(1.5)
        os.system("xdg-open https://www.facebook.com/profile.php?id=100057777742045")

 #data baee admin

 elif pil=="2":
        time.sleep(1.5)
        os.system("xdg-open https://discord.com/channels/782739765552218152/782739765552218155")

 #data base admin

 elif pil=="3":
        time.sleep(1.5)
        os.system("xdg-open https://chat.whatsapp.com/DboBkomj9CS3D2gUXYlMwH")

 #database admin

 elif pil=="4":
        time.sleep(1.5)
        os.system("xdg-open https://m.facebook.com/groups/192879305395245/?ref=group_browse")
#database bahan

 elif pil =="5":
	time.sleep(2)
	bersih()
        os.system("cd /data/data/com.termux/files/home")
	os.system("pkg update && pkg upgrade -y")
	os.system("pkg install bash php python python2 fish clang jq figlet ruby git nano -y")
	os.system("pip install --upgrade pip && pip install requests && pip install mechanize && pip2 install requests && pip2 install mechanize")
	os.system("pkg install wget -y")
        time.sleep(1)

#databe tools

 elif pil =="6":
	bersih()
	time.sleep(2)
	sys.exit()

#database admin

 elif pil =="0":
        bersih()
        mengetik("Terimakasih Telah Join Admin")

 #Else Kesalahan
 else:
     time.sleep(1.7)
     mengetik("[ + ] Masukan Input Yang Benar")
     menu1()

menu1()

#Menu2

def menu2():
 time.sleep(1.5)
 bersih()
 speed("""
 \033[1;91m██████╗ ██╗ ██████╗██╗  ██╗███████╗███████╗███████╗███████╗
 ██╔══██╗██║██╔════╝██║  ██║██╔════╝██╔════╝██╔════╝██╔════╝
 ██████╔╝██║██║     ███████║█████╗  ███████╗█████╗  █████╗  
 ██╔══██╗██║██║     ██╔══██║██╔══╝  ╚════██║██╔══╝  ██╔══╝  
 ██║  ██║██║╚██████╗██║  ██║███████╗███████║███████╗███████╗
 ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝""")
 time.sleep(1.2)
 print "\033[1;32m[ \033[1;35m> \033[1;32m]\033[1;35m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;32m[ \033[1;35m< \033[1;32m]"
 print "\033[1;32m[\033[1;35m===\033[1;32m]"
 print "\033[1;32m[ \033[1;35m• \033[1;32m] \033[1;33mAuthor   \033[1;31m: \033[1;37mRichesee"
 print "\033[1;32m[ \033[1;35m• \033[1;32m] \033[1;33mGithub   \033[1;31m: \033[1;37mhttps://github.com/Richesee"
 print "\033[1;32m[ \033[1;35m• \033[1;32m] \033[1;33mTeam     \033[1;31m: \033[1;37mU T B I <User Termux Beginners Indonesia>"
 print "\033[1;32m[ \033[1;35m• \033[1;32m] \033[1;33mNote     \033[1;31m: \033[1;37mShortcut Code No Enc <Free Recode>"
 print "\033[1;32m[ \033[1;35m• \033[1;32m] \033[1;33mWarning  \033[1;31m: \033[1;37mCopyright2021-hekelpro"
 print "\033[1;32m[\033[1;35m===\033[1;32m]"
 print "\033[1;32m[ \033[1;35m> \033[1;32m]\033[1;35m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;32m[ \033[1;35m< \033[1;32m]"
 time.sleep(1.5)
 mengetik("                 \033[1;35m[\033[1;37m \033[45;1mCreated Code By Richesee ID\033[40;1m \033[1;35m]")
 os.system("xdg-open https://github.com/hekelpro")
 speed("""
 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m1 Video-Donwloader FB|IG
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m2 Pintu-Tobat
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m3 Virtex-WhatsApp
 \033[1;35m╚══════════════════════════════╝

 \033[1;35m╔══════════════════════════════╗
 ╠═▶ \033[1;33m4 Cek-My/Ip
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m5 Ripper-By-Hekelpro
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m6 Install-Vid.Bok**
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m7 xnxx Clone-By-hekelpro
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m8 xnxx Clone-By-Asecx
 \033[1;35m╚══════════════════════════════╝

 \033[1;35m╔══════════════════════════════╗
 ╠═▶ \033[1;33m9 Anti-Recode-By/hekelpro
 \033[1;35m╚══════════════════════════════╝

 ╔══════════════════════════════╗
 ╠═▶ \033[1;33m0 Exit / Logout
 \033[1;35m╚══════════════════════════════╝
""")
 pil = raw_input("Pilih Sesuai Angka/Nomor : ")
 run_indo()
 #if/else/data
 if pil =="1":
	time.sleep(1.5)
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/hekelpro/video")
	os.system("cd video")
	os.system("python3 vid.py")
 #2if
 elif pil =="2":
	time.sleep(1.5)
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/hekelpro/Al-Quran")
	os.system("cd Al-Quran")
	os.system("python2 Al-Quran.py")
 #3if
 elif pil =="3":
	time.sleep(1.5)
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/hekelpro/virtex")
	os.system("cd virtex")
	os.system("python2 virtex.py")
 #4if
 elif pil =="4":
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/Bl4ckDr460n/My-Ip") 
	os.system("cd My-Ip && python2 My-Ip.py")
 #5if
 elif pil =="5":
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/hekelpro/ripper")
	os.system("cd ripper && python2 ripper.py")
 #6if
 elif pil =="6":
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/hekelpro/Vid-Bok")
	os.system("cd Vid-Bok && python3 main.py")
 #7if
 elif pil =="7":
	run_indo()
	os.system("xdg-open http://rizky-dev.6te.net/hentai/")
 #8if
 elif pil =="8":
	run_indo()
	os.system("xdg-open https://asecx.site/sex/")
 #9if
 elif pil =="9":
	os.system("cd /data/data/com.termux/files/home")
	os.system("git clone https://github.com/hekelpro/antirecode")
	os.system("cd antirecode && php crashcode.php")
 #0if
 elif pil =="0":
	bersih()
	print "\033[1;91mCopyRight2021 hekelpro"
	time.sleep(2.0)
	os.system("xdg-open https://github.com/hekelpro")
	time.sleep(1.0)
	sys.exit
 else:
	os.system("python2 Serba-Guna.py")
menu2()

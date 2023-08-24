from selenium import webdriver
from colorama import Fore, init
import os
from prettytable import PrettyTable

# Inicio colorama
init()

# Asigno valores a los colores
R = Fore.RED
G = Fore.GREEN
S = Fore.RESET
B = Fore.BLUE
urls = {
    'Instagram': 'https://www.instagram.com/',
    'GitHub': 'https://github.com/',
    'Twitter': 'https://twitter.com/',
    'TikTok': 'https://www.tiktok.com/',
    'YouTube': 'https://www.youtube.com/',
    'Facebook': 'https://www.facebook.com/',
    'LinkedIn': 'https://www.linkedin.com/',
    'Snapchat': 'https://www.snapchat.com/'
}

def clear():
    os.system('cls') if os.name == "nt" else os.system("clear")

clear()


def rm_FirefoxLog():
	if os.name == "nt":
		os.system("del geckodriver.log")
	else:
		os.system("rm geckodriver.log")	

if "geckodriver.log" in os.listdir():
		rm_FirefoxLog()

error = False
while True:
    print(f"{R}Selecciona una opción:{S}")
    table = PrettyTable(['#', 'Red Social', 'URL'])
    for i, (key, value) in enumerate(urls.items()):
        table.add_row([R + str(i+1)  + S, B + key + S, G + value + S])
    print(table)
    
    # for i, key in enumerate(urls.keys()):
    #     print(f"{G}[{i+1}] {key}")
    # print(S)
    if error:
        print(f'{R}[-]{S} Opción no válida')
        print()
    error = False
    print(f'Sitio web: {R}', end="")
    url = str(input()).lower()
    if not error:
        clear()
    if url == "1" or url == "instagram" or url == "ig":
        # clear()
        print(f'{G}Introduce el valor de la cookie de sesión de Instagram: \n{S}sessionid: {R}', end="")
        session_id_value = input()
        print(S)
        
        if os.name == "nt":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--incognito")
            driver = webdriver.Chrome(options=options)
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument('--private-window')
            driver = webdriver.Firefox(options=options)
        
        driver.get("https://www.instagram.com/")
        clear()
        script = f"document.cookie = 'sessionid={session_id_value};path=/';"
        driver.execute_script(script)
        # print(f'Script: {script}')
        driver.refresh()
        break
    elif url == "2" or url == "github" or url == "git":
        # clear()
        print(f'{G}Introduce el valor de la cookie de sesión de Github: \n{S}user_session: {R}', end="")
        user_session_value = input()
        print(S)
        if os.name == "nt":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--incognito")
            driver = webdriver.Chrome(options=options)
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument('--private-window')
            driver = webdriver.Firefox(options=options)
        driver.get("https://www.github.com/")
        clear()
        driver.execute_script(f"document.cookie = 'user_session={user_session_value};path=/';")
        driver.refresh()
        break
    elif url == "3" or url == "twitter":
        # clear()
        print(f'{G}Introduce el valor de la cookie de sesión de Twitter: \n{S}auth_token: {R}', end="")
        auth_token_value = input()
        print(S)
        if os.name == "nt":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--incognito")
            driver = webdriver.Chrome(options=options)
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument('--private-window')
            driver = webdriver.Firefox(options=options)
        driver.get("https://www.twitter.com/")
        clear()
        driver.execute_script(f"document.cookie = 'auth_token={auth_token_value};path=/';")
        driver.refresh()
        driver.get("https://www.twitter.com/home/")
        break
    elif url == "4" or url == "tiktok":
        # clear()
        print(f'{G}Introduce el valor de la cookie de sesión de TikTok: \n{S}sessionid: {R}', end="")
        sessionid_value = input()
        print(S)
        if os.name == "nt":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--incognito")
            driver = webdriver.Chrome(options=options)
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument('--private-window')
            driver = webdriver.Firefox(options=options)
        driver.get("https://www.tiktok.com/")
        clear()
        driver.execute_script(f"document.cookie = 'sessionid={sessionid_value};path=/';")
        driver.refresh()
        break
    elif url == "5" or url == "youtube" or url == "yt":
        # clear()
        print(f'Site: {G} YouTube{S}')
        print()
        print("Dos cookies disponibles:")
        print(f" 1- {G}__Secure-1PSID{S}")
        print(f" 2- {G}__Secure-3PSID{S}")
        print("")
        while True:
            cookie_option = int(input("Opción: "))
            if cookie_option == 1:
                cookie = '__Secure-1PSID'
                break
            if cookie_option == 2:
                cookie = '__Secure-3PSID'
                break
            else:
                print(f'{R}[-]{S} Opción no válida')
        print(f'{G}Introduce el valor de la cookie de sesión de Youtube: \n{S}{cookie}: {R}', end="")
        session_value = input()
        print(S)
        if os.name == "nt":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--incognito")
            driver = webdriver.Chrome(options=options)
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument('--private-window')
            driver = webdriver.Firefox(options=options)
        driver.get("https://www.youtube.com/")
        clear()
        script = f"document.cookie = '{cookie}={session_value};path=/; secure';"
        driver.execute_script(script) 
        driver.refresh()
        break
    elif url == "6":
        input(f"No disponible {Fore.RESET}(press ENTER)")
        clear()
        pass
    elif url == "7":
        input(f"No disponible {Fore.RESET}(press ENTER)")
        clear()
        pass
    elif url == "8":
        input(f"No disponible {Fore.RESET}(press ENTER)")
        clear()
        pass
    else:
        error = True
        clear()
        




print(f'{G}Presiona {B}ENTER{G} para cerrar el navegador.{S}')
input()
rm_FirefoxLog()
# Cierra la ventana del navegador
driver.quit()
exit(1)

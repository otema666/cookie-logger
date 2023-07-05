from re import T
from traceback import print_tb
from selenium import webdriver
from colorama import Fore, init
import os


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
    os.system('cls')

clear()




while True:
    print(f"{R}Selecciona una opción:")
    for i, key in enumerate(urls.keys()):
        print(f"{G}[{i+1}] {key}")
    print(S)
    
    url = int(input("Sitio web: "))
    clear()
    if url == 1:
        print(f'{G}Introduce el valor de la cookie de sesión de Instagram: \n{S}sessionid: {R}', end="")
        session_id_value = input()
        print(S)
        driver = webdriver.Chrome()
        driver.get("https://www.instagram.com/")
        clear()
        driver.execute_script(f"document.cookie = 'sessionid={session_id_value};path=/';")
        driver.refresh()
        break
    elif url == 2:
        print(f'{G}Introduce el valor de la cookie de sesión de Github: \n{S}user_session: {R}', end="")
        user_session_value = input()
        print(S)
        driver = webdriver.Chrome()
        driver.get("https://www.github.com/")
        os.system('cls')
        driver.execute_script(f"document.cookie = 'user_session={user_session_value};path=/';")
        driver.refresh()
        break
    elif url == 3:
        print(f'{G}Introduce el valor de la cookie de sesión de Twitter: \n{S}auth_token: {R}', end="")
        auth_token_value = input()
        print(S)
        driver = webdriver.Chrome()
        driver.get("https://www.twitter.com/")
        os.system('cls')
        driver.execute_script(f"document.cookie = 'auth_token={auth_token_value};path=/';")
        driver.refresh()
        driver.get("https://www.twitter.com/home/")
        break
    elif url == 4:
        print(f'{G}Introduce el valor de la cookie de sesión de TikTok: \n{S}sessionid: {R}', end="")
        sessionid_value = input()
        print(S)
        driver = webdriver.Chrome()
        driver.get("https://www.tiktok.com/")
        os.system('cls')
        driver.execute_script(f"document.cookie = 'sessionid={sessionid_value};path=/';")
        driver.refresh()
        break
    elif url == 5: 
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
        driver = webdriver.Chrome()
        driver.get("https://www.youtube.com/")
        os.system('cls')
        script = f"document.cookie = '{cookie}={session_value};path=/';"
        driver.execute_script(script) 
        print(f'Script: {script}')
        driver.refresh()
        break
    elif url == 6:
        pass
    elif url == 7:
        pass
    elif url == 8:
        pass
    else:
        print(f'{R}[-]{S} Opción no válida')




print(f'{G}Presiona {B}ENTER{G} para cerrar el navegador.{S}')
input()
# Cierra la ventana del navegador
driver.quit()
exit(1)

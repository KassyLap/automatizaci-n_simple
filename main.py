from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from funciones_agentes.obtener_clima import obtener_clima
from funciones_agentes.obtener_precio_accion import obtener_precio_accion
from utils.sanitizar import sanitizar

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

driver = webdriver.Chrome(
    service=Service(),
    options=options
)

def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    return None

print("Hola, soy tu precioso asistente virtual. 🤖 ¿En qué puedo ayudarte hoy, precios@? 👾")

while True:
    user_input = sanitizar(input("---> "))
    funcion_agente = procesar_input(user_input)

    if funcion_agente is None:
        print("No entendí tu solicitud. Intenta nuevamente.")
        continue

    respuesta = funcion_agente(driver, user_input)
    print(f">>> {respuesta}")

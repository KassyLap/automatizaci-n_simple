from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_precio_accion(driver, consulta):
    consulta = consulta.lower()
    for palabra in ["precio", "accion", "acciones", "valor", "de", "la"]:
        consulta = consulta.replace(palabra, "")
    consulta = consulta.strip()

    driver.get(f"https://www.google.com/search?q=acción+{consulta}&hl=es")

    try:
        wait = WebDriverWait(driver, 15)

        precio = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[jsname='L3mUVe']"))
        ).text

        divisa = driver.find_element(By.CSS_SELECTOR, "span[jsname='T3Us2d']").text

        empresa = driver.find_element(
            By.CSS_SELECTOR, "div[class*='PZPZlf']"
        ).text

        ticker = driver.find_element(
            By.CSS_SELECTOR, "div[class*='iAIpCb']"
        ).text

        return f"{empresa} ({ticker}) → ${precio} {divisa}"

    except Exception as e:
        return f"No se pudo obtener el precio de la acción ({type(e)})"

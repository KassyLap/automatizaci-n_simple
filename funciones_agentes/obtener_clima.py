from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_clima(driver, consulta):
    consulta = consulta.lower().replace("clima", "").strip()

    driver.get(f"https://www.google.com/search?q=clima+{consulta}&hl=es")

    try:
        wait = WebDriverWait(driver, 15)

        wait.until(EC.presence_of_element_located((By.ID, "wob_tm")))

        ciudad = driver.find_element(By.ID, "wob_loc").text
        temperatura = driver.find_element(By.ID, "wob_tm").text
        condicion = driver.find_element(By.ID, "wob_dc").text
        humedad = driver.find_element(By.ID, "wob_hm").text
        viento = driver.find_element(By.ID, "wob_ws").text

        return (
            f"El clima de hoy es {condicion}, "
            f"{temperatura}°C, humedad {humedad}, viento {viento}."
        )

    except Exception as e:
        return f"No se pudo obtener el clima ({type(e).__name__})"

# Librerías
from lib2to3.pgen2 import driver
from selenium import webdriver # Driver del navegador
from selenium.webdriver.common.by import By # Elementos html
from selenium.webdriver.common.keys import Keys # Inputs del teclado
import sys, os


options = webdriver.ChromeOptions()
#options.add_argument('--start-maximized')
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}

driver_path = '/app/bin/chromedriver'
#driver = webdriver.Chrome(driver_path, chrome_options = options)
driver = webdriver.Chrome( chrome_options = options)

####################################################
def errHandler():
    global driver
    global logdir, scriptname
    
    html = driver.page_source
    #Save return code
    with open(logdir + os.sep + scriptname + ".html", 'w') as fw:
        fw.write(html)

## Main
total = len(sys.argv)

if total < 2:
	print ("Error in params\nscript.py <log file dir>")
	sys.exit(2)

scriptname = os.path.basename(sys.argv[0])
logdir = sys.argv[1]

# print(scriptname)
# print(logdir + os.sep + scriptname + ".html")
# sys.exit(0)
driver.get("https://leroy:l3r0ym3rl1n.2021@wwwpre.leroymerlin.es")


'''
--------------------------------------------------------------
PASO 1 - Acceder a la página
--------------------------------------------------------------
'''
try:
    assert "Bricolaje" in driver.title
    print("\n\nPaso 1 completado: Acceso correcto a la página\n\n")
except:
    print('\n\nFallo en Paso 1\n\n')
    driver.close()
    sys.exit(1)
finally:
    driver.implicitly_wait(5)

'''
--------------------------------------------------------------
PASO 2 - Aceptar cookies
--------------------------------------------------------------
'''
try:
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    print("\n\nPaso 2 completado: Cookies aceptadas\n\n")
except:
    print('\n\nFallo en Paso 2\n\n')
    driver.close()
    sys.exit(1)
finally:
    driver.implicitly_wait(5)

'''
--------------------------------------------------------------
PASO 3 - Acceder a la URL del producto
--------------------------------------------------------------
'''
driver.get("https://wwwpre.leroymerlin.es/fp/82115600")
try:
    assert "GOOGLE Chromecast V3" in driver.title
    print("\n\nPaso 3 completado: Acceso correcto al producto\n\n")
except:
    print('\n\nFallo en Paso 3\n\n')
    driver.close()
    sys.exit(1)
finally:
    driver.implicitly_wait(5)

'''
--------------------------------------------------------------
PASO 4 - Añadir al carrito
--------------------------------------------------------------
'''
try:
    driver.find_element(By.ID, 'add-to-cart').click()
    print("\n\nPaso 4 completado: Producto añadido al carrito\n\n")
except:
    print('\n\nFallo en Paso 4\n\n')
    driver.close()
    sys.exit(1)
finally:
    driver.implicitly_wait(5)
    
driver.close()
print('\n\nTerminado\n\n')
sys.exit(0)
from selenium import webdriver #Permite o uso do browser
from selenium.webdriver.common.by import By # Permite a pesquisa por parametros
from selenium.webdriver.support ui. import WebDriverWait #Permite esperar a pagina carregar
from selenium.webdriver.support import expected_conditions as EC # Determina se a pagina carregou
from selenium.common.exceptions import TimeoutException #Anti-timeout # Resolve eventuais timeouts

driver_option = webdriver.FirefoxOptions()
driver_option.add_argument(' - incognito')

driver = webdriver.Firefox(options=options)

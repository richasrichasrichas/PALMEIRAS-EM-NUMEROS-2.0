# BIBLIOTECAS IMPORTADAS
import selenium
import pandas
from selenium import webdriver #Permite o uso do browser
from selenium.webdriver.common.by import By # Permite a pesquisa por parametros
from selenium.webdriver.support ui. import WebDriverWait #Permite esperar a pagina carregar
from selenium.webdriver.support import expected_conditions as EC # Determina se a pagina carregou
from selenium.common.exceptions import TimeoutException #Anti-timeout # Resolve eventuais timeouts

# CONFIGURAÇAO DO WEBDRIVER E DO SELENIUM
driver_option = webdriver.FirefoxOptions()
driver_option.add_argument(' - incognito')
geckodriver_path = '"C:\Users\ricar\OneDrive\Área de Trabalho\geckodriver.exe"'
def create_webdriver():
return webdriver.Firefox(executable_path=geckodriver_path options=driver_option)

# ABRE O SITE
browser = create_webdriver()
browser.get('https://fbref.com/en/squads/abdce579/Palmeiras-Stats')

# EXTRAI STANDARD STATS DA TEMPORADA 2026 DO PALMEIRAS NA SERIE A
head_stats = browser.find_elements_by_xpath('/html/body/div[4]/div[7]/div[3]/div[3]/table/thead')
body_stats = browser.find_elements_by_xpath('/html/body/div[4]/div[7]/div[3]/div[3]/table/tbody')

# EXTRAI OS STANDARD STATS DE CADA JOGADOR DURANTE A TEMPORADA 2026 DO PALMEIRAS NA SERIE A
stats_list {}
for stats in body_stats:
    player_name =  # NOME DO JOGADOR
    player_country = # NACIONALIDADE DO JOGADOR
    player_pos = # POSIÇÃO DO JOGADOR
    player_age = # IDADE DO JOGADOR
    player_mp = # PARTIDAS JOGADAS NA COMPETIÇÃO PELO JOGADOR
    player_starts = # NUMERO DE TITULARIDADES NA COMPETIÇÃO PELO JOGADOR
    player_mins = # MINUTOS JOGADOS NA COMPETIÇAO PELO JOGADOR
    player_90s = # MINUTOS JOGADOS NA COMPETIÇAO DIVIDIDO POR 90
    player_goals = # GOLS MARCADOS PELO JOGADOR NA COMPETIÇAO
    player_assists = # ASSISTENCIAS FEITAS PELO JOGADOR NA COMPETIÇAO
    player_ga = # GOLS + ASSISTENCIAS FEITAS PELO JOGADOR NA COMPETIÇAO
    player_npk = # GOLS MARCADOS PELO JOGADOR NA COMPETIÇAO, EXCLUINDO OS PENALTIS
    player_pk = # GOLS DE PENALTI CONVERTIDOS PELO JOGADOR NA COMPETIÇAO
    player_pkatt = # QUANTOS PENALTIS FORAM BATIDOS PELO JOGADOR NA COMPETIÇAO
    player_yellowcard = # QUANTOS CARTOES AMARELOS O JOGADOR RECEBEU NA COMPETIÇAO
    player_redcard = # QUANTOS CARTOES VERMELHOS O JOGADOR RECEBEU NA COMPETIÇAO
    player_goalsper90s = # QUANTOS GOLS O JOGADOR NA COMPETIÇAO TEM DIVIDIDOS POR 90 
    player_assistsper90s = # ASSISTENCIAS FEITAS PELO JOGADOR NA COMPETIÇAO DIVIDIDOS POR 90
    player_gaper90s = # GOLS + ASSISTENCIAS FEITAS PELO JOGADOR NA COMPETIÇAO DIVIDIDOS POR 90
    player_npkper90s = # GOLS MARCADOS PELO JOGADOR NA COMPETIÇAO, EXCLUINDO OS PENALTIS DIVIDIDOS POR 90
    player_npkassistsper90s = # GOLS, EXCLUINDO PENALTIS, E ASSISTENCIAS MARCADOS PELO JOGADOR NA COMPETIÇAO DIVIDIDOS POR 90
    
   
# EXTRAI OS DADOS PARA CSV PELO PANDAS
stats_df = pd.DataFrame.from_dict()

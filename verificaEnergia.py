from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Leer las credenciales del archivo
with open('credentials.txt', 'r') as f:
    user = f.readline().strip()
    password = f.readline().strip()
browser = webdriver.Chrome()
browser.maximize_window()
sleep(5)
browser.get('https://www.gokickoff.com/team_tactics.php') 

try:
    userInput = browser.find_element(By.NAME,'user_login')
    userInput.send_keys(user)
    passInput = browser.find_element(By.NAME,'pwd_login')
    passInput.send_keys(password)
    buttonInput = browser.find_element(By.XPATH,'/html/body/center/div[2]/div/div/div[5]/div[1]/div[2]/div/div/form/div[1]/span/span/input')
    buttonInput.click()
    sleep(5)
    rows = browser.find_elements(By.XPATH,'//table[@id="player-table"]/tbody/tr')
    
    min_efficiency = float('inf')  # Iniciar la eficiencia mínima con infinito
    min_efficiency_player = None  # Inicializar el jugador con la eficiencia mínima
    data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME,'td')
        player_id = cells[0].get_attribute('title')
        player_pos = cells[3].text
        player_name = cells[4].find_element(By.TAG_NAME,'a').text
        player_efficiency = float(cells[5].get_attribute('title').replace('%', ''))  # Eliminar '%' y convertir a flotante
        player_rate = cells[6].get_attribute('title')
        
        # Actualizar el jugador con la eficiencia mínima si es necesario
        if player_efficiency < min_efficiency:
            min_efficiency = player_efficiency
            min_efficiency_player = {
                'id': player_id,
                'pos': player_pos,
                'name': player_name,
                'efficiency': player_efficiency,
                'rate': player_rate,
            }

    # Si todos los jugadores tienen una eficiencia mayor que 92%, imprimir un mensaje
    if min_efficiency > 92:
        print(min_efficiency_player)
        print("Todos los jugadores tienen una eficiencia superior al 92%. Se procede a realizar actividades de dinero")
        sleep(5)
        browser.get('https://www.gokickoff.com/activity_souvenirs.php?type=3')
        print("Se realizo correctamente la venta de souvenir!!")
        sleep(5)
    else:
        # Imprimir el jugador con la eficiencia mínima
        print("Jugador con la eficiencia mínima:")
        print(min_efficiency_player)
        sleep(5)
        # ir a https://www.gokickoff.com/activity_player_detail.php?type=4&option=2&player_id= + player_id
        browser.get('https://www.gokickoff.com/activity_player_detail.php?type=4&option=2&player_id=' + min_efficiency_player['id'])
        print("Condicion fisica del jugador actualizada!")
        sleep(5)


except TypeError as e:
    print(e)
    browser.quit()
browser.quit()

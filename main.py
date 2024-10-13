from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

# Função para inicializar o Driver do Chrome
def get_driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Função para enviar uma mensagem no WhatsApp
def send_message(driver, contato, message):
    try:
        # Localizar o campo de pesquisa e digitar o nome do contato
        search_box = driver.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]')
        search_box.send_keys(contato)
        search_box.send_keys(Keys.ENTER)

        sleep(5)  # Reduzido o tempo de espera

        message_box = driver.find_element('xpath', '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)  # Pressione Enter para enviar a mensagem

        sleep(5)  # Reduzido o tempo de espera

    except Exception as e:
        print("Não foi possível enviar a mensagem:", e)

# Inicializa o driver e acessa o WhatsApp Web
driver = get_driver()
driver.get('https://web.whatsapp.com/')
sleep(15)  # Aguarde o usuário escanear o QR code

while True:
    try:
        # Verifique se o QR code foi escaneado
        qr_code = driver.find_element('xpath', '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas')
        if qr_code:
            print("QR code ainda está visível. Aguardando...")
            sleep(20)
        else:
            print("QR code escaneado. Preparando para enviar a mensagem.")
            break
    except Exception:
        break

contato = 'Bia'
mensagem = "Mensagem Automática. Teste..."

send_message(driver, contato, mensagem)

driver.quit()



from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi options untuk browser Firefox
options = Options()
options.headless = False  # Set ke True jika ingin menjalankan secara headless (tanpa tampilan browser)

# Tentukan path ke Gecko driver
gecko_driver_path = '/home/kali/Documents/geckodriver'  # Ganti dengan path yang sesuai di sistem Anda

# Inisialisasi driver menggunakan Gecko driver
web = webdriver.Firefox(options=options, executable_path=gecko_driver_path)

# Mulai Operasi
web.get('http://127.0.0.1:5000')
web.maximize_window()

wait = WebDriverWait(web, 10)

dos_section = web.find_element(By.XPATH, '/html/body/section[1]/nav/ul/li[2]/a')
dos_section.click()

time.sleep(1)

dos_button = web.find_element(By.XPATH, '/html/body/section[2]/section/section/section[1]/button/a')
dos_button.click()

wait.until(EC.title_is("Project DDos")) # Tunggu sampai judul halaman berubah

pilihan_SYN = web.find_element(By.XPATH, '/html/body/section[2]/section/button[1]')
pilihan_SYN.click()

ipv4 = "192.168.3.2"
ip = web.find_element(By.XPATH, '//*[@id="target-ip-field"]')
ip.send_keys(ipv4)

port = 80
po = web.find_element(By.XPATH, '//*[@id="port-number-field"]')
po.send_keys(port)

attack_duration = 10
to = web.find_element(By.XPATH, '//*[@id="attack-duration-field"]')
to.send_keys(attack_duration)

time.sleep(1)

buttonatk = web.find_element(By.XPATH, '/html/body/section[3]/button')
buttonatk.click()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyautogui as pya
import keyboard
import colorama
from colorama import init, Fore, Back, Style
from turtle import back


options = webdriver.ChromeOptions()
options.add_argument('--disable-logging')
options.add_argument("headless")
options.add_argument("--window-size=1366,768");
options.add_argument("--no-sandbox");
options.add_argument("--disable-gpu");
options.add_argument("--disable-crash-reporter");
options.add_argument("--disable-extensions");
options.add_argument("--disable-in-process-stack-traces");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("--log-level=3");
options.add_argument("--output=/dev/null");
init(convert=True)
print(Back.RED + '                                        ===CANLI GRAM ALTIN KURU===                                        ')
print(Back.RESET)

sayi1 = [995.5787] #Yeni kurla karşılaştırma yapmak için kullandığım rastgele sayı. İstediğiniz gibi değiştirebilirsiniz
driver = webdriver.Chrome(options=options)

k = 0
y=0
driver.get("https://canlidoviz.com/altin-fiyatlari/gram-altin")
print("=============================================================================")
print("Veriler alınıyor...")
while True:
        
        time.sleep(5)
        driver.refresh()
        time.sleep(3)
        satis = driver.find_element(By.XPATH,"/html/body/main/div/div[3]/section[1]/div/div[1]/div/div[2]/div[1]/ul/li[2]/strong").text
        alis = driver.find_element(By.XPATH, "/html/body/main/div/div[3]/section[1]/div/div[1]/div/div[2]/div[1]/ul/li[1]/strong").text
        time.sleep(3)
        if (float(satis) > float(sayi1[0])):
            print(Fore.GREEN)
            y+=1
            time.sleep(1)
            print("Satış = ",satis," Artıyor")
            print("Alış = ",alis)
            print("Artıyor = ",y)
            sayi1.clear()
        elif (float(satis) < float(sayi1[0]) ):
            print(Fore.RED)
            k+=1
            time.sleep(1)
            print("Satış = ",satis," Azalıyor")
            print("Alış = ",alis)
            print("Azalıyor = ",k)
            sayi1.clear()
        else:
            print("Değişim Bekleniyor olabilir veya piyasa kapalı")
        sayi1.append(satis)

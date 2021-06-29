import os, sys, subprocess, urllib, time, random, requests, colorama, selenium
from colorama import init, Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

init(autoreset=True)
white = Fore.WHITE + Style.BRIGHT
pink = Fore.MAGENTA + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT

os.chdir(os.path.dirname(__file__))
main_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dank.bin-checker')
try:
    os.mkdir(main_dir)
except:
    pass
os.chdir(main_dir)

try:
    fp = open('prefBrowser.txt', 'r')
except:
    print( "\n> Error! Please run setup.py")
    exit()
typex = fp.read()

try:
    open("generated.txt", "x")
except:
    pass

def bannerTop():
    banner = '''
__________.__                 _________ .__                   __                 
\______   \__| ____           \_   ___ \|  |__   ____   ____ |  | __ ___________ 
 |    |  _/  |/    \   ______ /    \  \/|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \\
 |    |   \  |   |  \ /_____/ \     \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
 |______  /__|___|  /          \______  /___|  /\___  >\___  >__|_ \\\___  >__|   
        \/        \/                  \/     \/     \/     \/     \/    \/       

              /-/                \-\              
            -- /                  \ --            
           /  /                    \  \           
       \  /  --\                  \--  \  /       
       |\-      --   |---\      --      -/|       
       \ -      /-  /     ----  \      -  /       
       --      -   /         |   -      --        
        -      /   | +    +  /   \      -         
      -/      |   /-        |     |      \-       
     /        /     \-      /  /  \        \      
    /        /   -\   \    | /-    \        \     
  -/        /      --\      /       \        \-   
 /         |          --  /-         |         \  
 |         /           | -           \         |  
 \      --|            | |            |--      /  
  | ---/               | |               \--- |   
  |/                   | |                   \|   
  ________.__      ________                 __    
 /   _____|________\______ \ _____    ____ |  | __
 \_____  \|  \_  __ |    |  \\\__  \  /    \|  |/ /
 /        |  ||  | \|    `   \/ __ \|   |  |    < 
/_______  |__||__| /_______  (____  |___|  |__|_ \\
        \/                 \/     \/     \/     \/
'''
    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]
    return ''.join(colored_chars)

sys.stdout.write(bannerTop())

reset = input( white + "\n> " + pink + "Reset generated.txt? { Will not skip old bins } <y|n> ")
if "y" in reset or "Y" in reset:
    open("generated.txt", "w")
    print( white + "\n> " + pink + "Cleared Genrated.txt!")

amount = int(input( white + "\n> " + pink + "How many would you like to generate? { Min 10 } "))

print( white + "\n> " + pink + "Checking Old Bins...")

old_generated = open("generated.txt", "r").read().splitlines()

print( white + "\n> " + pink + "Creating Bins...")

def generator():
    return str(random.randint(3, 5)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

generated = []

while len(generated) < amount:
    bins = generator()
    while bins in old_generated or bins in generated:
        bins = generator()
    generated.append(bins)

print( white + "\n> " + pink + "Saving Bins...")

txt = open("generated.txt", "a+")
for bins in generated:
    txt.write( bins + "\n")
txt.close()

print( white + "\n> " + pink + "Saved!")
print( white + "\n> " + pink + "Starting Browser...")

try:
    # For Chrome
    if typex == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(options = options, executable_path=r'./webdriver/chromedriver')
    # For Firefox
    elif typex == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-gpu")
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Firefox(options = options, executable_path=r'./webdriver/geckodriver')
    elif typex == '':
        print(red + 'Error - Run setup.py first')
        exit()
except Exception as e:
    time.sleep(0.4)
    print('\n' + red + 'Error - '+ str(e))
    exit()

driver.maximize_window()
driver.get("http://www.sayapro.us/bin/")

time.sleep(0.5)
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, 'preloader'))
)

print( white + "\n> " + pink + "Logging In...")

time.sleep(0.5)
driver.find_element_by_name('email').send_keys("dank@emailinfo.org")

time.sleep(0.5)
driver.find_element_by_name('password').send_keys("thisisatestaccount")

time.sleep(0.5)
driver.find_element_by_name('rememberme').click()

time.sleep(0.5)
driver.find_element_by_xpath('//button[contains(text(),"Login")]').click()

print( white + "\n> " + pink + "Navigating to bin-checker...")

time.sleep(0.5)
driver.get("http://www.sayapro.us/bin/")

time.sleep(0.5)
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, 'preloader'))
)

print( white + "\n> " + pink + "Pasting bins...")

paste = ""
for bins in generated:
    paste = paste + f"{bins}\n"

time.sleep(0.5)
driver.find_element_by_xpath('//textarea[@id="creditcard"]').send_keys(paste)

print( white + "\n> " + pink + "Starting Bin Checker...")

time.sleep(0.5)
driver.find_element_by_xpath('//button[@id="submit"]').click()

print( white + "\n> " + pink + "Checking...")

try:
    time.sleep(0.5)
    WebDriverWait(driver, 99999999999999999999).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'100%')]"))
    )
except:
    pass

print( white + "\n> " + pink + "Downloading...")

time.sleep(2)
WebDriverWait(driver, 60).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='result']/div[1]/h3/a"))
).click()

print( white + "\n> " + pink + "Complete! Check your downloads folder :)\n")
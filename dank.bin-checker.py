from setup import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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

amount = int(input( fw+sb + "\n> " + fm+sb + "How many would you like to generate? "))

print( fw+sb + "\n> " + fm+sb + "Creating Bins...")

txt = open("generated.txt", "a+")
for i in range(amount):
    generated_bin = str(random.randint(3, 5)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    txt.write( generated_bin + "\n")
txt.close()

print( fw+sb + "\n> " + fm+sb + "Saved!")
print( fw+sb + "\n> " + fm+sb + "Starting Browser...")

try:
    # For Chrome
    if typex == 'chrome':
        driver = webdriver.Chrome(executable_path=r'./webdriver/chromedriver')
    # For Firefox
    elif typex == 'firefox':
        # cap = DesiredCapabilities().FIREFOX
        # cap['marionette'] = True
        driver = webdriver.Firefox(executable_path=r'./webdriver/geckodriver')
    elif typex == '':
        print(fr + 'Error - Run setup.py first')
        exit()
except Exception as e:
    time.sleep(0.4)
    print('\n' + fr + 'Error - '+ str(e))
    exit()

driver.maximize_window()
driver.get("http://www.sayapro.us/bin/")

time.sleep(0.7)
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, 'preloader'))
)

print( fw+sb + "\n> " + fm+sb + "Logging In...")

time.sleep(0.7)
driver.find_element_by_name('email').send_keys("dank@emailinfo.org")

time.sleep(0.7)
driver.find_element_by_name('password').send_keys("thisisatestaccount")

time.sleep(0.7)
driver.find_element_by_name('rememberme').click()

time.sleep(0.7)
driver.find_element_by_xpath('//button[contains(text(),"Login")]').click()

print( fw+sb + "\n> " + fm+sb + "Navigating to bin-checker...")

time.sleep(0.7)
driver.get("http://www.sayapro.us/bin/")

time.sleep(0.7)
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, 'preloader'))
)

with open('generated.txt', 'r') as file:
    generated = file.read().rstrip('\n')

print( fw+sb + "\n> " + fm+sb + "Pasting from generated.txt...")

time.sleep(0.7)
driver.find_element_by_xpath('//textarea[@id="creditcard"]').send_keys(generated)

print( fw+sb + "\n> " + fm+sb + "Clearing generated.txt...")
open('generated.txt', 'w').close()

print( fw+sb + "\n> " + fm+sb + "Starting Bin Checker...")

time.sleep(0.7)
driver.find_element_by_xpath('//button[@id="submit"]').click()

print( fw+sb + "\n> " + fm+sb + "Checking...\n")

time.sleep(0.7)
WebDriverWait(driver, 999999).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'100%')]"))
)

#driver.find_element_by_class_name("btn btn-success btn-xs").click()

#time.sleep(4)
#WebDriverWait(driver, 60).until(
#    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'download')]"))
#).click()

print( fw+sb + "\n> " + fm+sb + "Complete! Please download the list manually :)")

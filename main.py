
def Initiating_Browser():
    global driver
    
    #Set Options for 
    load_dotenv()
    start_time = time.time()
    chrome_options = Options()
    chrome_options.binary_location = '/opt/chrome/chrome'
    chrome_options.add_argument("--kiosk")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("window-size=2560x1504.5")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
    chrome_options.add_argument(f"--data-path={mkdtemp()}")
    chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    driver = webdriver.Chrome("/opt/chromedriver", chrome_options=chrome_options)

    # Open the website
    driver.get('https://analyser.moneyfacts.co.uk/forms/frmLogin.aspx')

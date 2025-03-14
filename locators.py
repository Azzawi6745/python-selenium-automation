

driver_path = ChromeDriverManager().install()


service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.find_element(By.ID, 'twotabsearchtextbox')
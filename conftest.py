

@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.STELLA_URL)

    yield chrome_driver
    chrome_driver.quit()

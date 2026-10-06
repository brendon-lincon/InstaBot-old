from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstagramBot:

    def __init__(self, username, password):
        
        self.driver = None
        self.username = username
        self.password = password
        
        return None

    def openBrowser(self):
        
        self.driver = webdriver.Chrome()
        
        return None

    def closeBrowser(self):
        
        self.driver.close()
        
        return None
    
    def logon(self):

        def accessTheSite():
            self.driver.get('hhttps://www.instagram.com/accounts/login')
            return None

        def localizeInputs():
            self.usernameInput = self.driver.find_element_by_name('username')
            self.passwordInput = self.driver.find_element_by_name('password')    
            return None

        def clearInputs():
            self.usernameInput.clear()
            self.passwordInput.clear()
            return

        def dataInsertion():
            self.usernameInput.send_keys(self.username)
            self.passwordInput.send_keys(self.password)

        def submitForm():
            self.passwordInput.send_keys(Keys.RETURN)
            return None

        def call():
            try:
                accessTheSite()
                localizeInputs()
                clearInputs()
                dataInsertion()
                submitForm()
            except Exception as error:
                print('An error has occured: ', error)
                return False

        return call()



# import requests
# from bs4 import BeautifulSoup

# page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
# soup = BeautifulSoup(page.text, 'html.parser')

# #last_links = soup.find(class_='AlphaNav')
# #last_links.decompose()

# artist_name_list = soup.find(class_='BodyText')
# artist_name_list_items = artist_name_list.find_all('a')

# for artist_name in artist_name_list_items:
#     names = artist_name.contents[0]
#     print(names)
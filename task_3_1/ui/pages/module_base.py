from selenium import webdriver
from selenium.webdriver import ChromeOptions

from webdriver_manager.chrome import ChromeDriverManager
import math


class ModuleBase:

    def driver(self):
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")
        manager = ChromeDriverManager(version='latest')
        browser = webdriver.Chrome(executable_path=manager.install(),
                                   options=options,
                                   desired_capabilities={'acceptInsecureCerts': True}
                                   )
        return browser

    def calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))

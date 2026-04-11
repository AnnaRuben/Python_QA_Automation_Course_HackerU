def setUP(self):
    self.browser=webdriver.firefox()
    self.addCleanup(self.browser.quit)

def testPageTitle(self):
    self.browser.get("http://www.google.com")
    self.assertIn("Google", self.browser.title)
    

from wifipasswords import WifiPasswords

class Wifi:
    def getPs(self):
        self.pss=WifiPasswords().get_passwords()
        return self.pss
    



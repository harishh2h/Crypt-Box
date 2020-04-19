from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.snackbar import Snackbar
from kivy.properties import ObjectProperty
from plyer import filechooser
from kivy.config import Config

import pyAesCrypt

Config.set('graphics','resizable', False)
class btmnav(BoxLayout):
    scr_mngr = ObjectProperty(None)


    def file_pick(self): # To select file and save the path
        self.file_path = filechooser.open_file(title="Pick a file to encrypt..")
        if self.file_path != []:
            self.path=self.file_path[0]


    def user_password_en(self,password): # To get the password from encryption screen
        self.password=self.password_en.text
        self.Check_en()

    def Check_en(self):
        try:
            if self.password != "" and self.path != '':
                self.encrypt()
            elif self.password == "" :
                Snackbar(text="Enter password to continue !").show()
            else:
                pass

        except:
            Snackbar(text="Choose file to encrypt !").show()

    def encrypt(self):

        pyAesCrypt.encryptFile(str(self.path), str(self.path) + '.aes',str(self.password), 64 * 1024)
        Snackbar(text="Completed !").show()


    def user_password_de(self,password): # To get the password from decryption screen
        self.password=self.password_de.text
        self.Check_de()

    def Check_de(self):
        try:
            if self.password != "" and self.path != '':
                self.decrypt()
            elif self.password == "":
                Snackbar(text="Enter password to continue !").show()
            else:
                pass

        except:
            Snackbar(text="Choose file to decrypt !").show()

    def decrypt(self):
        try:
            pyAesCrypt.decryptFile(self.path, self.path[:-4]  ,self.password, 64 * 1024)
            Snackbar(text="Completed !").show()
        except:
            Snackbar(text="error try again correctly !").show() # error for incorrect password or any other things


class CRYPTBOXApp(MDApp):

    def build(self):
        Window.size = (350,600)
        return btmnav()



if __name__ == '__main__':
    app=CRYPTBOXApp()
    app.run()
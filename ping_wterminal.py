from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

import subprocess
import pythonping
import colorama
from colorama import Fore
colorama.init()

Window.clearcolor = (0.6, .6, .6, 0.5)
Window.size = (360, 600)

#x = (input("Enter Your Ip address separated by (,): "))


class PingApp(App):

    def build(self):
        layo = GridLayout(cols=2)
        #lab = Label(text='Enter ip address separated by commas')
        self.intxt = TextInput(
            text='Enter All IP Addresses Separated by comma')
        self.btn = Button(text='Ping'.upper(), size_hint=(0.3, 0.1),
                          pos_hint={'center_x': 0.5, 'center_y': 0.1},
                          font_size='20sp', on_press=self.prefunc,
                          on_release=self.relfunc)
        layo.add_widget(self.intxt)
        layo.add_widget(self.btn)
        return layo

    def prefunc(self, obj):
        print('----------Starting Ping process---------')
        ipaddr1 = self.intxt.text.split(',')
        for ip in ipaddr1:
            response = subprocess.Popen(
                ['ping', f'{ip}'], stdout=subprocess.PIPE, text=True)
            output = response.communicate()[0]
            if "Received = 4" and "Destination host unreachable" in output:
                print(Fore.RED + f'Unreachable --> Device: {ip}')
            elif " Lost = 4" in output:
                print(Fore.YELLOW + f"Down --> {ip}")
            else:
                print(Fore.GREEN + f"Up --> {ip}")

    def relfunc(self, obj):
        print('----------Ping process Finished---------')


if __name__ == "__main__":
    PingApp().run()

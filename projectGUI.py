import webbrowser
import tkinter
from tkinter import *

url_donate = "https://forms.gle/cw6j3NFK4HuHX6FY6"
url_get = 'https://docs.google.com/spreadsheets/d/1vVXxcJA-FR1sWHcOyxjkONe0j1W_ktpwcn_se3zbXks/edit?resourcekey#gid=394200555"
url_library = "https://venkateshwarschool-my.sharepoint.com/:p:/g/personaI/keishaarora278_vgs_net_in/EYtJTmKNI4NJtddzsjDH2FkBkOyeSDi_4h-7BMJNQwPauQ?e=9ez1qz"

window = tkinter.Tk()
window.title('BookDonating')

def link_donate():
    webbrowser.open(url_donate)

def link_get():
    webbrowser.open(url_get)

def link_library():
    webbrowser.open(url_library)

tkinter.Button(window, text='Donate', command=link_donate).pack()
tkinter.Button(window, text='Get', command=link_get).pack()
tkinter.Button(window, text='Library', command=link_library).pack()


from infi.systray import *
import socket
import ctypes


def meuIP(systray):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ctypes.windll.user32.MessageBoxW(0, s.getsockname()[0], "IP", 0)
    s.close()

menu_options = (("Meu IP", None, meuIP),)
systray = SysTrayIcon("icon.ico", "Teleperformance", menu_options)
systray.start()

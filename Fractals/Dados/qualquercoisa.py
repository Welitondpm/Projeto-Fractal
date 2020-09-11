# pip3 install py-cpuinfo

import cpuinfo
print(cpuinfo.get_cpu_info()['brand_raw'])


# import platform,socket,psutil
# from tkinter import *
# def verificarSistema():
#     info={}
#     info['platform']=platform.system()
#     info['platform-release']=platform.release()
#     info['platform-version']=platform.version()
#     info['architecture']=platform.machine()
#     info['hostname']=socket.gethostname()
#     info['processor']=platform.processor()
#     info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))
#     if(int(info['ram'])<2):
#         class Application:
#             def __init__(self, master=None):
#                 self.widget1 = Frame(master)
#                 self.widget1.pack(side=LEFT)
#                 self.msg = Label(self.widget1, text="ram insuficiente para o sistemacolibri")
#                 self.msg["font"] = ("Verdana", "10", "italic", "bold")
#                 self.msg.pack()
#                 self.sair = Button(self.widget1)
#                 self.sair["text"] = "OK"
#                 self.sair["font"] = ("Verdana", "10")
#                 self.sair["width"] = 5
#                 self.sair["command"] = self.widget1.quit
#                 self.sair.pack(side=RIGHT)
#         root = Tk()
#         Application(root)
#         root.mainloop()
#     if(int(info['ram'])<4):
#         class Application:
#             def __init__(self, master=None):
#                 self.widget1 = Frame(master)
#                 self.widget1.pack(side=LEFT)
#                 self.msg = Label(self.widget1, text="memoria ram fora do recomentdado")
#                 self.msg["font"] = ("Verdana", "10", "italic", "bold")
#                 self.msg.pack()
#                 self.sair = Button(self.widget1)
#                 self.sair["text"] = "OK"
#                 self.sair["font"] = ("Verdana", "10")
#                 self.sair["width"] = 5
#                 self.sair["command"] = self.widget1.quit
#                 self.sair.pack(side=RIGHT)
#         root = Tk()
#         Application(root)
#         root.mainloop()
#     if (info['platform-release']=="10"):
#         if(info['platform-release']=="8"):
#             if (info['platform-release'] == "8.1"):
#                 print()
#     else:
#         class Application:
#             def __init__(self, master=None):
#                 self.widget1 = Frame(master)
#                 self.widget1.pack(side=LEFT)
#                 self.msg = Label(self.widget1, text="sistema operacional incompativel com colibri")
#                 self.msg["font"] = ("Verdana", "10", "italic", "bold")
#                 self.msg.pack()
#                 self.sair = Button(self.widget1)
#                 self.sair["text"] = "OK"
#                 self.sair["font"] = ("Verdana", "10")
#                 self.sair["width"] = 5
#                 self.sair["command"] = self.widget1.quit
#                 self.sair.pack(side=RIGHT)
#         root = Tk()
#         Application(root)
#         root.mainloop()
#         print("sistema operacional incompativel com colibri")
#     print(info)
# verificarSistema()
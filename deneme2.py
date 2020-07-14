class User:
    def __init__(self, username, password , email):
        self.username=username
        self.password=password
        self.email=email


class Repository:
    def __init__(self):
        self.users=[]
        self.IsloggedIn = False
        self.CurrentUser = {}
        
    def register(self):
        pass
    def login(self):
        pass
    def savetofile(self):
        pass




while True:
    print('menü'.center(50,'*'))
    secim=input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz : ')
    if secim == '5':
        break
    else:
        if secim == '1':
            pass #register
        elif secim == '2':
            pass #Login
        elif secim == '3':
            pass #logout
        elif secim == '4':
            pass #Identity(display username)
        else:
            print('yanlış seçim')

from enemigo import *

class zombie(enemigo):
    def_init_(self,puntos_energia=10,ataque=1):
    super()._init_(tipo_enemigo="zombie",puntos_energia=puntos_energia,ataque=ataque)

    def habla(self):
        print("hummm......")

    def propagar_enfermedad(self):
        print("el zombie esta tratando de propagar su enfermedad!!!")
        
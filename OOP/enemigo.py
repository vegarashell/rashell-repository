class enemigo:
    tipo_enemigo: str
    puntos_energia: int=10
    ataque=1

    def _init_(self,tipo_enemigo,puntos_energia=10, ataque=1):
        self
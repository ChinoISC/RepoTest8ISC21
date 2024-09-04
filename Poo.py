from functions.roles import Roles

class PublicUsuario(Roles):
    def __init__(self,nombre,app,apm):
        self.nombre = nombre

    def nombre_usuario(self,in_nombre):
        return (in_nombre)
    
    def Admin(self):
        return 'Eres Admin'

Jose = PublicUsuario()
print(Jose.Admin())
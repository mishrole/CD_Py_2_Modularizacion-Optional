local_val = "unicornios mágicos"
def square(x):
    return x * x
class Usuario:
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hola"

# Pasamos esto dentro de la condición según namespace
# print(square(5))
# user = Usuario("Anna")
# print(user.name)
# print(user.di_hola())

# Namespace
# Imprime __main__ al ejecutar padre.py
# Imprime padre al ejecutar hijo.py con import padre.py
print(__name__)

if __name__ == '__main__':
    print('El archivo se está ejecutando directamente')
    
    print(square(5))
    user = Usuario("Anna")
    print(user.name)
    print(user.di_hola())
else:
    print('El archivo se está ejecutado porque es importado por otro archivo. El archivo se llama:', __name__)
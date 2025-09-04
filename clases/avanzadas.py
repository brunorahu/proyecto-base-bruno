class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado1 = 0
        self.resultado2 = 0


        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1:"))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2:"))
                break
            except Exception:
                print("Número inválido")
                continue    
    
    def potencia(self):
        self.resultado1 = "La potencia de " + str(self.num1) + " ^ " + str(self.num2) + " es igula a " + str(self.num1 ** self.num2)
        
    def raiz_cuadrada(self):
        self.resultado2 = "La raíz del número 1 es " + str(self.num1 ** .5) + " La raíz del número 2 es " + str(self.num2 ** .5)

    def mostrarResultado(self):
        print(self.resultado1)
        print(self.resultado2)
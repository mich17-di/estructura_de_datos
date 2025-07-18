#se importa la clase lista numero
from lista_dato import lista_numeros

objlista=lista_numeros()

#creamos la clase calculadora
class calculadora():
    
    def pedir_numero(self):
        numero1=input ("numero 1: ")
        numero2=input ("numero 2: ")
        return numero1, numero2
    
#se almacenan los datos 
    def almacenarDatos(self, dato1, dato2):
        dato_numero=[dato1, dato2]
        objlista.incluir_listas(dato_numero)

#nuevos datos para extender la lista
    def agregarLista(self):
        print ("\nDigite dos nuevo datos para extender la lista: ")
        num1,num2=self.pedirNumero()
        nuevaLista=[num1,num2]
        lista_numeros.insertarLista([nuevaLista])
    
# Se obtiene la posición en donde se desea insertar el dato ya determinado  
    def añadirDato(self):
        Dato1=input("\nDato 1:")
        Dato2=input("Dato 2:")
        sublista=([Dato1,Dato2])
        posicion=int(input(f"\nDigite la posición en que desea insertar la sublista: ")) 
        lista_numeros.almacenarDato(posicion,sublista)          
        return posicion,sublista



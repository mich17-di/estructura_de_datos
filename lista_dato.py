from formulario import calculadora 

class lista_numeros:
    
    def __init__(self):
        self.lista_numeros=[]
        
# Se guardan los datos anteriormente digitados
    def guardarDatos(self,datoNumero):
        self.lista_numeros.append(datoNumero)
        print(f"\nLista con datos agregados anteriormente: {self.lista_numeros}")
        
# Se inserta una nueva sublista para extenderla
    def insertarLista(self,nuevaLista):
        self.lista_numeros.extend(nuevaLista)
        print("\nLa lista con datos extendidos es: ",self.lista_numeros)

# Se insertan datos a la lista, dependiendo de la posiciónque se indique
    def almacenarDato(self,posicion,sublista):
        self.lista_numeros.insert(posicion,sublista)
        print(f"\nLista con los nuevos datos insertados: {self.lista_numeros}")

# Se elimina los datos de la sublista que se encuentre en la posición que se indique     
    def eliminarDato(self,posicion,):
        numeroEliminado=self.lista_numeros.pop(posicion)
        print(f"\nEl dato {numeroEliminado} ha sido eliminado")
        print(f"Lista actualizada: {self.lista_numeros}")
           
# Se elimina la sublista que contenga los números ingresados 
    def remover(self,datos):
        self.lista_numeros.remove(datos)
        print("\nLista actualizada con datos removidos: ",self.lista_numeros)
        
# Muestra la posición de la sublista que contenga los números ingresados        
    def mostrarPosicion(self,datos):
        print(f"\nLos datos {datos} se encuentran en posición: ", {self.lista_numeros.index(datos)})

# Muestra la posición de la sublista que contenga los números ingresados    
    def mostrarContador(self,datos):
        print(f"\nLos datos {datos} se repiten {self.lista_numeros.count(datos)} veces")

# Ordena las sublistas ingresadas de forma ascendente 
    def ordenAscendente(self):
        self.lista_numeros.sort()
        print ("\nLa lista ordenada ascendentemente es: ", self.lista_numeros)

# Ordena las sublistas ingresadas de forma descendente        
    def ordenDescendente(self):
        self.lista_numeros.reverse()
        print ("\nLa lista ordenada descendentemente es: ", self.lista_numeros)
        
# Se muestra el elemento encontrado en el indice que se que se indique
    def verNumero(self,posicion):
        numero=self.lista_numeros.index(posicion)
        return numero

                               
        
        
        
        
        
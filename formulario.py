
objlista=lista_numeros
class calculadora:
    
    def pedir_numero(self):
        numero1=input ("numero 1: ")
        numero2=input ("numero 2: ")
        return numero1, numero2
    
    def almacenarDatos(self, dato1, dato2):
        dato_numero=[dato1, dato2]
        objlista.incluir_listas(dato_numero)
        
calculadora=calculadora()
dato1,dato2=calculadora.pedir_numero()
calculadora.almacenarDatos(dato1,dato2)

dato1,dato2=calculadora.pedir_numero()
calculadora.almacenarDatos(dato1,dato2)




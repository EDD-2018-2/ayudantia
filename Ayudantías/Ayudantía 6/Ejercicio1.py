# Considere que una Cadena de Bloque atómica es una estructura de datos 
# donde existe una única dirección en cuanto al sentido,
#  por lo que un nodo solo puede apuntar al siguiente nodo de la cadena. 
# Además, debe saber que en cada cadena los componentes 
# poseen un identificador único que siempre se puede obtener, pero nunca modificar, 
# dado por la operación siguiente: 

# ID = Numero_Primo_(x-1) * Numero_Primo(x-2)

# Donde:
# Numero_Primo_(x-1) es el número primo antecesor a “x”. Ejemplos:
# Si x = 7, Numero_Primo(x-1) = 5 
# Si x = 10, Numero_Primo(x-1) = 7 

# Numero_Primo_(x-2) es el número primo antecesor a “Numero_Primo_(x-1)”. Ejemplos:
# Si Numero_Primo_(x-1) = 5, Numero_Primo(x-2) = 3 
# Si Numero_Primo_(x-1) = 11, Numero_Primo(x-2) = 7 

# Además, se considera que 

# x = Posicion_En_La_Cadena + ID_Nodo_Anterior 

# y Posicion_En_La_Cadena es el índice que ocupará el nodo en la cadena 
# considerando que el primero de la cadena es el índice 1. 

# El ID del primer bloque siempre será 6.

# Luego, el primer bloque de la cadena tendrá ID = 6, 
# el segundo bloque de la cadena tendrá el ID = 35, 
# el tercer bloque de la cadena tendrá el ID = 1147 y así sucesivamente.

# Considerando lo anterior genere en Python 3:
# (03 puntos) La clase Nodo para este enunciado con los atributos y métodos correspondientes.
# (03 puntos) La clase CadenaDeBloque que inicia vacía. Solo declare la clase y genere el constructor con un máximo de dos nodos centinela y sin otros atributos. 
# (04 puntos) Para la Clase CadenaDeBloque escriba el método “eliminarBloque(self)” que saca el último bloque ha sido ingresado en la cadena
# (10 puntos) Para la Clase CadenaDeBloque escriba el método “insertarBloque(self)” que ingresa un nuevo bloque a la cadena considerando lo descrito anteriormente.  

# No programe nada que no haya sido solicitado y  no asuma nada preexistente.

# def primos(numero_base):
#     es_primo = False
#     while True:

#     for a in range(numero)


class Nodo:

    def __init__(self, pos = 1, idAnterior = 0):
        self.next = None
        self.id = self.idGenerator(pos, idAnterior)
    
    def idGenerator(self, pos, idAnterior):
        if pos == 1:
            return 6
        x = pos + idAnterior
        primos = []
        for i in range(x-1, 1, -1):
            es_primo = True
            for j in range(2, i):
                if i%j == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(i)
                if len(primos) == 2:
                    break
        id = primos[0] * primos[1]
        return id
    
    def getId(self):
        return self.id

class CadenaDeBloque:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def eliminarBloque(self):
        if self.head == None:
            print("Cadena vacia")
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            print("Bloque eliminado")
        else:
            temp = self.head
            while True:
                if temp.next.next == None:
                    id = temp.next.getId()
                    temp.next = None
                    self.tail = temp
                    self.size -= 1
                    print("Bloque con id " + str(id) + " eliminado satisfactoriamente")
                    break
                temp = temp.next

    def insertarBloque(self):
        if self.head == None:
            nodo = Nodo()
            self.head = nodo
            self.tail = self.head
            self.size += 1
            print("Bloque agregado exitosamente, id: ", nodo.getId())
        else:
            nodo = Nodo(self.size+1, self.tail.getId())
            self.tail.next = nodo
            self.tail = nodo
            self.size += 1
            print("Bloque agregado exitosamente, id: ", nodo.getId())

if __name__=="__main__":
    cadena = CadenaDeBloque()
    cadena.insertarBloque()
    cadena.insertarBloque()
    cadena.insertarBloque()
    cadena.insertarBloque()
    cadena.eliminarBloque()
    cadena.eliminarBloque()
    cadena.eliminarBloque()
    cadena.eliminarBloque()
    cadena.eliminarBloque()
    pass
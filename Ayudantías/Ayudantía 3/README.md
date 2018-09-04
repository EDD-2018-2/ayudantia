## Contenidos

* Colas
* Colas de prioridad


## Colas

#### Implementación

```python

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def empty(self):
        return self.head == None
     def push(self, data, priority):
        node = Node(data, priority)
        if self.empty():
            self.head = node
            self.tail = node
            self.count += 1
        else:
            self.tail.next = node
            self.tail = node
            self.count += 1
    def find(self):
        if self.empty():
            return None
        else: 
            temp = self.head
            prev_high_node = temp
            high_node = temp
            while temp.next != None:
                if temp.next.priority > high_node.priority
                    prev_high_node = temp
                    high_node = temp.next
                temp = temp.next
        return prev_high_node, high_node
    def pop(self):
        if self.empty():
            print("Cola vacia")
        elif self.count == 1:
            self.head = None
            self.tail = None
        else:
            prev_dequeue, to_dequeue = self.find()
            if prev_dequeue == to_dequeue:
                self.head = to_dequeue.next
            else:
                prev_dequeue.next = to_dequeue.next
                to_dequeue.next = None
            self.count -= 1
    def front(self):
        if self.empty():
            return None
        return self.head
    def back(self):
        if self.empty():
            return None
        return self.tail
```


## Colas de prioridad

Es una EDD similar a las colas en la que los elementos además tienen asignada una prioridad.
En una cola de prioridad un elemento con mayor prioridad será desencolada antes que un elemento con mayor prioridad.

#### Operaciones

Debe soportar al menos las siguientes operaciones:

* Encolar: Que añada un elemento a la cola con su correspondiente prioridad.
* Desencolar: Que desencole el elemento con mayor prioridad.

## Ejercicios

#### Ejercicio 1

Implemente la clase Cola con los métodos:
* Push
* Pop
* Front
* Back
* Empty

#### Ejercicio 2

Sea Q una cola de enteros no vacía, y S una pila de enteros inicialmente vacía. Use sólo las operaciones de las clases `Pila` y `Cola` y una única variable auxiliar `x` para invertir el orden de los elementos en Q.

#### Ejercicio 3

Implementar Cola de prioridad

#### Ejercicio 4

Modifique la implementación de Cola de prioridad para que al insertar un elemento este sea ubicado en la cola de acuerdo a su prioridad.
"""
Diseñe un algoritmo de ordenamiento tipo *insertion sort* 
para ser utilizado sobre una pila. 
Indique la complejidad algorítmica del mejor y peor caso para su algoritmo.
"""
from stack import Stack, Node

def insertion_sort(stack):
    aux = Stack()
    while stack.size() > 0:
        current = stack.top()
        stack.pop()
        while True:
            if aux.size() == 0:
                aux.push(current.data)
                break
            elem = aux.top()
            aux.pop()
            if elem.data >= current.data:
                aux.push(elem.data)
                aux.push(current.data)
                break
            else:
                stack.push(elem.data)
    return aux

if __name__ == "__main__":
    stack = Stack()
    stack.push(180)
    stack.push(979)
    stack.push(932)
    stack.push(238)
    stack.push(346)
    stack.push(226)
    stack.push(643)
    stack.push(738)
    stack.push(132)
    stack.push(179)
    stack.push(400)
    stack.push(99)
    stack.push(238)
    stack.push(9)
    print("Tope: ", stack.top().data)
    stack = insertion_sort(stack)
    print("Pila ordenada: " + str(stack))

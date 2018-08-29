# Casino Mr. Burns

valores = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'D': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 20
}

pintas = {
    'T': 1,
    'D': 2,
    'C': 3,
    'P': 4
}

class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def __str__(self):
        return '{valor} de {pinta}'.format(valor = self.valor, pinta = self.pinta)
    
    def es_menor(self, carta):
        valor  = valores[self.valor]
        pinta = pintas[self.pinta]
        valor_carta = valores[carta.valor]
        pinta_carta = pintas[carta.pinta]

        if pinta < pinta_carta:
            return True
        elif pinta == pinta_carta:
            if valor < valor_carta:
                return True
        return False

    def es_igual(self, carta):
        if self.valor == carta.valor and self.pinta == carta.pinta:
            return True
        return False   
    
class Mazo:
    def __init__(self):
        self.mazo = []
    
    def __str__(self):
        texto = '=== Mazo ===\n'
        for carta in self.mazo:
            texto += carta.__str__() + '\n'
        return texto

    def agregar(self, carta):
        for _carta in self.mazo:
            if _carta.valor == carta.valor and _carta.pinta == carta.pinta:
                return False
        self.mazo.append(carta)
        return True
    
    def observar(self):
        if self.mazo[-1].es_menor(self.mazo[-2]):
            return 'Es menor'
        elif self.mazo[-1].es_igual(self.mazo[-2]):
            return 'Es igual'
        return 'Es mayor'     

if __name__=="__main__":
    carta = Carta('2', 'C')
    carta_2 = Carta('3', 'C')
    carta_3 = Carta('2', 'C')
    print(carta.es_menor(carta_2))
    print(carta.es_igual(carta_2))
    mazo = Mazo()
    print(mazo)
    mazo.agregar(carta)
    mazo.agregar(carta_2)
    print(mazo)
    mazo.agregar(carta_3)
    print(mazo)
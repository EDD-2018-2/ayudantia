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
    def __init__(self, numero, pinta):
        self.numero = numero
        self.pinta = pinta
    
    def __str__(self):
        return ("{numero} de {pinta}".format(numero = self.numero, pinta = self.pinta))
    
    def imprimir(self):
            print("{numero} de {pinta}".format(numero = self.numero, pinta = self.pinta))

    def es_igual(self, carta):
        if self.numero == carta.numero and self.pinta == carta.pinta:
            return True
        return False

    def es_menor(self, carta):
        valor = valores[self.numero]
        valor_carta = valores[carta.numero]
        pinta = pintas[self.pinta]
        pinta_carta = pintas[carta.pinta]

        if pinta < pinta_carta:
            return True
        elif pinta == pinta_carta:
            if valor < valor_carta:
                return True
        return False

        
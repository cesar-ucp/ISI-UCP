from pila import Pila
def verificarParentesis(cadenaSimbolos):
    p = Pila() #crear on objeto p de la clase Pila
    balanceados = True
    indice = 0
    while indice < len(cadenaSimbolos) and balanceados:
        simbolo = cadenaSimbolos[indice]
        if simbolo == "(":
            p.incluir(simbolo)
        else:
            if p.estaVacia():
                balanceados = False
            else:
                p.extraer()

        indice = indice + 1

    if balanceados and p.estaVacia():
        return True
    else:
        return False

print(verificarParentesis('()'))
print(verificarParentesis('((()))'))
print(verificarParentesis('(()'))

'( )'

p = ['(' ]
p = [ ]
"""
Módulo principal
"""

# Do módulo menus, do pacote graga, import o menu_principal
from graga.menus import menu_principal

def cena1():
    """
    DEscrição da cena 1
    """
    pass

def cena2():
    """
    DEscrição da cena 1
    """
    pass

def cena3():
    """
    DEscrição da cena 1
    """
    pass

def cena4():
    """
    DEscrição da cena 1
    """
    pass

# Função principal
def main():
    op = int(input(menu_principal))
    while op != 5:
        if op == 1:
            cena1()
        elif op == 2:
            cena2()
        elif op == 3:
            cena3()
        elif op == 4:
            cena4()
        else:
            print("Opção inválida")

        op = int(input(menu_principal))

# Chamada da função principal
main()
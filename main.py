# MODULO DE VENDAS LANCHONETE
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso  
# Created Date: Mar-2022
# version ='1.0'
# ---------------------------------------------------------------------------

from vendas import VendasLanchonete

if __name__ == "__main__":
    comanda1 = VendasLanchonete("Mesa-01")
    while True:
        print(" 1 -> Abrir a comanda.")
        print(" 2 -> Fechar a comanda.")
        print(" 3 -> Sair.")
        opcao = int(input("Digite sua opçcao: "))
        if opcao == 1:
            comanda1.cardapio()
            comanda1.fatura_comanda()
            print(comanda1.comanda)
            continue
        elif opcao == 2:
            comanda1.finaliza_comanda()
            continue
        elif opcao == 3:
            print("Saindo")
            break
        else:
            print("Opcao invalida...")
            continue

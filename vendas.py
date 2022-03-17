# MODULO DE VENDAS LANCHONETE
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso  
# Created Date: Mar-2022
# version ='1.0'
# ---------------------------------------------------------------------------


class VendasLanchonete:
    def __init__(self, comanda):
        self.comanda = comanda
        self.valor_pedido = 0
        self.lista_de_pedidos = []
        self.finalizada = False 


    def cardapio(self):
        print(41*"-")
        print("| 100 |      Hot-Dog         | R$ 9,00  |")
        print("| 101 |      X-Salada        | R$ 11,00 |")
        print("| 102 |      X-Tudo          | R$ 15,00 |")
        print("| 103 |      X-Tudo Duplo    | R$ 17,00 |")
        print("| 104 |      Pizz            | R$ 20,00 |")
        print("| 200 |      Refrigerante    | R$ 4,00  |")   
        print("| 201 |      Suco            | R$ 5,00  |")
        print("| 202 |      Agua            | R$ 2,00  |")
        print(41*"-")


    def fatura_comanda(self):
        lista_de_produtos = [[100,"Hot-Dog,",9],[101,"X-Salada",11],[102,"X-Tudo",15],[103,"X-Tudo Duplo",17],
        [104,"Pizza",20],[200,"Refrigerante",4],[201,"Suco",5],[202,"Agua",2]]
        if self.finalizada == False:
            print("DIGITE '0' PARA SAIR DO PEDIDO E FINALIZAR O PEDIDO")
            print("DIGITE '1' PARA O SUBTOTAL DA COMANDA.")
            print(f"SUA COMANDA É {self.comanda}")
            while True:    
                itens = int(input("Digite o codigo do item que deseja pedir: "))
                if itens == 0:
                    print("Saindo do pedido")
                    break
                elif itens == 1:
                    print(f"Subtotal da sua conta é: R$ {(float(self.valor_pedido)):.2f}")
                    continue
                else:
                    if itens in [lista_de_produtos[i][0] for i in range(len(lista_de_produtos))]:
                        for i in lista_de_produtos:
                            if i[0] == itens:
                                print(f"Codigo {i[0]}, pedido {i[1]}.")
                                self.lista_de_pedidos.append([i[1],i[2]])
                                self.valor_pedido = self.valor_pedido + i[2]
                                break
                    else:
                        print("Opcao invalida")          
        else:
            print(f"A comanda {self.comanda} esta finalizada.")


    def finaliza_comanda(self):
        if self.finalizada == False:
            self.finalizada = True
            print("Seu pedido foi: ")
            for i in self.lista_de_pedidos:
                print(f"{i[0]} - {i[1]}")
            print(f"Valor total de R$ {self.valor_pedido}")
            print("VOLTE SEMPRE...")
        else:
            print("Pedido da comanda ja esta finalizado.")

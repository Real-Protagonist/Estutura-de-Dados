# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 08:16:28 2023

@author: User
"""

import sys 
from collections import Counter

class nodoLista: #Representa os nós de uma lista encadeada
    def __init__(self, dado = 0, proximo_nodo = None):
        self.dado = dado
        self.proximo = proximo_nodo
    
    def __repr__(self):
        return '%s -> %s'% (self.dado, self.proximo)


class lista_encadeada: #Representa uma lista encadeada
    def __init__(self):
        self.cabeca = None
    
    def __repr__(self):
        return "[" +str(self.cabeca) + "]"
    
    def insere_inicio(self, lista, novo_dado):
        novo_nodo = nodoLista(novo_dado)      # Cria o node
        novo_nodo.proximo = lista.cabeca  # Faz o node apontar para a cabeca
        lista.cabeca = novo_nodo              # Faz o apontador da cabeca apontar para o node novo
        
    def inserir_depois_de(self, lista, nodo_anterior, novo_dado):
        assert nodo_anterior  #verificando se tem na lista
        novo_nodo = nodoLista(novo_dado)
        novo_nodo.proximo = nodo_anterior.proximo
        nodo_anterior.proximo = novo_nodo
    
    def busca_na_lista(self, lista, valor):
        valor_corrente = lista.cabeca
        print(lista.cabeca)
        print("Inicialmente esse é o valor_corrente: ", (valor_corrente))
        print("Inicialmente esse é o valor_corrente.dado: ", (valor_corrente.dado))
        while(valor_corrente and valor_corrente.dado != valor): #observa o par de dados 
            print("valor_corrente: %s ", (valor_corrente))
            print("valor_corrente.proximo: ", (valor_corrente.proximo))
            valor_corrente = valor_corrente.proximo
        return valor_corrente
    
    def remove(self, valor):
        assert self.cabeca #impossivel remover valor de lista vazia
        
        #removendo se for a cabeca da lista: 
        if(self.cabeca.dado == valor):
            self.cabeca = self.cabeca.proximo #recebe um vazio 
        
        else: 
            anterior = None
            corrente = self.cabeca
            
            print("---------------------------")
            print("valor de self corrente: ", corrente)
            print("valor de corrente.proximo: ", corrente.proximo )
            print("valor de self.cabeca: ", self.cabeca)
            print("---------------------------")
            
            #buscando o elemento
            while(corrente and corrente.dado != valor):
                anterior = corrente
                corrente = corrente.proximo
                print("---------------------------")
                print("valor de self corrente: ", corrente)
                print("valor de corrente.proximo: ", corrente.proximo )
                print("valor de self.cabeca: ", self.cabeca)
                print("---------------------------")
            # O nodo corrente é o nodo a ser removido.
            if corrente:                
                anterior.proximo = corrente.proximo
            else:
                # O nodo corrente é a cauda da lista.
                anterior.proximo = None
    
    def menu(self,lis):
        freq = Counter(lis).most_common()
        mas, men = freq[0], freq[-1]
        
        print(f'Mais: {mas[0]}, occorendo {mas[1]}')
        print(f'Mais: {men[0]}, occorendo {men[1]}')

        
if __name__ == '__main__':

    lista = lista_encadeada()
    print("Lista vazia:", lista)
    
    lista.insere_inicio(lista, "e")
    lista.insere_inicio(lista, "b")
    lista.insere_inicio(lista, "a") 
    lista.insere_inicio(lista, "a") 
    lista.insere_inicio(lista, "b") 
    lista.insere_inicio(lista, "a") 
    
    print("Lista: \n \n", lista)
    
    print("\n \n ")
    
    print("removendo elemento  5")
    
    #lista.remove("e")
    
    print("++++Lista: \n \n", lista)
    
    
    print("Buscando elemento na lista 7: \n \n")
    print("processo de busca na lista: \n \n")
    
    lista.busca_na_lista(lista, 7)
    lista.menu(lista)
    
    #lista.menu(lista)
    #nodo_anterior = lista.cabeca
    #lista.insere_depois(lista, nodo_anterior, 10)
    #print("Inserindo um novo elemento depois de um outro:", lista)
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:48:37 2023

@author: #...
"""
import collections

nome = ['a','a','b','a','b','e','a']

def opcao():
    opcao = input('''Digite uma opção: 
    1 - Imprimir Dados
    2 - Inserir Dados
    3 - Buscar Dados
    4 - Inverter
    5 - Ocorrencia
    X - Sair
    
    :''')
    print("")
    if opcao == '1':
        imprimir()
    elif opcao == '2':
        inserir()
    elif opcao == '3':
        buscar()
    elif opcao == '4':
        inverter(nome)
    elif opcao == '5':
        ocorrencia(nome)
    elif opcao.upper() == 'X':
        exit()
    else:
        print("Opção inválida, tente novamente!")

def imprimir():
    opcao_imprimir = input("Digite o numero do índice que você quer imprimir, ou escreva 'todos' para imprimir todos os elementos: ")
    print("")

    try:
        if opcao_imprimir.upper() == 'TODOS':
            for indice in range(0,len(nome)):
                print(f"Nome.{indice + 1}: {nome[indice]}")
        else:
            print(f"Nome.{int(opcao_imprimir)}: {nome[int(opcao_imprimir) - 1]}")
    except:
        print("Ocorreu um erro, tente novamente!")
        opcao()

def inserir():
    indice = input("Digite a posição em que você quer inserir o valor [escreva 'ultima' para inserir no final da lista]: ")
    valor = input("Digite o valor que você quer inserir: ")
    try:
        if indice.upper() == 'ULTIMA':
            nome.append(valor)
        else:
            nome.insert(int(indice) - 1,valor)
    except:
        print("Erro, tente novamente!")

def buscar():
    busca = input("Digite o nome do elemento que você deseja buscar ou a posição do mesmo: ")

    try:
        if not busca.isdigit():
            for indice in range(0,len(nome)):
                if busca == nome[indice]:
                    print(f"Nome.{indice + 1}: {nome[indice]}")
                    elemento_busca = indice
        elif busca.isdigit():
            print(nome[int(busca)-1])
            elemento_busca = int(busca)-1
        
        menu(elemento_busca)
        
    except:
        print("Elemento não encontrado!")
        
def excluir(elemento):
    del[nome[elemento]]
    print("Elemento excluido com sucesso!")

def alterar(elemento):
    nome[elemento] = input("Digite o novo valor do elemento: ")
    print("Elemento alterado com sucesso!")
    
#  FUNÇÃO INVERTER LISTA LINEAR
#+++++++++++++++++++++++++++++++++
def inverter(lista):
    print("LISTA INVERTIDA:\n")
    indice = (len(lista)) - 1
    i = 0
    while (indice >= i):
        print(f"Nome.{indice+1}: {lista[indice]}")
        indice -= 1

#  FUNÇÃO PARA MAIOR E MENOR OCORRÊNCIA
#+++++++++++++++++++++++++++++++++++++++
def ocorrencia(lista):
    maiorO = 0
    menor = len(lista)
    nmalist = []
    nmelist = []
    rept = collections.Counter(lista)
    for lis in lista:
        elem = lis
        if (rept[elem] > maiorO):
            nmalist.clear()
            maiorO = rept[elem]
            i = 0
            while (i < rept[elem]):
                nmalist.append(elem)
                i += 1
        elif (rept[elem] < menor):
            nmelist.clear()
            menor = rept[elem]
            i = 0
            while (i < rept[elem]):
                nmelist.append(elem)
                i += 1
                
    print(f"Maior ocorrência {maiorO}, valor ({nmalist})")
    print(f"Maior ocorrência {menor}, valor ({nmelist})")
    
def menu(x):
    menu = input('''Digite uma opção: 
    1 - Alterar Elemento
    2 - Excluir Elemento
    X - Voltar para o menu
    :''')
    print("")
    if menu == '1':
        alterar(x)
    elif menu == '2':
        excluir(x)
    elif menu.upper() == 'X':
        opcao() 
    else:
        print("Opção inválida, tente novamente!")

while True:
    print("")
    opcao()
    print("")
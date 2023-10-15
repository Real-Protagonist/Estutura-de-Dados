# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 09:57:15 2023

@author: #...
"""

import builtins
builtins.raw_input = builtins.input

class Node:

    def __init__(self,data):
        self.data = data
        self.next = next = None
        self.previous = previous = None
        

class DoublyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.numElements = 0
        self.exist = False

    def isEmpty(self):
        if self.head == self.tail == None:
            return True
        else:
            return False

    def insertEmptyList(self,element):
        node = Node(element)
        self.head = self.tail = node
        self.numElements += 1

    def append(self,element):
        if element != None:
            if self.isEmpty():
                self.insertEmptyList(element)
            else:
                node = Node(element)
                self.tail.next = node
                node.previous = self.tail
                self.tail = node
                self.numElements += 1
        else:
            raise IndexError ("\nO elemento é nulo!\n")

    def insertHead(self,element):
        if element != None:
            if self.isEmpty():
                self.insertEmptyList(element)
            else:
                node = Node(element)
                node.next = self.head
                self.head.previous = node
                self.head = node
                self.numElements += 1
        else:
            raise IndexError ("\nO elemento é nulo!\n")

    def insert(self,element,position):
        if element != None:
            if self.isEmpty():
                self.insertEmptyList(element)
            else:
                if position == self.numElements:
                    self.append(element)
                elif position == 1:
                    self.insertHead(element)
                elif position == 0:
                    print("\nA posição não existe!\n")
                else:
                    node = Node(element)
                    nodeAux = self.head
                    for index in range(position-2):
                        nodeAux = nodeAux.next
                    
                    node.previous = nodeAux
                    node.next = nodeAux.next

                    nodeAux.next.previous = node
                    nodeAux.next = node
                    self.numElements += 1
        else:
            raise IndexError ("\nO elemento é nulo!\n")
                
    def removeTail(self):
        if self.isEmpty():
            print("\nLista Vazia!\n")
        elif self.head == self.tail:
            print("Há apenas [1] elemento!")
            self.head = self.tail = None
            self.numElements = 0
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            self.numElements -= 1

    def removeHead(self):
        if self.isEmpty():
            print("\nLista Vazia!\n")
        elif self.head == self.tail:
            print("Há apena [1] elemento!")
            self.head = self.tail = None
            self.numElements = 0
        else:
            self.head = self.head.next
            self.head.previous = None
            self.numElements -= 1

    def removePosition(self,position):
        if position != None:
            if self.isEmpty():
                print("\nLista Vazia!\n")
            elif position == self.numElements:
                self.removeTail()  
            elif position > self.numElements:
                print(f"\nA posição {position} não existe na lista!\n")
            elif position == 1:
                self.removeHead()
            else:
                positionAux = self.head
                for index in range(self.numElements-2):
                    if index == position - 2:
                        positionAux.next = positionAux.next.next
                        positionAux.next.previous = positionAux
                        self.numElements -= 1
                    else:
                        positionAux = positionAux.next

    def removeElement(self,element):
        self.exist = False
        if element != None:
            if self.isEmpty():
                print("\nLista Vazia!\n")
            elif self.tail.data == element:
                self.removeTail()
            elif self.head.data == element:
                self.removeHead()
            else:
                nodeAux = self.head.next
                for index in range(self.numElements-2):
                    if nodeAux.data == element:
                        nodeAux.previous.next = nodeAux.next
                        nodeAux.next.previous = nodeAux.previous
                        self.numElements -= 1
                        self.exist = True
                    else:
                        nodeAux = nodeAux.next
                if self.exist == False:
                    print(f"\nO elemento {element} não existe na lista!\n")
        else:
            raise IndexError ("\nO elemento é nulo!\n")    

    def searchElement(self,element):
        if element != None:
            if self.isEmpty():
                print("\nLista Vazia!\n")
            elif self.head.data == self.tail.data == element:
                self.printData(self.head.data,1)
            elif self.tail.data == element:
                self.printData(self.tail.data,self.numElements)
            elif self.head.data == element:
                self.printData(self.head.data,1)
            else:
                nodeAux = self.head.next
                for index in range(self.numElements-2):
                    if nodeAux.data == element:
                        self.printData(nodeAux.data,index + 2)
                        self.exist = True
                    else:
                        nodeAux = nodeAux.next
                if self.exist == False:
                    print(f"\nO elemento {element} não existe na lista!\n")
        else:
            raise IndexError ("\nO elemento é nulo!\n")     

    def searchPosition(self,position):
        if position != None:
            if self.isEmpty():
                print("\nLista vazia!\n")
            elif position == self.numElements:
                self.printData(self.tail.data,position)
            elif position > self.numElements:
                print(f"\nA posição {position} não existe na lista!\n")
            else:
                positionAux = self.head
                for index in range(self.numElements - 1):
                    if index + 1 == position:
                        self.printData(positionAux.data,position)
                    positionAux = positionAux.next
        else:
            raise IndexError ("\nO elemento é nulo!\n")    

    def printData(self,element,position):
        print(f"O elemento existe na posição: {position}")
        print(f"O elemento é: {element}")
    
    def printList(self,node):
        if self.isEmpty():
            print("\nLista Vazia!\n")
        else:
            while (node is not None):
                print(f"O elemento é: {node.data}")
                node = node.next
    
    def printListInverse(self,node):
        if self.isEmpty():
            print("\nLista Vazia!\n")
        else:
            while (node is not None):
                print(f"O elemento é: {node.data}")
                node = node.previous

    def printHead(self):
        print(f"O início é: {self.head.data}")

    def printTail(self):
        print(f"Tail is: {self.tail.data}")

    def printNumberElementsList(self):
        print("\nO número de elementos é: " + str(self.numElements) + "\n\n")


#««««««««««««»»»»»»»»»»»»»»
#     FUNÇÃO CAPICUA 
#»»»»»»»»»»»»»»»»»»»»»»»»»»
def capicua(palavra):
   #cadeia = builtins.raw_input('cadeia:')
   cadeia = palavra
   if (cadeia[0:] == cadeia[::-1]):
       print (f'PALAVRA: {cadeia[0:]} --- capicua = ({cadeia[::-1]})')
   else:
       print (f'PALAVRA: {cadeia[0:]} --- nao capicua = ({cadeia[::-1]})')

if __name__=='__main__':
   dList = DoublyLinkedList()

   dList.insertHead("ana")
   dList.insertHead("casa")
   dList.insertHead("omo")
   
   #Print methods
   #dList.printList(dList.head)
   #dList.printHead()
   #dList.printTail()
   #dList.printNumberElementsList()
   
   
   #  PASSANDO AS PALAVRAS PARA A FUNÇÃO CAPICUA E VERIFICAR
   #++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   while (dList.head is not None):
       #print(dList.head.data)
       capicua(dList.head.data)
       dList.head = dList.head.next
       
   #i = 0
   #while(i <= dList.numElements):
    #   print(dList.searchPosition(i))
     #  i += 1
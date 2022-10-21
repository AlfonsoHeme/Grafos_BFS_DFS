import random 
import math

class Nodo:


	def __init__(self,id_nodo,i = 0,j = 0):
		self.__id_nodo = id_nodo
		self.__nodeName = str(i) + "." + str(j)
		self.__i = i
		self.__j = j

	def get_i(self):
		return self.__i

	def get_j(self):
		return self.__j

	def get_idNodo(self):
		return self.__id_nodo

	def getId(self):
		return self.__id_nodo

	def getKey(self,nodo,i=0, j=0):
		return str(nodo.get_i()+i)+"."+str(nodo.get_j()+j)


	def getCoordenadas(self):
		coordenadas = [get_i(),get_j()]
		return coordenadas

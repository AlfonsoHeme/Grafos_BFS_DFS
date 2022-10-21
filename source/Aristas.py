from source.Nodo import *
from source.Arista import *
import random

class Aristas(Arista):

	__Aristas={}
	__Elements={}
	__grados=[]

	def __init__(self):
		self.__Aristas = {}
		#self.__Elements = {}
		self.__grados = []

	def getAllAristas(self):
		return self.__Aristas

	def setAristas(self,nodo_A,nodo_B):
		if(isinstance(nodo_B,Nodo) and isinstance(nodo_B,Nodo)):
			if(nodo_A.getId() in self.__Aristas):
				aux = self.__Aristas[nodo_A.getId()]
				if(not aux.containsArista(nodo_B)):
					aux.set_Arista(nodo_B)
			else:
				self.__Aristas[nodo_A.getId()] = Arista(nodo_A,nodo_B)
		self.incrementaGrado(nodo_A.getId())
		self.incrementaGrado(nodo_B.getId())

	def getGrado(self, nodo):
		return self.__grados[nodo.getId()]		

	def inicializaGrado(self, n):
		self.__grados = [0 for _ in range(n)]

	def incrementaGrado(self, _id):
		if(len(self.__grados) > 0):
			if(isinstance(_id,int)):
				self.__grados[_id] += 1

	def probabilidadGrado(self,nodo,d):
		return 1-(self.getGrado(nodo)/d)

	def printAristas(self):
		for arista in self.__Aristas.values():
			print(str(arista.getId()) +" "+ str(arista.getAristas()))

	def getIds(self):
		return self.__Aristas.keys()

	def limpiaBuffer(self):
		self.__Aristas.clear()
		self.__grados.clear()


	def getAristas(self,key):
		if(key in self.__Aristas):
			return self.__Aristas[key].getAristas()
		return []

	def getRandomAristas(self):
		return self.__Aristas[random.choice(list(self.getIds()))]

	def generaAristasNodos(self, nodos):
		for nodoA in nodos:
			for nodoB in nodos:
				if(nodoA.getId() != nodoB.getId()):
					if(not self.isParalela(nodoA,nodoB)):
						self.setAristas(nodoA,nodoB)

	def exists(self, id_node):
		return id_node in self.__Aristas.keys()

	def printGrados(self):
		print(self.__grados)

	def getIdNodo_A(self):
		return self.__nodo_A

	def getIdNodo_B(self):
		return self.__nodo_B

	def isParalela(self,nodo_A, nodo_B):
		if(isinstance(nodo_A,Nodo) and isinstance(nodo_B,Nodo)):
			nodo_A = nodo_A.getId()
			nodo_B = nodo_B.getId()

		if(nodo_B in list(self.getIds())):
			if(self.__Aristas[nodo_B].containsArista(nodo_A)):
				return True

		if(nodo_A in list(self.getIds())):
			if(self.__Aristas[nodo_A].containsArista(nodo_B)):
				return True
		
		return False

	def getAristasById(self,id_nodo):
		res = []
		if(id_nodo in self.__Aristas):
		#	if(id_nodo in self.__Aristas):
			res.extend(self.getAristas(id_nodo))

		for arista in self.__Aristas.values():
			if(arista.containsArista(id_nodo)):
				res.append(arista.getId())

		#print("By Id"+str(res))
		return res

	def covertToElements(self):
		for key in self.__Aristas.keys():
			self.__Elements[key] = self.__Aristas[key].getAristas()

	def getElements(self):
		if(len(self.__Elements) == 0):
			self.covertToElements()
		return self.__Elements
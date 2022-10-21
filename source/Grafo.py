from source.Nodos import *
from source.Aristas import *


class Grafo:

	def __init__(self):
		self.Nodos = Nodos()		
		self.Aristas = Aristas();

	def printAristas(self):
		self.Aristas.printAristas()
	
	def grafoMalla(self,m,n, dirigido = False):
		self.Nodos.creaNodosXY(m,n)
		
		for _id in self.Nodos.getIds():
			n0 = self.Nodos.getNodo(_id)

			if((n0.get_i() + 1) < m):
				n1 = self.Nodos.getVecino(n0,1,0)
				self.Aristas.setAristas(n0,n1)
			
			if((n0.get_j() + 1) < n):
				n2 = self.Nodos.getVecino(n0,0,1)
				self.Aristas.setAristas(n0,n2)

		return self.getGraphivzText()


	def grafoErdosRenyi(self,n, m, dirigido=False, auto=False):
		if(m >= n-1):
			self.Nodos.creaNodos(n)
			i = 0
			while(i < m):
				n1 = self.Nodos.getRandomNodo()
				n2 = self.Nodos.getRandomNodo()
				if(n1.getId() != n2.getId()):
					if(not self.Aristas.isParalela(n1,n2)):
						self.Aristas.setAristas(n1,n2)
						i +=1
			return self.getGraphivzText()
		else:
			return "-1"

	def grafoGilbert(self,n, p, dirigido=False, auto=False):
		self.Nodos.creaNodos(n)	

		for _id in range(n):
			for _id2 in range(n):
				if(_id != _id2):
					if(not self.Aristas.isParalela(_id,_id2)):
						if(self.Nodos.ganaVolado(p)):
							n1 = self.Nodos.getNodo(_id)
							n2 = self.Nodos.getNodo(_id2)
							self.Aristas.setAristas(n1,n2)
		return self.getGraphivzText()

	def grafoGeografico(self,n, r, dirigido=False, auto=False):
		self.Nodos.creaNodosUnitario(n)
		for _id in range(n):
			for _id2 in range(n):
				if(_id != _id2):
					if(not self.Aristas.isParalela(_id,_id2)):
						n1 = self.Nodos.getNodo(_id)
						n2 = self.Nodos.getNodo(_id2)
						if(self.Nodos.isCerca(n1,n2,r)):
							self.Aristas.setAristas(n1,n2)

		return self.getGraphivzText()

	def grafoDorogovtsevMendes(self,n, dirigido=False):
		if(n >=3):
			self.Nodos.creaNodos(3)
			self.Aristas.setAristas(self.Nodos.getNodo(0),self.Nodos.getNodo(1))
			self.Aristas.setAristas(self.Nodos.getNodo(1),self.Nodos.getNodo(2))
			self.Aristas.setAristas(self.Nodos.getNodo(0),self.Nodos.getNodo(2))
			id_nodo = 3
			while(id_nodo < n):
				n0 = self.Nodos.addNodo(id_nodo)
				arista = self.Aristas.getRandomAristas();
				n1 = arista.getNodoA()
				n2 = arista.getNodoB()
				self.Aristas.setAristas(n0,n1)
				self.Aristas.setAristas(n0,n2)
				id_nodo += 1
			
		return self.getGraphivzText()

	def grafoBarabasiAlbert(self,n, d, dirigido=False, auto=False):
		self.Nodos.creaNodos(d)
		self.Aristas.inicializaGrado(n)
		self.Aristas.generaAristasNodos(self.Nodos.getNodos())
		id_nodo = d
		while(id_nodo < n):
			n0 = self.Nodos.addNodo(id_nodo)
			for nodo in self.Nodos.getNodos():
				if(n0.getId() != nodo.getId()):
					if(self.Nodos.volado(self.Aristas.probabilidadGrado(nodo,d))):
						self.Aristas.setAristas(n0,nodo)
			id_nodo += 1
		return self.getGraphivzText()


	def BFS(self, nodos_s):
		flag = True
		discover = []
		t = {}
		l =[]
		capa = 0
		l.append([nodos_s]);
		try:
			while (flag and len(l[capa]) != 0):
				inNode = l[capa].pop()
				discover.append(inNode)
				nodes = []
				for nodosB in self.Aristas.getAristasById(inNode):
					if(not nodosB in discover):
						nodes.append(nodosB)
						discover.append(nodosB)
				if(len(nodes) != 0):
					l.append(nodes)
					t[inNode] = list(nodes)

				if(len(l[capa]) == 0):
					capa +=1
		except:
			print("Terminando")
		return self.getGraphivzText(t,True)

	def DFSRecursivo(self,nodo_s,t = [],l ={},pos = -1):
		#print(self.Aristas.getElements())
		if(nodo_s not in t):
			#print("Buscando para ... "+str(nodo_s))
			t.append(nodo_s)
			for nodoB in self.Aristas.getAristasById(nodo_s):
				self.DFSRecursivo(nodoB,t,l,nodo_s)#Se elimina la asignacion de t
			if(pos not in l):
				l[pos] = [nodo_s]
			else:
				l[pos].append(nodo_s)
		#print("Arbol : "+str(len(l)))
		return l

	def DFS_R(self,nodo_s):
		return self.getGraphivzText(self.DFSRecursivo(nodo_s,t=[],l={}),True)
	
	def DFS_I(self,nodo_s):
		t ={}
		discover = []	
		pila = self.Aristas.getAristasById(nodo_s);
		discover.append(nodo_s)
		#print("pila inicial :" +str(pila))
		
		while(len(pila) > 0):
			nodoB = pila.pop()
			if(nodoB not in discover):
				#print("Buscando para "+str(nodo_s))
				#print("pila :" +str(pila))
				#print(self.Aristas.getAristasById(nodo_s))
				#print("Encontrados : "+ str(discover))
				#print("pila :" +str(pila))
			
				discover.append(nodoB)
				if(nodo_s not in t):
					t[nodo_s] = [nodoB]
				else:
					t[nodo_s].append(nodoB)

				if(len(self.Aristas.getAristasById(nodoB)) > 0):
					pila.extend(self.Aristas.getAristasById(nodoB))
				nodo_s = nodoB

		#print(t)
		return self.getGraphivzText(t,True)

	def getGraphivzText(self,grafo = None, dir = False):
		header = "graph {\n"
		Nodos = self.Nodos.toStringIds()
		Aristass =""
		typeArista = "--"
		cierre = "}"
		
		if(dir):
			typeArista = "->"
			header = "di"+header

		if(grafo == None):
			grafo = self.Aristas.getAllAristas()

		for _id in grafo.keys():
			_Aristas = None

			if(isinstance(grafo[_id],list)):
				_Aristas = grafo[_id]
			elif(isinstance(grafo[_id],Arista)):
				_Aristas = grafo[_id].getAristas()
			
			for id_Aristas in _Aristas:
				if(_id >= 0):
			 		Aristass += "\t"+str(_id)+ typeArista + str(id_Aristas) + ";\n"
		return header + Nodos + Aristass + cierre

	

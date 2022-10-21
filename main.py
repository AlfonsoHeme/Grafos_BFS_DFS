from source.Grafo import *
from source.File import *
import random


f = File()
nodos = [30,100,500]
colum = [6,10,25]

#gf0 = Grafo()
#tam = 30
#malla = gf0.grafoGeografico(tam,0.55)
#gf0.DFS_I(4)
#f.toGraphivzFile('Geografico_'+str(tam),gf0.DFS_I(4),'DFS_I')
#f.toGraphivzFile('Malla_'+str(tam),malla)

for data in zip(nodos,colum):
	rn = random.randint(1,data[0]-1)
	gf0 = Grafo()
	malla = gf0.grafoMalla(data[1],int(data[0]/data[1]))
	f.toGraphivzFile('Malla_'+str(data[0]),malla)
	f.toGraphivzFile('Malla_'+str(data[0]),gf0.BFS(rn),'BFS')
	f.toGraphivzFile('Malla_'+str(data[0]),gf0.DFS_R(rn),'DFS_R')
	f.toGraphivzFile('Malla_'+str(data[0]),gf0.DFS_I(rn),'DFS_I')


for tam in nodos:

	rn = random.randint(1,tam)

	gf = Grafo()
	erdos = gf.grafoErdosRenyi(tam,tam*8)
	f.toGraphivzFile('ErdosRenyi_'+str(tam),erdos)
	f.toGraphivzFile('ErdosRenyi_'+str(tam),gf.BFS(rn),'BFS')
	f.toGraphivzFile('ErdosRenyi_'+str(tam),gf.DFS_R(rn),'DFS_R')
	f.toGraphivzFile('ErdosRenyi_'+str(tam),gf.DFS_I(rn),'DFS_I')

	gf1 = Grafo()
	gilbert = gf1.grafoGilbert(tam,0.35)
	f.toGraphivzFile('Gilbert_'+str(tam),gilbert)
	f.toGraphivzFile('Gilbert_'+str(tam),gf1.BFS(rn),'BFS')
	f.toGraphivzFile('Gilbert_'+str(tam),gf1.DFS_R(rn),'DFS_R')
	f.toGraphivzFile('Gilbert_'+str(tam),gf1.DFS_I(rn),'DFS_I')
	
	gf2 = Grafo()
	geo = gf2.grafoGeografico(tam,0.35)
	f.toGraphivzFile('Geografico_'+str(tam),geo)
	f.toGraphivzFile('Geografico_'+str(tam),gf2.BFS(rn),'BFS')
	f.toGraphivzFile('Geografico_'+str(tam),gf2.DFS_R(rn),'DFS_R')
	f.toGraphivzFile('Geografico_'+str(tam),gf2.DFS_I(rn),'DFS_I')
	
	gf3 = Grafo()
	mendez = gf3.grafoDorogovtsevMendes(tam)
	f.toGraphivzFile('DorogovtsevMendes_'+str(tam),mendez)
	f.toGraphivzFile('DorogovtsevMendes_'+str(tam),gf3.BFS(rn),'BFS')
	f.toGraphivzFile('DorogovtsevMendes_'+str(tam),gf3.DFS_R(rn),'DFS_R')
	f.toGraphivzFile('DorogovtsevMendes_'+str(tam),gf3.DFS_I(rn),'DFS_I')

	gf4 = Grafo()
	albert = gf4.grafoBarabasiAlbert(tam,4)
	f.toGraphivzFile('BarabasiAlbert_'+str(tam),albert)
	f.toGraphivzFile('BarabasiAlbert_'+str(tam),gf4.BFS(rn),'BFS')
	f.toGraphivzFile('BarabasiAlbert_'+str(tam),gf4.DFS_R(rn),'DFS_R')
	f.toGraphivzFile('BarabasiAlbert_'+str(tam),gf4.DFS_I(rn),'DFS_I')
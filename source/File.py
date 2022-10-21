import os

class File:

	dir_name = 'Grafos/'

	def toGraphivzFile(self,nombreFichero,datos, opt = ""):
		nombreFichero += '.gv'
		if(len(opt) > 0):
			nombreFichero = opt+'_'+ nombreFichero
			self.dir_name = 'Grafos/'+opt+'/'
		else:
			self.dir_name = 'Grafos/'
		if not os.path.exists(self.dir_name):
			os.mkdir(self.dir_name)
		with open(self.dir_name+nombreFichero, 'w') as f:
			f.write(datos)

	
from particula import Particula
from algoritmos import distancia_euclidiana
import json
from pprint import pprint

class Particulas:
    def __init__(self):
        self.__particulas=[]
        #cambiar después
        self.d={}
        self.dA={}

    def agregar_inicio(self,particula:Particula):
        self.__particulas.insert(0,particula)
        self.dicc()
        self.diccAux()

    def agregar_final(self,particula:Particula):
        self.__particulas.append(particula)
        self.dicc()
        self.diccAux()

    def __str__(self):
        return "".join(str(par)+"\n" for par in self.__particulas)

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.count=0
        return self

    def __next__(self):
        if(self.count<len(self.__particulas)):
            particula=self.__particulas[self.count]
            self.count+=1
            return particula
        else:
            #ponemos una excepción que nos permita detenernos en esta posición
            raise StopIteration

        
    def guardar(self,ubicacion):
        #manejo de arhivos
        #forma 1
        """
        with open(ubicacion, 'w') as archivo:
            archivo.write
        """
        archivo=open(ubicacion,'w')
        #para pasarle los datos
        #archivo.write(str(self))
        #se le pasa una lista de diccionarios
        listaDicc=[par.to_json() for par in self.__particulas]
        json.dump(listaDicc,archivo,indent=5)

    def abrir(self,ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                #lista de diccionarios
                listaDicc=json.load(archivo)
                #convertiremos la lista de diccionarios a __particulas
                self.__particulas=[Particula(**lDicc) for lDicc in listaDicc]
                #Particula(id,origenX,origenY)
            return 1
        except:
            return 0

    def ordenar(self):
        print("ordenar")
        self.__particulas.sort(key=lambda par: par.distancia)
        self.__particulas.sort(key=lambda par: par.id)
        self.__particulas.sort(key=lambda par: par.velocidad)

    def dicc(self):
        for par in self.__particulas:
            origenX =   par.origenX
            origenY =   par.origenY
            destinoX =  par.destinoX
            destinoY =  par.destinoY
            distancia=  par.distancia
           # print("origenX: ")
           # print(origenX)
            if (origenX,origenY) in self.d:
                self.d[origenX,origenY].append((destinoX,destinoY,distancia))
            else:
                self.d[origenX,origenY]=[(destinoX,destinoY,distancia)]
            
            if (destinoX,destinoY) in self.d:
                self.d[destinoX,destinoY].append((origenX,origenY,distancia))
            else:
                self.d[destinoX,destinoY]=[(origenX,origenY,distancia)]
        """
        print("Dicc")

        for (origenX,destinoX) in self.d.items():
            print(origenX,destinoX)

        for orX,desX in self.d.items():
            print(orX,desX)

        """

    def diccAux(self):
        for par in self.__particulas:
            origenX =   par.origenX
            origenY =   par.origenY
            destinoX =  par.destinoX
            destinoY =  par.destinoY
            #print("origenX: ")
            #print(origenX)

            if (origenX,origenY) in self.dA:
                self.dA[origenX,origenY].append((destinoX,destinoY))
            else:
                self.dA[origenX,origenY]=[(destinoX,destinoY)]

            if (destinoX,destinoY) in self.dA:
                self.dA[destinoX,destinoY].append((origenX,origenY))
            else:
                self.dA[destinoX,destinoY]=[(origenX,origenY)]


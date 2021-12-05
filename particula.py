from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self,id,origenX,origenY,destinoX,destinoY,velocidad,red,green,blue):
        self.__id=id
        self.__origenX=origenX
        self.__origenY=origenY
        self.__destinoX=destinoX
        self.__destinoY=destinoY
        self.__velocidad=velocidad
        self.__red=red
        self.__green=green
        self.__blue=blue
        self.__distancia=distancia_euclidiana(origenX,destinoX,origenY,destinoY)
        
    def __str__(self):
        return "Id: "+str(self.__id)+" \nOrigen en x: "+str(self.__origenX)+" \nOrigen en y: "+str(self.__origenY)+" \nDestino en x: "+str(self.__destinoX)+" \nDestino en y: "+str(self.__destinoY)+" \nVelocidad: "+str(self.__velocidad)+" \nRed:  "+str(self.__red)+" \nGreen: "+str(self.__green)+" \nBlue: "+str(self.__blue)+" \nDistancia: "+str(self.__distancia)

    def to_json(self):
        #diccionarios
        return{
            "id":self.__id,
            "origenX":self.__origenX,
            "origenY":self.__origenY,
            "destinoX":self.__destinoX,
            "destinoY":self.__destinoY,
            "velocidad":self.__velocidad,
            "red":self.__red,
            "green":self.__green,
            "blue":self.__blue
        }
    
    @property
    def id(self):
        return self.__id

    @property
    def origenX(self):
        return self.__origenX

    @property
    def origenY(self):
        return self.__origenY

    @property
    def destinoX(self):
        return self.__destinoX

    @property
    def destinoY(self):
        return self.__destinoY

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue

    @property
    def distancia(self):
        return self.__distancia

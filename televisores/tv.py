import control
class TV:
    numTV = 0
    control = control()

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self.numTV += 1

    def getMarca(self):
        return self._marca

    def getCanal(self):
        return self._canal

    def getPrecio(self):
        return self._precio

    def getVolumen(self):
        return self._volumen

    def getControl(self):
        return self.control

    def setMarca(self,marca):
        self._marca = marca

    def getEstado(self):
        return self._estado

    def setCanal(self, canal):
        if(self.getEstado()):
            if(canal <= 120 & canal > 0):
                self._canal = canal

    def setPrecio(self, precio):
        self._precio = precio


    def setVolumen(self, volumen):
        self._volumen = volumen


    def setControl(self, control):
        self.control = control

    def getNumTV(self):
        return self.numTV

    def setNumTV(self, numTv):
        self.numTV = numTv

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False


    def canalUp(self):
        if(self.getEstado()):
            if(self.getCanal() >= 1 & self.getCanal() < 120):
                self.setCanal(self.getCanal()+1)

    def canalDown(self):
        if(self.getEstado()):
            if(self.getCanal() > 1 & self.getCanal() <= 120):
                self.setCanal(self.getCanal()-1)


    def volumenUp(self):
        if(self.getEstado()):
            if(self.getVolumen() >= 0 & self.getVolumen() < 7):
                self.setVolumen(self.getVolumen()+1)

    def volumenDown(self):
        if(self.getEstado()):
            if(self.getVolumen() > 0 & self.getVolumen() <= 7):
                self.setVolumen(self.getVolumen()-1)



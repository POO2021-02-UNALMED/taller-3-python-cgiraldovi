from televisores.TV import TV
from televisores.Control import Control
from televisores.Marca import Marca


def testEnlazar():
    marca = Marca("Semsung")

    tv = TV(marca, True)
    control = Control()
    control.enlazar(tv)
    assert(tv.getControl() != None)


def testEnlazarControl():
    marca = Marca("Semsung")

    tv = TV(marca, True)
    control = Control()

    control.enlazar(tv)

    assert(control.getTv() != None)

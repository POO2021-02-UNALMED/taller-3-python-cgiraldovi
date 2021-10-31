from src.dispositivos.celular import Celular
from src.dispositivos.almacenamientoExterno import AlmacenamientoExterno
from src.dispositivos.computador import Computador
from src.almacenamientos.ram import Ram
from src.almacenamientos.almacenamiento import Almacenamiento

if __name__ == "__main__":
    cel = Celular("Alejandro", "Realme 8 pro", Almacenamiento(128, "SSD"))
    alm = AlmacenamientoExterno("Curso POO")
    pc = Computador("Lenovo", "s330", Almacenamiento(2000, "HDD"), Ram(8, "DDR4"))
    pc.setConexion(cel)
    print(pc.getConexion())
    print("Cantidad de celulares: " + str(Celular.getCantidad()))
    print("Cantidad de almacenamientos externos: " + str(AlmacenamientoExterno.getCantidad()))
    print("Cantidad de computadores: " + str(Computador._computador_cantidad()))
    print(dir(Computador))
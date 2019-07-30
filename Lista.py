class Nodo:
    def __init__(self, dato=None, next=None):
        self.valor = dato
        self.sig = next

class Lista:
    def __init__(self):
        self.head = None
        self.tam = 0

    def insertarInicio(self, dato):
        if self.head is None:
            self.head = Nodo(dato)
            self.tam += 1
        else:
            nuevo = Nodo(dato, self.head)
            self.head = nuevo
            self.tam += 1

    def insertarFinal(self, dato):
        if self.head is None:
            self.head = Nodo(dato)
            self.tam += 1
        else:
            aux = self.head
            nuevo = Nodo(dato)
            while aux.sig is not None:
                aux = aux.sig
            aux.sig = nuevo
            self.tam += 1

    def recorrer(self):
        aux = self.head
        print("\nInicio ----------")
        while aux is not None:
            print(aux.valor)
            aux = aux.sig
        print("Final ----------\n")

    def eliminarSoloUno(self, dato):
        aux = self.head
        el = 0
        if aux.valor is dato:
            self.head = aux.sig
            self.tam -= 1
            el = 1
        else:
            while aux is not None:
                if aux.sig.valor is dato:
                    aux.sig = aux.sig.sig
                    self.tam -= 1
                    el = 1
                    break
                aux = aux.sig
        if el is 0:
            print("No se encuentra el dato a eliminar")
        else:
            print("Dato Eliminado")

    def eliminarTodos(self, dato):
        aux = self.head
        el = 0
        while aux is not None:
            if aux.valor is dato:
                self.head = aux.sig
                self.tam -= 1
                el = 1
            else:
                if aux.sig.valor is dato:
                    aux.sig = aux.sig.sig
                    self.tam -= 1
                    el = 1
            aux = aux.sig
        if el is 0:
            print("No se encuentra el dato a eliminar")
        else:
            print("Datos Eliminados")

    def modificarSoloUno(self, datoI, datoN):
        aux = self.head
        mod = 0
        while aux is not None:
            if aux.valor is datoI:
                aux.valor = datoN
                mod = 1
                break
            aux = aux.sig
        if mod is 0:
            print("No se encontro el dato a modificar")
        else:
            print("Modificado")

    def modificarTodos(self, datoI, datoN):
        aux = self.head
        mod = 0
        while aux is not None:
            if aux.valor is datoI:
                aux.valor = datoN
                mod = 1
            aux = aux.sig
        if mod is 0:
            print("No se encontro el dato a modificar")
        else:
            print("Modificado")


lista = Lista()
op = -1

print("Tarea 1 - 201603168")
while op is not 8:
    print("\n1. Insertar al Inicio")
    print("2. Insertar al Final")
    print("3. Modificar")
    print("4. Modificar Todas las coincidencias")
    print("5. Eliminar")
    print("6. Eliminar Todas las coincidencias")
    print("7. Listar - Mostrar")
    print("8. Salir")
    try:
        op = int(input())
        if op is 1:
            print("Ingrese el Dato")
            data = int(input())
            lista.insertarInicio(data)
        elif op is 2:
            print("Ingrese el Dato")
            data = int(input())
            lista.insertarFinal(data)
        elif op is 3:
            print("Dato a Modificar")
            dataI = int(input())
            print("Modificacion")
            dataF = int(input())
            lista.modificarSoloUno(dataI,dataF)
        elif op is 4:
            print("Datos a Modificar")
            dataI = int(input())
            print("Modificacion")
            dataF = int(input())
            lista.modificarTodos(dataI, dataF)
        elif op is 5:
            print("Dato a Eliminar")
            data = int(input())
            lista.eliminarSoloUno(data)
        elif op is 6:
            print("Datos a Eliminar")
            data = int(input())
            lista.eliminarTodos(data)
        elif op is 7:
            lista.recorrer()
        elif op is 8:
            print("Saliendo\n")
        else:
            print("Numero invalido")
    except:
        print("Error con los datos ingresados, pruebe un numero")

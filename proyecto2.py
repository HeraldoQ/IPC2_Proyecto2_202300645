from xml.dom import minidom
from flask import Flask, Blueprint, render_template, redirect, request
from graphviz import Digraph
import os, re
os.system("cls")

#---------------------------------------metodos o funciones-----------------------------------------







#-------------------------------------------------------------Clase y lista de productos
#--------------------------------------------------------------------------------------
class productoc:
    def __init__(self,numeroproducto,nombremaquina,tiempoensamblaje, nombre, elaboracion):
        self.numeroproducto = numeroproducto
        self.nombremaquina = nombremaquina
        self.tiempoensamblaje = tiempoensamblaje
        self.nombre = nombre
        self.elaboracion = elaboracion


class nodop:
    def __init__(self, productoc = None, siguiente = None):
        self.productoc = productoc
        self.siguiente = siguiente

class listaenlazadaproductos:
    def __init__(self):
        self.primero = None

    def insertar(self, productoc):
        if self.primero is None:
            self.primero = nodop(productoc = productoc)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodop(productoc = productoc)
    def recorrer(self):
        actual = self.primero
        while actual != None:
            print("Nombre de maquina = "+actual.productoc.nombremaquina)
            print("Tiempo de ensamblado = "+actual.productoc.tiempoensamblaje)
            print("Nombre de producto = "+actual.productoc.nombre)
            print("Elaboracion = "+actual.productoc.elaboracion)
            print("Numero de producto = "+str(actual.productoc.numeroproducto))
            a = actual.productoc.elaboracion+"/"+actual.productoc.nombre
            actual = actual.siguiente
            print("_________________________")
        
    def eliminartodo(self):
        self.primero = None
        return " "
    
    def buscar(self, nombre):
        actual = self.primero
        while actual != None:
            if actual.productoc.numeroproducto == nombre:
                a = actual.productoc.nombre
                return a
            actual = actual.siguiente

    def buscarm(self, nombre):
        actual = self.primero
        while actual != None:
            if actual.productoc.numeroproducto == nombre:
                a = actual.productoc.nombremaquina
                return a
            actual = actual.siguiente

    def buscarelaboracion(self, numeroproducto, nombreproducto):
        actual = self.primero
        while actual != None:
            if actual.productoc.numeroproducto == numeroproducto and actual.productoc.nombre == nombreproducto:
                a = actual.productoc.elaboracion
                return a
            actual = actual.siguiente


    def buscarnombrenummaq(self, nombre, nombremaquina):
        actual = self.primero
        while actual != None:
            if actual.productoc.numeroproducto == nombre and actual.productoc.nombremaquina == nombremaquina:
                a = actual.productoc.nombre
                return a
            actual = actual.siguiente



    def buscarelaboracionmaq(self, nombre, nombremaquina):
        actual = self.primero
        while actual != None:
            if actual.productoc.numeroproducto == nombre and actual.productoc.nombremaquina == nombremaquina:
                a = actual.productoc.elaboracion
                return a
            actual = actual.siguiente

    def buscarelaboracionmaqnum(self, nombre, nombremaquina, numeroproducto):
        actual = self.primero
        while actual != None:
            if actual.productoc.nombre == nombre and actual.productoc.nombremaquina == nombremaquina and actual.productoc.numeroproducto == numeroproducto:
                a = actual.productoc.elaboracion
                return a
            actual = actual.siguiente

    def buscarelaboracionnommaq(self, nombre, nombremaquina):
        actual = self.primero
        while actual != None:
            if actual.productoc.nombre == nombre and actual.productoc.nombremaquina == nombremaquina:
                a = actual.productoc.elaboracion
                return a
            actual = actual.siguiente
    def buscarensambladonommaq(self, nombre, nombremaquina):
        actual = self.primero
        while actual != None:
            if actual.productoc.nombre == nombre and actual.productoc.nombremaquina == nombremaquina:
                a = actual.productoc.tiempoensamblaje
                return a
            actual = actual.siguiente


    def buscarnumeromaq(self, nombre, nombremaquina):
        actual = self.primero
        while actual != None:
            if actual.productoc.numeroproducto == nombre and actual.productoc.nombremaquina == nombremaquina:
                a = actual.productoc.numeroproducto
                return a
            actual = actual.siguiente

    






#-------------------------------------------------------------Clase y lista de maquinas
#--------------------------------------------------------------------------------------
class maquinac:
    def __init__(self,numero, nombre, tiempo):
        self.numero = numero
        self.nombre = nombre
        self.tiempo = tiempo




class nodom:
    def __init__(self, maquinac = None, siguiente = None):
        self.maquinac = maquinac
        self.siguiente = siguiente
        

class listaenlazadamaquinas:
    def __init__(self):
        self.primero = None

    def insertar(self, maquinac):
        if self.primero is None:
            self.primero = nodom(maquinac = maquinac)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodom(maquinac = maquinac)
    def recorrer(self):
        actual = self.primero
        while actual != None:
            print("Numero de maquina = "+str(actual.maquinac.numero))
            print("Nombre de maquina = "+actual.maquinac.nombre)
            print("Tiempo de ensamblado = "+actual.maquinac.tiempo)
            
            actual = actual.siguiente
            print("_________________________")
    def eliminartodo(self):
        self.primero = None
        return " "
    def buscar(self, nombre):
        actual = self.primero
        while actual != None:
            if actual.maquinac.numero == nombre:
                a = actual.maquinac.nombre
                return a
            actual = actual.siguiente
    def buscarnombre(self, nombre):
        actual = self.primero
        while actual != None:
            if actual.maquinac.nombre == nombre:
                a = actual.maquinac.nombre
                return a
            actual = actual.siguiente


#---------------------------------------Clase y lista de lineas--------------------------------
class lineac:
    def __init__(self,numero, linea, componente):
        self.numero = numero
        self.linea = linea
        self.componente = componente


class nodol:
    def __init__(self, lineac = None, siguiente = None):
        self.lineac = lineac
        self.siguiente = siguiente

class listaenlazadalineas:
    def __init__(self):
        self.primero = None
    
    def insertar(self, lineac):
        if self.primero is None:
            self.primero = nodol(lineac = lineac)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodol(lineac = lineac)
    
    def recorrer(self):
        actual = self.primero
        while actual != None:
            print("Numero = "+str(actual.lineac.numero))
            print("linea = "+actual.lineac.linea)
            print("Componente = "+actual.lineac.componente)
            actual = actual.siguiente
            print("_________________________")

    def eliminartodo(self):
        self.primero = None
        return " "
    
    def buscarcomponentenum(self, numero):
        actual = self.primero
        while actual != None:
            if actual.lineac.numero == numero:
                a = actual.lineac.componente
                return a
            actual = actual.siguiente
    
    def buscarlineanum(self, numero):
        actual = self.primero
        while actual != None:
            if actual.lineac.numero == numero:
                a = actual.lineac.linea
                return a
            actual = actual.siguiente

    def buscarlinea(self, linea):
        actual = self.primero
        while actual != None:
            if actual.lineac.linea == linea:
                a = actual.lineac.linea
                return a
            actual = actual.siguiente
    
    def buscarcomponentelinea(self, linea):
        actual = self.primero
        while actual != None:
            if actual.lineac.linea == linea:
                a = actual.lineac.componente
                return a
            actual = actual.siguiente
    def editarlinea(self, linea, nuevalinea):
        actual = self.primero
        while actual != None:
            if actual.lineac.linea == linea:
                actual.lineac.linea = nuevalinea
                return actual.lineac.linea
            actual = actual.siguiente
    
#------------------------------------------Clase final-----------------------------------------

class finalc:
    def __init__(self,numero, linea, componente, ensamblando, esperando, ensamblado, tiempo):
        self.numero = numero
        self.linea = linea
        self.componente = componente
        self.ensamblando = ensamblando
        self.esperando = esperando
        self.ensamblado = ensamblado
        self.tiempo = tiempo


class nodof:
    def __init__(self, finalc = None, siguiente = None):
        self.finalc = finalc
        self.siguiente = siguiente

class listaenlazadafinal:
    def __init__(self):
        self.primero = None
    
    def insertar(self, finalc):
        if self.primero is None:
            self.primero = nodof(finalc = finalc)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodof(finalc = finalc)

    def recorrer(self):
        actual = self.primero
        while actual != None:
            print("Numero = "+str(actual.finalc.numero))
            print("linea = "+str(actual.finalc.linea))
            print("Componente = "+str(actual.finalc.componente))
            print("Ensamblado = "+str(actual.finalc.ensamblando))
            print("Esperando = "+str(actual.finalc.esperando))
            actual = actual.siguiente
            print("_________________________")
    
    def buscarensamblado(self, numero):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                a = actual.finalc.ensamblado
                return a
            actual = actual.siguiente

    def buscarensamblando(self, numero):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                a = actual.finalc.ensamblando
                return a
            actual = actual.siguiente
    
    def buscaresperando(self, numero):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                a = actual.finalc.esperando
                return a
            actual = actual.siguiente

    def buscarcomponente(self, numero):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                a = actual.finalc.componente
                return a
            actual = actual.siguiente

    def buscarcomponentelinea(self, linea):
        actual = self.primero
        while actual != None:
            if actual.finalc.linea == linea:
                a = actual.finalc.componente
                return a
            actual = actual.siguiente

    def buscarlinea(self, numero):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                a = actual.finalc.linea
                return a
            actual = actual.siguiente
    def buscartiempo(self, numero):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                a = actual.finalc.tiempo
                return a
            actual = actual.siguiente

    def editar(self, numero, nuevocomponente):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                actual.finalc.componente = nuevocomponente
                return actual.finalc.componente
            actual = actual.siguiente

    def editarensamblando(self, numero, nuevoensamblando):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                actual.finalc.ensamblando = nuevoensamblando
                return actual.finalc.ensamblando
            actual = actual.siguiente

    def editaresperando(self, numero, nuevoesperando):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                actual.finalc.esperando = nuevoesperando
                return actual.finalc.esperando
            actual = actual.siguiente
    
    def editarensamblado(self, numero, nuevoensamblado):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                actual.finalc.ensamblado = nuevoensamblado
                return actual.finalc.ensamblado
            actual = actual.siguiente
    def editartiempo(self, numero, nuevotiempo):
        actual = self.primero
        while actual != None:
            if actual.finalc.numero == numero:
                actual.finalc.tiempo = nuevotiempo
                return actual.finalc.tiempo
            actual = actual.siguiente

    def eliminartodo(self):
        self.primero = None
        return " "


#-------------------------------------------------------------Clase y lista de tabla

class tablac:
    def __init__(self,segundo, linea,texto):
        self.segundo = segundo
        self.linea = linea
        self.texto = texto

class nodot:
    def __init__(self, tablac = None, siguiente = None):
        self.tablac = tablac
        self.siguiente = siguiente

class listaenlazadatabla:
    def __init__(self):
        self.primero = None
    
    def insertar(self, tablac):
        if self.primero is None:
            self.primero = nodot(tablac = tablac)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodot(tablac = tablac)

    def recorrer(self):
        actual = self.primero
        while actual != None:
            print("Segundo = "+str(actual.tablac.segundo))
            print("Linea = "+str(actual.tablac.linea))
            print("Texto = "+actual.tablac.texto)
            actual = actual.siguiente
            print("_________________________")
    def eliminartodo(self):
        self.primero = None
        return " "
    
    def buscarlinea(self, segundo):
        actual = self.primero
        while actual != None:
            if actual.tablac.segundo == segundo:
                a = actual.tablac.linea
                return a
            actual = actual.siguiente
    def buscartexto(self, segundo, linea):
        actual = self.primero
        while actual != None:
            if actual.tablac.segundo == segundo and actual.tablac.linea == linea:
                a = actual.tablac.texto
                return a
            actual = actual.siguiente
       
    


#-------------------------------------------------------------Clase y lista de graficos

class graficoc:
    def __init__(self,numero, texto):
        self.numero = numero
        self.texto = texto

class nodog:
    def __init__(self, graficoc = None, siguiente = None):
        self.graficoc = graficoc
        self.siguiente = siguiente

class listaenlazadagraficos:
    def __init__(self):
        self.primero = None
    
    def insertar(self, graficoc):
        if self.primero is None:
            self.primero = nodog(graficoc = graficoc)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodog(graficoc = graficoc)

    def buscar(self, numero):
        actual = self.primero
        while actual != None:
            if actual.graficoc.numero == numero:
                a = actual.graficoc.texto
                return a
            actual = actual.siguiente
    def eliminartodo(self):
        self.primero = None
        return " "
    
    def recorrer(self):
        actual = self.primero
        while actual != None:
            print("Numero = "+str(actual.graficoc.numero))
            print("Texto = "+actual.graficoc.texto)
            actual = actual.siguiente
            print("_________________________")
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
archivo = ""

#------------------------------todo lo de flask inicial--------------------------------
app = Flask(__name__)
blueprints = Blueprint('Renderer', __name__, template_folder='templates')


#-------------------------------------------renders------------------------------------

@blueprints.route('/')
def inicio():
    return render_template('index.html', listap = listap, listam = listam, contadormaquinas = contadormaquinas, contadorproductos = contadorproductos,max_num = 0, segundoactual = 0, listafinal = listafinal, listatablas = listatablas)

@blueprints.route('/archivo')
def archivo():
    return render_template('archivo.html')

@blueprints.route('/reportes')
def reportes():
    return render_template('reportes.html')

@blueprints.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')




#-------------------------------------funciones---------------------------------------
listap = listaenlazadaproductos()
listam = listaenlazadamaquinas()


listaestatica = listaenlazadalineas()
listafinal = listaenlazadafinal()

listatablas = listaenlazadatabla()

listagraficos = listaenlazadagraficos()
global contadorproductos
contadorproductos = 0
global contadormaquinas
contadormaquinas = 0




@app.route('/enviar', methods=['POST'])
def enviar():
    global archivo
    global contadorproductos
    global contadormaquinas
    archivo = request.files['archivo']
    if archivo:
        contenido = archivo.read().decode('utf-8')
        
        xml = minidom.parseString(contenido)
        maquinas = xml.getElementsByTagName('Maquina')
        
        for maquina in maquinas:
            
            if contadormaquinas == 0:
                contadormaquinas = contadormaquinas + 1
                nombre = maquina.getElementsByTagName('NombreMaquina')
                tiempo = maquina.getElementsByTagName('TiempoEnsamblaje')
                m = maquinac(contadormaquinas, nombre[0].firstChild.data.strip(), tiempo[0].firstChild.data.strip())
                listam.insertar(m)
            
            elif contadormaquinas != 0:
                nombre = maquina.getElementsByTagName('NombreMaquina')
                tiempo = maquina.getElementsByTagName('TiempoEnsamblaje')
                
                nombrebusqueda = nombre[0].firstChild.data.strip()
                ##print(nombrebusqueda)
                busqueda = listam.buscarnombre(nombrebusqueda)
                ##print(busqueda)
                if busqueda == nombre[0].firstChild.data.strip():
                    print("Ya existe la maquina")
                

                else:
                    contadormaquinas = contadormaquinas + 1
                    
                    m = maquinac(contadormaquinas, nombre[0].firstChild.data.strip(), tiempo[0].firstChild.data.strip())
                    listam.insertar(m) 

            
            print("//////////////////")




            productos = maquina.getElementsByTagName('Producto')
            
            for producto in productos:
                contadorproductos = contadorproductos + 1
                
                nombreProducto = producto.getElementsByTagName('nombre') 
                elaboraciones = producto.getElementsByTagName('elaboracion')
                p = productoc(contadorproductos,nombre[0].firstChild.data.strip(), tiempo[0].firstChild.data.strip(), nombreProducto[0].firstChild.data.strip(), elaboraciones[0].firstChild.data.strip())
                listap.insertar(p)
        ##listap.recorrer() 
        ##print("//////////////////----------------")
        ##listam.recorrer()
        


        # for j in range(1, contadorproductos):
        #     if listap.buscarnombremaq(j, "TelevisoresPro") != None:
        #         print("Producto numero "+str(j))
        #         a = listap.buscarnombremaq(j, "TelevisoresPro")
        #         print(a)
            
        
        ##w = listam.buscar(2)
        ##print(w)
            

            
            


    return render_template('index.html', listap = listap, listam = listam, contadormaquinas = contadormaquinas, contadorproductos = contadorproductos ,max_num = 0, segundoactual = 0, listafinal = listafinal, listatablas = listatablas)

@app.route('/procesar', methods=['POST'])
def procesar():
    try:
        opcion_seleccionada = request.form['options']
        opcion2_seleccionada = request.form['options2']
        segundo_seleccionado = request.form['segundos']
        print("------------------------------------------------------")
        print("producto = "+opcion_seleccionada)
        print("maquina = "+opcion2_seleccionada)
        
        try:
            segundo_seleccionado = int(segundo_seleccionado)

        except:
            print("No se ingreso un numero")

        print("segundos = ", segundo_seleccionado)

        elaboracion = listap.buscarelaboracionnommaq(opcion_seleccionada, opcion2_seleccionada)
        print("Elaboracion = "+elaboracion)
        

        tiempo = listap.buscarensambladonommaq(opcion_seleccionada, opcion2_seleccionada)
        print("Tiempo de ensamblaje = "+tiempo)


        matches = re.findall(r'L(\d+)', elaboracion)
        max_num = max(map(int, matches))
        print("Numero de lineas = ",max_num)
        print("------------------------------------------------------")

        elaboracionlista = re.findall(r'L(\d+)C(\d+)', elaboracion)
        print(elaboracionlista)

        #^^^^^^^^^^^^^^^^ se obtienen las lineas y componentes de la elaboracion
        print(len(elaboracionlista))
        listaestatica.eliminartodo()
        listafinal.eliminartodo()
        listatablas.eliminartodo()
        listagraficos.eliminartodo()
        for i in range(0, len(elaboracionlista)):
            listaestatica.insertar(lineac(i+1, elaboracionlista[i][0], elaboracionlista[i][1]))
        listaestatica.recorrer()
        print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
        for i in range(1, max_num + 1):
            listafinal.insertar(finalc( i, i,0,False,False,False,0))
        listafinal.recorrer()

        
        for i in range(1, max_num + 1):
                a = listaestatica.buscarcomponentelinea(str(i))
                print("Componenteaaaa = "+a)


#esto de arriba recoge todos los datos
#--------------------------------------------------------------
        #inicia el proceso de ensamblado
        #verifica si el ultimo de la lista final, fue ensamblado
        ultimoensamblado = listafinal.buscarensamblado(max_num)
        print("Ultimo ensamblado = "+str(ultimoensamblado))
        segundoactual = 0

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if type(segundo_seleccionado) == int:
            segundoobtenido = segundo_seleccionado
        else:
            segundoobtenido = 800
        anterioresensamblando = False

        contadorgrafico = 0
        for i in range(1, len(elaboracionlista) + 1):
            print("linea pivote = ", listaestatica.buscarlineanum(i))
            lineapivote = listaestatica.buscarlineanum(i)
            print("componente pivote = ", listaestatica.buscarcomponentenum(i))
            componentepivote = listaestatica.buscarcomponentenum(i)
            pivoteensamblado = False
            
            while ultimoensamblado == False:
                if segundoactual != segundoobtenido and pivoteensamblado == False:
                    segundoactual = segundoactual + 1
                    print()
                    print()
                    print("Segundo actual = ", segundoactual)
                    


                    for i in range(1, max_num + 1):
                        a = listaestatica.buscarcomponentelinea(str(i))
                        if a == None:
                            #en este segundo, entra porque ya no hay mas componentes de ese numero i
                            a = -1
                        # a busca el componente actual de la linea, en la listaestatica, la que tiene los 3 que se deben obtener ahora
                        
                        componenteactual = listafinal.buscarcomponente(i) + 1
                        lineaactual = listafinal.buscarlinea(i)
                        listafinal.editartiempo(i, segundoactual)
                        if listafinal.buscarensamblando(i) == False and listafinal.buscarcomponente(i) < int(a):            
                            
                            listafinal.editar(i, componenteactual)
                            
                            if listafinal.buscarcomponente(i) != int(a)+1:
                                lineamovd = listafinal.buscarlinea(i)
                                lineamovd2 = "linea "+str(lineamovd)+" moverse adelante"
                                print("linea ", listafinal.buscarlinea(i), " moverse adelante")
                                
                                listatablas.insertar(tablac(segundoactual, lineamovd, lineamovd2))
                                continue
                        elif listafinal.buscarensamblando(i) == False and listafinal.buscarcomponente(i) > int(a) and int(a) != -1:
                            listafinal.editar(i, componenteactual-2)

                            if listafinal.buscarcomponente(i) != int(a)-1:
                                lineamovi = listafinal.buscarlinea(i)
                                lineamovi2 = "linea "+str(lineamovi)+" moverse atras"
                                print("linea ", listafinal.buscarlinea(i), " moverse atras")
                                
                                listatablas.insertar(tablac(segundoactual, lineamovi, lineamovi2))
                                continue
                        elif a == -1:
                            print("linea ", listafinal.buscarlinea(i), " no hacer nada")

                            lineamovn = listafinal.buscarlinea(i)
                            lineamovn2 = "linea "+str(lineamovn)+" no hacer nada"

                            listatablas.insertar(tablac(segundoactual, lineamovn, lineamovn2))

                        if int(listafinal.buscarcomponente(i)) == int(componentepivote) and listafinal.buscarensamblando(i) == False and int(listafinal.buscarlinea(i)) == int(lineapivote) and int(listafinal.buscartiempo(i)) <= segundoactual+1:
                            listafinal.editarensamblando(i, True)
                            listafinal.editaresperando(i, False)
                            tiempoactual = listafinal.buscartiempo(i)
                            if tiempo == 1:
                                listafinal.editartiempo(i, tiempoactual + int(tiempo))
                            else:
                                listafinal.editartiempo(i, tiempoactual + int(tiempo) - 1)
                            print("-------------------------------------------------/")
                            print("ENSAMBLANDO = "+str(listafinal.buscarensamblando(i)))
                            print("Esperando = "+str(listafinal.buscarensamblado(i)))
                            print("Componente = "+str(listafinal.buscarcomponente(i)))
                            print("Linea = "+str(listafinal.buscarlinea(i)))
                            print("Tiempo = "+str(listafinal.buscartiempo(i)))
                            print("-------------------------------------------------")
                            contadorgrafico = contadorgrafico + 1
                            lineagrafico = "L"+str(lineapivote)+"C"+str(componentepivote)
                            listagraficos.insertar(graficoc(contadorgrafico, lineagrafico))


                            ensamblandomov = listafinal.buscarlinea(i)
                            ensamblandomov2 = "linea "+str(ensamblandomov)+" comenzó a ensamblarse"

                            listatablas.insertar(tablac(segundoactual, ensamblandomov, ensamblandomov2))

                            
                        elif listafinal.buscarcomponente(i) == int(a) and int(listafinal.buscarlinea(i)) != int(lineapivote) and listafinal.buscaresperando(i) == False:
                            listafinal.editaresperando(i, True)
                            print("-------------------------------------------------/")
                            print("Ensamblando = "+str(listafinal.buscarensamblando(i)))
                            print("ESPERANDO = "+str(listafinal.buscaresperando(i)))
                            print("Componente = "+str(listafinal.buscarcomponente(i)))
                            print("Linea = "+str(listafinal.buscarlinea(i)))
                            print("Tiempo = "+str(listafinal.buscartiempo(i)))
                            print("-------------------------------------------------")

                            esperandomov = listafinal.buscarlinea(i)
                            esperandomov2 = "linea "+str(esperandomov)+" esperando"

                            listatablas.insertar(tablac(segundoactual, esperandomov, esperandomov2))



                        elif listafinal.buscaresperando(i) == True:
                            print("Linea ", lineaactual, " ESPERANDO")

                            esperandomov = listafinal.buscarlinea(i)
                            esperandomov2 = "linea "+str(esperandomov)+" esperando en cola"

                            listatablas.insertar(tablac(segundoactual, esperandomov, esperandomov2))


                        
                        elif listafinal.buscarensamblando(i) == True:
                            
                            if int(tiempo) >2:
                                print("Linea ", lineaactual, " ENSAMBLANDO")
                                ensamblandomov = listafinal.buscarlinea(i)
                                ensamblandomov2 = "linea "+str(ensamblandomov)+"sigue ensamblando"

                                listatablas.insertar(tablac(segundoactual, ensamblandomov, ensamblandomov2))


                        if listafinal.buscarensamblando(i) == True and int(listafinal.buscartiempo(i)) >= segundoactual:
                            
                            if int(listafinal.buscartiempo(i)) == segundoactual or tiempo == 1:
                                listafinal.editarensamblado(i, True)
                                listafinal.editaresperando(i, False)
                                listafinal.editarensamblando(i, False)
                                print("Linea ", lineaactual, " ensamblada")
                                pivoteensamblado = True
                                print("linea ensamblada ",listaestatica.buscarlinea(str(i)))
                                listaestatica.editarlinea(str(i), "0")

                                ensambladomov = listafinal.buscarlinea(i)
                                ensambladomov2 = "linea "+str(ensambladomov)+" ensamblada"

                                listatablas.insertar(tablac(segundoactual, ensambladomov, ensambladomov2))
                                
                            

                        # print("linea actual = ", listafinal.buscarlinea(i))
                        # print("Componente actual = "+str(listafinal.buscarcomponente(i)))
                            
                        
                else:
                    break
                
        print("-------------------------------------ajlvfjedrjv-----------------")
        listafinal.recorrer()
        
        print("------------------------------------------------------")
        listatablas.recorrer() 

        print("//////////////////////////////////////////////////////////////////////////////////////")
        
        
        
        
        
        
        
        listagraficos.recorrer()
        
        dot = Digraph(comment='Simple Line')
        
        for i in range(1, len(elaboracionlista) + 1):
            a = listagraficos.buscar(i)
            if a != None:
                dot.node(str(i), str(a))

        for i in range(1, len(elaboracionlista) + 1):
            a = listagraficos.buscar(i)
            if a != None:
                dot.edge(str(i), str(i + 1))
     
                
        
    
            # Generate the graph image
        
        # Save the graph as a PNG in the static directory
        dot.render('static/graph', format='png', cleanup=True)
    




    except:
        opcion_seleccionada = None
    

    return render_template('index.html', opcion_seleccionada = opcion_seleccionada, listap = listap, listam = listam, contadormaquinas = contadormaquinas, contadorproductos = contadorproductos, max_num = max_num, segundoactual = segundoactual, listafinal = listafinal, listatablas = listatablas)








app.register_blueprint(blueprints)













def main():
    print("iniciando programa")
    if __name__ == '__main__':
        app.run(debug=True)
main()
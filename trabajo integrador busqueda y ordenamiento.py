import time  #lo necesitamos para los tiempos de busqueda

# Funciones de ordenamiento:
def burbuja(lista, criterio): #funcion para el algoritmo burbuja
    #compara de a pares un elemento con el que le sigue en la lista, y si el primero es mayor los cambia de posicion
    #repite el proceso hasta que la lista este ordenada

    if criterio == "nombre": #el 0 indica que se esta ordenando por nombre, y el 1 por numero, lo mismo para todas las siguientes funciones
        indice = 0           #en caso de que criterio este mal escrito, se tomara por predeterminado el ordenamiento por numero
    else:
        indice = 1

    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1): 
            if lista[j][indice] > lista[j + 1][indice]: #se checkea si un nombre o numero en la lista es mayor al siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #si es mayor, se cambian sus posiciones en la lista
    return lista

def quicksort(lista, criterio): #funcion para el algoritmo quicksort. 
    #selecciona un elemnto base o "pivote" y divide todos los otros 
    #elementos de la lista entre los que son mayores y menores a ese

    if criterio == "nombre":
        indice = 0
    else:
        indice = 1

    if len(lista) <= 1:
        return lista#en caso de que la lista este vacia o con un solo elemento. ya que al final terminamos agregando 10 contactos, y luego 100 mas generados por computadora
                    #para no tener que agregar contactos cada vez que se incia el programa. esto no deberia ocurrir, pero lo dejamos a forma de historia del desarrollo del programa
    else:
        pivote = lista[0] #se toma el primer elemento como pivote
        menores = [x for x in lista[1:] if x[indice] <= pivote[indice]] #todos los valores menores al pivote
        mayores = [x for x in lista[1:] if x[indice] > pivote[indice]] #y todos los mayores
        return quicksort(menores, criterio) + [pivote] + quicksort(mayores, criterio) #reune la lista en orden: primero los menores, pivote, y mayores

# Funciones de busqueda:
def busqueda_lineal(lista, criterio, valor):#busca un valor en la lista comparando elemento por elemento.

    if criterio == "nombre":
        indice = 0
    else:
        indice = 1

    resultados = []# se agrego esta lista vacia porque nos dimos cuenta que si habia contactos con el mismo nombre solo nos devolvia uno solo. se hizo lo mismo con busqueda binaria
    for contacto in lista:
        if contacto[indice] == valor:
            resultados.append(contacto)
    return resultados 

def busqueda_binaria(lista, criterio, valor):#busca un valor en una lista dividiendo la lista a la mitad, pero solo funciona si el usuario ordena la lista antes

    if criterio == "nombre":
        indice = 0
    else:
        indice = 1

    izquierda = 0
    derecha = len(lista) - 1
    resultados =[]

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2 #posicion en el medio de la lista
        actual = lista[medio][indice] 
        if actual == valor:
            resultados.append(lista[medio])#agrega el contacto a "resultados"
            i = medio - 1 # checkea un valor a la izquierda de la lista
            while i >= 0 and lista[i][indice] == valor: #si el valor es igual lo agrega a "resultados"
                resultados.insert(0, lista[i])
                i -= 1
            i = medio + 1 # ahora checkea a la derecha y repíte los mismos pasos
            while i < len(lista) and lista[i][indice] == valor:
                resultados.append(lista[i])
                i += 1
            return resultados
        elif actual < valor:
            izquierda = medio + 1  #busca en la mitad derecha
        else:
            derecha = medio - 1  #busca en la mitad izquierda
    return None

# menu y programa principal:
def menu():#el menu principal del programa

    print("\n--- AGENDA DE CONTACTOS ---")
    print("1 - agregar contacto")
    print("2 - ver contactos")
    print("3 - ordenar contactos")
    print("4 - buscar contacto")
    print("5 - salir")

def main(): #funcion principal del programa
    #lista inicial con originalmente con 10 contactos, luego se le agregaron nombres generados por computadora para probar el funcionamiento con mas contactos
    agenda = [
        ["lucas", "1174834021"],
        ["lucas", "1152331321"], # se agregaron 2 nombres iguales para testear funcionamiento de multiples resultados
        ["carlos", "1524654423"],
        ["marta", "1135694331"],
        ["pedro", "1108674444"],
        ["sofia", "1557854399"],
        ["lucia", "1577793311"],
        ["juan", "1588956211"],
        ["elena", "150031123"],
        ["ramiro", "1197861568"],
        ['jorua', '1559846231'], #de aca en adelante todos los nombres son generados por computadora, para testear el funcionamiento con una lista mas grande
        ['cebowo', '1116294583'],
        ['qetube', '1575821349'],
        ['jubwuc', '1551983742'],
        ['enikuq', '1174358294'],
        ['rizafa', '1156173980'],
        ['oxeyok', '1179146358'],
        ['ezacen', '1153809467'],
        ['pevage', '1123985760'],
        ['fejido', '1145068297'],
        ['xabide', '1172309485'],
        ['lugoni', '1528469037'],
        ['dufado', '1117452396'],
        ['vokowa', '1534768210'],
        ['xekize', '1523987456'],
        ['vefoju', '1159723014'],
        ['kunavi', '1529756108'],
        ['yedawo', '1139658724'],
        ['tibage', '1574839201'],
        ['ribiro', '1520439762'],
        ['yekiqi', '1529378610'],
        ['ximeno', '1540283765'],
        ['zakapi', '1128039471'],
        ['noxebu', '1546732081'],
        ['jowuwa', '1571302957'],
        ['nasuzo', '1150938267'],
        ['hazanu', '1174893205'],
        ['megake', '1573948256'],
        ['wudida', '1521847639'],
        ['dagiva', '1559432758'],
        ['vuxopa', '1130482957'],
        ['hukode', '1529743160'],
        ['welumi', '1557382049'],
        ['kokanu', '1547893621'],
        ['runite', '1159423708'],
        ['dugame', '1137209846'],
        ['becoki', '1174956820'],
        ['qodawi', '1149538207'],
        ['zexopi', '1129738506'],
        ['cokuti', '1138940267'],
        ['rivubo', '1157842936'],
        ['gupope', '1529874362'],
        ['xikofa', '1117250834'],
        ['leruke', '1137582093'],
        ['femita', '1119365287'],
        ['qajazu', '1529376580'],
        ['goxena', '1172956830'],
        ['hobonu', '1572019348'],
        ['kanupo', '1157923846'],
        ['quzemu', '1129843065'],
        ['zefumi', '1148023571'],
        ['xifabi', '1118279456'],
        ['luzine', '1147029631'],
        ['mizavo', '1179384720'],
        ['vugalu', '1116497382'],
        ['cucalu', '1157802931'],
        ['zurida', '1549832067'],
        ['jofupo', '1157398206'],
        ['nujico', '1132940857'],
        ['ridojo', '1174082953'],
        ['deyepo', '1526749205'],
        ['kevago', '1559204738'],
        ['moziki', '1138520973'],
        ['fezama', '1520798426'],
        ['ciduge', '1119354728'],
        ['reliki', '1158302491'],
        ['fikolo', '1520937468'],
        ['vanigo', '1528493721'],
        ['duqeno', '1150923748'],
        ['yitubo', '1129407586'],
        ['garimo', '1178302745'],
        ['tuhefu', '1173024985'],
        ['ruciko', '1139408261'],
        ['cetubi', '1159302467'],
        ['xodeni', '1158490327'],
        ['hazoto', '1175093827'],
        ['xawupa', '1119572304'],
        ['funiko', '1158203947'],
        ['qoxelo', '1156203849'],
        ['tokene', '1150283496'],
        ['zuribu', '1118493027'],
        ['nelebu', '1179384021'],
        ['hejave', '1127390582'],
        ['kuciva', '1158392046'],
        ['denaco', '1158209384'],
        ['mewiki', '1150394726'],
        ['cerowo', '1159783204'],
        ['yalexo', '1148209573'],
        ['qiboru', '1117849023'],
        ['gugawi', '1128409261'],
        ['vivaxe', '1529837204'],
        ['nibuca', '1158034926'],
        ['zunibo', '1145802947'],
        ['vupene', '1157930261'],
        ['wokiza', '1158204981'],
        ['piwune', '1146920381'],
        ['xezupe', '1529073846'],
        ['jegulo', '1148029375'],
        ['cipimo', '1119582740'],
        ['yemaji', '1139408127'],
        ['bimota', '1147093845'],
        ['jubike', '1118029375'],
        ['kozeti', '1127402986']
        ]
    
    #bucle principal del menu. luego de que termina una de las funciones vuelve devuelta al menu
    encendido = True
    while encendido:

        menu()  
        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            #esto es para agregar mas contactos a la agenda, en caso de que se quiere testear con mas contactos
            nombre = input("nombre: ").lower() #esto es por si el usuario ingresa un nombre en mayusculas, ya que traeria problemas a la hora de buscarlo
            numero = input("numero: ")
            contacto = [nombre, numero]
            agenda.append(contacto) #agrega el contacto al final de la agenda, asi que se tendria que ordenar devuelta
            print("contacto agregado")

        elif opcion == "2":
            #muestra los contactos en la agenda
            print("\ncontactos:")
            for contacto in agenda:
                print(f"nombre: {contacto[0]}, numero: {contacto[1]}")

        elif opcion == "3":
            #ordena los contactos por nombre o numero

            criterio = input("ordenar por (nombre/numero): ").lower() 
            metodo = input("metodo (burbuja/quick): ").lower()

            iniciotimer = time.time() #empieza el timer
            if metodo == "burbuja":
                burbuja(agenda, criterio)
            elif metodo == "quick":
                agenda = quicksort(agenda, criterio)
            fintimer = time.time() #finaliza el timer

            print(f"ordenado por {criterio} usando {metodo} sort en {fintimer - iniciotimer:.6f} segundos.")#cuanto tiempo tardo en ordenar la agenda

        elif opcion == "4":
            #busca un contacto por nombre o numero

            criterio = input("buscar por (nombre/numero): ").lower()
            valor = input("valor a buscar: ").lower()
            metodo = input("metodo (lineal/binaria): ").lower()
            
            iniciotimer = time.time()
            if metodo == "lineal":
                resultado = busqueda_lineal(agenda, criterio, valor)
            elif metodo == "binaria":
                resultado = busqueda_binaria(agenda, criterio, valor)
            fintimer = time.time()

            #resultado de la busqueda
            if resultado:
                print(f"{len(resultado)} contacto(s) encontrado(s):")
                for contacto in resultado:
                    print(f"nombre: {contacto[0]} - numero: {contacto[1]}")
            else:
                print("valor no encontrado. En caso de ser busqueda binaria primero ordene la lista, si no es el caso revise el nombre o numero ingresado")
            print(f"busqueda realizada en {fintimer - iniciotimer:.6f} segundos") #esto muestra los decimales del timer, ya que la busqueda estaba tardando 
                                                                                #tan poco que no se podia ver la diferencia entre los tiempos

        elif opcion == "5":
            #sale del programa y se despide
            print("Adios!")
            encendido = False
        else:
            print("revise el numero ingresado")

main()
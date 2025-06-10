TP INTEGRADOR PROGRAMACION 1 UTN

Comision 16

Grupo: Lautaro Laner y Thiago Ezequiel Lagranda

link a video: https://www.youtube.com/watch?v=OfPOdR4ZZcE

---
AGENDA DE CONTACTOS - BUSQUEDA Y ORDENAMIENTO
---
El proyecto consiste en un programa de python para agendar y agregar contactos con nombre y numero de telefono,
ver la lista de contactos, ordenarlos por burbuja o quicksort, y buscarlos por 
nombre o numero, por algoritmo linear y binario, todo atravez de una interfaz simple

---
FUNCIONALIDADES PRINCIPALES:
---
Búsqueda de contactos por nombre o número:
  - Búsqueda lineal (En caso de no haber ordenado la lista)
  - Búsqueda binaria (requiere lista previamente ordenada)
Ordenamiento de la agenda:
  - Burbuja
  - Quicksort
Visualizacion por consola de agenda
Cronometrado de tiempo de busqueda
Agendar nuevos contactos

---
FUNCIONAMIENTO:
---
el programa le pide al usuario ingresar un numero del 1 al 5 para acceder a las diferentes opciones:

1 - AGREGAR CONTACTO:
    esto luego pide al usuario el nombre, y luego el numero, luego el contacto es agregado al final de la agenda
    
2 - VER CONTACTOS:
    esto muestra al usuario la lista con su orden (o desorden) actual
    
3 - ORDENAR CONTACTOS:
    primero pide al usuario por que criterio ordenar (nombre/numero), y luego el metodo de ordenamiento (burbuja/quicksort)
    
4 - BUSCAR CONTACTOS:
    primero pide al usuario por que criterio buscar (nombre/numero), luego que valor se busca,
    y luego que metodo se usa para buscar (linear/binario). #para que el metodo binario funcione se  
    debe ordenar la lista previamente
    
5 - SALIR:
    cierra el programa
    
cualquier otro numero le pide al usuario que revise el numero ingresado

---
REFLEXION:
---
fue un trabajo bastante dificil ya que una y otra vez encontramos casos particulares que nos hacian agregar funcionalidad adicional al codigo,
como fueron los casos de multiples contactos con el mismo nombre o numero,
o que el timer no mostrara los decimales, lo que nos obligo a buscar como solucionarlo por internet.
tambien nos ayudo a aplicar bien a las funciones, ya que no las habiamos aplicado antes en un proyecto tan grande, y en este caso separar todo el proyecto en pequeñas funciones lo hizo mucho
mas facil para repartir el trabajo de a 2 y para visualizar el funcionamiento del codigo

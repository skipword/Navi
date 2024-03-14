# Proyecto 5
En este proyecto consolidaremos todos los elementos desarrollados en prácticas anteriores. Se integrarán los dispositivos ALU y RAM del 2 y 3 en una computadora capaz de ejecutar programas escritos en lenguaje de máquina, como los hechos en el proyecto número 4. La computadora a hacer es denominada *Hack*, y sigue la arquitectura *Von Neumann*. Esta arquitectura se basa en una CPU que interactúa con el sistema de memoria, recibe datos de un dispositivo de entrada y envía datos a un dispisitivo de salida.

### Memory
La memoria de un sistema informático se puede dividir en dos partes: una física y otra lógica. Físicamente, la memoria está compuesta por registros con direcciones únicas que almacenan datos e instrucciones. Lógicamente, la memoria se divide en áreas dedicadas al almacenamiento de datos y de instrucciones de programas. Estas áreas se pueden gestionar juntas o separadas, dependiendo de la arquitectura del sistema. La memoria RAM permite acceder a cualquier registro de manera rápida y sin importar su ubicación en la memoria. La memoria de datos almacena variables y objetos mientras que la memoria de instrucciones guarda las instrucciones de los programas. Antes de ejecutar un programa, su código se carga en la memoria de instrucciones desde un dispositivo de almacenamiento externo como un disco.
![image](https://github.com/skipword/Navi/assets/159461539/7aa65ce7-f19d-4c4e-a090-5cd8096f9d16)
 


### CPU
La Unidad Central de Procesamiento (CPU) en la arquitectura de una computadora realiza la funcion de ejecutar las instrucciones de los programas que hemos realizado en las anteriores practicas. Para realizar las tareas la CPU está compuesta por tres componentes principales de hardware, la Unidad Aritmético-Lógica (ya trabajado en proyectos anteriores), un conjuntos de registros y una unidad de control(también trabajado en un proyecto anterior). Se le asignan instrucciones a la CPU con información sobre los cálculos que debe realizar, los registros a los que debe acceder y modificar, y las siguientes instrucciones que debe buscar y ejecutar.  
<img width="600" src="https://media.geeksforgeeks.org/wp-content/uploads/20230713124824/Components-of-computer-copy.webp">  

Para la plataforma Hack la CPU está diseñada para ejecutar instrucciones de 16 bits, así mismo esta CPU está diseñada para estar conectada a dos módulos de memoria distintos, una memoria de instrucciones y una memoria de datos, para poder leer y escribir los respectivos valores de los datos.


### Computer
Implementa una computadora completa con una memoria ROM de 32K palabras, una unidad central de procesamiento (CPU) y una memoria principal. La entrada de reset se utiliza para reiniciar la computadora. La ROM32K es una memoria de solo lectura que almacena las instrucciones del programa y proporciona la instrucción correspondiente a la dirección especificada por el contador de programa. El CPU ejecuta instrucciones y controla el flujo de datos y operaciones. La memoria principal almacena y recupera datos según la dirección proporcionada.

Una implementación específica del sistema "Computer" son "ComputerMax" y "ComputerAdd", "ComputerRect"

![computer](https://github.com/skipword/Navi/assets/159462338/8fdf73a9-c4c3-4455-bde1-b2d7e28752ec)

### ComputerMax:
Computadora con un conjunto amplio de instrucciones que incluye operaciones aritmeticas, lógicas y de control de flujo. Puede buscar y mantener el valor maximo de una serie de datos.

![computer2](https://github.com/skipword/Navi/assets/159462338/38ea4dd6-50de-4698-8bc6-57db9442793e)

### ComputerAdd:
Computadora especializada en operaciones de suma de números, ya sean enteros o en coma flotante.

![computer3](https://github.com/skipword/Navi/assets/159462338/0cbb79a2-9b41-4ee6-8a46-86aa1f19877e)

### ComputerRect:
Computadora optimizada para realizar cálculos relacionados con rectángulos, como área, perímetro, coordenadas y intersecciones.


## ¿Qué diferencia ven entre arquitectura computacional, arquitectura de software y arquitectura del sistema? 


## Referencias
- https://www.nand2tetris.org/_files/ugd/44046b_b2cad2eea33847869b86c541683551a7.pdf

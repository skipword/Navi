# Proyecto 4
Para avanzar en la construcción de un computador, el siguiente paso a seguir es familiarizarse con el lenguaje de máquina; ello implica escribir programas en *Hack assembly language*, traducirlos a binario con un ensamblador y evaluar el código resultante. Aunque muchas personas nunca escribirán programas directamente en lenguaje de máquina, su estudio es una buena base para el entendimiento de las arquitecturas informáticas, se le puede ver como un conjunto de reglas estándar diseñadas para manipular la memoria de una computadora y realizar operaciones con su procesador y registros.  Puesto a que este es un proyecto conjunto con el quinto, se usará un emulador CPU y un ensamblador para probar el código.

### Mult


### Fill
Este programa consiste en un bucle infinito que espera input del teclado, tiene dos estados:
- Dado el caso que se presione alguna tecla, la pantalla se pone negra.
- Si no se presiona una tecla, la pantalla se "limpia"

Los registros de los que se harán uso para completar esta tarea son:
- A: Se interpreta como valor de datos o como una dirección en la memoria
- D: Almacena valores de datos
- M: Vinculado a la memoria de datos, se usa para leer o escribir datos en esta

Ejemplos de su uso son
 ```
// if Memory[3]=5 then goto 100 else goto 200
@3
D=M // D=Memory[3]
@5
D=D-A // D=D-5
@100
D;JEQ // If D=0 goto 100, JEQ=Jump if Equal (saltar a una dirección si es cierto)
@200
0;JMP // Goto 200 JMP=Jump

//RAM[17] = 10
@10
D = A
@17
M = D
 ```
Ahora bien, tanto la pantalla como el teclado interactúan con la plataforma Hack por medio de *memory maps*, es decir, para pintar pixeles en la pantalla se escriben valores binarios en un segmento de memoria asociado con esta. La computadora Hack cuenta con una pantalla de 256 filas x 512 pixeles y su contenido se representa por un mapa de memoria de 8K que inicia en la dirección RAM 16384 (0x4000). Cada fila se representa en la RAM por 32 consecutivas palabras de 16 bits, y la dirección de memoria correspondiente a un pixel se calcula con Dirección de Memoria = 16384 + (fila * 32) + (columna / 16). 
 ```
// Pintar un solo punto en el primer pixel:
@SCREEN // Registro A apunta al primer pixel
M=1 //Pinta el pixel
 ```
En cuanto al teclado, la computadora Hack trabaja con este a través de un mapa de memoria de una palabra localizado en la dirección RAM 24576 (0x6000); ello implica que cuando una tecla es presionada su código ASCII de 16 bits aparece en RAM[24576], si nada ha sido presionado el valor que se muestra es 0.

Teniendo esto claro, el pseudocódigo para esta tarea es el siguiente
 ```
if(KBD > 0) goto BLACK
else goto WHITE
 ```

## ¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional?

## Referencias
- https://www.nand2tetris.org/_files/ugd/44046b_7ef1c00a714c46768f08c459a6cab45a.pdf
- https://zhongchuyun.gitbooks.io/nand2tetris/content/chapter_4.html
- https://www.jk-quantized.com/experiments/HomebrewComputer/Cheatsheets/hackASM.html

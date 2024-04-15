# Proyecto 7
En el contexto de nand2tetris se emplea un lenguaje de alto nivel denominado *jack* (lenguaje similar a java, introducido en el proyecto 9). Puesto a que una computadora no entiende ni ejecuta instrucciones escritas en este lenguaje, se requiere un compilador que traduzca el código fuente a a instrucciones comprensibles para el hardware (su código de máquina). 

<p align="center">
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fweb.stanford.edu%2Fclass%2Fcs101%2Fsoftware-compiler.png&f=1&nofb=1&ipt=839c2c41837c4ece7574022480470ed9b32e1792c4d0c2b55e255bca8b47598e&ipo=images" alt="Compilador">
</p>
<p align="center"><em>Compilación directa</em></p>

Si quiero asegurar la portabilidad de mi programa a distintas plataformas, debido a que pueden tener diferentes procesadores e instrucciones de máquina, debo hacer uso de más de un compilador. Para garantizar la flexibilidad y facilitar este proceso se hace uso de una compilación de dos niveles (two-tier compilation):
1. Traducir el código de alto nivel a un lenguaje intermedio, como el código de máquina virtual.
2. Traducir el lenguaje intermedio a código de máquina nativo específico de la plataforma de destino mediante un traductor de máquina virtual.

<p align="center">
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgur.com%2FPJME67T.png&f=1&nofb=1&ipt=750d8af959d730d1e9a0134f25fd6a546f8fd3da338370e359539f4773164a30&ipo=images" alt="Compilador">
</p>
<p align="center"><em>Two-tier compilation</em></p>

Así pues, en el presente proyecto se desarrollará un traductor básico de máquina virtual a lenguaje de ensamblador Hack, centrándonos en la implementación de las operaciones de aritmética de pila y acceso a la memoria del lenguaje de la máquina virtual.

### Arithmetic Stack
* Estructura de datos de pila (stack): Tiene una estructura de de Last In, First Out (LIFO) para almacenar los valores y resultados de las operaciones.
* Operaciones de la pila: Se deben poder realizar operaciones básicas de una pila, como push (añadir un elemento al inicio de la pila) y pop (eliminar y devolver el primer elemento de la pila).
* Operaciones aritméticas: Presenta funciones para realizar operaciones aritméticas básicas en la pila. Por ejemplo, ;la sumar (add), resta (sub), multiplicación (mult), división (div), etc.
* Operaciones lógicas: Se implementan operaciones lógicas, como and, or, not, etc; las cuales operan con booleanos (1 o 0).

### Memory access commands
* Instrucciones de acceso a memoria: Deben haber instrucciones que permitan acceder y manipular la memoria del sistema. Operaciones como push, pop, push constant, pop local, push argument, pop static, push pointer, pop pointer, push temp, pop temp, etc
* Gestión de segmentos de memoria: Debe incluir gestión de diferentes segmentos de memoria, como la memoria local, los argumentos, el segmento estático, etc.
* Manejo de punteros y direcciones de memoria: Capaz de manipular direcciones de memoria y punteros.

## Referencias
- https://www.maxdemaio.com/blog/vm-stack
- https://www.nand2tetris.org/project07
- https://github.com/rose/nand2tetris/blob/master/vm1.py
- https://www.cs.huji.ac.il/course/2002/nand2tet/docs/ch_7_vm_I.pdf
- https://www.csie.ntu.edu.tw/~cyy/courses/introCS/21fall/lectures/handouts/lec11_VMI.pdf

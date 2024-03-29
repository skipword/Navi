# Proyecto 2
Para el segundo proyecto se busca construir diseños de compuertas lógicas que representen números y realicen operaciones aritméticas entre estos. Más específicamente, el objetivo es desarrollar una Unidad Aritmético Lógica (ALU) completamente funcional. Esta ALU es una parte fundamental de la CPU ((Unidad Central de Procesamiento) y su correcta implementación nos ayudará a entender mejor el funcionamiento de una computadora. Dado que estamos tratando con compuertas lógicas, las operaciones como la suma o resta se incorporarán utilizando el sistema binario.

### HalfAdder

Half Adder (medio sumador) es un circuito lógico digital básico que realiza la suma de dos bits individuales y produce dos resultados: la suma de los bits (bit menos significativo) y un acarreo (bit más significativo). Es decir, toma dos bits de entrada y produce dos bits de salida. El medio sumador es fundamental en la construcción de circuitos aritméticos más complejos, como sumadores completos y sumadores de múltiples bits.

*Diagrama de un HalfAdder*

<img width="400" src="https://www.watelectronics.com/wp-content/uploads/Half-Adder-1.jpg">

*Tabla de verdad HalfAdder*


|   a   |   b   |  sum  | carry |
|-----------|-----------|-----------|----------|
|   0   |   0   |   0   |   0   |
|   0   |   1   |   1   |   0   |
|   1   |   0   |   1   |   0   |
|   1   |   1   |   0   |   1   |


### FullAdder
A diferencia del halfAdder, el FullAdder computa la suma de 3 bits: a, b y un bit carry-in, este último se introduce en el sistema para tener en cuenta acarreos de sumas previas que ocurren cuando el resultado de una suma excede 1. La implementación a HDL sigue la misma lógica que la suma de números binarios, se suma desde el digito menos significativo (derecha) hasta el más significativo (izquierda) y cuando una suma supera 1 se acarrea 1
al siguiente orden superior; esto se modela en 2 etapas:
  - Suma parcial: HalfAdder suma A y B, ejemplo A=1, B=1, suma1=0 carry1=1
  - Suma final: Con otro HalfAdder se suma el resultado de la etapa anterior con su carry y una compuerta or se encarga de combinar los acarreos generados por las dos sumas ejemplo suma2=1, carry2=0, carryfinal=1

*Ejemplo suma de dos números binarios*

<img width="400" src="https://bam.files.bbci.co.uk/bam/live/content/zc6gr82/medium">

*Tabla de verdad FullAdder*

| a | b | c | carry | suma |
|-----------|-----------|-----------|----------|----------|
|  0  |  0  |  0  |  0  |  0  |
|  0  |  0  |  1  |  0  |  1  |
|  0  |  1  |  0  |  0  |  1  |
|  0  |  1  |  1  |  1  |  0  |
|  1  |  0  |  0  |  0  |  1  |
|  1  |  0  |  1  |  1  |  0  |
|  1  |  1  |  0  |  1  |  0  |
|  1  |  1  |  1  |  1  |  1  |

### Add16

En un add16, se suman dos números binarios de 16 bits bit a bit, empezando por el bit menos significativo (el bit 0) hasta el bit más significativo (el bit 15). Si hay un acarreo generado por la suma de dos bits, se lleva a cabo al siguiente bit más significativo. 
Para construir un add16, se pueden utilizar 16 fulladder en cascada. Cada fullader recibe dos bits de los números que se están sumando y el bit de acarreo de la suma anterior (a excepcón del primer fullader, quien recibe dos bits de los números que se están sumando y el acarreo de entrada (Cin) va a tierra debido a que al inicio no hay acarreo). El bit de acarreo de salida fullader se alimenta como entrada al siguiente sumador completo en la cadena. De esta manera, cada sumador completo contribuye a la suma total de los números de 16 bits. Finalmente para los casos en los que el resultado de la suma da 17 bits, el add16 tiene 16 salidas (una por cada suma de dos numeros binarios bit a bit) y una salida número 17 quien es el Cout o el ultimo acarreo.

Su tabla de verdad es demasiado extensa debido a que son numeros de 16 bits. pero sigue la misma logica que el halfadder y el fulladder.



### Inc16

Inc16 es un acrónimo que representa "Incrementador de 16 bits". Es un componente digital que toma una entrada de 16 bits y la incrementa en 1, produciendo la salida correspondiente. Este tipo de componente es comúnmente utilizado en circuitos digitales y en sistemas de procesamiento de datos para realizar operaciones de suma, incremento o conteo de valores binarios de 16 bits.

*Chip INC16*

![inc16](https://github.com/skipword/Navi/assets/159462338/03af0416-706c-4b57-bfa0-89c439ba375d)


### ALU
El ALU está diseñado para entregar 18 funciones diferentes como salida(output), usando valores de 16 bits, tiene 6 bits de control, dos entradas, la entrada *x* y *y* de 16 bits cada una.
La manipulación de los bits de control para la entrada *x* son *zx* y *nx*, en tanto para la entrada *y* son *zy* y *ny*, las funciones modificadas son usadas en la operación determinada por la entrada *f*, además con la entrada *no* se puede modificar la salida.
Asi mismo se puede obtener más información de la salida según se usa el status de los bit *zr* y *ng*.
*Tabla ALU*
| zx | nx | zy | ny | f | no | out |
|----|----|----|----|---|----|-----|
|  1 |  0 |  1 |  0 | 1 |  0 |   0 |
|  1 |  1 |  1 |  1 | 1 |  1 |   1 |
|  1 |  1 |  1 |  0 | 1 |  0 |  -1 |
|  0 |  0 |  1 |  1 | 0 |  0 |   x |
|  1 |  1 |  0 |  0 | 0 |  0 |   y |
|  0 |  0 |  1 |  1 | 0 |  1 |  !x |
|  1 |  1 |  0 |  0 | 0 |  1 |  !y |
|  0 |  0 |  1 |  1 | 1 |  1 |  -x |
|  1 |  1 |  0 |  0 | 1 |  1 |  -y |
|  0 |  1 |  1 |  1 | 1 |  1 | x+1 |
|  1 |  1 |  0 |  1 | 1 |  1 | y+1 |
|  0 |  0 |  1 |  1 | 1 |  0 | x-1 |
|  1 |  1 |  0 |  0 | 1 |  0 | y-1 |
|  0 |  0 |  0 |  0 | 1 |  0 | x+y |
|  0 |  1 |  0 |  0 | 1 |  1 | x-y |
|  0 |  0 |  0 |  1 | 1 |  1 | y-x |
|  0 |  0 |  0 |  0 | 0 |  0 | x&y |
|  0 |  1 |  0 |  1 | 0 |  1 | x|y |

Control para x
cuando ZX es ==1 todo los 16 bits serán 0
Cuando nx ==1 negara la entrada de x (!x)
Zx==1&&Nx==1 --> todos los 16 bits serán 1
Cuando ambos están desactivados *x* seguirá sin cambios
Se puede observar su comportamiento en la siguiente tabla
**Tabla de verdad'
| zx| x | outputs|
|----|----|----|
|0|0|0|
|0|1|1|
|1|0|0|
|1|1|0|

Lo que es representado mediante Zx'X
## Bibliografía
- https://www.nand2tetris.org/_files/ugd/44046b_f0eaab042ba042dcb58f3e08b46bb4d7.pdf
- https://gittest2121.gitbook.io/nand2tetris/combinational-chips/full-adder-chip

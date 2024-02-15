# Proyecto 1
En el presente proyecto se trabajarán y comprenderán los conceptos fundamentales del álgebra booleana y su aplicación en la lógica digital. Para ello, usaremos la compuerta NAND para construir demás compuertas lógicas (Not, And, Or, Xor, DMux, Not16, etc) por medio de HDL (Hardware Description Language) y el Hardware Simulator proporcionado. A continuación se detalla el desarrollo de cada una de las compuertas

### NAND
La base con la que se construirán los demás bloques. Su funcionamiento se resume en producir una salida verdadera (1) si alguna de sus entradas es falsa (0), es decir, solo tiene una salida falsa cuando ambas entradas son verdaderas.
| A  | B | SALIDA |
|----|:--:|------:|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

<img src="https://www.build-electronic-circuits.com/wp-content/uploads/2022/09/Logic-symbol-NAND-gate-text.png">

### Not
La compuerta NOT, que realiza la operación de inversión lógica, utiliza internamente una compuerta NAND para su funcionamiento. La compuerta NOT toma una sola entrada y produce una salida que es el inverso lógico de la entrada: si la entrada es 0, la salida es 1; si la entrada es 1, la salida es 0.
| ENTRADA | SALIDA |
|----|------:|
| 0 | 1 |
| 1 | 0 |
<img src="https://portalacademico.cch.unam.mx/sites/default/files/cyc1u2oa5p08e04.jpg">

### And
Al contrario que la NAND, la compuerta AND resulta en una salida verdadera (1) si todas sus entradas son verdaderas, en caso contrario, resulta en una salida baja (0)
| A  | B | SALIDA |
|----|:--:|------:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

<img src="https://www.build-electronic-circuits.com/wp-content/uploads/2022/09/Logic-symbol-AND-gate-text.png">


### Or
Para la compuerta OR se distingue en que sus salidas bajas (0) será en cuyo momento ambas entradas sean 0, por lo tanto en el momento donde cualquier entrada sea (1) el resultado de la compuerta OR será alto (1).
| A  | B | SALIDA |
|----|:--:|------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

<img src="https://mielectronicafacil.com/wp-content/uploads/2020/08/compuerta-logica-or-simbolo.jpg">

## Xor
La compuerta Xor genera una salida alta (1) siempre que sus 2 entradas son diferentes, en caso de tener las 2 entradas iguales su salida es baja(0).

| A  | B | SALIDA |
|----|:--:|------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLtW-ly6W_g7oWNnJ2Qyfk1W7IwrFMiEkWgucB2KwvIVHuQ9eeOvg4JXY3_z43O0lL4t3Ah5RvrFZ3QI7zPdD5biOKUSZ3i84Hu9qKG6qmusPJEc0trI0bnQ13KptAPaV24uj-4W1z/s1600/circuito-combinacional.gif">

### Mux

### DMux
Es un componente digital que toma una entrada y la dirige hacia una de sus dos salidas dependiendo de una señal de selección. Si la señal de selección está en estado bajo, la entrada se dirige a una de las salidas, mientras que si la señal de selección está en estado alto, la entrada se dirige a la otra salida. Esencialmente, el DMux divide una señal de entrada en dos salidas distintas basadas en una señal de control.

| IN  | SEL | A | B|
|--|:--:|:--:|--:|
|   0   |   0   |   0   |   0   |
|   0   |   1   |   0   |   0   |
|   1   |   0   |   1   |   0   |
|   1   |   1   |   0   |   1   |
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Demultiplexer_Example01.svg/525px-Demultiplexer_Example01.svg.png">
### Not16

### And16
Para realizar este proceso lógico se utilizó la compuerta And ya explicada pero se replica el proceso 16 veces para obtenerse el And16
### Or16
Este proceso logico se realiza de fonrma similar a la compuerta Or explicada anteriormente, pero acepta 16 bits en cada una de sus entradas, es decir recibe 16 "a" y 16 "b" obteniendo 16 salidas correspondientes a cada par de entradas 
### Mux16

### Or8Way
Es una compuerta lógica que toma ocho entradas y produce una salida. La salida es 1 si al menos una de las entradas es 1, y es 0 si todas las entradas son 0. Esencialmente, realiza la operación OR en todas las entradas para determinar la salida.

|     IN     | OUT |
|--|--:|
|  00000000  |  0  |
|  11111111  |  1  |
|  00010000  |  1  |
|  00000001  |  1  |
|  00100110  |  1  |

<img src="https://nand2tetris-hdl.github.io/img/or8.png">

### Mux4Way16

### Mux8Way16

### DMux4Way


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Demultiplexer_Example01.svg/525px-Demultiplexer_Example01.svg.png">


### DMux8Way

## Preguntas adicionales:
1. ¿Que consideraciones importantes debe tener en cuenta para trabajar con Nand2Tetris?

Para trabajar con Nand2Tetris, es fundamental comprender su objetivo educativo, tener habilidades de programación, seguir el material del curso para guiar el progreso, dividir el trabajo en etapas manejables, estar dispuesto a experimentar y ser creativo en el proceso de realizacion de el trabajo.



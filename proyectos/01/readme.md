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

### And

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
La compuerta Xor genera una salida alta (1) siempre que sus 2 entradas son diferentes.

| A  | B | SALIDA |
|----|:--:|------:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

<img src="https://mielectronicafacil.com/wp-content/uploads/2020/08/compuerta-logica-or-simbolo.jpg](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLtW-ly6W_g7oWNnJ2Qyfk1W7IwrFMiEkWgucB2KwvIVHuQ9eeOvg4JXY3_z43O0lL4t3Ah5RvrFZ3QI7zPdD5biOKUSZ3i84Hu9qKG6qmusPJEc0trI0bnQ13KptAPaV24uj-4W1z/s1600/circuito-combinacional.gif)https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLtW-ly6W_g7oWNnJ2Qyfk1W7IwrFMiEkWgucB2KwvIVHuQ9eeOvg4JXY3_z43O0lL4t3Ah5RvrFZ3QI7zPdD5biOKUSZ3i84Hu9qKG6qmusPJEc0trI0bnQ13KptAPaV24uj-4W1z/s1600/circuito-combinacional.gif">

### Mux

### DMux

### Not16

### And16

### Or16

### Mux16

### Or8Way

### Mux4Way16

### Mux8Way16

### DMux4Way

### DMux8Way

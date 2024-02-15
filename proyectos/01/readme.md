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

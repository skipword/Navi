# Proyecto 2
Para el segundo proyecto se busca construir diseños de compuertas lógicas que representen números y realicen operaciones aritméticas entre estos. Más específicamente, el objetivo es desarrollar una Unidad Aritmético Lógica (ALU) completamente funcional. Esta ALU es una parte fundamental de la CPU ((Unidad Central de Procesamiento) y su correcta implementación nos ayudará a entender mejor el funcionamiento de una computadora. Dado que estamos tratando con compuertas lógicas, las operaciones como la suma o resta se incorporarán utilizando el sistema binario.

### HalfAdder

### FullAdder
A diferencia del halfAdder, el FullAdder computa la suma de 3 bits: a,b y un bit carry-in, este último se introduce en el sistema para tener en cuenta acarreos de sumas previas, que ocurren cuando el resultado de una suma excede 1. La implementación a HDL sigue la misma lógica que la suma de números binarios, se suma desde el digito menos significativo (derecha) hasta el más significativo (izquierda) y cuando una suma supera 1 se acarrea 1
al siguiente orden superior; esto se modela gracias al HalfAdder codificado previamente. 


*Ejemplo suma de dos números binarios*

<img width="400" src="https://bam.files.bbci.co.uk/bam/live/content/zc6gr82/medium">

*Tabla de verdad FullAdder*

| a | b | c | carry-out | suma |
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

### Inc16

### ALU

## Bibliografía
- https://www.nand2tetris.org/_files/ugd/44046b_f0eaab042ba042dcb58f3e08b46bb4d7.pdf
- https://gittest2121.gitbook.io/nand2tetris/combinational-chips/full-adder-chip

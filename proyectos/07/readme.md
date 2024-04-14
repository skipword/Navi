# Proyecto 7
En el contexto de nand2tetris se emplea un lenguaje de alto nivel denominado *jack* (lenguaje similar a java, introducido en el proyecto 9). Puesto a que una computadora no entiende ni ejecuta instrucciones escritas en este lenguaje, se requiere un compilador que traduzca el código fuente a a instrucciones comprensibles para el hardware (su código de máquina). 

<p align="center">
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fweb.stanford.edu%2Fclass%2Fcs101%2Fsoftware-compiler.png&f=1&nofb=1&ipt=839c2c41837c4ece7574022480470ed9b32e1792c4d0c2b55e255bca8b47598e&ipo=images" alt="Compilador">
</p>
<p align="center"><em>Compilador</em></p>

Si quiero asegurar la portabilidad de mi programa a distintas plataformas, debido a que pueden tener diferentes procesadores e instrucciones de máquina, debo hacer uso de más de un compilador. Para garantizar la flexibilidad y facilitar este proceso se hace uso de una compilación de dos niveles (two-tier compilation):
1. Traducir el código de alto nivel a un lenguaje intermedio, como el código de máquina virtual.
2. Traducir el lenguaje intermedio a código de máquina nativo específico de la plataforma de destino mediante un traductor de máquina virtual.

<p align="center">
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.imgur.com%2FPJME67T.png&f=1&nofb=1&ipt=750d8af959d730d1e9a0134f25fd6a546f8fd3da338370e359539f4773164a30&ipo=images" alt="Compilador">
</p>
<p align="center"><em>Two-tier compilation</em></p>

Así pues, en el presente proyecto se desarrollará un traductor básico de máquina virtual a lenguaje de ensamblador Hack, centrándonos en la implementación de las operaciones de aritmética de pila y acceso a la memoria del lenguaje de la máquina virtual.

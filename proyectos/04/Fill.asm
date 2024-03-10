// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.


(RESTART)
@SCREEN
D=A
@0
M=D    //se guarda direccion de memoria de la pantalla en RAM[0]

///////////////////////////
(KBDCHECK) //loop para verificar si se presiona una tecla

@KBD
D=M
@BLACK
D;JGT    //si el valor en RAM[24576] es mayor que 0, pasa a black
@WHITE
D;JEQ    //si es igual que 0, pasa a white

@KBDCHECK
0;JMP  //salta al inicio de la funcion (bucle)
///////////////////////////
(BLACK)
@1
M=-1    //guarda en RAM[1] el valor del color negro (-1=11111111111111)
@CHANGE
0;JMP //salta a change

(WHITE)
@1
M=0    //guarda en RAM[1] el valor del blanco
@CHANGE
0;JMP //salta a change
//////////////////////////
(CHANGE)
@1    
D=M    //guarda en d el valor a pintar (blanco o negro)

@0
A=M    //en RAM[0] obtiene la direccion de memoria del pixel a llenar
M=D    //lo pinta

@0
M=M+1   //avanza al siguiente pixel

@24576      //carga la direccion de memoria del teclado
D=A
@0
D=D-M //calcula la diferencia entre la dirección de memoria del teclado (D) y la dirección de memoria del siguiente pixel (M) 

@CHANGE
D;JGT    // si es mayor que 0, implica que faltan pixeles por llenar (sigue presionada una tecla)

/////////////////////////
@RESTART
0;JMP
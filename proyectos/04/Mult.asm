@R2
M=0  // Inicializa R2 a 0

@R0
D=M  // Carga el valor de R0 en D
@STEP
D;JGT  // Salta a STEP si R0 es mayor que 0

@END
0;JMP  // Salta a END

(STEP)
    @R2
    D=M  // Carga el valor de R2 en D
    @R1
    D=D+M  // Suma el valor de R1 a D
    @R2
    M=D  // Guarda el resultado en R2
    @R0
    D=M-1  // Decrementa el valor de R0
    M=D  // Guarda el nuevo valor de R0
    @STEP
    D;JGT  // Salta a STEP si R0 es mayor que 0

(END)
    @END
    0;JMP  // Salta a END

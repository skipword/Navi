// push constant3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer0
@0
D=A
@3
D=A+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push constant3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer1
@1
D=A
@3
D=A+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push constant32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop this2
@2
D=A
@THIS
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push constant46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that6
@6
D=A
@THAT
D=M+D
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
// push pointer0
@0
D=A
@3
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push pointer1
@1
D=A
@3
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
M=M+1
// push this2
@2
D=A
@THIS
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1
// push that6
@6
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M+D
@SP
M=M+1

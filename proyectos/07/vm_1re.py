
#!/usr/bin/python
import os, sys


class Parser:
  def __init__(self, source):
    self.infile = open(source)
    self.command = ["nada"]
    self.advanceReachedEOF = False

    self.cType = {
        "sub" : "math",
        "add" : "math",
        "neg" : "math",
        "eq"  : "math",
        "gt"  : "math",
        "lt"  : "math",
        "and" : "math",
        "or"  : "math",
        "not" : "math",
        "push" : "push",
        "pop"  : "pop",
        "EOF"  : "EOF",
        }

  def hasMoreCommands(self):
    position = self.infile.tell()
    self.advance()
    self.infile.seek(position)
    return not self.advanceReachedEOF

  def advance(self):
    thisLine = self.infile.readline()
    if thisLine == '':
      self.advanceReachedEOF = True
    else:
      splitLine = thisLine.split("/")[0].strip()
      if splitLine == '':
        self.advance()
      else:
        self.command = splitLine.split()

  def commandType(self):
    return self.cType.get(self.command[0], "invalid cType")

  def arg1(self):
    return self.command[1]

  def arg2(self):
    return self.command[2]
  
class CodeWriter:
  def __init__(self, dest):
    self.root = dest[:-4].split('/')[-1]
    self.outfile = open(dest, "w")
    self.nextLabel = 0

  def setFileName(self, source):
    self.fileName = source[:-3]

  def writeArithmetic(self, command):
    trans = ""

    if command in ["add", "sub", "and", "or"]:
       trans += "@SP\n"  # pop first value into D
       trans += "AM=M-1\n"
       trans += "D=M\n" 
       trans += "@SP\n"  # get second value
       if command in  ["add", "sub"]:
        trans += "AM=M-1\n" #pop into M
        trans += f"M=M{'+' if command == "add" else '-'}D\n"
        trans += "@SP\n"
        trans += "M=M+1\n" 
       elif command in  ["or", "and"]:
        trans += "A=M-1\n" #get second value into M
        trans += f"M=D{'|' if command in ['or'] else '&'}M\n"

    elif command in ["neg", "not"]:
        trans += "@SP\n" # get (not pop) value into M
        trans += "A=M-1\n" 
        trans += f"M={'-' if command == 'neg' else '!'}M\n"

    elif command in ["eq", "gt", "lt"]:
        label = str(self.nextLabel)
        self.nextLabel += 1
        trans += "@SP\n" # pop first value into D
        trans += "AM=M-1\n"
        trans += "D=M\n" 
        trans += "@SP\n" # get second value into M
        trans += "A=M-1\n"
        trans += "D=M-D\n" # D = older value - newer
        trans += f"M=-1\n" # tentatively put true on stack
        trans += f"@{command}True{label}\n" # jump label
        if command == "eq":
            trans += "D;JEQ\n" # conditional jump
        elif command == "gt":
            trans += "D;JGT\n" # conditional jump
        elif command == "lt":
            trans += "D;JLT\n" # conditional jump
        trans += "@SP\n" # set to false otherwise
        trans += "A=M-1\n"
        trans += "M=0\n" 
        trans += f"({command}True{label})\n"
    else:
        trans = f'{command} no implementado\n'
    self.outfile.write("// " + command + "\n" + trans)

  def writePushPop(self, command, segment, index):
    trans = ""
    if command == "push":
      trans += "// push " + segment + index + "\n"
      if segment in ["constant", "this","that","argument","local","temp","pointer"]:
        trans += "@" + index + "\n" # load index into A
        trans += "D=A\n" # move it to D
        segment_com= {"this": "THIS", "that": "THAT", "argument": "ARG","local":"LCL"}

        if segment in ["this","that","argument","local"]:
            trans += f"@{segment_com[segment]}\n"  #segmentos en mayus y abreviacion
            trans += "A=M+D\n" 
            trans += "D=M\n"
        elif segment == "temp":
            trans += "@5\n"
            trans += "A=A+D\n" 
            trans += "D=M\n"
        elif segment == "pointer":
            trans += "@3\n"
            trans += "A=A+D\n" 
            trans += "D=M\n"

        trans += "@SP\n" # load 0 into A (M[0] contains stack pointer)
        trans += "A=M\n" # load stack pointer
        trans += "M=D\n" # put D onto stack
        trans += "@SP\n" # load stack pointer address into A
        trans += "M=M+1\n" # increment stack pointer
      elif segment == "static":
        trans += "@" + self.root + "." + index + "\n"
        trans += "D=M\n"
        trans += "@SP\n" 
        trans += "A=M\n" 
        trans += "M=D\n"
        trans += "@SP\n"
        trans += "M=M+1\n"
      else:
        trans += segment + " no implementado\n"

    elif command == "pop":
      trans += "// pop " + segment + index + "\n"

      if segment in ["constant", "this","that","argument","local","temp","pointer"]:
        trans += "@" + index + "\n" # get address into R13
        trans += "D=A\n"
        segment_com= {"this": "THIS", "that": "THAT", "argument": "ARG","local":"LCL"}

        if segment in ["this","that","argument","local"]:
            trans += f"@{segment_com[segment]}\n"  #segmentos en mayus y abreviacion
            trans += "D=M+D\n" 
            trans += "@R13\n"
            trans += "M=D\n"
        elif segment == "temp":
            trans += "@5\n"
            trans += "D=A+D\n" 
            trans += "@R13\n"
            trans += "M=D\n"
        elif segment == "pointer":
            trans += "@3\n"
            trans += "D=A+D\n" 
            trans += "@R13\n"
            trans += "M=D\n"
        trans += "@SP\n" # pop value into D
        trans += "AM=M-1\n"
        trans += "D=M\n"
        trans += "@R13\n" # address back in A (no touchy D)
        trans += "A=M\n"
        trans += "M=D\n"

      elif segment == "static":
        trans += "@SP\n" # pop value into D
        trans += "AM=M-1\n"
        trans += "D=M\n"
        trans += "@" + self.root + "." + index + "\n"
        trans += "M=D\n"
      else:
        trans += segment + " no se puede hacer pop\n"
    self.outfile.write(trans)

  def writeError(self):
    self.outfile.write("commando no se reconoce\n")
    

def main():
    input_file = sys.argv[1]
    output_file = input_file + ".asm"  # Nombre del archivo de salida
    parser = Parser(input_file + ".vm")
    writer = CodeWriter(output_file)
  
    while parser.hasMoreCommands():
        parser.advance()
        cType = parser.commandType()
        if cType == "push" or cType == "pop":
            writer.writePushPop(cType, parser.arg1(), parser.arg2())
        elif cType == "math":
            writer.writeArithmetic(parser.command[0])
        else:
            writer.writeError()

    if os.path.exists(output_file):
        print("El archivo", output_file, "se ha creado")
    else:
        print("El archivo", output_file, "no se ha creado.")

    return output_file  

if __name__ == "__main__":
    main()

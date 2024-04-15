
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
        arithmetic_commands = {
            "add": "M=M+D\n",
            "sub": "M=M-D\n",
            "neg": "M=-M\n",
            "not": "M=!M\n",
            "or": "M=D|M\n",
            "and": "M=D&M\n"
        }
        if command in arithmetic_commands:
            trans += "@SP\n"  # pop first value into D
            trans += "AM=M-1\n"
            trans += "D=M\n"
            trans += "@SP\n"  # pop second value into M
            trans += "AM=M-1\n"
            trans += arithmetic_commands[command]
            if command in ["add", "sub", "or", "and"]:
                trans += "@SP\n"
                trans += "M=M+1\n"
        elif command in ["eq", "gt", "lt"]:
            jump = {"eq": "JEQ", "gt": "JGT", "lt": "JLT"}[command]
            label = str(self.nextLabel)
            self.nextLabel += 1
            trans += "@SP\n"  # pop first value into D
            trans += "AM=M-1\n"
            trans += "D=M\n"
            trans += "@SP\n"  # get second value into M
            trans += "A=M-1\n"
            trans += "D=M-D\n"
            trans += "M=-1\n"  # tentatively put true on stack
            trans += f"@{command}True{label}\n"  # and jump to end if so
            trans += f"D;{jump}\n"
            trans += "@SP\n"  # set to false otherwise
            trans += "A=M-1\n"
            trans += "M=0\n"
            trans += f"({command}True{label})\n"
        else:
            trans = f"{command} not implemented yet\n"
        self.outfile.write(f"// {command}\n{trans}")

    def writePushPop(self, command, segment, index):
        trans = ""
        if command == "push":
            trans += f"// push {segment} {index}\n"
            address_commands = {
                "constant": ["@", "A=M", "M=D"],
                "static": ["@" + self.root + "." + index, "D=M"],
                "this": ["@" + index, "D=A", "@THIS", "A=M+D", "D=M"],
                "that": ["@" + index, "D=A", "@THAT", "A=M+D", "D=M"],
                "argument": ["@" + index, "D=A", "@ARG", "A=M+D", "D=M"],
                "local": ["@" + index, "D=A", "@LCL", "A=M+D", "D=M"],
                "temp": ["@" + index, "D=A", "@5", "A=A+D", "D=M"],
                "pointer": ["@" + index, "D=A", "@3", "A=A+D", "D=M"]
            }
            if segment in address_commands:
                trans += "\n".join(address_commands[segment]) + "\n"
                trans += "@SP\n"
                trans += "A=M\n"
                trans += "M=D\n"
                trans += "@SP\n"
                trans += "M=M+1\n"
            else:
                trans += f"{segment} not implemented yet, can't push\n"
        elif command == "pop":
            trans += f"// pop {segment} {index}\n"
            address_commands = {
                "static": ["@SP", "AM=M-1", "D=M", "@" + self.root + "." + index, "M=D"],
                "this": ["@" + index, "D=A", "@THIS", "D=M+D", "@R13", "M=D", "@SP", "AM=M-1", "D=M", "@R13", "A=M", "M=D"],
                "that": ["@" + index, "D=A", "@THAT", "D=M+D", "@R13", "M=D", "@SP", "AM=M-1", "D=M", "@R13", "A=M", "M=D"],
                "argument": ["@" + index, "D=A", "@ARG", "D=M+D", "@R13", "M=D", "@SP", "AM=M-1", "D=M", "@R13", "A=M", "M=D"],
                "local": ["@" + index, "D=A", "@LCL", "D=M+D", "@R13", "M=D", "@SP", "AM=M-1", "D=M", "@R13", "A=M", "M=D"],
                "temp": ["@" + index, "D=A", "@5", "D=A+D", "@R13", "M=D", "@SP", "AM=M-1", "D=M", "@R13", "A=M", "M=D"],
                "pointer": ["@" + index, "D=A", "@3", "D=A+D", "@R13", "M=D", "@SP", "AM=M-1", "D=M", "@R13", "A=M", "M=D"]
            }
            if segment in address_commands:
                trans += "\n".join(address_commands[segment]) + "\n"
            else:
                trans += f"{segment} not implemented yet, can't pop\n"
        self.outfile.write(trans)

    def writeError(self):
        self.outfile.write("Whoopsie, command not recognized\n")


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

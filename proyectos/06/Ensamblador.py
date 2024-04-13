def ensamblador(archivo_entrada):
    # Diccionarios para mapear mnemónicos a códigos binarios
    comp_dict = {
        "0": "0101010", "1": "0111111", "-1": "0111010",
        "D": "0001100", "A": "0110000", "M": "1110000",
        "!D": "0001101", "!A": "0110001", "!M": "1110001",
        "-D": "0001111", "-A": "0110011", "-M": "1110011",
        "D+1": "0011111", "A+1": "0110111", "M+1": "1110111",
        "D-1": "0001110", "A-1": "0110010", "M-1": "1110010",
        "D+A": "0000010", "D+M": "1000010", "D-A": "0010011",
        "D-M": "1010011", "A-D": "0000111", "M-D": "1000111",
        "D&A": "0000000", "D&M": "1000000", "D|A": "0010101",
        "D|M": "1010101"
    }

    dest_dict = {
        "null": "000", "M": "001", "D": "010", "MD": "011",
        "A": "100", "AM": "101", "AD": "110", "AMD": "111"
    }

    jump_dict = {
        "null": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
        "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
    }

    tabla_simbolos = {
        "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
        "R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5,
        "R6": 6, "R7": 7, "R8": 8, "R9": 9, "R10": 10, "R11": 11,
        "R12": 12, "R13": 13, "R14": 14, "R15": 15, "SCREEN": 16384,
        "KBD": 24576
    }

    # Primera pasada para procesar etiquetas y añadir símbolos predefinidos
    with open(archivo_entrada, "r") as archivo:
        direccion_rom = 0
        for linea in archivo:
            linea = linea.strip()
            if not linea or linea.startswith("//"):
                continue
            if linea.startswith("("):
                etiqueta = linea.strip("()")
                tabla_simbolos[etiqueta] = direccion_rom
            else:
                direccion_rom += 1

    # Segunda pasada para traducir las instrucciones
    with open(archivo_entrada, "r") as archivo:
        direccion_ram = 16
        with open(archivo_entrada.replace(".asm", ".hack"), "w") as archivo_salida:
            for linea in archivo:
                linea = linea.strip()
                if not linea or linea.startswith("//") or linea.startswith("("):
                    continue
                if linea.startswith("@"):
                    simbolo = linea[1:]
                    try:
                        direccion = int(simbolo)
                    except ValueError:
                        if simbolo not in tabla_simbolos:
                            tabla_simbolos[simbolo] = direccion_ram
                            direccion_ram += 1
                        direccion = tabla_simbolos[simbolo]
                    direccion_binaria = format(direccion, "016b")
                    archivo_salida.write(direccion_binaria + "\n")
                else:
                    dest_comp_jump = linea.split(";")
                    if "=" in dest_comp_jump[0]:
                        destino, comp = dest_comp_jump[0].split("=")
                    else:
                        destino = "null"
                        comp = dest_comp_jump[0]
                    if len(dest_comp_jump) > 1:
                        salto = dest_comp_jump[1]
                    else:
                        salto = "null"
                    comp_binario = comp_dict[comp]
                    dest_binario = dest_dict[destino]
                    salto_binario = jump_dict[salto]
                    instruccion_binaria = "111" + comp_binario + dest_binario + salto_binario
                    archivo_salida.write(instruccion_binaria + "\n")

# ==== USAR EN CADA UNO DE LOS ARCHIVOS PROPORCIONADOS EN EL PROYECTO ==== #      
#ensamblador("\Add.asm")
#ensamblador("\Max.asm")
#ensamblador("\MaxL.asm")
#ensamblador("\Pong.asm")
#ensamblador("\PongL.asm")
#ensamblador("\Rect.asm")
#ensamblador("\RectL.asm")

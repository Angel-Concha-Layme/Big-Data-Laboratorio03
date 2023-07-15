#!/usr/bin/python3
import sys

# Entrada: líneas de texto desde STDIN
for line in sys.stdin:
    # Elimina espacios al inicio y final de la línea
    line = line.strip()
    # Divide la línea en palabras
    words = line.split()
    # Escribe los resultados a STDOUT
    for word in words:
        # Separa la palabra y la cuenta por un tab
        print('%s\t%s' % (word, 1))


# Entrada e Saída de Vários Tipos

import struct

linha = input().split(" ")
a = int(linha[0])
b = struct.unpack('f', struct.pack('f', float(linha[1])))[0]
c = linha[2]
d = ' '.join(linha[3:])

print(a, end="")
print("{:6f}".format(b), end="")
print(c, end="")
print(d)

print("{}\t{:6f}\t{}\t{}".format(a, b, c, d))
print('%10d%10.6f%10c%10s' % (a, b, c, d))

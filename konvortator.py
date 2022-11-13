with open('aeojaoej.txt') as f:
    lines = f.readlines()

with open('Början.txt') as f:
    början = f.read()

with open('Mitten.txt') as f:
    Miten = f.read()

with open('Slutet.txt') as f:
    Slutet = f.read()


f.close()

texten = början 


for line1 in lines:
    tesam = line1.split()
    texten += Miten
    texten = texten.replace("xan", tesam[0])
    texten = texten.replace("yan", tesam[1])
    texten = texten.replace("zan", tesam[2])
    
texten += Slutet

print(texten)
file = open('bp.sbc', 'w')
file.write(texten)
file.close()
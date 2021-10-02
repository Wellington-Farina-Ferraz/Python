x1 = float (input("Cordenada do primeiro ponto x: "))
y1 = float (input("Cordenada do primeiro ponto y: "))
x2 = float (input("Cordenada do segundo ponto x: "))
y2 = float (input("Cordenada do segundo ponto y: "))

dist = ((x1 - x2 )**2 + (y1 - y2)**2) **0.5

if (dist >=10):
    print ("longe")
else:
    print("perto")
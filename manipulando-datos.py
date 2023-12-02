#int
type(3*9)
#float
type(5.2 + 2.37)
#bool
type(3 <= 5 and 7 > 6.5)
#str
type('Donde queda' + 'Rio de janeiro?')

#CONVERSIÓN DE VALORES

#conversion a str

condicion = 'Son las ' + str(3+12) #'Son las 15'
# print(condicion)

#conversion a int

entero = int(3.55546)
# print(entero)
int('3') + 12 #15

#conversion a float

flotante = float(3)
# print(flotante)

float('3.5') + 12 #15.5

#conversion a bool

bool(0) #False
bool(False) #False
bool(15.5) #True
bool('True') #True
bool('False') #True 
bool('0') #True

#conversion a str

str(3.0)
str(8 + 1.76) + 'segundos'
str(3 < 5 and 9.76 < 10)
import decimal
import fractions
print(decimal.getcontext())
print(decimal.Decimal(5))
from decimal import Decimal
print(Decimal(7))
print(Decimal('0.8'))
print(Decimal(0.8)-Decimal(0.7)) #here 0.8 rep float so python convert that into str and rep and send to decimal,These rounded float values are then passed to theDecimalconstructor and used to construct
#the internal base-10 representations which will be used for the computation. 
print(Decimal('0.8')-Decimal('0.7'))
decimal.getcontext().traps[decimal.FloatOperation]=True
try:
    print(Decimal(0.8)-Decimal(0.7)) #decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
except decimal.DecimalException as ex:
    print("Exception:" ,str(ex))
a=Decimal('3.00')
print(a**2) # Precision maintained
decimal.getcontext().prec=6 #Change the precision
print(Decimal('1.234567')+Decimal('1'))
print(Decimal('Infinity'))
print(Decimal('NaN'))
print(Decimal('NaN') + Decimal('1.414'))
#print(Decimal('1.4') + 0.6) #TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'
print(-7%3) #sign taken from dividend This means that -7 is 2 greater than the largest multiple of 3 which is less than -7, which is -9. 
print(Decimal(-7) % Decimal(3)) #This means that -7 is one less than the next multiple of three towards zero from -7, which is-6.
print(-7 // 3)
print(Decimal(-7)/Decimal(3)) #means that 3 divides into the next multiple of 3 towards zero from -7, which is -6, -2 times
print(Decimal('0.81').sqrt())
print(abs(-5))
print(abs(fractions.Fraction(-5, 1)))
print(round(0.2812,3))
print(round(0.625, 1))
print(round(1.5))
print(round(2.5))#To avoid bias, when there are two equally close alternatives rounding is towards even numbers
print(round(Decimal('3.25'), 1))
print(round(fractions.Fraction(57, 100), 2))
print(bin(42))
print(oct(42))
print(hex(42))
print(hex(42)[2:])
print(int("2a", base=16))
print(int("acghd", base=18))
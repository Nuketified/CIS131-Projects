

from fractions import Fraction

a = Fraction(1,3)
b = Fraction(1,5)
print("a =",a)
print("b =",b,"\n")

print("a + b =",a + b)

print("a - b =",a - b,"\n") 

print("a * b =",a * b)
print("a / b =", a / b)

print(a,b)


float_a = float(a)
float_b = float(b)
print(f"{a} = {float_a}\n{b} = {float_b}\n")



complex_1 = complex(1,7)
complex_2 = complex(5,2)

print("complex_1 + complex_2 =",complex_1 + complex_2)
print("complex_1 - complex_2 =",complex_1 - complex_2)

print("The real part of complex_1 =",complex_1.real)
print("The imaginary part of complex_1 =",complex_1.imag)

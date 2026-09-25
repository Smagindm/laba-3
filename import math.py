import math
a=-0.2
b=0.9
x= (a+b) / 2
term1 = (x*math.sin(x)**2)/math.cos(2*x)
term2 = (math.exp(-2*x)*(math.cos(x)+math.sin(x))) / (math.sin(x) - math.cos(x))
y = x**2 * (term1 + term2)
print(f"Значение при x = {x}:{y}")

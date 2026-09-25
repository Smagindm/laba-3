import math
x=0.75
numerator = math.asin(x)**2 + math.acos(x)**2
demirator = math.sin(x)**2+math.cos(x)**2
y=(2**x)*numerator/demirator
print(f"Значение при x= {x}:{y}")
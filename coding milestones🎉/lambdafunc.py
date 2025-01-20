def give(x):
  return lambda y : y * x

double = give(3)
triple= give(4)

print(double(11))
print(triple(8))
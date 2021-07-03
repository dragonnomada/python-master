primos = []

n = 2

while len(primos) < 100:
  es_primo = True
  
  for p in primos:
    if n % p == 0:
      es_primo = False

  if es_primo:
    primos.append(n)

  n = n + 1
  
print(primos)
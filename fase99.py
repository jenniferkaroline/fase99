def desafio1():
  C = float(input("digite a temperatura em graus °C: "))
  F = ((9 * C) / 5) + 32
  print('a temperatura de {}°C é equivalente a {}°F'.format(C, F))

def desafio2():
  s = input("você se identifica como homem ou como mulher? ")
  h = float(input("digite sua altura: "))
  if s == "homem":
    ph = (72.7 * h) - 58
    print("o peso ideal para um homem é {:.1f} ".format(ph))
  else:
    pm = (62.1 * h) - 44.7
    print("o peso ideal para uma mulher é {:.1f} ".format(pm))

def desafio3():
  r = float(input("raio do círculo: "))
  a = (3.14 * r ** 2)
  print("a área do círculo com raio de {} é igual a {:.2f} ".format(r, a))

def desafio4():
  l = float(input("digite o lado de um quadrado: "))
  aq = l ** 2
  print("a área do quadrado com lado de {} é igual a {:.2f}".format(l, aq))
    

































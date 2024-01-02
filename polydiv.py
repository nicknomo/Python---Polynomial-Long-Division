from fractions import Fraction

def printpolynomial(polynomial):
  for x in range(len(polynomial)):
    if (len(polynomial)-x-1)==1:
      print(Fraction(polynomial[x]),"x +",end=" ")

    elif len(polynomial)-x-1==0:
      print(Fraction(polynomial[x]))

    else:
      print(Fraction(polynomial[x]),"x^",len(polynomial)-x-1," +",end=" ")  

  

print("Enter the degree/power of the polynomial you are dividing: ")
degree1 = int(input())
dividend = []
divisor = []
for x in range(degree1+1):
  print("Enter the coefficient for x^", degree1-x ,": ")
  dividend.append(float(input()))


print("Enter the degree/power of the polynomial you are dividing by: ")
degree2=int(input())

for x in range(degree2+1):
  print("Enter the coefficient for x^", degree2-x ,": ")
  divisor.append(float(input()))

if degree2>degree1:
  print("The divisor is larger than the dividend.")
  print("Maybe you have them reversed?")

quotient = [0.0]*(degree1-degree2+1)
tempdividend = dividend.copy()
tempdivisor = divisor.copy()




for x in range(degree1-degree2+1):
  quotientcoefficient = tempdividend[0]/divisor[0]
  quotient[x] = quotientcoefficient

  for z in range(len(tempdivisor)):
    tempdivisor[z] = round(tempdivisor[z] *-quotientcoefficient,13)

  for z in range(len(tempdivisor)):
    tempdividend[z] = tempdividend[z] + tempdivisor[z]

  tempdividend = tempdividend[1:]

  tempdivisor = divisor.copy()
  


print()
print()



remainder=tempdividend.copy()
print("Quotent is:")
printpolynomial(quotient)


print()
print("Remander is:")
printpolynomial(remainder)

print("/")
printpolynomial(divisor)

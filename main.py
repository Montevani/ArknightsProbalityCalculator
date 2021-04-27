import math

#Para 1~49:  f(x) = 1-e^(-0.02*x) [62.4689%]
#1-math.exp(-0.02*x)
#Para 50~99: f(x) = 1-e^(-(0.02+0.02*x)*x)
#1-math.exp(-(0.02+0.02*x)*x)

while True:
  try:
    last = int(input('How many times have you rolled since your last 6*? '))
    if isinstance(last, int):  #optional
        if 0 <= last <=98:
            break
  except ValueError:
    print("Please enter a value between 0 and 98!")

while True:
  try:
    nrolls = int(input('How many times are you going to roll? '))
    if isinstance(nrolls, int):  #optional
        if 0 <= nrolls:
            break
  except ValueError:
    print("Please enter a number bigger than 0!")
if nrolls == 69:
  print("Nice.")

while True:
  try:
    feat = int(input('How many 6* operators are featured in the banner? '))
    if isinstance(feat, int):  #optional
        if feat == 1 or feat == 2:
            break
  except ValueError:
    print("So far we only had banners with 1 or 2 featured 6* operators.")

succ = 0.02/(feat+1)

if nrolls+last > 99:
    cdfa=100
    #cdff

elif 98 > (nrolls+last) > 50:
    #cdfa=100
    #cdff=50+25+12.5+...

else:
    cdfa = (1-math.exp(-0.02*nrolls))*100
    cdff = (1-math.exp(-succ*nrolls))*100
    


print("\nYour chances of getting any 6* character is {:.2f}%".format(cdfa))
print("and your chances of getting a featured 6* character is {:.2f}%".format(cdff))

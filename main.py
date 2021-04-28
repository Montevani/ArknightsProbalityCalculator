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

loop = 0
cdfa = cdfl = cdff =  1
rollNumber = last

for rolls in range(nrolls):
  rollNumber=rollNumber+1

  if rollNumber <= 49:
    cdfa = cdfa*0.98
    #cdfl = cdfl*0.993
  elif 50 <= rollNumber <= 99:
    cdfa = cdfa*(1-((rollNumber-49)*0.02))
    #cdfl = cdfl*(1-((rollNumber-49)*0.007))
  
  if rollNumber == 99:
    rollNumber = 0
    loop = loop +1

faill = (1-0.35)**loop
failf = (1-0.5/feat)**loop

totalfaill = faill #multiplica algo que faz no roll 99 ser 0.65 e no 1 ser 0.993
totalfailf = failf #multiplica algo que faz no roll 99 ser 0.75 e no 1 ser 0.995

cdfl = 1-totalfaill
cdff = 1-totalfailf
cdfa = 1-cdfa

print("\nHere are your chances of getting:")
print("Any 6* operator: {:.2f}%".format(cdfa*100))
print("A specific 6* operator: {:.2f}%".format(cdff*100))
print("A specific limited 6* operator: {:.2f}%".format(cdfl*100))
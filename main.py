import math

print("\n----- Arknights Probability Calculator -----\n")
while True:
  try:
    last = int(input('How many times have you rolled since your last 6* (0~98)? '))
    if isinstance(last, int):  #optional
        if 0 <= last <=98:
            break
  except ValueError:
    print("Please enter a valid number between 0 and 98!")

while True:
  try:
    nrolls = int(input('How many times are you going to roll? '))
    if isinstance(nrolls, int):  #optional
        if 0 <= nrolls:
            break
  except ValueError:
    print("Please enter a valid number!")
if nrolls == 69:
  print("Nice.")

loop = 0
cdfa = partial =  1
rollNumber = last

for rolls in range(nrolls):
  rollNumber=rollNumber+1

  if rollNumber <= 49:
    cdfa = cdfa*0.98
    partial = partial*0.98

  elif 50 <= rollNumber <= 99:
    cdfa = cdfa*(1-((rollNumber-49)*0.02))
    partial = partial*(1-((rollNumber-49)*0.02))
  
  if rollNumber == 99:
    rollNumber = 0
    partial = 1
    loop = loop +1


totalfailf1 = ((1-0.5)**loop)*(1-((1-partial)*(0.5)))
totalfailf2 = ((1-0.25)**loop)*(1-((1-partial)*(0.25)))
totalfaill = ((1-0.35)**loop)*(1-((1-partial)*(0.35)))

cdfa = 1-cdfa
cdff1 = 1-totalfailf1
cdff2 = 1-totalfailf2
cdfl = 1-totalfaill

print("\nHere are your chances of getting:")
print("- Any 6* operator: {:.4f}%".format(cdfa*100))
print("- A featured operator in a standard banner with a SINGLE rate-up 6*: {:.4f}%".format(cdff1*100))
print("- A specific featured operator in a standard banner with TWO rate-up 6*s: {:.4f}%".format(cdff2*100))
print("- A specific featured operator in a LIMITED banner: {:.4f}%".format(cdfl*100))
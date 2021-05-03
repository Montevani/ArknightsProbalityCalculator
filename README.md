# ArknightsProbalityCalculator
What are your odds of getting a rate-up 6* operator on your next roll?  
After inputing how many times you plan to roll and when was the last time your got a 6* operator this program will calculate your chances of getting a 6* operator.

<p align="center">
  <img width="640" height="270" src="https://github.com/Montevani/ArknightsProbalityCalculator/blob/main/pictures/ArkLogo.jpg">
</p>

### What is Arknights?
If you're here you probably already knows what Arknights is but just in case: Arknights is a Chinese tower defense mobile game developed by Studio Montagne and Hypergryph and published by Yostar and Hypergryph. In the game players can use in-game currency to randomly obtain new characters (operators) through a gacha system, a game mechanic similar to slot machines and roulette wheels. Characters are ranked by their rarity and strength, with 6* operators being the most rare and usually the most powerful.

### What are the odds for a single pull?
It depends on the banner. So far Arknights had 3 different types of banner:
Standard banners with a single featured operator, standard banners with two featured operators and limited banners with two featured operators.
**The odds of getting a 6 stars operator is always 2%** across all 3 types of banner but the chances of getting the featured operators are different for each banner:
For standard banners there's a 50% chance that any 6* operator you get will be one of the featured characters. That chance is increased to 70% in limited banners. If more than a single character is featured on the banner the rate-up is equally shared between the two (although we're still not 100% sure about that. It needs more testing).
In other words:

For **standard banners with a SINGLE rate-up operator** your chances of getting a specific featured 6 stars is: ***1%***  
For **standard banners with a TWO rate-up operators** your chances of getting a specific featured 6 stars is: ***0.5%***  
For **limited banners** your chances of getting a specific featured 6 stars is: ***0.7%***  

Arknights has a second mechanic to ensure that even the unluckiest doctor will get at least a single 6* operator after enough rolls: The pity rate!
After 50 attempts without a single 6* operators your odds will start to **increase by 2% every attempt until you get a 6*** operator. After getting a 6* operator your odds will go back to the regular 2% and will only start increasing again after 50 unlucky rolls.
For example, your odds of getting a 6* operator on your first 50 rolls are 2% on each roll. If you didn't get a single 6* so far your chances will increase to 4% on your 51th roll, on roll 52 it'll be 6% and so on until you reach roll 99 where your chances will have increased all the way to 100%.  

Your **pity rate is shared across all standard banners** but is unique for limited banners. So, if you roll 20 times on today's standard banner you'll be on roll 21 on next month's standard banner. But if you rolled 40 times on today's banner or on W's limited banner you'll still be on roll 0 on Rosmonti's limited banner. Keep that in mind when deciding when or on what to roll.

<p align="center">
  <img width="640" height="200" src="https://github.com/Montevani/ArknightsProbalityCalculator/blob/main/pictures/Banner.jpg">
</p>  

### How does this calculator works?
Calculating your odds of getting a 6* operator without the pity rate (first 50 rolls) is quite simple.  
Let's say you want to know your odds for **n** attempts. All you have to do is calculate your chances of not getting a single 6* operator in **n** attempts consecutively and subtract it from 100%:
<p align="center">
  <img width="200" height="20" src="https://github.com/Montevani/ArknightsProbalityCalculator/blob/main/pictures/Eq1.jpg">
</p>
The exact way Arknights calculates what operator you're going to get is a mystery but it's assumed the game first checks if you're going to pull a 6* operator or not and then, after that is confirmed, it chooses what operator will pop out of the recruitment bag.
For example, your chances of getting Rosmontis from the last limited banner with your 10 free rolls is going to be:  
<p align="center">
  <img width="465" height="20" src="https://github.com/Montevani/ArknightsProbalityCalculator/blob/main/pictures/Eq2.jpg">
</p>
Similarly your chances of getting Mudrock (the other featured 6* operator) would also be **6.40%** and your chances of getting a random 6* operator would be **5.49%**:
<p align="center">
  <img width="455" height="70" src="https://github.com/Montevani/ArknightsProbalityCalculator/blob/main/pictures/Eq5.jpg">
</p>
Things get more complicated after the the pity rate. The function that would describe your chances of getting a 6* operator taking it into account can be written as:
<p align="center">
  <img width="630" height="80" src="https://github.com/Montevani/ArknightsProbalityCalculator/blob/main/pictures/Eq3.jpg">
</p>  
Where n is the number of rolls you're planning to attempt, r is the number of the current roll and rate is your chance of getting your target operator.  
For example, your chances of getting a specific operator in a limited banner after 60 rolls and starting from roll 0 would be:
<p align="center">
  <img width="585" height="60" src="https://github.com/Montevani/ArknightsProbalityCalculator/blob/main/pictures/Eq4.jpg">
</p>

### But there's a problem...!
As we already know the pity rate resets immediately after the player manages to roll a 6* operator and unfortunately that last equation doesn't take that into consideration. 

### Graphs!

(insert graphs here)

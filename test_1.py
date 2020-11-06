


"""
The program is trying to determine which payment option is better (more money).
First option is 100 dollars per day for 10 days. The second option is 1 dollar
a day with it being doubled each day for 10 days. There will be two functions to calculate the pay rate.
Function1 will calculate the amount for the first option, function2 will calculate the amount for the second option.

function1 will output 100 * 10 days
function2 will will loop 10 times, with each time, doubling the amount and add the amount to the total

if the amount is equal, we output to the user "Option 1 and option 2 pay the same"
if option 1 is better, we output to the user "Option 1 is better"
If the option2 is better, we output to the user "Option 2 is better"
"""

"""

# option1
return 100 * 10

# option2
amount = 1 
list1 = []
loop 10 times
 add amount to list1
 amount *= 2
return amount
# main  
   var1 = option1
  var2= option2

If var1 = var 2
   "option 1 and option 2 pays the same"
If var1 < var2
   "option 2 is better"
else
  "option 1 is better"

main
"""

def option 1():
   return 100 * 10

def option2():
   amount = 1
   list 1 = []
   for i in range (0 , 10):
      list1.addend(amount)
      amount *= 2
   print("list1", list1)
   total = sum (list1)
   return total

def main():
 answer = ""
 var1 = option1 #1000
 var2 = option2 #1023
 print("from main: var1", var1 "var2", var2)
 if var1 == var2:
    answer = "Option1 and option 2 pays the same"
if var1 < var2:
   answer = "Option 2 is better"
else:
   answer = "Option 1 is better"
print(answer)

var1 = option1()
var2 = option2()
print(var1)
print (var2)

main()
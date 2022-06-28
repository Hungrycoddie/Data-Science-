# >  greater than 
# >= greater than or equal to 
# <  less than 
# <= less than or equal to 
# == Assign value of quality from the liught to left 
# != NOT EQUAL TO 
# if   ..  If the answer to  the question is true go ahead and exicute it 
#elif  else if 
#or 
#*********************************************
#methord 1
score = int (input("score: "))

if score >= 90 and score <=100:
    print ("Grade: A")

if score > 100 and score >100:
    print ("Grade: Outstanding")

elif score >= 80 and score < 90:
    print ("Grade: B")

elif score >= 70 and score < 80:
    print ("Grade: C")

elif score >= 60 and score <70:
    print ("Grade: D")

#else should be used at the last 
else:
     print("FAIL")


#*****************************************
#methord 2

score = int (input("score: "))

if score >=90:
    print ("Grade: A")

elif score >= 80:
    print ("Grade: B")

elif score >= 70:
    print ("Grade: C")

elif score >= 60:
    print ("Grade: D")

else:
    print("FAIL")

#**************************************
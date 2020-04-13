#Command to the user requesting to enter 5 random numbers  
print("Please do enter the 5 Random numbers: ")

#Command for the user to take 5 random numbers
n1 = int(input("Enter the First Number, n1: "))
n2 = int(input("Enter the Seond Number, n2: "))
n3 = int(input("Enter the Third Number, n3: "))
n4 = int(input("Enter the Fouth Number, n4: "))
n5 = int(input("Enter the Fifth Number, n5: "))

#List declarations which will be taken and used in the program
L1 = [n1,n2,n3,n4, n5]
L2 = []
L3 = []

print()
print("The comma seperated Numbers list is: ", L1)
print()

#Get Average Function
def getAverage():
  Ave = sum(L1)/len(L1)
  print("The Average of given 5 numbers is:" + " " + str(Ave))

#Get Largest number Function
def getLargest():
  Largest = max(L1)
  print("The largest of the given 5 numbers is:" + " " + str(Largest))

#Get Smallest number Function
def getSmallest():
  Smallest = min(L1)
  print("The smallest of the given 5 numbers is:" + " " + str(Smallest))

#Check if Order of the numbers Function
def isOrdered():
  for num in range(0, len(L1)-1):
    if L1[num] < L1[num+1]:
      L2.append(L1[num])
    elif (L1[num] > L1[num+1]) :
      L3.append(L1[num])
    else:
      pass

  if len(L2) == len(L1)-1:
    L2.append(L1[len(L1)-1])
  elif len(L3) == len(L1)-1:
    L3.append(L1[len(L1)-1])

  if len(L2) == len(L1):
    print("The Given numbers are in Accending order and they are represented as: " ,L2)
  elif len(L3) == len(L1):
    print("The Given numbers are in Decending order and they are represented as: ", L3)
  else:
    print("The Given numbers are in out of Order and they are represented as: ", L1)


#Calling of the Functions for Output
getAverage()
print()
getLargest()
print()
getSmallest()
print()
isOrdered()
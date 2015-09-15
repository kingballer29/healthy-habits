#QualityLife
#By Tom Biju

import csv #python module to parse the csv data easily

class qualityLife():

  def getAverageLifeExpectancy():
  
    f=open('life_expectancy.csv') #opening file for use
    csv_file=csv.reader(f) #csv object

    boolean=False #variable to allow us to skip the first line in the file which just contains headings
    neighborhoodNamesLifeExpectancy={}
    
    for row in csv_file:
      if(boolean):
        neighborhoodNamesLifeExpectancy[row[1]]=row[len(row)-1]
      boolean=True
  
    f.close() #closing file
  
    z=open('farmers_markets.csv')
    csv_opener=csv.reader(z)
    boolean=False
    farmersMarketLocations=[]
    for line in csv_opener:
      if(boolean):
        farmersMarketLocations.append(line[0])
      boolean=True
    z.close()
    goodFood=[]
    for location in farmersMarketLocations:
      for neighborhood in neighborhoodNamesLifeExpectancy:
        if neighborhood in location:
          goodFood.append(neighborhood)

    s=open('Senior_Centers.csv')
    csv_canopener=csv.reader(s)
    boolean=False
    seniorCenterLocations=[]
    for line in csv_canopener:
      if(boolean):
        seniorCenterLocations.append(line[1])
      boolean=True
    s.close()
    seniorCare=[]
    for center in seniorCenterLocations:
      for neighborhood in neighborhoodNamesLifeExpectancy:
        if neighborhood in center:
          seniorCare.append(neighborhood)
          
    l=open('library_visits.csv')
    librarycsv=csv.reader(l)
    boolean=False
    libraryVisits=[]
    for row in librarycsv:
      if(boolean):
        libraryVisits.append(row[0])
      boolean=True
      libraries=[]
    for library in libraryVisits:
      for neighborhood in neighborhoodNamesLifeExpectancy:
        if neighborhood in library:
          libraries.append(neighborhood)
    
    return goodFood, seniorCare, libraries, neighborhoodNamesLifeExpectancy
  
  def getAverage(li):
    a=len(li)
    li=map(float,li)
    sumTotal=0
    for item in li:
      sumTotal+=item
    return (sumTotal/a)
      
  def getHardshipIndex():
    h=open('income.csv')
    csv_accessor=csv.reader(h)
    boolean=False
    hardshipDictionary={}
    for row in csv_accessor:
      if(boolean):
        hardshipDictionary[row[1]]=row[len(row)-1]
      boolean=True
    h.close()
    return hardshipDictionary

  def writeToCSVFiles():
    f=open('life_expectancy.csv') #opening file for use
    csv_file=csv.reader(f) #csv object

    boolean=False #variable to allow us to skip the first line in the file which just contains headings
    neighborhoodNames=[]
    lifeExpectancies=[]
    
    for row in csv_file:
      if(boolean):
        neighborhoodNames.append(row[1])
        lifeExpectancies.append(row[len(row)-1])
      boolean=True
  
    f.close() #closing file
    
    with open('life_expectancy_data.csv','w',newline='')as fp:
      a=csv.writer(fp, delimiter=',')
      data=[neighborhoodNames,lifeExpectancies]
      a.writerows(data)
    return lifeExpectancies
  
  def simplifyData(x,y,z):
     if len(x)>=len(y):
       first=x
       checkAgain=y
     else:
       first=y
       checkAgain=x
     if len(checkAgain)>=len(z):
        second=checkAgain
        third=z
     else:
        second=z
        third=checkAgain
     return second, third
    
  def findIdealNeighborhoods(y,z):
    ideal=[]
    i=0
    for items in y:
      for thing in z:
        if items in thing:
          ideal.append(thing)
    return ideal
  
  def writeIdeal(ideal):
    with open('ideal_neighborhoods.csv','w',newline='')as fp:
      x=csv.writer(fp, delimiter=",")
      x.writerows(ideal)
      
  def writeHardshipIndex():
    h=open('income.csv')
    csv_accessor=csv.reader(h)
    boolean=False
    hardshipNames=[]
    hardshipIndices=[]
    for row in csv_accessor:
      if(boolean):
        hardshipNames.append(row[1])
        hardshipIndices.append(row[len(row)-1])
      boolean=True
    h.close()
    with open('hardship_data.csv','w',newline='')as fp:
      a=csv.writer(fp, delimiter=',')
      data=[hardshipNames,hardshipIndices]
      a.writerows(data)
    return hardshipIndices
if __name__=="__main__":
    print("Let's try to see how various things come into play for life expectancy")
    print("Here are some Chicago neighborhoods and their life expectancies\n")
    b=qualityLife.getAverageLifeExpectancy()
    print(b)
    print("\n")
    averageLife=qualityLife.writeToCSVFiles()
    averageLifeExpectancyChicago=qualityLife.getAverage(averageLife)
    print("\n")
    print("The average life expectancy for all of Chicago is: ")
    print(averageLifeExpectancyChicago)
    print("\n")
    g=qualityLife.simplifyData(b[0],b[1],b[2])
    n=qualityLife.findIdealNeighborhoods(g[0],g[1])
    qualityLife.writeIdeal(n)
    hardshipIndices=qualityLife.getHardshipIndex()
    print("The hardship indices for Chicago: ")
    print("\n")
    print(hardshipIndices)
    print("\n")
    print("Neighborhoods that have senior centers include: ")
    print(b[2])
    print("\n")
    print("Ones that have libraries: ")
    print("\n")
    print(b[2])
    print("\n")
    print("Ones that have healthy food opportunities: ")
    print("\n")
    print(b[0])
    print("\n")

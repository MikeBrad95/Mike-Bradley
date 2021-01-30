
# coding: utf-8

# In[ ]:


import csv 
import statistics

filename = 'TotalPopSex.csv'
fileobject = open(filename)
data = csv.reader(fileobject)
data_list = list(data)


# In[ ]:


for i in range(len(data_list)):
    if "Germany" in data_list[i][1]:
        print("Germany", i)
    elif "Finland" in data_list[i][1]:
        print("Finland", i)
        
germany_data = [int(i.replace(" ","")) for i in data_list[2][12:]]
finland_data = [int(i.replace(" ","")) for i in data_list[1][12:]]

years = [int(i.replace(" ","")) for i in data_list[0][12:]]
startIndex = 0
endIndex = 0

for i in years:
    if i == 1990:
        startIndex = years.index(i)
    elif i == 2030:
        endIndex = years.index(i)
        
years = years[startIndex:endIndex+1]
germany_data = germany_data[startIndex:endIndex+1]
finland_data = finland_data[startIndex:endIndex+1]


# In[ ]:


import matplotlib.pyplot as plt

plt.plot(years, germany_data)
plt.plot(years, finland_data)
plt.xlabel('Years')
plt.ylabel('Population in thousands')
plt.title('Appendix 1')
plt.plot(years, germany_data, "-b", label="Germany")
plt.plot(years, finland_data, "-r", label="Finland")
plt.legend(loc="upper left")
plt.ylim(0,90000)
plt.show()

plt.plot(years, germany_data)
plt.xlabel('Years')
plt.ylabel('Population, in thousands')
plt.title('Appendix 2')
plt.show()

plt.plot(years, finland_data,  color = 'red')
plt.xlabel('Years')
plt.ylabel('Population, inthousands')
plt.title('Appendix 3')
plt.show()


# In[ ]:


import csv 

filename = 'CrudeBirthRate.csv'
fileobject = open(filename)
data = csv.reader(fileobject)
data_list = list(data)


# In[ ]:


for i in range(len(data_list)):
    if "Germany" in data_list[i][1]:
        print("Germany", i)
    elif "Finland" in data_list[i][1]:
        print("Finland", i)
        
germany_data = [float(i.replace(" ","")) for i in data_list[2][3:]]
print(germany_data)
finland_data = [float(i.replace(" ","")) for i in data_list[1][3:]]
years = [(i.replace(" ","")) for i in data_list[0][3:9]]

startIndex = 0
endIndex = 0
for i in years:
    if i == '1990-1995':
        startIndex = years.index(i)
    elif i == '2015-2020':
        endIndex = years.index(i)
        
years = years[startIndex:endIndex+1]
germany_data = germany_data[startIndex:endIndex+1]
finland_data = finland_data[startIndex:endIndex+1]


# In[ ]:


import matplotlib.pyplot as plt

plt.plot(years, germany_data)
plt.plot(years, finland_data)
plt.xlabel('Years')
plt.ylabel('Population in thousands')
plt.title('Appendix 4')
plt.plot(years, germany_data, "-b", label="Germany")
plt.plot(years, finland_data, "-r", label="Finland")
plt.legend(loc="upper left")
plt.show()

plt.plot(years, germany_data)
plt.xlabel('Years')
plt.ylabel('Population, in thousands')
plt.title('Appendix 5')
plt.show()

plt.plot(years, finland_data, color = 'red')
plt.xlabel('Years')
plt.ylabel('Population, in thousands')
plt.title('Appendix 6')
plt.show()


# In[ ]:


import csv 

filename = 'CrudeDeathRate.csv'
fileobject = open(filename)
data = csv.reader(fileobject)
data_list = list(data)


# In[ ]:


for i in range(len(data_list)):
    if "Germany" in data_list[i][1]:
        print("Germany", i)
    elif "Finland" in data_list[i][1]:
        print("Finland", i)
        
germany_data = [float(i.replace(" ","")) for i in data_list[2][3:]]
print(germany_data)
finland_data = [float(i.replace(" ","")) for i in data_list[1][3:]]
years = [(i.replace(" ","")) for i in data_list[0][3:9]]

startIndex = 0
endIndex = 0
for i in years:
    if i == '1990-1995':
        startIndex = years.index(i)
    elif i == '2015-2020':
        endIndex = years.index(i)
        
years = years[startIndex:endIndex+1]
germany_data = germany_data[startIndex:endIndex+1]
finland_data = finland_data[startIndex:endIndex+1]


# In[ ]:


plt.plot(years, germany_data)
plt.plot(years, finland_data)
plt.xlabel('Years')
plt.ylabel('Population in thousands')
plt.title('Appendix 7')
plt.plot(years, germany_data, "-b", label="Germany")
plt.plot(years, finland_data, "-r", label="Finland")
plt.legend(loc="upper left")
plt.show()

plt.plot(years, germany_data)
plt.xlabel('Years')
plt.ylabel('Population, in thousands')
plt.title('Appendix 8')
plt.show()

plt.plot(years, finland_data, color = 'red')
plt.xlabel('Years')
plt.ylabel('Population, in thousands')
plt.title('Appendix 9')
plt.show()


# In[ ]:


import csv 

filename = 'NetMigrationRate.csv'
fileobject = open(filename)
data = csv.reader(fileobject)
data_list = list(data)


# In[ ]:


for i in range(len(data_list)):
    if "Germany" in data_list[i][1]:
        print("Germany", i)
    elif "Finland" in data_list[i][1]:
        print("Finland", i)
        
germany_data = [float(i.replace(" ","")) for i in data_list[2][3:]]
finland_data = [float(i.replace(" ","")) for i in data_list[1][3:]]
years = [(i.replace(" ","")) for i in data_list[0][3:9]]

startIndex = 0
endIndex = 0

for i in years:
    if i == '1990-1995':
        startIndex = years.index(i)
    elif i == '2015-2020':
        endIndex = years.index(i)
        
years = years[startIndex:endIndex+1]
germany_data = germany_data[startIndex:endIndex+1]
finland_data = finland_data[startIndex:endIndex+1]


# In[ ]:


import matplotlib.pyplot as plt

plt.plot(years, germany_data)
plt.plot(years, finland_data)
plt.xlabel('Years')
plt.ylabel('Population in thousands')
plt.title('Appendix 10')
plt.plot(years, germany_data, "-b", label="Germany")
plt.plot(years, finland_data, "-r", label="Finland")
plt.legend(loc="upper left")
plt.show()

plt.plot(years, germany_data)
plt.xlabel('Years')
plt.ylabel('Population, in thousands')
plt.title('Appendix 11')
plt.show()

plt.plot(years, finland_data, color = 'red')
plt.xlabel('Years')
plt.ylabel('Population, in thousands')
plt.title('Appendix 12')
plt.show()


# In[ ]:


def turn_100():
    current_year = 2020
    age = int(input("How old are you?: "))
    born_year = current_year - age
    hundred_year = born_year+100
    return 'You will turn 100 in', hundred_year
print(turn_100())


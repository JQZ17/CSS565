import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("*******/Train.txt", sep="|",
                 names=["duration", "protocoltype", "service", "flag", "srcbytes", "dstbytes", "land", "wrongfragment",
                        "urgent", "hot", "numfailedlogins", "loggedin", "numcompromised", "rootshell", "suattempted",
                        "numroot", "numfilecreations", "numshells", "numaccessfiles", "numoutboundcmds", "ishostlogin",
                        "isguestlogin", "count", "srvcount", "serrorrate", "srvserrorrate",
                        "rerrorrate", "srvrerrorrate", "samesrvrate", "diffsrvrate", "srvdiffhostrate", "dsthostcount",
                        "dsthostsrvcount", "dsthostsamesrvrate", "dsthostdiffsrvrate", "dsthostsamesrcportrate",
                        "dsthostsrvdiffhostrate", "dsthostserrorrate", "dsthostsrvserrorrate",
                        "dsthostrerrorrate", "dsthostsrvrerrorrate", "attack", "lastflag"])

print(df.head())
df.drop(['numfailedlogins', 'loggedin', 'numcompromised', 'rootshell', 'suattempted', 'numroot', 'numfilecreations',
         'numshells', 'numaccessfiles', 'numoutboundcmds', 'ishostlogin', "rerrorrate",
         'isguestlogin', 'count', 'srvcount', 'serrorrate', 'srvserrorrate', 'srvrerrorrate', 'samesrvrate',
         'diffsrvrate', 'srvdiffhostrate', "dsthostsamesrcportrate", 'dsthostsrvdiffhostrate', 'dsthostserrorrate',
         'dsthostsrvserrorrate',
         'dsthostrerrorrate', 'dsthostsrvrerrorrate', 'lastflag'], axis=1, inplace=True)
print(df.head())

x = df['attack'].copy()
for i in range(20):
    if x[i] != 'normal':
        x[i] = 'attack'
df['attack'] = x
print(df)


dsthostcount = df['dsthostcount']
dsthostsrvcount = df['dsthostsrvcount']
combine = np.random.normal(size=(20, 2), loc=0, scale=1)
for i in range(20):
    combine[i] = [dsthostcount[i], dsthostsrvcount[i]]
data = np.array(combine)

# data = np.random.normal(size = (1000, 2), loc= 0, scale= 1)
# print(data)
#plt.boxplot(data, labels=['dsthostcount', 'dsthostsrvcount'])
#plt.show()

dsthostsamesrvrate = df['dsthostsamesrvrate']
dsthostdiffsrvrate = df['dsthostdiffsrvrate']
combineTwo = np.random.normal(size=(20, 2), loc=0, scale=1)
for i in range(20):
    combineTwo[i] = [dsthostsamesrvrate[i], dsthostdiffsrvrate[i]]
dataTwo = np.array(combineTwo)

# data = np.random.normal(size = (1000, 2), loc= 0, scale= 1)
# print(data)
#plt.boxplot(dataTwo, labels=['dsthostsamesrvrate', 'dsthostsamesrvrate'])
#plt.show()

new_variable = dsthostsrvcount.copy()
for i in range(20):
    new_variable[i] = dsthostcount[i] + 3

df.insert(11, 'new_variable', new_variable)

dataThree = np.array(df['new_variable'])
dataFour = np.array(dsthostcount)
plt.boxplot(dataThree, labels=['new_variable'])
plt.show()
plt.boxplot(dataFour, labels=['dsthostcount'])
plt.show()
sum_1 = 0
sum_2 = 0
max_1 = 0
max_2 = 0
min_1 = dsthostcount[0]
min_2 = new_variable[0]
for i in range(20):

    sum_1 = sum_1 + dsthostcount[i]

    if dsthostcount[i] >= max_1:
        max_1 = dsthostcount[i]
    if dsthostcount[i] <= min_1:
        min_1 = dsthostcount[i]

    if new_variable[i] >= max_2:
        max_2 = new_variable[i]
    if new_variable[i] <= min_2:
        min_2 = new_variable[i]
    sum_2 = sum_2 + new_variable[i]

one = dsthostcount.copy()
one = one.values.tolist()
one.sort()
two = new_variable.copy()
two = two.values.tolist()
two.sort()
median_1 = (one[9] + one[10]) / 2
median_2 = (two[9] + two[10]) / 2
range_1 = max_1 - min_1
range_2 = max_2 - min_2
print(range_1)
print(range_2)

print(median_1)
print(median_2)
print('********************')

dsthostcount_plus = dsthostcount.copy()
for i in range(20):
    dsthostcount_plus[i] = dsthostcount[i]
dsthostcount_plus[20] = 200
dsthostcount_plus[21] = 260

new_variable_plus = new_variable.copy()
for i in range(20):
    new_variable_plus[i] = new_variable[i]
new_variable_plus[20] = 198
new_variable_plus[21] = 202


max_plus_1 = 0
max_plus_2 = 0
min_plus_1 = dsthostcount_plus[0]
min_plus_2 = new_variable_plus[0]

for i in range(20):

    if dsthostcount_plus[i] >= max_plus_1:
        max_plus_1 = dsthostcount_plus[i]
    if dsthostcount_plus[i] <= min_plus_1:
        min_plus_1 = dsthostcount_plus[i]

    if new_variable_plus[i] >= max_plus_2:
        max_plus_2 = new_variable_plus[i]
    if new_variable_plus[i] <= min_plus_2:
        min_plus_2 = new_variable_plus[i]

one_plus = dsthostcount_plus.copy()
one_plus = one_plus.values.tolist()
one_plus.sort()
two_plus = new_variable_plus.copy()
two_plus = two_plus.values.tolist()
two_plus.sort()
median_plus_1 = (one_plus[9] + one_plus[10]) / 2
median_plus_2 = (two_plus[9] + two_plus[10]) / 2
range_plus_1 = max_plus_1 - min_plus_1
range_plus_2 = max_plus_2 - min_plus_2
print(median_plus_1)
print(median_plus_2)
print(range_plus_1)
print(range_plus_2)

combineFour = np.random.normal(size=(22, 2), loc=0, scale=1)
for i in range(22):
    combineFour[i] = [dsthostcount_plus[i], new_variable_plus[i]]
dataFour = np.array(combineFour)

# data = np.random.normal(size = (1000, 2), loc= 0, scale= 1)
# print(data)
plt.boxplot(dataFour, labels=['dsthostcount_plus', 'new_variable_plus'])
plt.show()

print('finish')

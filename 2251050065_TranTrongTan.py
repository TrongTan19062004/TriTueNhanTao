import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=[4879,12104,12756,6792,142984,120536,51118,49528]
#Cau 1
dimasters=pd.Series(data)
print(dimasters)

Index=["Mercury", "Venus", "Earth", "Mars", "Jupyter", "Saturn", "Uranus", "Neptune"]
dimasters=pd.Series(data,index=Index)
# print(dimasters)
# print(dimasters["Earth"])

#Cau 4
print(dimasters["Mercury"])
#Cau 5
print(dimasters["Mercury":"Mars"])
#Cau 6
dimasters['Ploto']=2370
print(dimasters)
#Cau 7
data2={'dimasters':[4879,12104,12756,6792,142984,120536,51118,49528,2370],

      'avg_temp':[167,464,15,-65,-110, -140, -195, -200, -225],
      'gravity':[3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]
      }
plants=pd.DataFrame(data2)
print(plants)
#=========================Cau 8============================
print(plants.head(5))
#=========================Cau 9============================
print(plants.tail(3))
#=========================Cau 10============================
print(plants.columns)
#=========================Cau 11============================
planets=pd.DataFrame(data2,index=dimasters.index)
#=========================Cau 12============================
print(planets["dimasters"])
#=========================Cau 13============================
print(planets[["dimasters","gravity"]])
#=========================Cau 14============================
print(planets.loc["Earth","gravity"])
#=========================Cau 15============================
print(planets.loc[["Earth"],["dimasters","gravity"]])
#=========================Cau 16============================
print(planets.loc["Earth":"Saturn",["dimasters","gravity"]])
#=========================Cau 17============================
print(planets["dimasters"]>1000)
#=========================Cau 18============================
print(planets[planets["dimasters"]>10000] )
#=========================Cau 19============================

print(planets[(planets["avg_temp"] > 0) & (planets["gravity"] > 5)])
#=========================Cau 20============================
planets.sort_values(by="dimasters",ascending=True)
print(planets.sort_values(by="dimasters",ascending=True))
#=========================Cau 21============================
print("========================Cau21==========================")

print(planets.sort_values(by="dimasters",ascending=False))
#=========================Cau 22============================
print("========================Cau22==========================")
print(planets.sort_values(by="gravity", ascending=False))
#-------------------------Cau23-------------------------------

print(planets.loc["Mercury"].sort_values)


#====================SEABORN============================
# ====================Cau1===============================
tips = sns.load_dataset("tips")
sns.set_style("whitegrid")
g = sns.lmplot(x="tip", y="total_bill", data=tips,
               aspect=2)
g = (g.set_axis_labels("Tip", "Total bill(USD)").
     set(xlim=(0, 10), ylim=(0, 100)))
plt.title("Cau 1")
plt.show()
#===================Cau2=================================
print("Cau2")
print("2.",sns.get_dataset_names())
#===================Cau3==================================
#3
tips_df = sns.load_dataset('tips')
print("3.",tips_df.head())
#4
tips = sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.show()
#5
sns.set(font_scale=1.2)
sns.set_style("darkgrid")
tips = sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.show()
#6
tips = sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', hue='day', data=tips)
plt.show()
#7
tips = sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', size='size', data=tips)
plt.show()
#8
tips = sns.load_dataset('tips')
g = sns.FacetGrid(tips, col="time")
g.map(sns.scatterplot, 'total_bill', 'tip')
plt.show()
#9
tips = sns.load_dataset('tips')
g = sns.FacetGrid(tips, col="time", row="sex")
g.map(sns.scatterplot, 'total_bill', 'tip')
plt.show()

#=======================================PANDAS=======================================
#=================CAU1====================
print("-------------1------------")
gapminder= pd.read_csv('04_gap-merged.tsv',header=None,nrows=5)
print(gapminder)

print("-------------2------------")
data= pd.read_csv('04_gap-merged.tsv',sep='\t')
print(data.shape)
#3
print("-------------3------------")
print(data.columns)
#4
print("-------------4------------")
print(data.dtypes)
#5
print("-------------5------------")
country=data['country']
print('head',country.head(5))
#6
print('head',country.tail(6))
#7
print(data[['country','continent','year']].head(5))
#8
print(data._ixs(0))
print(data._ixs(99))
#9
print(data._ixs(1,axis=1))
print(data._ixs(5,axis=1))
#10
last_index=data.index[-1]
print(data.loc[last_index])
#11
print(data.iloc[[0,99,999]])
index_value=data.index
print(data.loc[[index_value[0],index_value[99],index_value[999]]])
#12
print(data.iloc[42],['country'])
print(data.loc[42],['country'])
#13
print(data.iloc[[0,99,999],[0,5,3]])
#14
gapminder2= pd.read_csv('04_gap-merged.tsv',header=None,nrows=10)
print(gapminder2)
#15
print(data.groupby('year')['lifeExp'].mean())
#16
res={}
unique_year=data['year'].unique()

for year in unique_year:
    subset = data[data['year']==year]
    res[year]=subset['lifeExp'].mean()
for year,avg in res.items():
    print(year,avg)
#17
series= pd.Series(['banana',42],index=[0,1])
print(series)
#18
series['Person']= 'Wes MCKinney'
series['Who']='Creator of Pandas'
print(series)
#19
dict = {
    "Occupation": ["Chemist", "Statistician"],
"Born": ["1920-07-25", "1876-06-13"],
"Died": ["1958-04-16", "1937-10-16"],
"Age": [37, 61]
}
print(pd.DataFrame(dict,index=['Franklin','Gosset']))

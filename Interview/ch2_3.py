import pandas as pd 

names1880=pd.read_csv('pydata-book-master/ch02/names/yob1880.txt',names=['name','sex','births'])
#names1880=pd.read_csv('names\yob1880.txt',names=['name','sex','births'])
names1880.groupby('sex').births.sum()

years=range(1880,2011)
pieces=[]
columns=['name','sex','births']

for year in years:
    path='pydata-book-master/ch02/names/yob%d.txt' %year
    frame=pd.read_csv(path,names=columns)

    frame['year']=year
    pieces.append(frame)

names=pd.concat(pieces,ignore_index=True)

total_births=names.pivot_table('births',index='year',columns='sex',aggfunc='sum')

total_births.plot(title='Total births by sex and year')

def add_prop(group):
    births=group.births.astype(float)

    group['prop']=births/births.sum()
    return group
names=names.groupby(['year','sex']).apply(add_prop)

np.allclose(names.groupby(['year','sex']).prop.sum(),1)

def get_top1000(group):
    return group.sort_index(by='births',ascending=False)[:1000]
grouped=names.groupby(['year','sex'])
top1000=grouped.apply(get_top1000)

boys=top1000[top1000.sex=='M']
girls=top1000[top1000.sex=='F']
total_births=top1000.pivot_table('births',index='year',columns='name',aggfunc=sum)

subset=total_births[['John','Harry','Mary','Marilyn']]
subset.plot(subplots=True,figsize=(12,10),grid=False,title="Num of birth per year")

table=top1000.pivot_table('prop',index='year',columns='sex',aggfunc=sum)
table.plot(title='Sum of table1000.prop by year and sex',
           yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10))









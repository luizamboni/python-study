import pandas as pd


df = pd.read_csv("./support/dataset/super_hero_powers.csv")


# project
df1 = df[['Agility', 'hero_names']]

# groupby
import pdb; pdb.set_trace()
df1_group = df1.groupby('Agility')

# out group
print df1_group.count()
print df1_group.describe()



# select

df_heros_with_agility =  df[(df.Agility == True)]

print(df_heros_with_agility)
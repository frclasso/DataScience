import pandas as pd

tips = pd.read_csv('tips.csv')

# Criando catergorias (sex) permite melhor performance

# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

# Print the info of tips
print(tips.info())

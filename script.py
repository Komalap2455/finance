#%% read csv file
import pandas as pd
df = pd.read_csv('Aggregate_Expenditure.csv')
print(df)
# %%UnicodeDecodeError: 'utf-8' codec can't decode byte 0x96 in position 573: invalid start byte
# Solution: encoding='latin1'
df = pd.read_csv('Aggregate_Expenditure.csv', encoding='latin1')
print(df)

# %%
df.head()
# %%
# Basic github

# connect vscode to github
# Intialise git: git init
# add: gid add .
# commit: git commit -a -m “This is a message for your commit”
# add remote: paste git link and name them “I have used sopost”
# git remote add origin <REMOTE_URL>
# git push origin master
# To ignore files and folder use .gitignore

# touch .gitignore
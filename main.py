import pandas as pd
import numpy as np

df = pd.read_csv('ViewingActivity.csv')

users = df['Profile Name'].unique()

df = df[df['Supplemental Video Type'].isna()]
df['Start Time'] = pd.to_datetime(df['Start Time'])



def duration_hrs(df):
    
    df['Duration'] = df['Duration'].astype(str)

    hr = df['Duration'].str.split(':').str[0].astype(int)
    min = df['Duration'].str.split(':').str[1].astype(int)
    sec = df['Duration'].str.split(':').str[2].astype(int)

    df['Duration (hrs)'] = hr + min/60 + sec/3600
        
    return df

df['Year'] = df['Start Time'].dt.strftime('%Y')
years = df['Year'].unique()

# print(duration_hrs(df).head(10))
print(len(df['Title'].unique()))


# for user in users:
#     user_df = df[df['Profile Name'] == user]
#     print(user_df)

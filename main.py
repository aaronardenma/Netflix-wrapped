import pandas as pd
import numpy as np

df = pd.read_csv('ViewingActivity.csv')

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

users = df['Profile Name'].unique()
years = df['Year'].unique()



df = df.drop(columns= ['Attributes', 'Bookmark', 'Latest Bookmark'])

duration_hrs(df)
sum_durations_df = df[['Title', 'Duration (hrs)']]
sum_durations_df = sum_durations_df.groupby(by = ['Title']).sum().sort_values(by= ['Duration (hrs)'], ascending= True).rename(columns={'Duration (hrs)': 'Total Duration (hrs)'})

print(sum_durations_df.head(20))




### Stats
number_content_pieces_watched = len(df['Title'].unique())

# print(duration_hrs(df).head(10))
# for user in users:
#     user_df = df[df['Profile Name'] == user]
#     print(user_df)

import pandas as pd
import numpy as np

df = pd.read_csv('ViewingActivity.csv')
netflix_titles = pd.read_csv('netflix_titles.csv')

df = df[df['Supplemental Video Type'].isna()]

df['Start Time'] = pd.to_datetime(df['Start Time'])

def duration_hrs(df):
    df['Duration'] = df['Duration'].astype(str)

    hr = df['Duration'].str.split(':').str[0].astype(int)
    min = df['Duration'].str.split(':').str[1].astype(int)
    sec = df['Duration'].str.split(':').str[2].astype(int)

    df['Duration (hrs)'] = hr + min/60 + sec/3600
        
    return df

df['Year'] = df['Start Time'].dt.strftime('%Y').astype(int)

users = df['Profile Name'].unique()
years = df['Year'].unique()

print(df[df['Year'] == 2022])

# df = df.drop(columns= ['Attributes', 'Bookmark', 'Latest Bookmark'])

# duration_hrs(df)

# ### Total durations per content in descending order

titles = df['Title']
for title in titles:
    netflix_titles[netflix_titles['title'] == title]


def sum_duration_unique_content(df):
    sum_durations_df = df[['Title', 'Duration (hrs)']]
    sum_durations_df = (sum_durations_df.groupby(by = ['Title'])
                        .sum()
                        .sort_values(by= ['Duration (hrs)'], ascending= True)
                        .rename(columns={'Duration (hrs)': 'Total Duration (hrs)'}))


    return sum_durations_df


# # print(netflix_titles[netflix_titles['title'].duplicated()])


# ### Stats
# number_content_pieces_watched = len(df['Title'].unique())

# def total_hrs_watched():
#     return
# total_hrs_watched = sum_durations_df['Total Duration (hrs)'].sum().round(2)

# print(total_hrs_watched)

# for user in users:
#     user_df = df[df['Profile Name'] == user]

#     for year in years:
#         df[df['Year'] == year]
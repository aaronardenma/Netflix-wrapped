import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv('ViewingActivity.csv')
k_netflix_titles = pd.read_csv('netflix_titles.csv')

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

# print(df[df['Year'] == 2022])

# df = df.drop(columns= ['Attributes', 'Bookmark', 'Latest Bookmark'])

duration_hrs(df)

# ### Total durations per content in descending order
df['Title'] = df['Title'].astype(str)
# df['Title'] = df['Title'].str.strip()

df['title 2'] = df['Title'].str.split(':').str[0]
titles2 = df['title 2']

_type2_found = []
_country2_found = []

for row_idx, title in enumerate(titles2):
    kaggle_row_idx = np.where(title == k_netflix_titles['title'])[0]
    if len(kaggle_row_idx) == 1:
        kaggle_row_idx = kaggle_row_idx[0]
        type_found = k_netflix_titles['type'][kaggle_row_idx]
        country_found = k_netflix_titles['country'][kaggle_row_idx]

    else:
        type_found = np.nan
    _type2_found += [type_found]
    _country2_found += [country_found]

_type2_found = pd.Series(_type2_found)
_country2_found = pd.Series(_country2_found)
df['Type 2'] = _type2_found
df['Country 2'] = _country2_found


titles = df['Title']
# print(df['title 2'].head(10))
_type_found = []
_country_found = []

for row_idx, title in enumerate(titles):
    kaggle_row_idx = np.where(title == k_netflix_titles['title'])[0]
    if len(kaggle_row_idx) == 1:
        kaggle_row_idx = kaggle_row_idx[0]
        type_found = k_netflix_titles['type'][kaggle_row_idx]
        country_found = k_netflix_titles['country'][kaggle_row_idx]

    else:
        type_found = np.nan
    _type_found += [type_found]
    _country_found += [country_found]

_type_found = pd.Series(_type_found)
_country_found = pd.Series(_country_found)
df['Type'] = _type_found
df['Country'] = _country_found

# df['Title'].str.split(':').str[0]

t = df['Title'].str.split(':')[:2]
titles3 = ":".join(t)

_type3_found = []
_country3_found = []

for row_idx, title in enumerate(titles3):
    kaggle_row_idx = np.where(title == k_netflix_titles['title'])[0]
    if len(kaggle_row_idx) == 1:
        kaggle_row_idx = kaggle_row_idx[0]
        type_found = k_netflix_titles['type'][kaggle_row_idx]
        country_found = k_netflix_titles['country'][kaggle_row_idx]

    else:
        type_found = np.nan
    _type3_found += [type_found]
    _country3_found += [country_found]

_type3_found = pd.Series(_type3_found)
_country3_found = pd.Series(_country3_found)
df['Type 3'] = _type3_found
df['Country 3'] = _country3_found

# print(df['Type'].isna().sum())

df['Type'] = df['Type'].fillna(df['Type 2'])
df['Type'] = df['Type'].fillna(df['Type 3'])

print(df['Type'].isna().sum())

# print(((df.loc[df['Type'].isna(), 'title 2']).unique()))

# print(df['Type'].isna().sum())

    # k_netflix_titles[k_netflix_titles['title'] == title]



# def sum_title_watchtime(df):
# filtered_title_df = df[['Title', 'Duration (hrs)']]
# sum_title_watchtime_df = (filtered_title_df.groupby(by = ['Title'])
#                     .sum()
#                     .sort_values(by= ['Duration (hrs)'], ascending= True)
#                     .rename(columns={'Duration (hrs)': 'Total Duration (hrs)'}))


# filtered_type_df = df[['Type', 'Duration (hrs)']]
# sum_type_watchtime_df = (filtered_type_df.groupby(by=['Type'])
#                          .sum()
#                          .sort_values(by= ['Duration (hrs)'], ascending = True)
#                          .rename(columns = {'Duration (hrs)': 'Total Duration (hrs)'}))
# print(sum_type_watchtime_df)
    # return sum_title_watchtime_df



# k_netflix_titles.drop_duplicates(subset=['title'])
# print(k_netflix_titles[k_netflix_titles['title'].duplicated()])


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
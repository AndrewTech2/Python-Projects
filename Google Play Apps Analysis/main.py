import pandas, string

def is_english(st):
    strikes = 0
    for char in st:
        if ord(char) not in range(128):
            strikes += 1
            if strikes == 3:
                return False
    return True

df = pandas.read_csv('googleplaystore.csv')
df = df[df['Price'] == '0']
for ind, row in df.iterrows():
    title = row['App']
    if not is_english(title):
        df = df.drop([ind])
unique = []
for ind, row in df.iterrows():
    title = row['App']
    if title not in unique:
        unique.append(title)
    else:
        df = df.drop([ind])

genres_df = df.groupby('Genres')['App'].count()
genres_df = genres_df.sort_values(ascending=False)
genres = genres_df.to_dict()
df_dict = df.to_dict()
print("Most successful genres:")
for genre in genres:
    print(f"{genre}: {genres[genre]} apps")
    ind = list(df[df['Genres'] == genre]['Installs'].sort_values(ascending=False).to_dict().keys())[0]
    print(f"Most popular: {df_dict['App'][ind]}")
    print()
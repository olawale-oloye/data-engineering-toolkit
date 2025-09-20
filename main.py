df['Average weight (lb)'] = df['Average weight'].apply(lambda x: float(re.findall(r"\d+\.\d+", x)[1]) )
df['Average weight (Kg)'] = df['Average weight'].apply(lambda x: float(re.findall(r"\d+\.\d+", x)[0]) )
df.drop(columns = 'Average weight' , inplace=True)
df.rename(columns = {'Adult population (millions)': 'Adult population (M)'}, inplace=True)
df['% Overweight'] = df['% Overweight'].apply(lambda x: float(re.findall(r'\d+\.\d', x)[0]) )

print(df)

sns.barplot(x=df['Region'], y=df['Average weight (Kg)'], hue=df['Region'])
plt.xticks(rotation= 70)
plt.show()
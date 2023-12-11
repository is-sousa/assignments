import argparse
import pandas as pd
import numpy as np

def load_data():
    data = pd.read_csv('life_expectancy/data/eu_life_expectancy_raw.tsv', sep='\t')
    return data

def clean_data(data, country):
    data[['unit', 'sex', 'age', 'region']] = data[r'unit,sex,age,geo\time'].str.split(
        ',', expand=True)

    data.drop(columns=data.columns[0], inplace=True)

    cleaned_data = pd.melt(data, id_vars=['unit', 'sex', 'age', 'region'], var_name='year',
                        value_name='value')

    cleaned_data['value'] = cleaned_data['value'].str.replace(r'[^0-9.]', '', regex=True)

    cleaned_data['value'] = cleaned_data['value'].replace('', np.nan)

    cleaned_data['year'] = cleaned_data['year'].astype(int)

    cleaned_data['value'] = cleaned_data['value'].astype(float)

    portugal_data = cleaned_data[cleaned_data['region'] == country]

    portugal_data = portugal_data.dropna(subset=['value'])

    return portugal_data

def save_data(portugal_data):
    portugal_data.to_csv('life_expectancy/data/pt_life_expectancy.csv', index=False)

def main():
    data = load_data()
    cleaned_data = clean_data(data, 'PT')
    save_data(cleaned_data)
    return clean_data

if __name__ == '__main__':  # pragma: no cover
    main()

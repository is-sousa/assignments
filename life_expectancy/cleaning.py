from enum import Enum
import pandas as pd
import numpy as np

class Region(Enum):
    PT = 'PT'
    BE = 'BE'
    BG = 'BG'
    AT = 'AT'
    CH = 'CH'
    CY = 'CY'
    CZ = 'CZ'
    DK = 'DK'
    EE = 'EE'
    EL = 'EL'
    ES = 'ES'
    EU = 'EU'
    FI = 'FI'
    FR = 'FR'
    HR = 'HR'
    HU = 'HU'
    IS = 'IS'
    IT = 'IT'
    LI = 'LI'
    LT = 'LT'
    LU = 'LU'
    LV = 'LV'
    MT = 'MT'
    NL = 'NL'
    NO = 'NO'
    PL = 'PL'
    RO = 'RO'
    SE = 'SE'
    SI = 'SI'
    SK = 'SK'
    DE = 'DE'
    AL = 'AL'
    EA = 'EA'
    EF = 'EF'
    IE = 'IE'
    ME = 'ME'
    MK = 'MK'
    RS = 'RS'
    AM = 'AM'
    AZ = 'AZ'
    GE = 'GE'
    TR = 'TR'
    UA = 'UA'
    BY = 'BY'
    UK = 'UK'
    XK = 'XK'
    FX = 'FX'
    MD = 'MD'
    SM = 'SM'
    RU = 'RU'
    EA18 = 'EA18'
    EA19 = 'EA19'
    EFTA = 'EFTA'
    EEA30_2007 = 'EEA30_2007'
    EEA31 = 'EEA31'
    EU27_2007 = 'EU27_2007'
    EU28 = 'EU28'

    @classmethod
    def get_actual_countries(cls):
        return [region.value for region in cls if len(region.value) == 2]

def load_data(file_path='life_expectancy/data/eu_life_expectancy_raw.tsv'):
    data = pd.read_csv(file_path, sep='\t')

    return data

def clean_data(data, country: Region):
    df = data.copy()

    df[['unit', 'sex', 'age', 'region']] = df[df.columns[0]].str.split(
        ',', expand=True)

    df.drop(columns=df.columns[0], inplace=True)

    cleaned_data = pd.melt(df, id_vars=['unit', 'sex', 'age', 'region'], var_name='year',
                        value_name='value')

    cleaned_data['value'] = cleaned_data['value'].str.replace(r'[^0-9.]', '', regex=True)

    cleaned_data['value'] = cleaned_data['value'].replace('', np.nan)

    cleaned_data['year'] = cleaned_data['year'].astype(int)

    cleaned_data['value'] = cleaned_data['value'].astype(float)

    country_data = cleaned_data[cleaned_data['region'] == country.value]

    country_data = country_data.dropna(subset=['value'])

    return country_data

def save_data(country_data, file_path='life_expectancy/data/country_life_expectancy.csv'):
    country_data.to_csv(file_path, index=False)

def main():
    data = load_data()
    countries = Region.get_actual_countries()

    for country in countries:
        cleaned_data = clean_data(data, Region[country])
        save_data(cleaned_data)
        return cleaned_data

if __name__ == '__main__':  # pragma: no cover
    main()

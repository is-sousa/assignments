import argparse
import pandas as pd
import numpy as np
from life_expectancy.cleaning import load_data, clean_data

def create_input_fixture():
    data = load_data()

    sample_data = data.sample(n=500)

    sample_data.to_csv('life_expectancy/tests/fixtures/eu_life_expectancy_raw.tsv', sep='\t', index=False)

    return sample_data

def create_output_fixture(sample_data):
    clean_data = clean_data(sample_data, 'PT')

    clean_data.to_csv('life_expectancy/tests/fixtures/eu_life_expectancy_expected.csv', index=False)

    return clean_data

def main():
    create_input_fixture = create_input_fixture()
    create_output_fixture = create_output_fixture(create_input_fixture)
    print("Cleaned DataFrame:")
    print(create_output_fixture)

if __name__ == '__main__':  # pragma: no cover
    main()
"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import clean_data, Region
from life_expectancy.tests import FIXTURES_DIR


def test_clean_data(eu_life_expectancy_input, eu_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    
    cleaned_data = clean_data(eu_life_expectancy_input, Region['PT'])

    pd.testing.assert_frame_equal(
        cleaned_data, eu_life_expectancy_expected
    )
    
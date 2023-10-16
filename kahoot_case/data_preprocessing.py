import pandas as pd

def load_data():
    """
    Loads the datasets and returns them.
    
    Returns:
    - cwur: DataFrame containing CWUR data.
    - shanghai: DataFrame containing Shanghai data.
    - times: DataFrame containing Times data.
    - country_mapping: DataFrame containing country mapping data.
    - educational_expenditure: DataFrame containing educational expenditure data.
    """
    cwur = pd.read_csv('/mnt/data/cwurData.csv')
    shanghai = pd.read_csv('/mnt/data/shanghaiData.csv')
    times = pd.read_csv('/mnt/data/timesData.csv')
    country_mapping = pd.read_csv('/mnt/data/school_and_country_table.csv')
    educational_expenditure = pd.read_csv('/mnt/data/education_expenditure_supplementary_data.csv')
    
    return cwur, shanghai, times, country_mapping, educational_expenditure

def preprocess_and_merge(cwur, shanghai, times, country_mapping, educational_expenditure):
    """
    Preprocesses the data and merges it.
    
    Parameters:
    - cwur: DataFrame containing CWUR data.
    - shanghai: DataFrame containing Shanghai data.
    - times: DataFrame containing Times data.
    - country_mapping: DataFrame containing country mapping data.
    - educational_expenditure: DataFrame containing educational expenditure data.
    
    Returns:
    - merged_data: Merged DataFrame for CWUR.
    - merged_data_shanghai: Merged DataFrame for Shanghai.
    - merged_data_times: Merged DataFrame for Times.
    """
    # Preprocess CWUR data
    cwur_2015 = cwur[cwur['year'] == 2015][['world_rank', 'institution', 'country']]

    # Preprocess Shanghai data
    shanghai_2015 = shanghai[shanghai['year'] == 2015][['world_rank', 'university_name', 'national_rank']]
    shanghai_2015['world_rank'] = shanghai_2015['world_rank'].str.split('-').str[0]

    # Preprocess Times data
    times_2015 = times[times['year'] == 2015][['world_rank', 'university_name', 'country']]
    times_2015['world_rank'] = times_2015['world_rank'].str.split('-').str[0]

    # Merge data
    merged_data = cwur_2015.merge(country_mapping, left_on='institution', right_on='school_name', how='left')
    merged_data = merged_data.merge(educational_expenditure, on='country', how='left')

    merged_data_shanghai = shanghai_2015.merge(country_mapping, left_on='university_name', right_on='school_name', how='left')
    merged_data_shanghai = merged_data_shanghai.merge(educational_expenditure, on='country', how='left')

    merged_data_times = times_2015.merge(country_mapping, left_on='university_name', right_on='school_name', how='left')
    merged_data_times = merged_data_times.merge(educational_expenditure, on='country', how='left')
    
    return merged_data, merged_data_shanghai, merged_data_times

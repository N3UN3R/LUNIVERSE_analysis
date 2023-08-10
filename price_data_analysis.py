import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime, timezone

def csv_reader(file):
    """ reads csv file into pandas dataframe"""
    data = pd.read_csv(file)# index_col=0)#uses first column as index

    return data


def create_markt_prices_dict(data2019, data2020, data2021, data2022):
    market_prices = pd.DataFrame()
    # market_prices['Date'] = time
    # market_prices['Date'] = pd.to_datetime(data2019['Datum (MEZ)'])
    market_prices['market price 2019'] = pd.to_numeric(data2019['Day Ahead Auktion'])
    market_prices['market price 2020'] = pd.to_numeric(data2020['Day Ahead Auktion'])
    market_prices['market price 2021'] = pd.to_numeric(data2021['Day Ahead Auktion'])
    market_prices['market price 2022'] = pd.to_numeric(data2022['Day Ahead Auktion'])
    market_prices['Date2'] = pd.to_datetime(time_stamps['time'])
    market_prices.set_index(market_prices['Date2'], inplace=True)

    return market_prices


def get_hourly_data_for_days(market_prices):
    monthly_data = {}
    for month, group in market_prices.resample('M', on='Date2'):
        monthly_data[month] = {}
        for day, group2 in group.resample('D', on='Date2'):
            monthly_data[month][day] = group2

    return monthly_data


def get_minimum_values_dictionaries(monthly_data):
    month_key_list = list(monthly_data.keys())

    minimums_2019 = {}
    minimums_2020 = {}
    minimums_2021 = {}
    minimums_2022 = {}
    for month in month_key_list:
        # monthly_data[month] = werte für den Januar
        # monthly_data[month]
        day_keys = list(monthly_data[month].keys())
        for day in day_keys:
            minimum_index = monthly_data[month][day]['market price 2019'].idxmin()
            minimum_value = monthly_data[month][day]['market price 2019'][minimum_index]
            minimums_2019[minimum_index] = minimum_value

            minimum_index = monthly_data[month][day]['market price 2020'].idxmin()
            minimum_value = monthly_data[month][day]['market price 2020'][minimum_index]
            minimums_2020[minimum_index] = minimum_value

            minimum_index = monthly_data[month][day]['market price 2021'].idxmin()
            minimum_value = monthly_data[month][day]['market price 2021'][minimum_index]
            minimums_2021[minimum_index] = minimum_value

            minimum_index = monthly_data[month][day]['market price 2022'].idxmin()
            minimum_value = monthly_data[month][day]['market price 2022'][minimum_index]
            minimums_2022[minimum_index] = minimum_value

    return minimums_2019, minimums_2020, minimums_2021, minimums_2022


def create_dataframes_for_charging_simulation(monthly_data):
    charging_df = {}

    month_key_list = list(monthly_data.keys())
    for month in month_key_list:
        day_keys = list(monthly_data[month].keys())
        charging_df[month] = {}

        for day in day_keys:
            df = monthly_data[month][day]
            filtered_df = df[(df['Date2'].dt.hour >= 18) | (df['Date2'].dt.hour < 0)]
            charging_df[month][day] = filtered_df

    return charging_df


def count_occurence_of_values(data):
    tempDf = pd.DataFrame()
    tempDf.index = list(data.keys())
    tempDf['prices'] = list(data.values())
    tempDf['date'] = list(data.keys())
    tempDf['Hour'] = tempDf['date'].dt.hour

    counter_frame = tempDf.groupby('Hour').count()

    return counter_frame

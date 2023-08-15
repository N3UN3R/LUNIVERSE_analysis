from price_data_analysis import *
from saving_calculations import *

if __name__ == '__main__':

    #read in data
    csv_data_2019 = csv_reader("energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2019.csv")
    data2019 = csv_data_2019.iloc[1:]
    csv_data_2020 = csv_reader("energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2020.csv")
    data2020 = csv_data_2020.iloc[1:]
    csv_data_2021 = csv_reader("energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2021.csv")
    data2021 = csv_data_2021.iloc[1:]
    csv_data_2022 = csv_reader("energy-charts_Stromproduktion_und_Börsenstrompreise_in_Deutschland_2022.csv")
    data2022 = csv_data_2022.iloc[1:]

    #create market prices dataframe
    market_prices = create_markt_prices_dict(data2019, data2020, data2021, data2022)

    #get monthly data
    monthly_data = get_hourly_data_for_days(market_prices)

    #dictionaries with minimum prices of each day
    minimums_2019, minimums_2020, minimums_2021, minimums_2022 = get_minimum_values_dictionaries(monthly_data)


    end_consumer_prices = market_prices
    end_consumer_prices['market price 2019'] = (end_consumer_prices['market price 2019']+14.735)*1.19
    end_consumer_prices['market price 2020'] = (end_consumer_prices['market price 2020']+14.735)*1.19
    end_consumer_prices['market price 2021'] = (end_consumer_prices['market price 2021']+14.735)*1.19
    end_consumer_prices['market price 2022'] = (end_consumer_prices['market price 2022']+14.735)*1.19
    end_consumer_prices
    
    
    #calculate mean price
    mean_price_2019 = end_consumer_prices['market price 2019'].mean()
    mean_price_2019

    #calculate sacvings water boiler
    _,total_cost_2019, total_savings = savings_of_water_boiler(minimums_2019)

    #calculate savings of EV
    _,total_cost_euroEV, total_savingsEV = savings_of_electric_vehicle(minimums_2019)



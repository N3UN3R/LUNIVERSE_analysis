def savings_of_electric_vehicle(price_dict):
    
    minimum_values = price_dict.values()
    df = pd.DataFrame(price_dict.values(), index=price_dict.keys(), columns=['prices'])
    
    #power of 5.5 kW over 1 hour assuming 1 hour consumption for each day
    df['prices'] = df['prices']*5.5
    total_cost_euro = sum(df['prices'])/100
    
    #reference
    electricity_price = mean_price_2019
    costs = 2000 * electricity_price/100
    
    total_savings = costs -total_cost_euro
    
    return df,total_cost_euro, total_savings

df,total_cost_euro, total_savings = savings_of_electric_vehicle(minimums_2019)
total_savings

def savings_of_water_boiler(price_dict):
    """ input: minimums2019"""
    minimum_values = price_dict.values()
    df = pd.DataFrame(price_dict.values(), index=price_dict.keys(), columns=['prices'])
    #power of 2 kW over 1 hour assuming 1 hour consumption for each day
    df['prices'] = df['prices']*2
    total_cost_euro = sum(df['prices'])/100
    
    #reference
    electricity_price = 30.43
    costs = 730 * electricity_price/100
    
    total_savings = costs -total_cost_euro
    
    return df,total_cost_euro, total_savings


_,total_cost_2019, total_savings = savings_of_water_boiler(minimums_2019)

total_cost_2019
total_savings


def savings_of_electric_vehicle2(price_dict):
    
    minimum_values = price_dict.values()
    df = pd.DataFrame(price_dict.values(), index=price_dict.keys(), columns=['prices'])
    
    #power of 5.5 kW over 1 hour assuming 1 hour consumption for each day
    df['prices'] = df['prices']*5.5
    total_cost_euro = sum(df['prices'])/100
    
    #reference
    electricity_price = 30.43
    costs = 2000 * electricity_price/100
    
    total_savings = costs -total_cost_euro
    
    return df,total_cost_euro, total_savings

df,total_cost_euro, total_savings = savings_of_electric_vehicle(minimums_2019)
total_savings

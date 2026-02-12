import yfinance as yf
import pandas as pd
from prettytable import PrettyTable

#%% 1
print("\n Question 1:")
stocks = ['AAPL', 'ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT' ]
start_date = '2013-01-01'
end_date = '2024-05-22'

features = ['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']

data = {}
for stock in stocks:
    df = yf.download(stock, start=start_date, end=end_date, auto_adjust=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    data[stock] = df[features]
print("\nAll stock data loaded successfully!\n")

#%% function for making tabular response
def build_stats_table(data, stocks, features, stat_name, stat_func):
    title = f"{stat_name} Value comparison"
    table = PrettyTable()
    header = ['Name'] + [f"{f} ($)" if f != 'Volume' else 'Volume' for f in features]
    table.field_names = header

    stats_dict = {}
    for stock in stocks:
        vals = stat_func(data[stock][features])
        stats_dict[stock] = vals
        row = [stock] + [f"{v:.2f}" for v in vals]
        table.add_row(row)

    stats_df = pd.DataFrame(stats_dict, index=features).T

    max_vals = stats_df.max()
    min_vals = stats_df.min()
    max_companies = stats_df.idxmax()
    min_companies = stats_df.idxmin()

    table.add_row(['Maximum Value'] + [f"{v:.2f}" for v in max_vals])
    table.add_row(['Minimum Value'] + [f"{v:.2f}" for v in min_vals])
    table.add_row(['Maximum company name'] + list(max_companies))
    table.add_row(['Minimum company name'] + list(min_companies))

    table_str = table.get_string()
    table_width = len(table_str.split('\n')[0])
    print(title.center(table_width))
    print(table)
    print()
    return stats_df

#%% 2

print("\n Question 2:")
mean_df = build_stats_table(data, stocks, features, "Mean",
                            lambda df: df.mean())

#%% 3

print("\nQuestion 3:")
var_df = build_stats_table(data, stocks, features, "Variance",
                           lambda df: df.var())

#%% 4

print("\nQuestion 4:")
std_df = build_stats_table(data, stocks, features, "Standard Deviation",
                           lambda df: df.std())

#%% 5

print("\nQuestion 5:")
median_df = build_stats_table(data, stocks, features, "Median",
                              lambda df: df.median())

#%% 6
print("\nQuestion 6:")
def display_corr_matrix(stock_name, df):
    corr = df.corr()
    title = 'Correlation matrix for ' + stock_name

    table = PrettyTable()
    table.field_names = [''] + list(corr.columns)
    for idx in corr.index:
        row = [idx] + [f"{v:.2f}" for v in corr.loc[idx]]
        table.add_row(row)
    table_str = table.get_string()
    table_width = len(table_str.split('\n')[0])
    print(title.center(table_width))
    print(table)
    return corr


aapl_corr = display_corr_matrix('AAPL', data['AAPL'])

#%% 7
remaining_stocks = ['ORCL', 'TSLA', 'IBM', 'YELP', 'MSFT']
for id, stock in enumerate(remaining_stocks):
    print(f'Question 7({id + 1})')
    corr = display_corr_matrix(stock, data[stock])
    print()

#%% 8
print("\nQuestion 8:")
print("\nVolatility (Standard Deviation) Comparison - Adj Close:")
vol_table = PrettyTable()
vol_table.field_names = ['Company', 'Std Dev of Adj Close ($)', 'Risk Level']

adj_close_std = {}
for stock in stocks:
    std_val = data[stock]['Adj Close'].std()
    adj_close_std[stock] = std_val

sorted_stocks = sorted(adj_close_std.items(), key=lambda x: x[1])

for stock, std_val in sorted_stocks:
    if std_val == sorted_stocks[0][1]:
        risk = 'LOWEST (Safest)'
    elif std_val == sorted_stocks[-1][1]:
        risk = 'HIGHEST (Riskiest)'
    else:
        risk = 'Moderate'
    vol_table.add_row([stock, f"{std_val:.2f}", risk])

print(vol_table)

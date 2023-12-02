import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

# Fetch historical data for a stock
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data['Daily Move'] = stock_data['Close'].pct_change() * 100
    return stock_data

# Calculate average moves
def calculate_average_moves(data):
    avg_move_up = data[data['Daily Move'] > 0]['Daily Move'].mean()
    avg_move_down = data[data['Daily Move'] < 0]['Daily Move'].mean()
    return avg_move_up, avg_move_down

# Count occurrences in percentage bins
def count_occurrences(data, bins):
    categories = pd.cut(data['Daily Move'], bins, right=False)
    counts = categories.value_counts().sort_index()
    return counts

# Plot function for daily moves and occurrences
def plot_data(data, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Main function to run the analysis
def main():
    # User input for ticker and start date
    ticker = input("Enter the ticker symbol (e.g., 'TSLA'): ")
    start_date = input("Enter the starting date (format: 'YYYY-MM-DD'): ")
    end_date = datetime.now().strftime('%Y-%m-%d')
    
    # Fetch and analyze the stock data
    stock_data = fetch_stock_data(ticker, start_date, end_date)

    # Calculate average moves
    avg_move_up, avg_move_down = calculate_average_moves(stock_data)
    print(f"Average Move Up per Day: {avg_move_up:.2f}%")
    print(f"Average Move Down per Day: {avg_move_down:.2f}%")

    # Count occurrences in percentage bins
    bins = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    occurrences = count_occurrences(stock_data, bins)
    print("\nOccurrences per Day in Percentage Bins:")
    print(occurrences)

    # Plotting
    plot_data(occurrences, 'Occurrences in Percentage Bins', 'Percentage Bins', 'Number of Days')

if __name__ == "__main__":
    main()
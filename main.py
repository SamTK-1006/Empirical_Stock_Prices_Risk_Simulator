import Phase_1_Empirical_Time_Series
import Phase_2_Distribution
import Phase_3_Monte_Carlo
import Phase_3_Monte_Carlo_GBM
import yfinance as yf
import pandas as pd

def main():
    print("Empirical Time Series Analysis")
    choice = input("Would you like to use your own data or use live data? (own/live): ").strip().lower()
    data = None

    if choice == "own":
        file_path = input("Enter the path to your CSV file: ").strip()
        data = pd.read_csv(file_path)[["Date", "Close"]].dropna().head(756)

        # Converting Date to datetime and setting it as index
        data["Date"] = pd.to_datetime(data["Date"])
        data.set_index("Date", inplace=True)
    elif choice == "live": 
        ticker = input("Enter the ticker symbol (e.g., AAPL): ").strip()
        data = yf.download(ticker, period = "3y", interval = "1d")["Close"].dropna()
    else:
        print("Invalid choice. Please enter 'own' or 'live'.")

    if data is not None:
        while True:
            choice = input("What would you like to view? \n 1. Time Series Analysis\n 2. Distribution Analysis\n 3. Monte Carlo Simulations\n 4. Exit\nEnter your choice (1/2/3/4): ").strip().lower()
            if choice == "1" or choice == "time series analysis":
                Phase_1_Empirical_Time_Series.time_series(data) 

            elif choice == "2" or choice == "distribution analysis":
                ("Distribution Analysis")
                da = input("Choose distribution analysis type: \n 1. Normal Distribution Overlay\n 2. Q-Q Plot\nEnter your choice (1/2): ").strip().lower()
                if da == "1" or da == "normal distribution overlay":
                    Phase_2_Distribution.distribution_ticker(data)
                elif da == "2" or da == "q-q plot":
                    Phase_2_Distribution.generate_qq(data)
                    
            elif choice == "3" or choice == "monte carlo simulations":
                print("Monte Carlo Simulations")
                mc = input("Choose simulation type: \n 1. Geometric Brownian Motion (GBM)\n 2. Standard\n 3. Comparison of Models\nEnter your choice (1/2/3): ").strip().lower()
                if mc == "1" or mc == "gbm":
                    Phase_3_Monte_Carlo_GBM.Monte_Carlo_Simulations(data)
                elif mc == "2" or mc == "standard":
                    Phase_3_Monte_Carlo.Monte_Carlo_Simulations(data)
                elif mc == "3" or mc == "comparison of models":
                    print("Comparison of Models")
                    Phase_3_Monte_Carlo_GBM.Comparison_of_Models(data)
                    
            elif choice == "4" or choice == "exit":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":    
    main()

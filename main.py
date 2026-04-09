import Phase_1_Empirical_Time_Series
import Phase_2_Distribution
import Phase_3_Monte_Carlo
import yfinance as yf
import pandas as pd

def main():
    print("Empirical Time Series Analysis")
    choice = input("Would you like to use your own data or use live data? (own/live): ").strip().lower()
    
    if choice == "own":
        file_path = input("Enter the path to your CSV file: ").strip()
        data = pd.read_csv(file_path)[["Date", "Close"]].dropna().head(756)
        Phase_1_Empirical_Time_Series.use_own(data)
        
        temp = input("Type 'next' to proceed to distribution analysis: ").strip().lower()
        print("Distribution Analysis")
        Phase_2_Distribution.distribution_ticker(data)
        Phase_2_Distribution.generate_qq(data)
        
        temp = input("Type 'next' to proceed to Monte Carlo simulations: ").strip().lower()
        print("Monte Carlo Simulations")
        Phase_3_Monte_Carlo.Monte_Carlo_Simulations(data)

    elif choice == "live": 
        ticker = input("Enter the ticker symbol (e.g., AAPL): ").strip()
        data = yf.download(ticker, period = "3y", interval = "1d")["Close"].dropna()
        Phase_1_Empirical_Time_Series.use_yahoo(data)
        
        temp = input("Type 'next' to proceed to distribution analysis: ").strip().lower()
        print("Distribution Analysis")
        Phase_2_Distribution.distribution_ticker(data)
        Phase_2_Distribution.generate_qq(data)
        
        temp = input("Type 'next' to proceed to Monte Carlo simulations: ").strip().lower()
        print("Monte Carlo Simulations")
        Phase_3_Monte_Carlo.Monte_Carlo_Simulations(data)
    
if __name__ == "__main__":    
    main()

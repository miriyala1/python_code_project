import os
import smtplib
import yfinance as yf
import pandas as pd
import numpy as np

# Environment variables for sensitive data
# Set your keys and emails in the environment variables
OPENAI_API_KEY = os.getenv('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')
SEC_API_API_KEY = os.getenv('edd2540a66b00d4fa9a0c7f05077bda5a001e01283c6bcc4568ac05e0239ad6a')
SERPER_API_KEY = os.getenv('82d61422f23a5c4b0f961a56802d19b81e1b30bd')

# Email configuration

sender_email = os.getenv('miriyaladivya090906@gmail.com')  # Your email
rec_email = os.getenv('miriyaladivya4@gmail.com')         # Recipient's email
password = os.getenv('Divya09@')      # Email password

class StockAlertSystem:
    def __init__(self, symbol, target_price, target_volume, prediction_days):
        self.symbol = symbol
        self.target_price = target_price
        self.target_volume = target_volume
        self.prediction_days = prediction_days

    def fetch_stock_data(self):
        """Fetches stock data using yfinance."""
        data = yf.download(self.symbol, period='1mo', interval='1d')
        return data

    def analyze_market_conditions(self):
        """Analyzes market conditions for alerts."""
        data = self.fetch_stock_data()
        
        # Get the latest price and volume
        latest_price = data['Close'].iloc[-1]
        latest_volume = data['Volume'].iloc[-1]

        print(f"Latest price of {self.symbol}: {latest_price:.2f}")
        print(f"Latest volume of {self.symbol}: {latest_volume}")

        return latest_price, latest_volume

    def check_thresholds(self, latest_price, latest_volume):
        """Check if any thresholds are met for alerts."""
        alerts = []
        if latest_price >= self.target_price:
            alerts.append(f"Alert: {self.symbol} has reached the target price of {self.target_price:.2f}.")

        if latest_volume >= self.target_volume:
            alerts.append(f"Alert: {self.symbol} has exceeded the target volume of {self.target_volume}.")

        return alerts

    def send_email(self, message):
        """Sends an email with the given message."""
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, rec_email, message)
                print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    def make_predictions(self):
        """Predicts future price based on historical data."""
        # Placeholder for a prediction model; this can be improved with ML models
        historical_prices = self.fetch_stock_data()['Close']
        future_prediction = historical_prices.iloc[-1] * np.random.uniform(0.95, 1.05)  # Random prediction for example
        return future_prediction

    def run(self):
        """Main execution method."""
        latest_price, latest_volume = self.analyze_market_conditions()
        alerts = self.check_thresholds(latest_price, latest_volume)

        # Make a prediction
        future_prediction = self.make_predictions()
        alerts.append(f"Prediction: The future price of {self.symbol} is estimated to be {future_prediction:.2f}.")

        # Send alerts via email if any alerts exist
        if alerts:
            message = "\n".join(alerts)
            self.send_email(message)
        else:
            print("No alerts to send.")

# Example usage
if __name__ == "__main__":
    # Define your parameters
    stock_symbol = 'AAPL'          # Stock symbol
    target_sell_price = 150.00     # Example target price
    target_volume = 1000000        # Example target volume
    prediction_days = 7            # Days for prediction (not used in this placeholder)

    stock_alert_system = StockAlertSystem(stock_symbol, target_sell_price, target_volume, prediction_days)
    stock_alert_system.run()

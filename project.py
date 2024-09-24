import os
import pandas as pd
import yfinance as yf
import smtplib

# Load API keys from environment variables
OPENAI_API_KEY = os.getenv('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')
SEC_API_API_KEY = os.getenv('edd2540a66b00d4fa9a0c7f05077bda5a001e01283c6bcc4568ac05e0239ad6a')
SERPER_API_KEY = os.getenv('')

# Email configuration (use environment variables for security)
sender_email = os.getenv('miriyaladivya4@gmai.com')
rec_email = os.getenv('miriyaladivya090906@gmail.comL')
password = os.getenv('Divya09@')
target_sell_price = 100.00  # Set your target sell price

def fetch_stock_price(symbol):
    """Fetches the latest stock price for the given symbol."""
    data = yf.download(symbol=symbol, interval='1m', outputsize='full')
    close_data = data['Close']
    return close_data.iloc[0]  # Get the most recent close price

def send_email(message):
    """Sends an email with the given message."""
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, rec_email, message)
            print("Email was sent")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    symbol = 'AAPL'
    previous_price = fetch_stock_price(symbol)
    print(f"Previous price of {symbol}: {previous_price:.6f}")

    # Prepare the message
    message = f"Subject: STOCK ALERT!\n\nThe stock is at the price you stated: {previous_price:.6f}"

    # Check if the previous price exceeds the target sell price
    if previous_price > target_sell_price:
        send_email(message)
    else:
        print('Price does not exceed target sell price')

if __name__ == '_main_':
    main()
# app.py
import os
import sys
from buy import auto_buy  # Example: import a function from buy.py
# Add the Python2 directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Utils.helper import some_helper_function  # Example: import a helper function

def main():
    print("Starting the bot...")
    auto_buy()  # Example call to a function in buy.py
    some_helper_function()  # Example call to a helper function

if __name__ == "__main__":
    main()


import pandas as pd  # This will fail - pandas not in requirements.txt
import requests      # This will also fail

def main():
    print("Starting application...")
    df = pd.DataFrame({'A': [1, 2, 3]})
    response = requests.get('https://api.example.com')
    print(df)

if __name__ == "__main__":
    main()
import pandas as pd
import datetime
import time

df = pd.read_csv("C:/Users/atrke/Downloads/coffe_1.csv")
#create a function to grab Large iced Americano when time is between 7:00am and 9:00am from the data

# Define the function
def grab_large_iced_americano():
    # Get the current time
    now = datetime.datetime.now()

    # Check if the current time is between 7:00am and 9:00am
    if 7 <= now.hour <= 9:
        # Filter the data to get the large iced Americano
        large_iced_americano = df[(df['size'] == 'Large') & (df['condition'] == 'Iced') & (df['coffee'] == 'Americano')]
        return large_iced_americano
    else:
        return None

# Call the function
result = grab_large_iced_americano()
if result is not None:
    print(result.head(1))
else:
    print("It's not between 7:00am and 9:00am. Pick another menu!")

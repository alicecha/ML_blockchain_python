import pandas as pd
import os

def get_data():
    # Get list of all csv file names
    files = []
    for _,_, file in os.walk("."):
        for file_name in file:
            if file_name.endswith("csv"):
                files.append(file_name)

    # Merge all .csv into one dataframe
    df = None
    for file in files:
        if df is None:
            df = pd.read_csv(f"./data/{file}")
        else:
            temp_df = pd.read_csv(f"./data/{file}")
            df = pd.merge(df, temp_df)

    # Convert timestamp from unix to datetime
    # dev-note: to_datetime will not display time if 00:00:00
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    return(df)

if __name__ == "__main__":
    df = get_data()
    df.info()
    print(df)

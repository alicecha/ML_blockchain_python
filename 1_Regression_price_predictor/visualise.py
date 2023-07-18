from get_data import get_data
import matplotlib.pyplot as pyplot

# Plot timeseries for all features
def visualise(df):
    columns = list(df.columns[1:])
    # Define size of output
    fig = pyplot.figure(figsize=(20, 9))

    # Define nb columns and rows
    COLUMNS = 2
    ROWS = 4

    # Plot each feature against time
    for i in range(len(columns)):
        fig.add_subplot(ROWS, COLUMNS, i+1)
        pyplot.plot(df["timestamp"],
                    df[columns[i]])
        pyplot.title(f"{columns[i]}")

    # Add padding between charts
    fig.tight_layout(pad=2.0)

    # Display output   
    pyplot.show()

if __name__ == "__main__":
    visualise(get_data())
import matplotlib.pyplot as plt

def visualize_data(df):
    # Convert Spark DataFrame to Pandas DataFrame for visualization
    pandas_df = df.toPandas()

    # Simple plot example
    plt.figure(figsize=(10,6))
    plt.bar(pandas_df['group_column'], pandas_df['mean_value'])
    plt.xlabel('Group')
    plt.ylabel('Mean Value')
    plt.title('Mean Value by Group')
    
    # Save the plot as an image
    plt.savefig('images/plot1.png')
    
    # Show the plot
    plt.show()
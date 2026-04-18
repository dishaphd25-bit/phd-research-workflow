import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure results folder exists
os.makedirs('results', exist_ok=True)

# Step 14: Read the cleaned data
try:
    df = pd.read_csv('data/cleaned_data.csv')

    # Plot 1: Bar chart of scores
    plt.figure(figsize=(10,6))
    df.plot(kind='bar', x='student_id', y='experiment_score', color='skyblue')
    plt.title('Experiment Scores')
    plt.savefig('results/scores_plot.png')

    # Plot 2: Scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['temperature'], df['humidity'], color='red')
    plt.xlabel('Temperature')
    plt.ylabel('Humidity')
    plt.title('Temp vs Humidity')
    plt.savefig('results/temp_humidity_plot.png')

    print("Step 15: Success! Plots saved in results/ folder.")
except Exception as e:
    print(f"Error: {e}")
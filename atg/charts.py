"""Chart generation module for visualizing workout progress.

Creates matplotlib charts showing progress over time.
"""

import matplotlib.pyplot as plt

def generate_progress_chart(df, output_path):
  """Generate and save a progress chart showing max weight over time.

  Creates a line chart with one line per exercise, showing the maximum
  weight lifted on each date.

  Args:
      df (pd.DataFrame): Pivot table with dates as index and exercises as columns
      output_path (str): Path to save the PNG chart

  Returns:
      str: The output_path (for chaining/verification)
  """
  # Plot a line for each exercise
  for column in df.columns:
    plt.plot(df.index, df[column], label=column, marker='o')

  # Configure chart labels and legend
  plt.xlabel('Date')
  plt.ylabel('Max Weight (kg)')
  plt.title('Workout Progress Over Time')
  plt.legend()

  # Rotate x-axis labels for better readability
  plt.xticks(rotation=45)

  # Adjust layout to prevent label cutoff
  plt.tight_layout()

  # Save chart to file and clean up
  plt.savefig(output_path)
  plt.close()  # Close the figure to free memory

  return output_path

"""Chart generation module for visualizing workout progress.

Creates matplotlib charts showing progress over time.
"""

import pandas as pd
import matplotlib.pyplot as plt


def generate_progress_chart(df: pd.DataFrame, output_path: str) -> str:
  """Generate and save a progress chart showing max weight over time.

  Creates a line chart with one line per exercise, showing the maximum
  weight lifted on each date.

  Args:
      df (pd.DataFrame): Pivot table with dates as index and exercises as columns
      output_path (str): Path to save the PNG chart

  Returns:
      str: The output_path (for chaining/verification)
  """
  # Plot each exercise line chart using pandas plotting
  fig, ax = plt.subplots()
  df.plot(ax=ax, marker='o', linestyle='-', linewidth=1.5)

  # Configure chart labels and legend
  ax.set_xlabel('Date')
  ax.set_ylabel('Max Weight (kg)')
  ax.set_title('Workout Progress Over Time')
  ax.legend()
  ax.grid(True, linestyle='--', alpha=0.3)

  # Format x-axis dates and improve label placement
  fig.autofmt_xdate(rotation=45, ha='right')

  # Adjust layout to prevent label cutoff
  fig.tight_layout()

  # Save chart to file and clean up
  fig.savefig(output_path)
  plt.close(fig)

  return output_path

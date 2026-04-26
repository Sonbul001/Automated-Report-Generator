"""Data processing module for fitness analytics.

Calculates summary statistics, per-exercise metrics, and progress tracking.
"""

import pandas as pd

def get_summary(df):
  """Calculate overall fitness summary statistics.

  Args:
      df (pd.DataFrame): Processed workout dataframe

  Returns:
      dict: Summary containing total volume, sets, reps, sessions, and date range
  """
  # Work with a copy to avoid modifying original data
  df = df.copy()

  # Determine first and last workout dates
  first_session = df['date'].min()
  last_session = df['date'].max()

  # Calculate total days of training
  days_diff = (last_session - first_session).days

  return {
    'total_volume': df['volume'].sum(),      # Sum of all workout volumes
    'total_sets': df['sets'].sum(),          # Total sets performed
    'total_reps': df['reps'].sum(),          # Total repetitions
    'total_sessions': df['date'].nunique(),  # Number of unique workout dates
    'first_session': first_session,          # Earliest workout date
    'last_session': last_session,            # Latest workout date
    'date_range': days_diff                  # Days between first and last workout
  }

def get_exercise_stats(df):
  """Calculate statistics for each exercise.

  Args:
      df (pd.DataFrame): Processed workout dataframe

  Returns:
      pd.DataFrame: Per-exercise statistics including volume, max/avg weight
  """
  # Work with a copy to avoid modifying original data
  df = df.copy()

  # Group by exercise and aggregate key metrics
  result = df.groupby('exercise').agg(
    total_volume=('volume', 'sum'),          # Total volume per exercise
    max_weight=('weight_kg', 'max'),         # Heaviest weight lifted
    avg_weight=('weight_kg', 'mean'),        # Average weight per exercise
    total_sessions=('date', 'nunique')       # Number of times exercise was done
  ).reset_index()

  return result

def get_progress_overtime(df):
  """Track maximum weight over time for each exercise.

  Creates a pivot table with dates as rows and exercises as columns,
  showing the maximum weight lifted on each date for each exercise.

  Args:
      df (pd.DataFrame): Processed workout dataframe

  Returns:
      pd.DataFrame: Pivot table with dates as index, exercises as columns
  """
  return df.pivot_table(
    values='weight_kg',         # Values to display
    index='date',              # Rows: dates
    columns='exercise',        # Columns: exercise names
    aggfunc='max'             # Use maximum weight per date/exercise combination
  )
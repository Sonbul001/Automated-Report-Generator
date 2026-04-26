"""Data loading module for workout CSV files.

Handles loading, parsing, and initial data preparation.
"""

import pandas as pd

def load_data(file_path):
    """Load workout data from CSV and prepare it for analysis.

    Args:
        file_path (str): Path to the CSV file containing workout data

    Returns:
        pd.DataFrame: Processed dataframe with volume calculated, or None if error

    Expected columns: date, exercise, sets, reps, weight_kg
    """
    try:
        # Read CSV and parse date column as datetime
        data = pd.read_csv(file_path, parse_dates=['date'])

        # Sort by date for chronological analysis
        data = data.sort_values('date').reset_index(drop=True)

        # Calculate volume (sets × reps × weight) for each workout
        # Volume is a key metric for tracking total work done
        data['volume'] = data['sets'] * data['reps'] * data['weight_kg']

        return data
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None
"""Data loading module for workout data.

Handles loading, parsing, and initial data preparation from CSV
files or Google Sheets using a service account.
"""

import pandas as pd
import gspread

def load_csv_data(file_path):
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

def load_sheets_data(sheet_name: str):
    """Load workout data from a Google Sheets spreadsheet.

    Args:
        sheet_name (str): The title of the Google Sheets document.

    Returns:
        pd.DataFrame: Processed dataframe with volume calculated, or None if error
    """
    try:
        # Authenticate using a service account JSON credentials file.
        gc = gspread.service_account(filename='credentials.json')

        # Open the named Google Sheets document and read the first worksheet.
        sheet = gc.open(sheet_name)
        worksheet = sheet.sheet1
        records = worksheet.get_all_records()
        df = pd.DataFrame(records)

        # Convert the date column to datetime for sorting and time-series analysis.
        df['date'] = pd.to_datetime(df['date'])

        data = df.sort_values('date').reset_index(drop=True)

        # Compute the workout volume metric used throughout the report.
        data['volume'] = data['sets'] * data['reps'] * data['weight_kg']

        return data
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None
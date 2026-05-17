"""Automated Report Generator - Main Entry Point

This module orchestrates the complete workflow:
1. Load workout data from CSV
2. Calculate fitness statistics
3. Generate visualizations
4. Create PDF report with all results
"""

from atg import load_csv_data, load_sheets_data
from atg import get_summary, get_exercise_stats, get_progress_overtime
from atg import generate_progress_chart
from atg import generate_report
from datetime import datetime
import argparse


def main(use_sheets: bool = False) -> None:
  """Main execution function - generates complete fitness report.

  Set USE_SHEETS = True to load data from Google Sheets, or False to load
  from the local CSV file at `data/workouts.csv`.
  """
  try:
    if use_sheets:
      df = load_sheets_data('Fitness Report')
    else:
      df = load_csv_data('data/workouts.csv')
  except Exception as e:
    print(e)
    return

  # Calculate overall fitness summary (total volume, sessions, date range, etc.)
  summary = get_summary(df)

  # Calculate per-exercise statistics (max weight, average weight, etc.)
  stats = get_exercise_stats(df)

  # Prepare time-series data for progress visualization
  progress = get_progress_overtime(df)

  # Create timestamped output paths to avoid overwriting previous reports
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  output_path = f'output/{timestamp}'

  # Generate progress visualization chart
  chart = generate_progress_chart(progress, f'{output_path}_chart.png')

  # Generate final PDF report with summary, stats, and chart
  generate_report(summary, stats, chart, f'{output_path}_report.pdf')

  print(f"Report generated: output/{timestamp}_report.pdf")


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "--use-sheets",
    action="store_true",
  )
  args = parser.parse_args()
  main(use_sheets=args.use_sheets)
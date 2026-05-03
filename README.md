# Automated Report Generator

A Python application that analyzes workout data and generates comprehensive fitness progress reports with charts and statistics.

## Features

✨ **Data Processing**
- Load and parse workout data from CSV files or Google Sheets
- Calculate total volume (sets × weight × reps)
- Track sessions over time
- Group exercises by type

📊 **Analytics**
- Per-exercise statistics (total sets, average weight, average reps)
- Progress tracking over time with visualizations
- Session count and date range analysis
- Multi-dimensional data aggregation

📈 **Report Generation**
- Automatic PDF report creation with:
  - Fitness progress summary
  - Exercise statistics table
  - Progress charts
  - Date range and session information
  - Total volume calculations

## Project Structure

```
automated-report-generator/
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── data/
│   └── workouts.csv       # Sample workout data
├── output/                # Generated reports and charts
└── src/
    ├── loader.py          # Data loading utilities
    ├── processor.py       # Data processing and aggregations
    ├── charts.py          # Chart generation
    └── report.py          # PDF report generation
```

## Installation

1. **Clone or create the project:**
```bash
cd automated-report-generator
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Required packages:
- `pandas` - Data manipulation and analysis
- `matplotlib` - Chart visualization
- `reportlab` - PDF report generation
- `gspread` - Google Sheets API integration
- `google-auth` - Service account authentication for Sheets

## Usage

### Basic Usage

Run the main script to generate a complete report:

```bash
python main.py
```

This will:
1. Load workout data from `data/workouts.csv` or Google Sheets
2. Calculate fitness statistics
3. Generate a progress chart (PNG)
4. Create a comprehensive PDF report
5. Save both files to the `output/` directory with timestamps

### Google Sheets Integration

To load workout data from Google Sheets instead of CSV, place your service account credentials file as `credentials.json` in the project root and update `main.py`:

```python
USE_SHEETS = True
```

The default sheet name is `Fitness Report`, and the loader reads the first worksheet (`sheet1`).

The Google Sheets workflow requires:
- A valid `credentials.json` service account file
- The sheet shared with the service account email
- Column headers: `date`, `exercise`, `sets`, `reps`, `weight_kg`

### Expected Output

```
Report generated: output/20260426_153022_report.pdf
```

Files created:
- `output/20260426_153022_chart.png` - Progress visualization
- `output/20260426_153022_report.pdf` - Full fitness report

### Data Format

Your `data/workouts.csv` should have the following columns:

```csv
date,exercise,sets,reps,weight_kg
2024-01-01,Bench Press,3,8,100
2024-01-02,Squats,4,5,120
2024-01-03,Bench Press,4,6,105
```

If using Google Sheets, the sheet must expose the same column headers in the first row and the target sheet should be shared with your service account email.

**Required columns:**
- `date` - Workout date (YYYY-MM-DD format)
- `exercise` - Exercise name
- `sets` - Number of sets
- `reps` - Number of repetitions
- `weight_kg` - Weight used in kilograms

## Key Functions

### `src/loader.py`
- `load_csv_data(file_path)` - Load and prepare CSV workout data
- `load_sheets_data(sheet_name)` - Load and prepare workout data from Google Sheets

### `src/processor.py`
- `get_summary(df)` - Calculate overall fitness summary
- `get_exercise_stats(df)` - Get statistics per exercise
- `get_progress_overtime(df)` - Track progress by date

### `src/charts.py`
- `generate_progress_chart(progress, output_path)` - Create visualization

### `src/report.py`
- `generate_report(summary, stats, chart, output_path)` - Generate PDF report

## Report Contents

The generated PDF includes:

1. **Title & Summary**
   - Date range of workouts
   - Total sessions completed
   - Total volume lifted

2. **Exercise Statistics Table**
   - Exercise names
   - Total sets per exercise
   - Average weight used
   - Average reps
   - Calculated volume

3. **Progress Chart**
   - Visual representation of workout progress over time

## Troubleshooting

**Issue: ModuleNotFoundError**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python environment is activated

**Issue: File not found**
- Check that `data/workouts.csv` exists
- Ensure `output/` directory exists

**Issue: PDF not generated**
- Verify `reportlab` is installed
- Check file permissions in output directory

---

**Created:** April 2026
**Status:** Active Development

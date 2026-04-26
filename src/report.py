"""PDF report generation module.

Creates professional PDF reports combining fitness summary, statistics, and charts.
"""

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors

def generate_report(summary, stats, chart, output_path):
  """Generate a comprehensive PDF fitness report.

  Creates a multi-page PDF containing:
  - Fitness summary (date range, sessions, total volume)
  - Exercise statistics table
  - Progress visualization chart

  Args:
      summary (dict): Overall fitness summary from get_summary()
      stats (pd.DataFrame): Per-exercise statistics from get_exercise_stats()
      chart (str): Path to the progress chart image
      output_path (str): Path where PDF will be saved
  """
  # Create PDF document
  doc = SimpleDocTemplate(output_path)

  # Get default document styles
  styles = getSampleStyleSheet()

  # Build document elements in order
  elements = []

  # Add title and summary section
  elements.append(Paragraph('Fitness Progress Report', styles['Title']))
  elements.append(Paragraph(
    f"Date Range: {summary['first_session'].date()} → {summary['last_session'].date()}",
    styles['Normal']
  ))
  elements.append(Paragraph(f"Sessions: {summary['total_sessions']}", styles['Normal']))
  elements.append(Paragraph(
    f"Total Volume: {summary['total_volume']:,.0f} kg",
    styles['Normal']
  ))

  # Add spacing between sections
  elements.append(Spacer(1, 0.3 * inch))

  # Add exercise statistics table
  elements.append(Paragraph('Exercise Statistics', styles['Heading1']))

  # Convert dataframe to table format
  headers = list(stats.columns)
  rows = stats.values.tolist()
  data = [headers] + rows

  # Create and style the table
  table = Table(data)
  table.setStyle(TableStyle([
    # Style header row with grey background and white text
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    # Add gridlines to all cells
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
  ]))
  elements.append(table)

  # Add spacing before chart
  elements.append(Spacer(1, 0.3 * inch))

  # Add progress chart
  elements.append(Paragraph('Progress Over Time', styles['Heading1']))
  elements.append(Image(chart, width=4*inch, height=3*inch))

  # Build and write the PDF document
  doc.build(elements)

import click
import csv
from openpyxl import Workbook, load_workbook

header = []
final_data = []
def save_file(file):
    # No need to open the file; it's already available as an InMemoryUploadedFile
    # Process the file directly
    file_content = file.read().decode('utf-8')
    print("File Content:")
    print(file_content)
    return click.echo(f"Data loaded.")

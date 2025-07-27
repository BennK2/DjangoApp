import pandas as pd

# Load the Excel file
excel_file = "Final_WFC_stockPrices.xlsx"  # Replace with your actual file name
xls = pd.ExcelFile(excel_file)

# List to store data frames
data_frames = []

# Loop through sheets and append them with an identifier
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    df["Sheet_Name"] = sheet_name  # Add a column to identify the sheet
    data_frames.append(df)

# Concatenate all data frames into one
merged_df = pd.concat(data_frames, ignore_index=True)

# Save to CSV
csv_file = "Final_WFC_stockPrices.csv"  # Desired output CSV file name
merged_df.to_csv(csv_file, index=False)

print(f"CSV file '{csv_file}' created successfully.")
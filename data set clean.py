import pandas as pd

# Load the dataset from the provided file path
file_path = r'C:\Users\eesho\Downloads\Tata Visualization\Online Retail Data Set.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows to understand the data structure
print(data.head())

# Step 1: Filter out invalid quantities (quantity should be >= 1)
data_cleaned = data[data['Quantity'] >= 1]

# Step 2: Filter out invalid unit prices (unit price should be >= 0)
data_cleaned = data_cleaned[data_cleaned['UnitPrice'] >= 0]

# Step 3: (Optional) You can reset the index if needed after cleanup
data_cleaned = data_cleaned.reset_index(drop=True)

# Display the cleaned data
print(data_cleaned.head())

# Save the cleaned data to a new Excel file
output_path = r'C:\Users\eesho\Downloads\Tata Visualization\Cleaned_Online_Retail_Data_Set.xlsx'
data_cleaned.to_excel(output_path, index=False)

print(f"Cleaned data saved to {output_path}")

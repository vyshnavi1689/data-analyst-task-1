# Import necessary libraries
import pandas as pd

# Step 1: Load the Dataset
try:
    df = pd.read_csv(r"C:\Users\vyshu\OneDrive\Documents\data analyst\archive (1)\marketing_campaign.csv")
    print("Original Dataset:")
    print(df.head())
except FileNotFoundError:
    print("❌ Error: 'marketing_campaign.csv' not found. Please check the path.")
    exit()

# Track initial stats
initial_shape = df.shape
nulls_before = df.isnull().sum().sum()
duplicates_before = df.duplicated().sum()

# Step 2: Handle Missing Values
df.ffill(inplace=True)
nulls_after = df.isnull().sum().sum()
nulls_filled = nulls_before - nulls_after

# Step 3: Remove Duplicate Rows
df.drop_duplicates(inplace=True)
duplicates_removed = duplicates_before

# Step 4: Standardize Text Values (example: gender, country names)
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].astype(str).str.lower().str.strip()

# Step 5: Convert Date Formats (example: 'Date')
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%d-%m-%Y')

# Step 6: Rename Column Headers
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Step 7: Check and Fix Data Types (example: age)
if 'age' in df.columns:
    # Only convert non-null values to int, or handle gracefully
    df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(0).astype(int)

# Step 8: Save Cleaned Dataset
df.to_csv('cleaned_netflix.csv', index=False)

# Step 9: Final Summary
final_shape = df.shape

print("\n✅ Cleaned Dataset Preview:")
print(df.head())

print("\n📊 Summary of Changes:")
print(f"- Original shape: {initial_shape}")
print(f"- Final shape: {final_shape}")
print(f"- Missing values filled: {nulls_filled}")
print(f"- Duplicate rows removed: {duplicates_removed}")
print(f"- Column names standardized (lowercase, no spaces)")
if 'Gender' in df.columns:
    print(f"- 'Gender' column standardized (lowercased & stripped)")
if 'Date' in df.columns:
    print(f"- 'Date' column converted to datetime format")
if 'age' in df.columns:
    print(f"- 'age' column converted to integer type")

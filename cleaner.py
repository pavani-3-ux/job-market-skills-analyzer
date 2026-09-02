import pandas as pd

# Read raw data
df = pd.read_csv("data/raw_jobs.csv")

print("Original number of jobs:", len(df))

# Remove duplicate jobs
df = df.drop_duplicates()

# Remove rows where title is missing
df = df.dropna(subset=["title"])

# Clean text columns
text_columns = ["title", "company", "location", "description", "category"]

for column in text_columns:
    if column in df.columns:
        df[column] = df[column].fillna("").str.strip()

# Convert salary columns to numeric
df["salary_min"] = pd.to_numeric(df["salary_min"], errors="coerce")
df["salary_max"] = pd.to_numeric(df["salary_max"], errors="coerce")

# Convert created date to datetime
df["created"] = pd.to_datetime(df["created"], errors="coerce", utc=True)

# Remove timezone because Excel does not support timezone-aware datetimes
df["created"] = df["created"].dt.tz_localize(None)

# Create average salary column
df["average_salary"] = (df["salary_min"] + df["salary_max"]) / 2

# Save cleaned data as CSV
df.to_csv("data/cleaned_jobs.csv", index=False)

# Save cleaned data as Excel
df.to_excel("data/cleaned_jobs.xlsx", index=False)

print("Cleaned number of jobs:", len(df))
print("CSV saved: data/cleaned_jobs.csv")
print("Excel saved: data/cleaned_jobs.xlsx")
print("Data cleaning completed successfully!")
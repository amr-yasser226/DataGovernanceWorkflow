import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r"C:\ZC\Data Governance\DataGovernanceWorkflow\data\ssh_logs_processed.csv"
df = pd.read_csv(file_path)

dataset_description = (
    "Dataset Description:\n"
    "This dataset contains SSH log data. Each record typically includes:\n"
    "- Date and Time when the log was recorded\n"
    "- IP address and Port used during the SSH connection attempt\n"
    "- Username and Password fields attempted\n"
    "- Country and City indicating the geographic origin\n"
    "It can be used to analyze security events and detect potential anomalies.\n"
)
print(dataset_description)

def profile_numeric(column_data: pd.Series) -> str:
    """Compute statistics for numeric columns."""
    min_val = column_data.min()
    max_val = column_data.max()
    mean_val = column_data.mean()
    # Sometimes mode returns multiple values; we'll choose the first one.
    mode_val = column_data.mode().iloc[0] if not column_data.mode().empty else np.nan
    data_type = str(column_data.dtype)
    null_count = column_data.isnull().sum()

    return (
        f"Min: {min_val}, Max: {max_val}, Mean: {mean_val:.2f}, "
        f"Mode: {mode_val}, Data type: {data_type}, Nulls: {null_count}"
    )

def profile_datetime(column_data: pd.Series) -> str:
    """Profile for datetime columns: earliest date, latest date, data type, and null count."""
    column_data = pd.to_datetime(column_data, errors='coerce')
    min_val = column_data.min()
    max_val = column_data.max()
    data_type = str(column_data.dtype)
    null_count = column_data.isnull().sum()
    return (
        f"Earliest: {min_val}, Latest: {max_val}, Data type: {data_type}, Nulls: {null_count}"
    )

def profile_categorical(column_data: pd.Series) -> str:
    """Profile for categorical/text columns: unique values list (or count), data type, and null count."""
    data_type = str(column_data.dtype)
    null_count = column_data.isnull().sum()
    unique_vals = column_data.dropna().unique()
    unique_sample = list(unique_vals[:5])
    return (
        f"Unique (sample): {unique_sample}, Data type: {data_type}, Nulls: {null_count}"
    )

rows = []
for col in df.columns:
    if col.lower() in ['port']:
        profiling_info = profile_numeric(df[col])
    elif col.lower() in ['date']:
        profiling_info = profile_datetime(df[col])
    else:
        profiling_info = profile_categorical(df[col])
    
    dependencies = "Manual analysis required"
    
    notes = ""
    if col.lower() == "date":
        notes = "May correlate with Time to show trends."
    elif col.lower() == "time":
        notes = "Check for peaks in activity based on time of day."
    elif col.lower() == "ip":
        notes = "Useful for geolocation and threat detection."
    elif col.lower() == "port":
        notes = "Identify commonly targeted ports (e.g., SSH on port 22)."
    elif col.lower() == "username":
        notes = "Analyze repeated login attempts for specific usernames."
    elif col.lower() == "password":
        notes = "Look for patterns in attempted passwords."
    elif col.lower() == "country":
        notes = "Can indicate regional trends."
    elif col.lower() == "city":
        notes = "Further granularity for geographic analysis."
    
    rows.append({
        "Column Name": col,
        "Profiling Info": profiling_info,
        "Dependencies": dependencies,
        "Notes": notes
    })
result_df = pd.DataFrame(rows)
styled_df = result_df.style.set_properties(**{
    'white-space': 'pre-wrap',
    'text-align': 'left'
}).set_table_styles([
    {'selector': 'th', 'props': [('text-align', 'left')]}
]).hide(axis='index')
styled_df = styled_df.apply(lambda x: ['background-color: #f9f9f9' if x.name % 2 == 0 else '' for _ in x], axis=1)
print(styled_df)

df['Datetime'] = pd.to_datetime(df['Date'] + " " + df['Time'], errors='coerce')

if df['Datetime'].isnull().sum() > 0:
    print("Warning: Some Date/Time conversions failed. Please verify the format in your CSV.")
df['Hour'] = df['Datetime'].dt.hour
hourly_counts = df.groupby('Hour').size().sort_index()
print("\nLogin attempts by hour:")
print(hourly_counts)

plt.figure(figsize=(10, 5))
hourly_counts.plot(kind='bar', color='skyblue')
plt.title("Login Attempts by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Login Attempts")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

country_counts = df['Country'].value_counts()
print("\nLogin attempts by Country:")
print(country_counts)

top_countries = country_counts.sort_values(ascending=False).head(15)
others_sum = country_counts.sum() - top_countries.sum()
country_counts_grouped = top_countries.copy()
if others_sum > 0:
    country_counts_grouped['Others'] = others_sum
plt.figure(figsize=(10, 5))
country_counts_grouped.plot(kind='bar', color='lightgreen')
plt.title("Login Attempts by Country")
plt.xlabel("Country")
plt.ylabel("Number of Login Attempts")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

city_counts = df.groupby(['Country', 'City']).size().reset_index(name='Count')
print("\nLogin attempts by Country and City:")
print(city_counts.sort_values(by='Count', ascending=False))
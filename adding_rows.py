import pandas as pd
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def load_password_list(filepath):
    """
    Load common passwords from the rockyou.txt file.
    Each password should be on a separate line.
    """
    with open(filepath, "r", encoding="utf8", errors="ignore") as file:
        passwords = file.read().splitlines()
    return passwords
rockyou_filepath = r"C:\ZC\Data Governance\DataGovernanceWorkflow\data\rockyou.txt"
common_passwords = load_password_list(rockyou_filepath)

def random_ip():
    """Generate a random IPv4 address."""
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_port():
    """Generate a random port number in a typical range (1 - 65535)."""
    return random.randint(1, 65535)

def random_username():
    """Generate a random username from a predefined pool."""
    user_pool = ["root", "admin", "test", "user", "guest"]
    return random.choice(user_pool)

def random_password():
    """Select a random password from the RockYou password list."""
    return random.choice(common_passwords)

def random_country_city():
    """Pick a random country-city pair from a predefined set."""
    locations = [
        ("United States", "Seattle"),
        ("United States", "Los Angeles"),
        ("Indonesia", "Jakarta"),
        ("Australia", "Sydney"),
        ("United Kingdom", "London"),
        ("Germany", "Berlin"),
        ("Brazil", "São Paulo")
    ]
    return random.choice(locations)

def random_datetime(base_date):
    """Generate a random datetime offset from a base date."""
    delta_days = random.randint(-30, 30)
    random_time = base_date + timedelta(days=delta_days,
                                        hours=random.randint(0, 23),
                                        minutes=random.randint(0, 59),
                                        seconds=random.randint(0, 59))
    return random_time
original_csv_path = r"C:\ZC\Data Governance\DataGovernanceWorkflow\data\ssh_logs_processed(1).csv"
df_original = pd.read_csv(original_csv_path)
num_new_rows = 25000

new_rows = []
base_date = datetime(2024, 8, 16, 10, 0, 0)

for _ in range(num_new_rows):
    dt = random_datetime(base_date)
    date_str = dt.strftime("%m/%d/%Y")
    time_str = dt.strftime("%H:%M:%S")
    ip_str = random_ip()
    port_val = random_port()
    user_str = random_username()
    pass_str = random_password()
    country, city = random_country_city()

    new_rows.append({
        "Date": date_str,
        "Time": time_str,
        "IP": ip_str,
        "Port": port_val,
        "Username": user_str,
        "Password": pass_str,
        "Country": country,
        "City": city
    })
df_synthetic = pd.DataFrame(new_rows)
df_final = pd.concat([df_original, df_synthetic], ignore_index=True)
output_csv_path = r"C:\ZC\Data Governance\DataGovernanceWorkflow\data\ssh_logs_processed.csv"
df_final.to_csv(output_csv_path, index=False)

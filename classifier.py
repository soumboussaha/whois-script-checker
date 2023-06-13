import pandas as pd
import whois
from retrying import retry

# Read the CSV file containing the list of domains
input_file = "document.csv"
df = pd.read_csv(input_file)
print("File Read")

# Function to retrieve the owner name for a domain with retry mechanism
@retry(stop_max_attempt_number=3, wait_fixed=2000)
def get_owner_name(domain):
    try:
        print(domain)

        result = whois.whois(domain)
        print(domain + ' -> ' + str(result))
        return result
    except:
   
        return None

# Apply the get_owner_name function to each domain in the DataFrame
print("Get Owner Name")

df['Owner'] = df['URL'].apply(get_owner_name)

# Save the updated DataFrame to a new CSV file
output_file = "domains_with_owners.csv"
df.to_csv(output_file, index=False)

print("CSV file saved with domain owners.")

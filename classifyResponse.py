import pandas as pd
import json

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('domains_with_owners.csv')

# Create the third column and initialize it with empty strings
df['Value'] = ''




# Read the CSV file containing valid org values
valid_org_values_df = pd.read_csv('valid_org_values.csv')

# Extract the org values from the DataFrame
valid_org_values = valid_org_values_df['Value'].tolist()

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    whois_response = str(row['Owner'])  # Convert to string
    domain = row['URL']
    print("domain -> " + domain)
    try:
        # Parse the JSON response
        response_data = json.loads(whois_response)

        # Check if 'org' exists and has a non-empty value
        if 'org' in response_data and response_data['org']:
            org_value = response_data['org']
            if org_value in valid_org_values:
                df.at[index, 'Value'] = domain
                print("output -> " + domain)
            else:
                df.at[index, 'Value'] = org_value
                print("output -> " + org_value)
        else:
            df.at[index, 'Value'] = domain
            print("output -> " + domain)

    except (json.JSONDecodeError, TypeError):
        df.at[index, 'Value'] = domain
        print("output -> " + domain)

# Save output DataFrame
df.to_csv('output_clustering.csv', index=False)





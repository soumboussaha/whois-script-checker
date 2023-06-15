import pandas as pd
import json

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('domains_with_owners.csv')

# Create the third column and initialize it with empty strings
df['Value'] = ''

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    whois_response = str(row['Owner'])  # Convert to string
    domain = row['URL']
    print("domain -> "+domain)
    try:
        # Parse the JSON response
        response_data = json.loads(whois_response)

        # Check if 'org' exists and has a non-empty value
        if 'org' in response_data and response_data['org']:
            org_value = response_data['org']
            if org_value != 'REDACTED FOR PRIVACY':
                df.at[index, 'Value'] = org_value
                print("output-> "+org_value)

        # If 'org' doesn't exist or has an empty value, check if 'registrant' exists and has a non-empty value
        elif 'registrant' in response_data and response_data['registrant']:
            registrant_value = response_data['registrant']
            if registrant_value != 'REDACTED FOR PRIVACY':
                df.at[index, 'Value'] = registrant_value
                print("output-> "+registrant_value)
            # If neither 'org' nor 'registrant' exists or have empty/null/'REDACTED' values, populate with the domain
        else:
            df.at[index, 'Value'] = domain
            print("output-> "+domain)

    except (json.JSONDecodeError, TypeError):
        df.at[index, 'Value'] = domain
        print("output-> "+domain)

# save output DataFrame
df.to_csv('output_clustering.csv', index=False)




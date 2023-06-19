import pandas as pd
import json

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('domains_with_owners.csv')

# Create the third column and initialize it with empty strings
df['Value'] = ''

# Specify the valid org values
valid_org_values = [
    "Privacy service provided by Withheld for Privacy ehf",
    "Contact Privacy Inc. Customer 0130027497",
    "Contact Privacy Inc. Customer 0141730466",
    "Contact Privacy Inc. Customer 7151571251",
    "Jewella Privacy LLC Privacy ID# 10439376",
    "Whois Privacy (enumDNS dba)",
    "Digital Privacy Corporation",
    "Contact Privacy Inc. Customer 0165685487",
    "Contact Privacy Inc. Customer 0165632015",
    "privacymanager.io",
    "Domains By Proxy, LLC",
    "NameBrightPrivacy.com",
    "Whois Privacy Protection Service by onamae.com",
    "Redacted for Privacy Purposes",
    "Domain Privacy Service FBO Registrant.",
    "Contact Privacy Inc. Customer 0147711685",
    "Jewella Privacy LLC Privacy ID# 12406208",
    "Contact Privacy Inc. Customer 0164203610",
    "GLOBAL DOMAIN PRIVACY SERVICES INC",
    "Whois Privacy - Com Laude",
    "Super Privacy Service LTD c/o Dynadot",
    "Contact Privacy Inc. Customer 0165685485",
    "Contact Privacy Inc. Customer 0159414542",
    "See PrivacyGuardian.org",
    "DOMAIN PRIVACY SERVICE FBO REGISTRANT",
    "MyPrivacy.net Ltd.",
    "Data Protect",
    "REDACTED FOR PRIVACY"
]

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





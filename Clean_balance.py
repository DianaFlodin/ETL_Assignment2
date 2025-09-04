import pandas as pd
import re

df = pd.read_csv(
    "C:\\Users\\Diana\\Downloads\\Raw_Loan_Balance.csv",
    sep=';',
    engine='python',
    on_bad_lines='skip',
    quoting=3
)

print("Kolonner funnet:", df.columns.tolist())

if 'ChannelID' in df.columns:
    df['ChannelID'] = df['ChannelID'].astype(str).str.replace(r'\D', '', regex=True)
    df['ChannelID'] = df['ChannelID'].replace({'nan': '', 'NULL': ''})
else:
    print("Advarsel: 'ChannelID' finnes ikke i dataene!")

for col in ['MaturityDate', 'CalculatedMaturityDate']:
    if col in df.columns:
        df[col] = df[col].replace({'NULL': '', 'nan': ''})
        df[col] = df[col].replace('', pd.NA)
    else:
        print(f"Advarsel: '{col}' finnes ikke i dataene!")

if 'Balance' in df.columns:
    df['Balance'] = df['Balance'].astype(str).str.replace(',', '.', regex=False)
    df['Balance'] = df['Balance'].str.replace(r'[^0-9\.]', '', regex=True)
    df['Balance'] = df['Balance'].replace({'NULL': '', 'nan': ''})
else:
    print("Advarsel: 'Balance' finnes ikke i dataene!")

df = df.astype(str).apply(lambda col: col.str.replace(',', '.', regex=False))
df = df.replace({'Yes': 1, 'No': 0, 'NULL': '', 'nan': ''})

if 'LoanAccountId' in df.columns:
    df = df.drop_duplicates(subset=['LoanAccountId'], keep='first')

if 'PrecedingId' in df.columns:
    df['PrecedingId'] = df['PrecedingId'].replace({'': '0', 'NULL': '0', 'nan': '0'})
    df['PrecedingId'] = df['PrecedingId'].astype(str).str.replace(r'\D', '', regex=True)
    df['PrecedingId'] = df['PrecedingId'].replace('', '0')

df.to_csv("C:\\Users\\Diana\\Visualstudio\\VSC\\Raw_Loan_Balance_clean.csv", index=False, sep=';')
import pandas as pd

df = pd.read_csv(
    "C:\\Users\\Diana\\Downloads\\Raw_Loan_Transaction.csv",
    sep=';',
    engine='python',
    on_bad_lines='skip',
    quoting=3
)

print("Kolonner funnet:", df.columns.tolist())

if 'IsDirectDebit' in df.columns:
    df['IsDirectDebit'] = df['IsDirectDebit'].replace({'Yes': 1, 'No': 0, 'NULL': 0, '': 0, 'nan': 0})

if 'PrecedingId' in df.columns:
    df['PrecedingId'] = df['PrecedingId'].replace({'': '0', 'NULL': '0', 'nan': '0'})
    df['PrecedingId'] = df['PrecedingId'].astype(str).str.replace(r'\D', '', regex=True)
    df['PrecedingId'] = df['PrecedingId'].replace('', '0')

if 'Amount' in df.columns:
    df['Amount'] = df['Amount'].astype(str).str.replace(',', '.', regex=False)
    df['Amount'] = df['Amount'].str.replace(r'[^0-9\.]', '', regex=True)
    df['Amount'] = df['Amount'].replace({'NULL': '0', 'nan': '0', '': '0'})

df = df.astype(str).apply(lambda col: col.str.replace(',', '.', regex=False))
df = df.replace({'Yes': 1, 'No': 0, 'NULL': '', 'nan': ''})

if 'LoanTransactionId' in df.columns:
    df = df.drop_duplicates(subset=['LoanTransactionId'], keep='first')

df.to_csv("C:\\Users\\Diana\\Visualstudio\\VSC\\Raw_Loan_Transaction_clean.csv", index=False, sep=';')
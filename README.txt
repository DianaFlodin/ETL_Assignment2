# Låneportfölj – Datapipeline Proof of Concept

## Om projektet
Detta projekt är ett Proof of Concept (POC) för en bank, där målet är att bygga en end-to-end datapipeline för låneportföljen och skapa en interaktiv dashboard i Excel (eller Power BI).

## Dataflöde
1. **Rådata**  
   - Raw_Loan_Account.csv  
   - Raw_Loan_Balance.csv  
   - Raw_Loan_Transaction.csv

2. **Datarening**  
   - Python-script (`Clean_data.py`, `Clean_balance.py`, `Clean_transaction.py`) renar alla rådatafiler:
     - Tar bort dubbletter
     - Konverterar decimaler (komma till punkt)
     - Tar bort/ersätter NULL och tomma värden
     - Konverterar "Yes"/"No" till 1/0
     - Säkerställer att alla numeriska kolumner endast innehåller giltiga tal

3. **Import till SQL**  
   - Rensade CSV-filer importeras till SQL Server via SSIS.

4. **Analytiskt lager**  
   - Faktatabeller och dimensionstabeller byggs i SQL (se egna SQL-script).
   - Exempel: Dim_LoanAccount, Fact_LoanBalance, Fact_LoanTransaction

5. **Dashboard**  
   - Data modelleras och visualiseras i Excel (eller Power BI).
   - Dashboarden visar dynamiskt:
     - Lånekonto
     - Lånetransaktion
     - Transaktionsbelopp
     - Lånesaldo

## Filstruktur
```
LoanPortfolioPOC/
│
├── Clean_data.py
├── Clean_balance.py
├── Clean_transaction.py
├── Raw_Loan_Account_clean.csv
├── Raw_Loan_Balance_clean.csv
├── Raw_Loan_Transaction_clean.csv
├── SQL/
│   └── analytical_layer.sql
├── Dashboard.xlsx
└── README.md
```

## Så här kör du pipeline
1. **Rena data**  
   Kör Python-scriptet för varje rådatafil:
   ```
   python Clean_data.py
   python Clean_balance.py
   python Clean_transaction.py
   ```
2. **Importera till SQL**  
   Använd SSIS för att ladda in de rensade CSV-filerna till SQL Server.

3. **Bygg analytiskt lager**  
   Kör SQL-scriptet för att skapa faktatabeller och dimensionstabeller.

4. **Öppna dashboard**  
   Öppna `Dashboard.xlsx` (eller Power BI-fil) för att se visualiseringarna.

## Förutsättningar
- Python 3.x med pandas installerat
- SQL Server och SSIS
- Excel eller Power BI

## Kontakt
Frågor? Kontakta [din e-postadress eller namn].

from connect import connect
import pandas as pd

# Function that runs SQL query to find all members with overdrawn checking accounts and prints the results
def overdrawn_checking():
    # Connect to db and run query from specified SQL file
    conn = connect()
    with open('./sql/checking_over.sql', 'r') as file:
        query = file.read()
    df = pd.read_sql(query, conn)

    # Create a new column combining first and last name
    df['full_name'] = df['first_name'] + ' ' + df['last_name']

    # Drop the first and last name columns and reorder so that the full_name column is before the current_balance column
    overdrawn = (df.query('current_balance < 0')).drop(columns=['first_name', 'last_name', 'overdrawn'])
    overdrawn = overdrawn.loc[:, ['full_name', 'current_balance']]
    print(f'\nList of members with overdrawn checking accounts: \n{overdrawn}\n')

# Function that runs SQL query to find all members with overpaid loans and prints the results
def overpaid_loans():
    # TODO: This block can be moved to a util probably (connect, run sql, return a df. Something along these lines)
    conn = connect()
    with open('./sql/loan_over.sql', 'r') as file:
        query = file.read()
    df = pd.read_sql(query, conn)

    # Create a new column that has the members full name, looks better when printing results
    df['full_name'] = df['first_name'] + ' ' + df['last_name']

    # Drop the first and last name columns and reorder so that the full_name columns is before the current_debt column
    overpaid = (df.query('current_debt < 0')).drop(columns=['first_name', 'last_name']).loc[:, ['full_name', 'current_debt']]
    print(f'\nList of members with overpaid loans: \n{overpaid}\n')

# Function that runs multiple SQL queries to calculate the total assets and prints the result
def asset_total():
    # Connect to the db and run queries to get the totals for current checking account balances and current loan amounts (current meaning we account for the transactions)
    conn = connect()
    with open('./sql/checking_totals.sql', 'r') as file:
        checking_query = file.read()
    with open('./sql/loan_totals.sql', 'r') as file:
        loan_query = file.read()
    
    checking_df = pd.read_sql(checking_query, conn)
    loan_df = pd.read_sql(loan_query, conn)

    # Get a sum of the current_balance and current_loans column to get the sum of assets, then round to the second decimal point
    total_assets = round(checking_df['current_balance'].sum() - loan_df['current_loans'].sum(), 2)
    print(f'\nSum total asset size: {total_assets}\n')
    

if __name__ == '__main__':
    overdrawn_checking()
    overpaid_loans()
    asset_total()
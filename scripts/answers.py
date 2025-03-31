from connect import connect
import pandas as pd

def overdrawn_checking():
    conn = connect()

    with open('./sql/checking_over.sql', 'r') as file:
        query = file.read()

    df = pd.read_sql(query, conn)
    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    overdrawn = (df.query('current_balance < 0')).drop(columns=['first_name', 'last_name', 'overdrawn'])
    overdrawn = overdrawn.loc[:, ['full_name', 'current_balance']]
    print(f'\nList of members with overdrawn checking accounts: \n{overdrawn}\n')

def overpaid_loans():
    # This block can be moved to a util probably, connect, run sql, return a df
    conn = connect()
    with open('./sql/loan_over.sql', 'r') as file:
        query = file.read()

    df = pd.read_sql(query, conn)
    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    overpaid = (df.query('current_debt < 0')).drop(columns=['first_name', 'last_name']).loc[:, ['full_name', 'current_debt']]
    print(f'\nList of members with overpaid loans: \n{overpaid}\n')

def asset_total():
    conn = connect()
    with open('./sql/checking_totals.sql', 'r') as file:
        checking_query = file.read()
    with open('./sql/loan_totals.sql', 'r') as file:
        loan_query = file.read()
    
    checking_df = pd.read_sql(checking_query, conn)
    loan_df = pd.read_sql(loan_query, conn)

    total_assets = round(checking_df['current_balance'].sum() - loan_df['current_loans'].sum(), 2)
    print(f'\nSum total asset size: {total_assets}\n')
    

if __name__ == '__main__':
    overdrawn_checking()
    overpaid_loans()
    asset_total()
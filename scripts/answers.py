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
    print(f'\nList of members with overdrawn checking accounts: \n{overdrawn}')

def overpaid_loans():
    # This block can be moved to a util probably, connect, run sql, return a df
    conn = connect()
    with open('./sql/loan_over.sql', 'r') as file:
        query = file.read()

    df = pd.read_sql(query, conn)
    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    overpaid = (df.query('current_debt < 0')).drop(columns=['first_name', 'last_name']).loc[:, ['full_name', 'current_debt']]
    print(f'\nList of members with overpaid loans: \n{overpaid}')

if __name__ == '__main__':
    overdrawn_checking()
    overpaid_loans()
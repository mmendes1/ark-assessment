## Arkartechture Engineering Assignment
Description: Repository for any relevant code pertaining to the Arkatechture Engineering Assessment.\
Author: Michael Mendes

### Commands
- Start Postgres server: pg_ctl start -l log/db_log.txt
  - **Note**: The `PGDATA` environment variable must be set, or this command must be run with `-D /path/to/postgres/data`
- Stop Postgres server: pg_ctl stop -m smart
- Connect to database via command line: psql -U postgres

### Run Project Locally
**Note**: Please ensure you have installed PostgreSQL before following these instructions.
1. Create two folders called `configs` and `log` in the root repository.
2. Use the *Start Postgres Server* command listed above to start your PostgreSQL server.
   **Note**: If you see an error saying that the environment variable `PGDATA` is unset, please set this according to your Operating System.\
             e.g If you are on a Windows machine, you can run the following command in Powershell `$env:PGDATA = 'C:\Program Files\PostgreSQL\17\data'` (Make sure the path matches your machines)
3. Run the SQL scripts titled `create_db_0326.sql` in the `sql/historical` folder to create the database.
4. In the `configs` folder create a file called `database.ini`.
5. In this file, enter your database connection information in the following format:
    ```ini
    [postgresql]
    host=localhost
    database=YOUR_DATABASE
    user=YOUR_USERNAME
    password=YOUR_PASSWORD
    ```
6. Install all dependencies listed in `requirements.txt`
   **Note**: The main required packages are `pandas` and `psycopg2`, all other packages will be installed as dependencies.
7. Run `main.py` after the database has started.
8. If you want the modified column to update on data changes, run the sql in the updated_at_0329.sql` file in `sql/historical` on your database.
 
### Environment Variables
| Name   | Description |
| ------ | ----------- |
| PGDATA | Path to the installed instance of Postgres |

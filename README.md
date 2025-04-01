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
3. In the `configs` folder create a file called `database.ini`.
4. In this file, enter your database connection information in the following format:
    ```ini
    [postgresql]
    host=localhost
    database=YOUR_DATABASE
    user=YOUR_USERNAME
    password=YOUR_PASSWORD
    ```
5. Install all dependencies listed in `requirements.txt`
6. Run `main.py` after the database has started.
 
### Environment Variables
| Name   | Description |
| ------ | ----------- |
| PGDATA | Path to the installed instance of Postgres |

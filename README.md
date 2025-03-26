## Arkartechture Engineering Assignment
Description: Repository for any relevant code pertaining to the Arkatechture Engineering Assessment.\
Author: Michael Mendes

### Commands
- Start Postgres server: pg_ctl start -l log/db_log.txt
  - **Note**: The `PGDATA` environment variable must be set, or this command must be run with `-D /path/to/postgres/data`
- Stop Postgres server: pg_ctl stop -m smart

### Environment Variables
| Name   | Description |
| ------ | ----------- |
| PGDATA | Path to the installed instance of Postgres |

/**
Descritpion: SQL to create a function that will updated the modified column with the current date/time when changes are made
Ran by Mike Mendeas on ark_assess db on 03/30/2025
**/

--Set search path to the 'dbo' schema
SELECT pg_catalog.set_config('search_path', 'dbo', false);

--Create function that will run whenever trigger detects changes to update the modified column to the current date/time
CREATE FUNCTION update_modified_column() RETURNS trigger LANGUAGE plpgsql AS $$ BEGIN NEW.modified = (now() at time zone 'UTC'); RETURN NEW; END; $$;

--Setup trigger to auto update modified column when data is changed on any of the tables
CREATE TRIGGER update_data_systems_modtime BEFORE UPDATE ON accounts FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
CREATE TRIGGER update_data_systems_modtime BEFORE UPDATE ON custom_fields FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
CREATE TRIGGER update_data_systems_modtime BEFORE UPDATE ON checking FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
CREATE TRIGGER update_data_systems_modtime BEFORE UPDATE ON loans FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
CREATE TRIGGER update_data_systems_modtime BEFORE UPDATE ON members FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
CREATE TRIGGER update_data_systems_modtime BEFORE UPDATE ON transactions FOR EACH ROW EXECUTE PROCEDURE update_modified_column();
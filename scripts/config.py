from configparser import ConfigParser

# Function that reads a config file for the database connection and returns said config
def load_config(filename='database.ini', section='postgresql'):
  parser = ConfigParser()
  parser.read('./configs/' + filename)

  config={}
  # Make sure config parser has data to read, then load the params from the data and save to the config object
  if parser.has_section(section):
      params = parser.items(section)
      for param in params:
          config[param[0]] = param[1]
  else:
      raise Exception('Section {0} not found in the {1} file'.format(section, filename));
  return config

if __name__ == '__main__':
    config = load_config()
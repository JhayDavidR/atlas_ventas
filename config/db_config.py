import configparser
import os

def get_db_config(section):
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_path)

    if section in config:
        return dict(config[section])
    else:
        raise Exception(f"Sección '{section}' no encontrada en config.ini")
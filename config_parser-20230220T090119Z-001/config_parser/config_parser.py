import os
import configparser
import json
import yaml
from .file_utils import get_file_extension


class ConfigParser:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path

    def read_config(self):
        file_extension = get_file_extension(self.config_file_path)
        if file_extension == '.conf':
            return self.read_config_from_conf()
        elif file_extension == '.cfg':
            return self.read_config_from_cfg()
        elif file_extension == '.yaml':
            return self.read_config_from_yaml()

    def read_config_from_conf(self):
        parser = configparser.ConfigParser()
        parser.read(self.config_file_path)
        config_dict = {}
        for section in parser.sections():
            for key, value in parser.items(section):
                config_dict[key] = value
        return config_dict

    def read_config_from_cfg(self):
        parser = configparser.ConfigParser()
        parser.read(self.config_file_path)
        config_dict = {}
        for section in parser.sections():
            for key, value in parser.items(section):
                config_dict[key] = value
        return config_dict

    def read_config_from_yaml(self):
        with open(self.config_file_path, 'r') as f:
            config_dict = yaml.load(f, Loader=yaml.FullLoader)
        return config_dict

    def write_config(self, file_type=None):
        config_dict = self.read_config()
        if file_type == '.env':
            self.write_config_to_env(config_dict)
        elif file_type == '.json':
            self.write_config_to_json(config_dict)
        elif file_type == 'os_env':
            self.write_config_to_os_env(config_dict)

    def write_config_to_env(self, config_dict):
        with open('.env', 'w') as f:
            for key, value in config_dict.items():
                f.write(f'{key}={value}\n')

    def write_config_to_json(self, config_dict):
        with open('config.json', 'w') as f:
            json.dump(config_dict, f)

    def write_config_to_os_env(self, config_dict):
        for key, value in config_dict.items():
            os.environ[key] = value

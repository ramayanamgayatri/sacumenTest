import os
from config_parser.config_parser import ConfigParser
from config_parser.exceptions import InvalidFileTypeError, ConfigFileNotFoundError


def test_read_config_from_conf():
    config_file_path = os.path.join(os.getcwd(), 'tests', 'test_files', 'test_config.conf')
    parser = ConfigParser(config_file_path)
    config_dict = parser.read_config()
    assert config_dict == {'key1': 'value1', 'key2': 'value2'}

def test_read_config_from_cfg():
    config
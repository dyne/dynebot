import logging
from configparser import ConfigParser
from os.path import dirname, abspath, join
from os import getenv

CONFIG_FILE_ENV = "DYNEBOT_CONFIGFILE"
DEFAULT_CONFIG_FILENAME = "config.ini"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)


class BaseConfig(object):
    def __init__(self):
        self._directory = dirname(abspath(__file__))
        _default_config = join(self._directory, DEFAULT_CONFIG_FILENAME)
        self._config_file = getenv(CONFIG_FILE_ENV, _default_config)

    def parse_config(self):
        config_parser = ConfigParser()
        _config_files = config_parser.read(self._config_file)
        if _config_files:
            log.info("Correctly loading configuration from => %s" % self._config_file)
        else:
            raise RuntimeError(
                'No configuration file was found. Please set following environment variable "%s" '
                "containing the path to the configuration file" % CONFIG_FILE_ENV
            )
        return config_parser

    @property
    def values(self):
        return self.parse_config()

    def get(self, name):
        return self.values.get("DEFAULT", name)

    def getint(self, name):
        return self.values.getint("DEFAULT", name)

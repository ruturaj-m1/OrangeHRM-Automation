"""Reads YAML config and JSON test data from the config/ folder."""
import json
import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, "config")


def load_config() -> dict:
    """Load config.yaml as a dictionary."""
    with open(os.path.join(CONFIG_DIR, "config.yaml"), "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_test_data() -> dict:
    """Load test_data.json as a dictionary."""
    with open(os.path.join(CONFIG_DIR, "test_data.json"), "r", encoding="utf-8") as f:
        return json.load(f)


CONFIG = load_config()
TEST_DATA = load_test_data()

import os

WORKSHOP_URL = os.environ.get("WORKSHOP_URL", None)
WORKSHOP_PASSWORD = os.environ.get("WORKSHOP_PASSWORD", None)
CSV_PATH = os.environ.get("CSV_PATH", "output/table.csv")

try:
    from local_creds import *  # noqa
except ImportError:
    pass

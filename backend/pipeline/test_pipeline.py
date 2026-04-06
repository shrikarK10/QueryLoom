import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm.llm_planner import plan_query
from utils.logger import logger as log
from utils.schema_updater import format_schema , build_column_mapping
import re
import sys
import os
from connectors.sqlite_connector import SQLiteConnector
from utils.config import DB_PATH

# Set up connector
connector = SQLiteConnector(DB_PATH)
schema = connector.get_schema()

formatted_schema = format_schema(schema)
log("Schema Extracted", formatted_schema)

column_mapping = build_column_mapping(schema)
print(plan_query("Get customers from Canada", formatted_schema, column_mapping))
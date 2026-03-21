from fastapi import APIRouter
from connectors.sqlite_connector import SQLiteConnector
from pipeline.querymind_pipeline import run_querymind
from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

router = APIRouter()

import os
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "AdventureWorks-sqlite.db")
connector = SQLiteConnector(db_path)

@router.post("/query")
def query(data: QueryRequest):
    return run_querymind(data.query, connector)
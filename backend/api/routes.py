from fastapi import APIRouter
from connectors.sqlite_connector import SQLiteConnector
from pipeline.querymind_pipeline import run_querymind
from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

router = APIRouter()

connector = SQLiteConnector(r"D:\PROJECT\QueryMind\backend\api\AdventureWorks-sqlite.db")

@router.post("/query")
def query(data: QueryRequest):
    return run_querymind(data.query, connector)
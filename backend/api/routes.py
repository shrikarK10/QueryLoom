# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from connectors.sqlite_connector import SQLiteConnector
from pipeline.querymind_pipeline import run_querymind
from pydantic import BaseModel
from utils.config import DB_PATH

class QueryRequest(BaseModel):
    query: str

router = APIRouter()

connector = SQLiteConnector(DB_PATH)

@router.post("/query")
def query(data: QueryRequest):
    return run_querymind(data.query, connector)
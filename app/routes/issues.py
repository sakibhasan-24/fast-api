import uuid
from fastapi import APIRouter,HTTPException,status
from app.schemas import issueCreate,issueOut,issueUpdate
from app.storage import load_data,save_data
router = APIRouter(prefix="/api/v1/issues",tags=["issues"])

@router.get("/",response_model=list[issueOut])
async def get_issues():
    issues=load_data()
    return issues



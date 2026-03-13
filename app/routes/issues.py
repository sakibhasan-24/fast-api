import uuid
from fastapi import APIRouter,HTTPException,status
from app.schemas import issueCreate,issueOut,issueUpdate,IssueStatus
from app.storage import load_data,save_data
router = APIRouter(prefix="/api/v1/issues",tags=["issues"])

@router.get("/",response_model=list[issueOut])
async def get_issues():
    issues=load_data()
    return issues


# create issue
@router.post("/",response_model=issueOut,status_code=status.HTTP_201_CREATED)
async def create_issue(payload:issueCreate):
    issues=load_data()
    
    new_issue={
        "id":str(uuid.uuid4()),
        "title":payload.title,
        "description":payload.description,
        "priority":payload.priority,
        "status":IssueStatus.open
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue

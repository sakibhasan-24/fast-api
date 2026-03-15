import uuid
from fastapi import APIRouter,HTTPException,status
from app.schemas import issueCreate,issueOut,issueUpdate,IssueStatus
from app.storage import load_data,save_data
router = APIRouter(prefix="/api/v1/issues",tags=["issues"])

@router.get("/",response_model=list[issueOut])
async def get_issues():
    issues=load_data()
    return issues


# get an single issue

@router.get("/{issue_id}",response_model=issueOut,status_code=status.HTTP_200_OK)
async def get_issue(issue_id:str):
    issues=load_data()
    for issue in issues:
        if issue["id"]==issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Issue not found")

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


# update issue
@router.patch("/{issue_id}", response_model=issueOut,status_code=status.HTTP_200_OK)
async def update_issue(issue_id: str, payload: issueUpdate):
    
    issues = load_data()

    for issue in issues:

        if issue["id"] == issue_id:

            update_data = payload.model_dump(exclude_unset=True)

            for key, value in update_data.items():
                issue[key] = value

            save_data(issues)

            return issue

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found"
    )

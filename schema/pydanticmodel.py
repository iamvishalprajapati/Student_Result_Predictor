from typing import Annotated
from pydantic import BaseModel, Field

class StudentValidation(BaseModel):
    studyhours: Annotated[int, Field(..., gt=0, description='Student Study Hours')]
    attendance: Annotated[int, Field(..., gt=0, description='Student Attendance')]
    pastscore: Annotated[int, Field(..., gt=0, description='Student Past Score')]
    sleephours: Annotated[int, Field(..., gt=0, description='Student Sleep Hours')]

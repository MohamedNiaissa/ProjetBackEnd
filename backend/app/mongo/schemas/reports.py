from typing import Optional
from pydantic import BaseModel, Field


# shared properties of all Reports
class ReportBase(BaseModel):
	reason: int
	user_id: str
	target: str
	target_id: str


# properties received by API on creation
class ReportCreate(BaseModel):
    pass


# properties received on update
class ReportToUpdate(BaseModel):
    pass


class ReportInDBBase(BaseModel):
    id: str = Field(alias="_id")


# additional properties to return via API
class Report(ReportInDBBase):
    pass


# additional properties stored in data
class ReportInDB(ReportInDBBase):
    pass

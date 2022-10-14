from typing_extensions import Self
from pydantic import BaseModel, Field
from mongo.schemas.reports import ReportBase


class Report(BaseModel):
	reason: int
	userId: str
	target: str
	targetId: str
	
	@classmethod
	def assert_model(self, report_data: ReportBase) -> Self:
		return self(
			reason=report_data.reason,
			userId=report_data.user_id,
			target=report_data.target,
			targetId=report_data.target_id,
		)

	class Config:
		schema_extra = {
			"example": {
				"id": 12,
				"user_id": 930,
				"post_id": 3984,
				"comment_id": 22,
				"reason": 1
			}
		}
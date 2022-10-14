from typing import List
from xmlrpc.client import Boolean
from fastapi import HTTPException, status
from pymongo.collection import Collection
from pymongo.database import Database
from mongo.models.reports import Report

from mongo.init_db import get_db
from bson import ObjectId

class CRUDReports():
	db_reports: Collection

	def __init__(self, db: Database):
		"""_summary_

		Args:
			db (Database): _description_
		"""
		self.db_reports = db.get_collection("reports")


	def get_all(self) -> List:
		"""_summary_

		Returns:
			List: _description_
		"""
		return list(self.db_reports.find())


	def create(self, request_data: Report) -> Boolean:
		"""_summary_

		Args:
			request_data (Report): _description_

		Returns:
			Boolean: _description_
		"""
		request_data.userId = ObjectId(request_data.userId)
		request_data.targetId = ObjectId(request_data.targetId)
		self.db_reports.insert_one(request_data.__dict__)
		return True


	def delete(self, id: str):
		"""_summary_

		Args:
			id (str): _description_

		Raises:
			HTTPException: _description_
		"""
		count = self.db_reports.delete_one({"_id": ObjectId(id)})
		if count.deleted_count is 0:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				details="Report doesn't exist"
			)


reports = CRUDReports(next(get_db()))
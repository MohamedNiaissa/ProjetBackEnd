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

	def __init__(self, db: Database) -> None:
		""" Init Reports class with the required database collection

		Args:
			db (Database): mongodb database
		"""
		self.db_reports = db.get_collection("reports")


	def get_all(self) -> List:
		""" Get all documents in the collection reports

		Returns:
			List: reports documents
		"""
		return list(self.db_reports.find())


	def create(self, report_data: Report) -> None:
		""" Create a report in the database

		Args:
			report_data (Report): report data
		"""
		report_data.userId = ObjectId(report_data.userId)
		report_data.targetId = ObjectId(report_data.targetId)
		self.db_reports.insert_one(report_data.__dict__)


	def delete(self, id: str):
		""" Delete a report in the database

		Args:
			id (str): id of the report

		Raises:
			HTTPException: raise 400 if report was not found
		"""
		count = self.db_reports.delete_one({"_id": ObjectId(id)})
		if count.deleted_count == 0:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="Report doesn't exist"
			)


reports = CRUDReports(next(get_db()))
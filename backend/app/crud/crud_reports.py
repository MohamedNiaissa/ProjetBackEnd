from fastapi import HTTPException
from pymongo.collection import Collection
from pymongo.database import Database

from api.v1.endpoints import reports
from api.deps import get_db
from core.config import settings

class CRUDReports():
    db_reports: Collection

    def __init__(self, db: Database):
        self.db_reports = db.get_collection("reports")


    def get(self, id: str):
        """
        Fetch the list of all reports or fetch a report by its ID, if the ID is mentionned

        Args:
            id (int): id of the report

        Returns:
            JSON: JSON of the whole list of reports or just a JSON with a specific report
        """
        try:
            return {}
        except HTTPException:
            pass 


    def create(self):
        """
        Create a report and insert the data in the reports collection

        Returns:
            JSON: inserted data report
        """
        try:
            return {}
        except HTTPException:
            pass 


    def delete(self, id: str):
        """
        Delete a specific report

        Args:
            id (int): id of the report

        Returns:
            JSON: all the infos of the report 
        """
        try:
            return {}
        except HTTPException:
            pass 


reports = CRUDReports(next(get_db()))
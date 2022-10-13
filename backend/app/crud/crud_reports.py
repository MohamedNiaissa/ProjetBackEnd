from api.v1.endpoints import reports
from core.config import Settings
from fastapi import HTTPException

class CRUD_reports():
    
    def get(id):        
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


    def create():
        """
        Create a report and insert the data in the reports collection

        Returns:
            JSON: inserted data report
        """
        try:
            return {}
        except HTTPException:
            pass 


    def delete(id):
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

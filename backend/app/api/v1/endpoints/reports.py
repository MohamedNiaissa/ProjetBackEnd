from typing import Any, List

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard

from mongo.schemas.reports import *
from mongo.models.reports import Report
from crud.crud_reports import reports
from mongo.schemas.reports import ReportBase

router = APIRouter()


@router.get("/")
@auth_guard("admin")
def get_report(request: Request) -> List:
	""" Get all the reports from the database

	Args:
		request (Request): request of the endpoint, user admin details are attached to it

	Raises:
		HTTPException: raise 404 if no reports were found

	Returns:
		List: reports documents
	"""
	reports_list = reports.get_all()
	if len(reports_list) is 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="No reports were found",
		)
	return reports_list


@router.post("/")
@auth_guard("user")
def create_report(request: Request, request_create: ReportBase = Body(...)) -> Any:
	""" User can submit a report, it can be a post or a comment

	Args:
		request (Request): request of the endpoint, user details are attached to it
		request_create (ReportCreate, optional): arguments necessary to create a report . Defaults to Body(...).

	Returns:
		Any: default status for code 200
	"""
	report_data = Report.assert_model(request_create)
	reports.create(report_data)
	return { "status": "OK" }


@router.delete("/{id}")
@auth_guard("admin")
def delete_report(request: Request, id: str) -> Any:
	""" Delete a report in the database

	Args:
		request (Request): request of the endpoint, user amdin details are attached to it
		id (str): id of the report

	Returns:
		Any: default status for code 200
	"""
	reports.delete(id)
	return { "status": "OK" }

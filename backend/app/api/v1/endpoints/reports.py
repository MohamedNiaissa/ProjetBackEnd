from typing import Any, List

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard
from mongo.models.reports import Report
from crud.crud_reports import reports
from mongo.schemas.reports import ReportCreate, ReportBase

router = APIRouter()


@router.get("/")
@auth_guard("admin")
def get_report(request: Request):
	"""_summary_

	Args:
		request (Request): _description_

	Raises:
		HTTPException: _description_

	Returns:
		_type_: _description_
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
def create_report(request: Request, request_create: ReportBase = Body(...)):
	"""_summary_

	Args:
		request (Request): _description_
		request_create (ReportCreate, optional): _description_. Defaults to Body(...).

	Returns:
		_type_: _description_
	"""
	report_data = Report.assert_model(request_create)
	reports.create(report_data)
	return { "status": "OK" }


@router.delete("/{id}")
@auth_guard("admin")
def delete_report(request: Request, id: str):
	"""_summary_

	Args:
		request (Request): _description_
		id (str): _description_

	Returns:
		_type_: _description_
	"""
	reports.delete(id)
	return { "status": "OK" }

###### History

## 0.0.1 (2022-09-11)
Backend setup.
* .gitignore
* .md

## 0.1.0 (2022-09-11)
Backend setup.
* project structure added (empty)

## 0.2.0 (2022-10-11)
Backend can be launched
* project structure refactored
* check added before launching server, raise error if mongodb is not found
* run server with uvicorn

## 0.2.1 (2022-10-11)
Added requirements
* generated requirements.txt with pipreqs
* fastapi
* pymongo
* tenacity
* uvicorn

## 0.2.2 (2022-10-11)
Updated requirements
* python-dotenv

## 0.2.3 (2022-10-12)
Put templates of endpoints
* comments.py
* likes.py
* posts.py 
* reports.py
* users.py

## 0.2.4 (2022-10-12)
Updated models
* added users basemodel

## 0.2.5 (2022-10-12)
Updated models
* added comments basemodel

## 0.2.6 (2022-10-22)
Updated models
* added posts basemodel

## 0.2.7 (2022-10-22)
Updated templates for CRUD
* CRUD users template
    * add docstring for the functions in the class CRUD_users

## 0.2.8 (2022-10-11)
Added JWT encode, decode + database init dependence
* added python-jose lib
* added passlib lib
* jwt encode
* jwt decode
* auth guard (soon a decorator)
* password checks
* db instance dependence

## 0.2.11 (2022-10-11)
Updated templates for CRUD
* CRUD reports template
    * add docstring for the functions in the class CRUD_reports


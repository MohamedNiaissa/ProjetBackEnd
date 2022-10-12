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
* project structure refractored
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

## 0.2.7 (2022-10-11)
Added JWT encode, decode + database init dependence
* added python-jose lib
* added passlib lib
* jwt encode
* jwt decode
* auth guard (soon a decorator)
* password checks
* db instance dependence
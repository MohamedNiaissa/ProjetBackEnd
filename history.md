###### History

## 0.0.1 (2022-10-11)
Backend setup.
* .gitignore
* .md

## 0.1.0 (2022-10-11)
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

## 0.2.6 (2022-10-12)
Updated models
* added posts basemodel

## 0.2.7 (2022-10-12)
Updated templates for CRUD
* CRUD users template
    * add docstring for the functions in the class CRUD_users

## 0.2.8 (2022-10-12)
Added JWT encode, decode + database init dependence
* added python-jose lib
* added passlib lib
* jwt encode
* jwt decode
* auth guard (soon a decorator)
* password checks
* db instance dependence

## 0.2.9 (2022-10-12)
Updated models
* added reports basemodel

## 0.2.10 (2022-10-12)
Updated models
* added likes basemodel

## 0.2.11 (2022-10-12)
Updated templates for CRUD
* CRUD reports template
    * add docstring for the functions in the class CRUD_reports

## 0.2.12 (2022-10-12)
Updated templates for CRUD
* CRUD posts template
    * add docstring for the functions in the class CRUD_posts

## 0.2.13 (2022-10-12)
Updated templates for CRUD
* CRUD likes template
    * add docstring for the functions in the class CRUD_likes

## 0.2.14 (2022-10-12)
Updated templates for CRUD
* CRUD comments template
    * add docstring for the functions in the class CRUD_comments

## 0.2.15 (2022-10-13)
Updated schema
* added schema for users

## 0.2.16 (2022-10-13)
Updated schema
* added schema for likes
* Fixed authors display

## 0.2.17 (2022-10-13)
Added auth guard decorator + integrations
* specify user role
* link to jwt decode and return user
* generator yield for mongodb database
* routes order fixed

## 0.2.18 (2022-10-13)
* Fix several CRUD issues
    * bad imports
    * rename 
    * put the fonctions in a good order

## 0.2.19 (2022-10-13)
Updated schemas
* added schema for posts

## 0.2.20 (2022-10-13)
Updated CRUD
* added db collection
* comments
* likes
* posts
* reports
* users

## 0.2.21 (2022-10-13)
Updated schemas
* added schema for reports

## 0.2.22(2022-10-13)
Updated schemas
* added schema for comments

## 0.2.23 (2022-10-13)
Updated models
* added config for user models
* improved config for comment models
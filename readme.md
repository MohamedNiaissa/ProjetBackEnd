# Social Network Backend

**Table of Contents**
* [Installation](#installation)
* [Backend Router](#Backend.router)

## Installation

Create your own venv and activate it
run `$ pip install -r requirements.txt`
run `cd backend`
run `sh prestart.sh`

## Backend.router

#### General information
---
###### Router : **/api**

###### Versionning :

* ###### **/v1**

#### Controllers
---
###### > **/auth**

| Routes Method | Query Params | Description | Trottle |
| :-------------------- | :-------------------: | :--------------- | ---------: |
| `post("/signup")`     | none                  | Auth signup | none |
| `post("/login")`      | none                  | Auth login | none |
| `post("/test-token")` | none                  | Retrieve a user | none |

###### > **/users**

| Routes Method | Query Params | Description | Trottle |
| :-------------------- | :-------------------: | :--------------- | ---------: |
| `get("/")`            | ?`page=n`&`items=n`   | Retrieve list of `n` users data (admin) | none |
| `get("/{id}")`        | none                  | Retrieve user data | none |
| `get("/me")`          | none                  | Retrieve user data | none |
| `patch("/me")`        | none                  | Modify a user | none |
| `delete("/me")`       | none                  | Delete a user | none |

###### > **/posts**

| Routes Method | Query Params | Description | Trottle |
| :-------------------- | :-------------------: | :--------------- | ---------: |
| `get("/")`            | ?`page=n`&`items=n`   | Retrieve list of n post data | none |
| `get("/{id}")`        | none                  | Retrieve post data | none |
| `post("/")`           | none                  | Create a post | none |
| `patch("/{id}")`      | none                  | Modify a post | none |
| `delete("/{id}")`     | none                  | Delete a post | none |


###### > **/comments**

| Routes Method | Query Params | Description | Trottle |
| :-------------------- | :-------------------: | :--------------- | ---------: |
| `get("/post/{id}")`   | ?`page=n`&`items=n`   | Retrieve list of `n` comments data by post id | none |
| `post("/")`           | none                  | Create a comment | none |
| `patch("/{id}")`      | none                  | Modify a comment | none |
| `delete("/{id}")`     | none                  | Delete a comment | none |

###### > **/likes**

| Routes Method | Query Params | Description | Trottle |
| :-------------------- | :-------------------: | :--------------- | ---------: |
| `get("/posts/{id}")`  | none                  | Retrieve user like state on post | none |
| `get("/comments/{id})`| none                  | Retrieve user like state on comment | none |
| `post("/posts")`      | none                  | Manage like state on post | none |
| `post("/comments")`   | none                  | Manage like state on comment | none |

###### > **/reports**

| Routes Method | Query Params | Description | Trottle |
| :-------------------- | :-------------------: | :--------------- | ---------: |
| `get("/")`            | ?`page=n`&`items=n`   | Retrieve list of `n` report data (admin) | none |
| `post("/")`           | none                  | Create a report | none |
| `delete("/{id}")`     | none                  | Delete a report (admin) | none |

### End

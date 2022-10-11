# Social Network Backend

**Table of Contents**
* [Installation](#installation)
* [Backend Router](#Backend.router)
* [WIP](#WIP)

## Installation

`ongoing...`

## Backend.router

#### General information
---
###### Router : **/api**

###### Versionning :

* ###### **/v1**

#### Controllers
---
###### > **/users**

| Routes Method | Query Params | Description | Trottle |
| :-------------------- | :-------------------: | :--------------- | ---------: |
| `get("/")`            | ?`page=n`&`items=n`   | Retrieve list of `n` users data (admin) | none |
| `get("/{id}")`        | none                  | Retrieve user data (admin) | none |
| `get("/me")`          | none                  | Retrieve user data (auth) | none |
| `post("/")`           | none                  | Create a user | none |
| `patch("/{id}")`      | none                  | Modify a user | none |
| `delete("/{id}")`     | none                  | Delete a user | none |

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
| `get("/")`            | ?`page=n`&`items=n`   | Retrieve list of `n` comments data | none |
| `get("/{id}")`        | none                  | Retrieve comment data | none |
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

## WIP

### End

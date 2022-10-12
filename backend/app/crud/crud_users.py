import imp
from api.v1.endpoints import users
from core.config import Settings

class CRUD_user():
    """
    Make sure to have the connection with the db and the users collection, so we can do all the oprations that we need
    in the functions below.
    """
        
    def get_all():
        """
        This function fetch all the users from the collection called users

        Returns:
            JSON: informations of all users
        """
        try:
            return {}
        except HTTPException:
            pass 
    
    def get_by_id(id):
        """
        This function fetch the user chosen by its ID from the collection called users
        Returns:
            JSON: informations of the choosen user
        """
        try:
            return {}
        except:
            pass

    def get_my():
        """
        This function fetch the current connected user from the collection called users
        Returns:
            JSON: informations of my user
        """
        try:
            return {}
        except:
            pass

    def create():
        """
        Create a user and insert it on the users collection

        Returns:
            JSON: inserted infos for the created user
        """
        try:
            return {}
        except HTTPException:
            pass 


    def modify(id):
        """
        Modify one or more specific data from a specific user

        Args:
            id (number): id of the user

        Returns:
            JSON: All the informations of this same user 
        """
        try:
            return {}
        except HTTPException:
            pass 

    def delete(id):
        """
        Delete a specific user     

        Args:
            id (number): id of the user

        Returns:
            JSON: All the informations of this same user 
        """
        try:
            return {}
        except HTTPException:
            pass 
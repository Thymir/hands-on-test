class BooklineAPI:

    def __init__(self) -> None:
        pass

    def insert_customer_email(self, email: str) -> None:
        """Insert an email in the database.

        If not successful, raise an InsertEmailError.
        """
        #  implementation for testing
        if (email == "email@error.com"): # insertion failed
            raise InsertEmailError
        else:
            pass
        #raise NotImplementedError


class InsertEmailError(Exception):
    pass

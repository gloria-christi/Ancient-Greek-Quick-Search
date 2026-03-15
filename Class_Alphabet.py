
class Alphabet:

    def __init__(self, word):
        self.WorD = word
        

    def file_checker(self, value):
        ERROR = "ERROR - Word not found in database"

        if value == "Not Found":
            return ERROR
        else:
            return self.WorD 
        


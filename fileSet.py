# Program: fileSet.py
# Usage: Provides Set Implementation using HashMap and along with File Redudandancy

import os

class userSet1():
    def __init__(self, fileAddr: str):
        # variable to store the file address
        self.__fileAddr = fileAddr

        # File Present 
        self.__filePresent = True

        # variable to store the set data
        self.__dataset = set()

        # variable to store the user count
        self.__userCount = 0

        # Read the Previous Users from the given file address
        # Enclosed in Try Block for better protection from the exceptions
        try:
            # Open the file in read mode
            # Read the previous users
            # Put in Try Block, So if the file doesn't exist it will throw error
            self.__fileHandle = open(file = self.__fileAddr, mode = "r")

            # If No Exception is Raised then the file exists and User data can be read
            users = [user.strip() for user in self.__fileHandle.readlines()]

            # Update the User Count
            self.__userCount = len(users)

            # Populate the set datastructure
            for user in users:
                self.__dataset.add(user)

            # Change the fileHandle to appendmode
            # Close the current fileHandle
            self.__fileHandle.close()
            
            # Open the same file in Append Mode
            self.__fileHandle = open(file = self.__fileAddr, mode = "a")
        except FileNotFoundError:
            # The file is not present
            # Set the __filePresent flag to False
            # This makes the fileHandle Close operation hassle free

            self.__filePresent = False
            raise FileNotFoundError("Given File Address is Invalid") from None

        print(self.__dataset)

    def getUserCount(self):
        return self.__userCount
    
    def addUser(self, username):
        # If the user is already present in the set
        # Do Nothing
        if self.__dataset.__contains__(username):
            return None

        # The Given user is not present in the set
        # Update the dataset, userCount and also the file
        self.__dataset.add(username)
        self.__userCount += 1

        self.__fileHandle.write(username + "\n")
        
    def __del__(self):
        if self.__filePresent:
            # Safely Close the File Handle
            self.__fileHandle.close()


# if __name__ == '__main__':
#     obj1 = userSet1("test.txt")
#     # obj2 = userSet1("test1.txt")

#     obj1.addUser("jaidheer")
#     obj1.addUser("Mehar Srinivas")
#     obj1.addUser("Kumar Rajesh")
#     obj1.addUser("Franklin")

#     obj1.addUser("jaidheer")
#     obj1.addUser("sankar")

#     print(obj1.getUserCount())






    

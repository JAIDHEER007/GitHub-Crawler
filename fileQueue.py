# Program: fileQueue.py
# Usage: Provides Set Implementation using HashMap and along with File Redudandancy

import os
from collections import deque

class userQueue1():
    # Basic fileQueue Implementation without any Optimizations
    
    def __init__(self, fileAddr: str):
        # variable to store the file address
        self.__fileAddr = fileAddr

        # File Present 
        self.__filePresent = True

        # variable to store the set data
        self.__dataset = deque()

        # Read the Previous Users from the given file address
        # Enclosed in Try Block for better protection from the exceptions
        try:
            # Open the file in read mode
            # Read the previous users
            # Put in Try Block, So if the file doesn't exist it will throw error
            
            with open(file = self.__fileAddr, mode = "r") as fileHandle:
                users = [user.strip() for user in fileHandle.readlines()]    
                for user in users:
                    self.__dataset.append(user)
            
        except FileNotFoundError:
            # The file is not present
            # Set the __filePresent flag to False
            # This makes the fileHandle Close operation hassle free

            self.__filePresent = False
            raise FileNotFoundError("Given File Address is Invalid") from None

    def writeDeque(self):
        with open(file = self.__fileAddr, mode = "w") as fileHandle:
            for user in self.__dataset:
                fileHandle.write(user + "\n")
        
    def addUser(self, username):
        self.__dataset.append(username)
        self.writeDeque()

    def popUser(self):
        self.__dataset.popleft()
        self.writeDeque()

    def printQueue(self):
        print(self.__dataset)

# if __name__ == '__main__':
#     obj1 = userQueue1("test.txt")
#     obj1.addUser("kumar rajesh")

#     obj1.printQueue()

#     obj1.popUser()

#     obj1.printQueue()






    

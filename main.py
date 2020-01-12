import xml.dom.minidom
from queries import *
import time

def main():
    #Loading and Parsing XML database
    document = xml.dom.minidom.parse("database.xml")

    #Print all staffs
    print("Original State")
    getAllStaff(document)

    #Add Staff
    insertStaff(document, "Demeqe", "400,000")
    print("Demeqe was inserted")
    time.sleep(2)
    getAllStaff(document)

    #Delete Staff
    if (deleteStaff(document, "Demeqe") ==True):
        print("Demeqe was deleted")
    else:
        print("Demeqe couldn't be deleted")
    time.sleep(2)
    getAllStaff(document)

    #Edit Staff
    insertStaff(document, "Demeqe", "400,000")    
    if (modifyStaff(document, "Demeqe", "500,000") ==True):
        print("Demeqe was modified.")
    else:
        print("Demeqe couldn't be modified")
    time.sleep(2)
    getAllStaff(document)

if __name__ == "__main__":
    main()





import xml.dom.minidom
from xml.etree import ElementTree

def getAllStaff(document):
    staffs = document.getElementsByTagName("staff")
    for staff in staffs:
        s_id = staff.getAttribute("id")
        name = staff.getElementsByTagName("name")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print("id: %s, name: %s, salary: %s" % (s_id, name.firstChild.data, salary.firstChild.data))

def insertStaff(document, name, salary):
    root = ElementTree.parse("database.xml").getroot()    
    new_staff = ElementTree.Element("staff")
    new_name = ElementTree.Element("name")
    new_salary = ElementTree.Element("salary")
    new_name.text  = name
    new_salary.text  = salary
    new_staff.set("id", "%s" % (document.getElementsByTagName("staff").length+1))
    new_staff.append(new_name)
    new_staff.append(new_salary)
    root.append(new_staff)

    tree = ElementTree.ElementTree()
    tree._setroot(root)
    tree.write("database.xml")

def deleteStaff(document, name):
    root = ElementTree.parse("database.xml").getroot()    
    for staff in root.findall('staff'):
        if(staff.find('name').text==name):
            root.remove(staff)
            tree = ElementTree.ElementTree()
            tree._setroot(root)
            tree.write("database.xml")
            return True
    return False
def modifyStaff(document, name, salary):
    root = ElementTree.parse("database.xml").getroot()    
    for staff in root.findall('staff'):
        if(staff.find('name').text==name):
            staff.find('salary').text = salary
            tree = ElementTree.ElementTree()
            tree._setroot(root)
            tree.write("database.xml")
            return True
    return False

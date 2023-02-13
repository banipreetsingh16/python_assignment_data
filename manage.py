# [
# {
#   'roll_num':1,
#   'name': John,
#   'subjects':[Hindi, English],
#   'class':'Five'
# }]

# 1. List Students
# 2. Search Student
# 3. Update Student
# 4. Delete Student
# 5. Add Student
# 6. Exit
# Please choose option:

data=[
    {
        "roll_no":1,
        'name':'Banipreet Singh',
        'subjects': ["Punjabi", "English", "Hindi"],
        'class':'Sixteen'
    },
        {
        "roll_no":2,
        'name':'Punar Pratap Singh',
        'subjects': ["Punjabi", "English", "Hindi"],
        'class':'Sixteen' 
    },
        {
        "roll_no":3,
        'name':'Upneet Kaur',
        'subjects': ["Punjabi", "English", "Hindi"],
        'class':'Fifteen' 
    },
    {
        "roll_no":4,
        'name':'Arshdeep Singh',
        'subjects': ["Punjabi", "English", "Hindi"],
        'class':'Fifteen' 
    }
     ]
print(
"1. List Students\n" 
"2. Search Student\n" 
"3. Update Student\n"
"4. Delete Student\n"
"5. Add Student\n"
"6. Exit\n"
)

def list_of_students():
    list_name = []
    for i in data:
        list_name.append(i["name"])
    return list_name

def search_student():
    input_search = int(input("Enter the Roll Number: " ))
    for i in data:
        if i["roll_no"] == input_search:
            return i

def update_student():
    input_search = int(input("Enter the Roll Number: " ))
    for i in data:
        if i["roll_no"] == input_search:
            print("Element found at index: ")
            print("1. Update Name")
            print("2. Update Subect")
            print("3. Update Class")
            choose=int(input("Choose the option: " ))
            if choose==1:
                inp_new_name = input("Enter the Updated Name: \n")
                i.update({"name": inp_new_name})
                print("Updated name is: ",inp_new_name)

            elif choose==2:
                index=int(input("Enter the index of the Subect which you want to update"))
                update_subject=input("Enter the updated Subject: ")
                i["subjects"][index] = update_subject
                print(i["subjects"])

def delete_subject():
    input_search = input("Enter name:- \n")
    for i in data:
        if i['name'] == input_search:
            print("Element found at index:- ", i)
            inp_del = input("Are you sure you want to delete it y/n? \n")
            if inp_del == 'y':
                del i
                print("Record Deleted \n")
                print(data)
            else:
                pass

def add_new_student():
    temp = {
            "roll_no": 0,
            'name':'',
            'subjects': [],
            'class':''
           }
    inp_roll_no = int(input("Enter roll number:- \n"))
    inp_name = input("Enter name:- \n")
    inp_class = input("Enter class:- \n")
    for i in range(3):
        inp_subject = input("Enter subject name:- \n")
        temp["subjects"].append(inp_subject)
    temp.update({"roll_no":inp_roll_no, 'name':inp_name, 'class':inp_class})
    data.append(temp)
    print(data) 


option=int(input("Choose the option:" ))
if option == 1:
    result= list_of_students()
    print(result)

elif option == 2:
    search = search_student()
    print(search)

elif option == 3:
    update_student()

elif option == 4:
    delete_subject()

elif option == 5:
    add_new_student()

elif option == 6:
    exit
    

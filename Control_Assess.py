import re
import time

Name = ["Awa", "William", "Kehinde", "Ejike", "Elyas", "Martins", "Inno"]

x = True
while x:
    Id_no = (input("Enter ID Number: "))
    if Id_no == "0":
        break

    if len(Id_no) == 7:
        print("Access Granted " + Name[0])
        print(time.asctime())
    elif not re.search("[0-9]", Id_no):
        break
    elif re.search("\s", Id_no):
        break
    else:
        x: bool = False

        if len(Id_no) == 6:
            print("Access Granted " + Name[1])
            print(time.asctime())
        elif not re.search("[0-9]", Id_no):
            break
        elif re.search("\s", Id_no):
            break
        else:
            x: bool = False

            if len(Id_no) == 5:
                print("Access Granted " + Name[2])
                print(time.asctime())
            elif not re.search("[0-9]", Id_no):
                break
            elif re.search("\s", Id_no):
                break
            else:
                x: bool = False

                if len(Id_no) == 4:
                    print("Access Granted " + Name[3])
                    print(time.asctime())
                elif not re.search("[0-9]", Id_no):
                    break
                elif re.search("\s", Id_no):
                    break
                else:
                    x: bool = False

                    if len(Id_no) == 3:
                        print("Access Granted " + Name[4])
                        print(time.asctime())
                    elif not re.search("[0-9]", Id_no):
                        break
                    elif re.search("\s", Id_no):
                        break
                    else:
                        x: bool = False

                        if len(Id_no) == 2:
                            print("Access Granted " + Name[5])
                            print(time.asctime())
                        elif not re.search("[0-9]", Id_no):
                            break
                        elif re.search("\s", Id_no):
                            break
                        else:
                            x: bool = False

                            if len(Id_no) == 1:
                                print("Access Granted " + Name[6])
                                print(time.asctime())
                            elif not re.search("[0-9]", Id_no):
                                break
                            elif re.search("\s", Id_no):
                                break
                            else:
                                x: bool = False
                                breakpoint(x)
if x:
    print("Wrong Access ID")
    print("Contact Access Control ETX: 2345")
    print(time.asctime())

print("\n\n")

filename = ""
filename = input("Please enter the file name to read <Hit Enter to Quit>: ")
repeat = True
if(filename == ""):
    print("Thank you.")
else:
    while repeat:
        try:
            file = open(filename, "r")
            repeat = False
        except:
            print("Error: file not found.")
            filename = input("Please enter the file name to read <Hit Enter to Quit>: ")
    text = file.read()
    line = ""
    total = ""
    step = 0

    while text != "":
        line = text#.substr(0-"\n").trim()
        if line#.charAt(0) == 1:
            #total = total + "\n, " + line.substr(3-end)
            step = 1
        elif line#.charAt(0) == 2:
            if step == 1:
                #total = total.substr(0-before last ", ") + line.substr(3-end)
            if step == 2:
                #
            if step == 3:
                #total = total + "\n" + line.substr(3-end) + ", [No First Name]"
            step = 2
        elif line#.charAt(0) == 3:
            #total = total + "\n" + line.substr(3-6) + "-" + line.substr(6-9)
            #+ "-" + line.substr(9-end)
            step = 3

    ######## Array Tests #########
    #arr = [line]
    #print(arr)

    ######## Pseudocode ##########
    #while text != "":
        #read the next line - put this str into "line"
        #convert data within line into a total str format (with "Lastname, Firstname
        #\nXXX-XXX-XXXX"
        #format by using concat into total)
            #must account for missing data - if there's no last/first name, add
            #"[No Last/First Name]"
    ### SHOULD BE DONE ALREADY ### - convert data into proper format
    #print data into a new .txt

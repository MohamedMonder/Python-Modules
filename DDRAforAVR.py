def DDRAMode():
    File = open("init.c","w+")
    File.write("void Init_PORTA_DIR (void)\n{\n")
    i=0
    DDR=""
    while i<8:
        while 1:
            value = str(input("Please enter Bit no. "+str(i)+" Mode as Output or Input: "))
            value =value.lower()
            if value =='input':
                DDR+="0"
                break
            elif value =='output':
                DDR+="1"
                break
            else:
                print("Incorrect Mode ")
        i+=1
    DDR="0b"+DDR
    File.write("    DDRA = "+ DDR+";\n}") 
    File.close()  

        
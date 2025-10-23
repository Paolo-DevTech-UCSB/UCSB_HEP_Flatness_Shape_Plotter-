



def Make_Diff_Plot(selected_file, selected_file2, folder_path, modulename, modulename2, ShapeID, ShapePlot):
    #print(selected_file, selected_file2, folder_path, modulename, ShapeID)
    ###################### PROGRAM DOES 1 - 2 so : Final goes in the first slot. (most of the time)
    MaskShape = ShapeID;
    #print("this is shape ID:", ShapeID)
    
    ##- 1 -##
    fileloco = selected_file;
    #modulename = fileloco.replace("C:\\Users\\Admin\\Documents\\OGPQualityControl-master\\data\\HD full\\","").replace(".xls","")
    df = pd.read_excel(fileloco)
    my_array = df.values
    newlist = [];
    
    ##- 1 -##
    for line in my_array:
        newline = [];
        elcount = 0;
        for entry in line:
            
            if type(entry) == float:
                newline.append('')
                elcount = elcount + 1; 
            else:
                newline.append(entry)
        if elcount < 8:
            newlist.append(newline);
            
    ##- 1 -##
    previousline = ['','','']; 
    beforeline = ['','','']; 
    rawheightslist = []
    for line in newlist:
        if 'J' not in str(line[2]):
            if 'flat' or 'Thick' in line[2]:
                #print(line)
                rawheightslist.append(line)
            elif 'flat' or 'Thick' in beforeline[2]: 
                #print(line);
                rawheightslist.append(line)
            elif 'flat' or 'Thick' in previousline[2]: 
                #print(line);
                rawheightslist.append(line)

        beforeline = previousline;    
        previousline = line;   
        
    ##- 1 -##
    lastname = '';
    Heightlist = []; LineNames = []; skiplines = 0; 
    for line in rawheightslist:
        if type(line[2]) is str:
            if 'FD' in line[2]:
                skiplines  = 3;
        if skiplines == 0:
            if 'flat' or 'Thick' in line[2]:
                lastname = line[2];
            #if line[3] == 'X':
            #    print("X is recognized")
            if line[3] == 'X':
                #print(lastname, 'X:', line[5])
                Heightlist.append([lastname, 'X', line[5], line[2]])
                LineNames.append(line[2])
                #print(line[2])

            if line[3] == 'Y':
                #print(lastname, 'Y:', line[5])
                Heightlist.append([lastname, 'Y', line[5], line[2]])
            if line[3] == 'Z':
                #print(lastname, 'Z:', line[5])
                Heightlist.append([lastname, 'Z', line[5], line[2]])
        else: skiplines = skiplines - 1;
    
    #print(LineNames)
    #LineNames = [];
    
    #print("List 1:")
    #print(Heightlist)

    ##- 2 -##   
    if ShapePlot == True:
        fileloco2 = selected_file;
        print("Making a Shape Plot..")
    else:
        fileloco2 = selected_file2;
        
    #modulename2 = fileloco2.replace("C:\\Users\\Admin\\Documents\\OGPQualityControl-master\\data\\HD full\\","").replace(".xls","")
    #modulename2 = selected_file.replace(folder_path,"").replace(".xls","")
    df2 = pd.read_excel(fileloco2)
    my_array2 = df2.values
    newlist2 = []; 

    ##- 2 -##        
    for line in my_array2:
        newline = [];
        elcount = 0;
        for entry in line:
            
            if type(entry) == float:
                newline.append('')
                elcount = elcount + 1; 
            else:
                newline.append(entry)
        if elcount < 8:
            newlist2.append(newline);        

    ##- 2 -##
    rawheightslist2 = []
    for line in newlist2:
        if 'J' not in str(line[2]):
            if 'flat' or 'Thick' in line[2]:
                #print(line)
                rawheightslist2.append(line)
            elif 'flat' or 'Thick' in beforeline[2]: 
                #print(line);
                rawheightslist2.append(line)
            elif 'flat' or 'Thick' in previousline[2]: 
                #print(line);
                rawheightslist2.append(line)
                
        beforeline = previousline;    
        previousline = line;    



    ##- 2 -##        
    lastname2 = '';
    Heightlist2 = []; LineNames2 = []; past = False; skiplines = 0
    for line in rawheightslist2:
        if type(line[2]) is str:
            if 'FD' in line[2]:
                skiplines  = 3;
        if skiplines == 0:
            if type(line[2]) is str:
                if 'BacksideSurface' in line[2]:
                    past = False;
                elif 'Backside' in line[2]:
                    print('going past')
                    past = True;
            if past != True:
            
                #print(line[2], line[5], line[3])
                #if type(line[2]) is str:
                #    if 'BacksideSurface' in line[2]:
                #        print('present')
                if 'flat' or 'Thick' in line[2]:
                    lastname2 = line[2];
                if line[3] == 'X':
                    #print(lastname2, 'X:', line[5])
                    Heightlist2.append([lastname2, 'X', line[5], line[2]])
                    LineNames2.append(line[2])
                    #print(line[2])
                if line[3] == 'Y':
                    #print(lastname2, 'Y:', line[5])
                    Heightlist2.append([lastname2, 'Y', line[5], line[2]])
                if line[3] == 'Z':
                    #print(lastname2, 'Z:', line[5])
                    Heightlist2.append([lastname2, 'Z', line[5], line[2]])
        else: skiplines = skiplines - 1
            
    #print(LineNames)
            
            
            
    ##############################################
            
    exclude_strings = {'#','Glass', 'HB', 'J', 'Top', 'Left', "Bot", "bottom", 'bot', 'Bottom', 'Right', 'FD1', 'FD2', 'FD3', 'FD4', 'FD4rough', 'FD2rough'}
    Heightlist = [array for array in Heightlist if not any(exclude in array[0] for exclude in exclude_strings)]
    Heightlist2 = [array for array in Heightlist2 if not any(exclude in array[0] for exclude in exclude_strings)]
    

        
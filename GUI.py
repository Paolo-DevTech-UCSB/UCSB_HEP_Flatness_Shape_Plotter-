




def OldMain():
    
    campaign = False;
    if campaign: 
        print("The Important Plots are:")
        print("All PreRad: Cycle 0 [-35] vs [RT]")
        print("All PreRad: Cycle 0 [RT] vs Cycle 10 [RT]")
        #print("PreRad: Cycle 0 [RT] vs PostRad: Cycle 0 [RT]")
        print("PreRad: Cycle 10 [RT] vs PostRad: Cycle 0 [RT] (Rad Change)")
        #print("PreRad: Cycle 0 [RT] vs PostRad: Cycle 30 [RT]")
        print("All PostRad: Cycle 0 [RT] vs Cycle 30 [RT] (Thermal Change)")
        print("PreRad: Cycle 0 [RT] vs PostRad: Cycle 1 [RT]")
        print("PreRad: Cycle 0 [RT] vs PostRad: Cycle 50 [RT]")
        print("PreRad: Cycle 0 [RT] vs PostRad: Cycle 50 [Bare]")
    
    ###### GET INSTRUCTIONS ########
    gotshape = False; gottype = False;
    while gotshape == False:
        Shape = input("Enter The Shape of the Module: ");
        if Shape in Shapes:
            gotshape = True;
    while gottype == False:
        Process = input("Are we making a Shape Plot or Height (Difference) Plot?:")
        if Process in ProcessTypes:
            gottype = True;
    #################################
    
    ######INTERPRET INSTRUCTIONS#####
    ShapePlot = False; DiffPlot = False;
    if Process in ShapePlotKeys:
        ShapePlot = True;
    elif Process in HeightDiffKeys: 
        DiffPlot = True;
        
    ShapeID = '';
    
    #print("This is the transacation happening: ", Shape, LDRightKeys)

    if Shape in LDTopKeys: ShapeID = 'LDT';
    elif Shape in HDTopKeys: ShapeID = 'HDT';
    elif Shape in LDBotKeys: ShapeID = 'LDB';
    elif Shape in LDRightKeys: ShapeID = 'LDR';
    elif Shape in LDLeftKeys: ShapeID = 'LDL';
    elif Shape in LDFiveKeys: ShapeID = 'LD5';
    elif Shape in LDFullKeys: ShapeID = 'LDF';
    elif Shape in HDFullKeys: ShapeID = 'HDF';
    elif Shape in HDBottomKeys: ShapeID = 'HDB';
    else:  print("no shape detected ")
    
    #print("this is Shape ID:", ShapeID)
    #################################'LDT''HDT''LDB''LDR''LDL''LD5''LDF''HDF'
    
    #############LOOK IN DATA FOLDER FOR APPROPRIATE FOLDER#############
    # Specify the folder path
    folder_path = "C:\\Users\\Admin\\Documents\\OGPQualityControl-master\\data\\"
    if ShapeID == 'LDT':
        folder_path = folder_path + "LD TOP\\"
    if ShapeID == 'HDT':
        folder_path = folder_path + "HD TOP\\"
    if ShapeID == 'LDB':
        folder_path = folder_path + "LD Bottom\\"
    if ShapeID == 'LDR':
        folder_path = folder_path + "LD Right\\"
    if ShapeID == 'LDL':
        folder_path = folder_path + "LD Left\\"
    if ShapeID == 'LD5':
        folder_path = folder_path + "LD Five\\"
    if ShapeID == 'LDF':
        folder_path = folder_path + "LD Full\\"
    if ShapeID == 'HDF':
        folder_path = folder_path + "HD Full\\"
    if ShapeID == 'HDB':
        folder_path = folder_path + "HD Bottom\\"
        
    
    # List all files in the folder
    #files = os.listdir(folder_path)
    #print(f"Files in folder: {files}")  # Debugging print
    
    # Iterate over each file and get the last access time
    #for file in files:
        #file_path = os.path.join(folder_path, file)
        #print(f"Checking file: {file_path}")  # Debugging print
        #if os.path.isfile(file_path):
        #    last_access_time = os.path.getatime(file_path)
        #    last_access_date = datetime.datetime.fromtimestamp(last_access_time)
        #    print(f"File: {file} - Last Accessed: {last_access_date}")
        #else:
        #    print(f"{file_path} is not a file.")  # Debugging print
    
    recent_files = get_recent_files(folder_path);
    
    file_dict = {};
    # Print the list of recent files with corresponding numbers
    #print("Most recent files:")
    for i, file in enumerate(recent_files):
        #print(f"{i + 1}: {file}")
        filename = os.path.basename(file)
        # Extract the main name part, e.g., "MLR3TX-SB0002"
        main_name = filename.split()[0]
        if main_name not in file_dict:
            file_dict[main_name] = []
        file_dict[main_name].append((i + 1, filename))

    # Print the organized files with the original enumerated numbers
    print("\nOrganized files by name:")
    for main_name, files in file_dict.items():
        print(f"Name: {main_name}")
        for file_info in files:
            # Print original enumerated number and file name without the main name part
            enumerated_number, filename = file_info
            description = filename.replace(main_name, '').strip()
            print(f"  {enumerated_number}: {description}")
    

    # Print the list of recent files with corresponding numbers
    #rint("Most recent files:")
    #for i, file in enumerate(recent_files):
    #    print(f"{i + 1}: {file}")

    # Ask the user to select a file
    if DiffPlot is True:
        file_number = int(input("Enter the number of the file you would like to use in the plot (final in f-i): ")) - 1
    else:
        file_number = int(input("Enter the number of the file you would like to use in the plot: ")) - 1
    #);
    # Define and print the selected file
    selected_file = recent_files[file_number]
    
    
    if DiffPlot is True:
        file_number2 = int(input("Enter the number of the file you would like to use in the plot(initial in f-i): ")) - 1
        print();
        # Define and print the selected file
        selected_file2 = recent_files[file_number2]
    
    
    print(f"Selected file: {selected_file}")
    print(f"Selected path: {folder_path}")
    modulename = selected_file.replace(folder_path,"").replace(".xls","")
    print(f"Module Name: {modulename}")
    print();
    
    if DiffPlot is True:
        print(f"Selected file (2): {selected_file2}")
        print(f"Selected path (2): {folder_path}")
        modulename2 = selected_file2.replace(folder_path,"").replace(".xls","")
        print(f"Module Name (2): {modulename2}")
        print();
    else: modulename2 = modulename;
    
    #print(selected_file, folder_path, modulename, ShapeID)
    
    if ShapePlot is True:
        Make_Diff_Plot(selected_file, selected_file, folder_path, modulename, modulename2, ShapeID, ShapePlot)
    elif DiffPlot is True:
        Make_Diff_Plot(selected_file, selected_file2, folder_path, modulename, modulename2, ShapeID, ShapePlot)
        
   
    
    
    
    
    
    
    
    
    
    
OldMain();
    
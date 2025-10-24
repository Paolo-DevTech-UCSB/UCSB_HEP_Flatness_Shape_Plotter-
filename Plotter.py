           
        
        
    timer = timer + 1;
        #print(line, timer);
        if timer > 3:
            timer = 0;
            xchk = ychk = zchk = False;
        
        if xchk and ychk and zchk and nameyet:
            
            #print(tempsX,tempsY,tempsZ, b+1)
            OGHeights2.append([float(tempsX) - 140, float(tempsY) - 300, float(tempsZ), b + 1])
            OGHeightsX2.append(float(tempsX) - 140)
            OGHeightsY2.append(float(tempsY) - 300)
            OGHeightsZ2.append(float(tempsZ))
            
            OGpoint2 = np.array([[float(tempsX) - 140, float(tempsY) - 300, float(tempsZ)]])
            
            OGpoints2 = np.vstack([OGpoints2, OGpoint2])
            
            #print(point)
            
            xchk = ychk = zchk = False;
            zchk = False;
            timer = 0;
            b += 1


    #print()
    #print(OGHeights2)        
    #print()

    
    #print(OGpoints , OGpoints2)
    #### THIS CENTERS THE MEASUREMENTS ###  
    ##- 1 -##       
    if MaskShape == 'LDR':
        ShapeAdjustmentX = -30;
        ShapeAdjustmentY = 0;
    if MaskShape == 'LDT':
        ShapeAdjustmentX = 0;
        ShapeAdjustmentY = -50;
    if MaskShape == 'HDB':
        ShapeAdjustmentX = -15;
        ShapeAdjustmentY = 0;
    else: 
        ShapeAdjustmentX = 0;
        ShapeAdjustmentY = 0;
        
    scale = 100/100;    
    
    
    
    AvgX = sum(OGHeightsX)/len(OGHeightsX) + ShapeAdjustmentX;      
    AvgY = sum(OGHeightsY)/len(OGHeightsY) + ShapeAdjustmentY;
    
    AvgZ = sum(OGHeightsZ)/len(OGHeightsZ);      
    AvgZ2 = sum(OGHeightsZ2)/len(OGHeightsZ2);
    
    #if ShapePlot: print( )
        #print(" File 1: Coordinate Averages:", AvgX, AvgY);
    #else: 
        #print("File 1: Coordinate Averages:", AvgX, AvgY); 
        #print("File 2: Coordinate Averages:", AvgX, AvgY);
    
    #ShapeAdjustments
    if MaskShape == 'LDF' or MaskShape == 'HDF' or MaskShape == 'LD5':
        shadjX = 0; shadjy = 0;
    elif MaskShape == 'LDR':
        shadjX = 0; shadjy = 0;
    elif MaskShape == 'LDL':
        shadjX = -40; shadjy = 0;
    elif MaskShape == 'LDT':
        shadjX = 0; shadjy = 0;
    elif MaskShape == 'LDB':
        shadjX = 0; shadjy = 0;
    elif MaskShape == 'HDT':     
        shadjX = 0; shadjy = 40;
    elif MaskShape == 'HDB':     
        shadjX = 0; shadjy = 0;
    else:
        shadjX = 0; shadjy = 0;

    
    
    
    for line in OGHeights:
        Heights.append([(line[0]- AvgX + shadjX)*scale, (line[1] - AvgY + shadjy)* scale, line[2], line[3]])
        HeightsX.append(line[0]- AvgX + shadjX)
        HeightsY.append(line[1] - AvgY + shadjy)
        HeightsZ.append(line[2])

        point = np.array([(line[0]- AvgX + shadjX)*scale, (line[1] - AvgY + shadjy)*scale, line[2]])

        points = np.vstack([points, point])
        
        ##- 2 -## 
    AvgX2 = sum(OGHeightsX2)/len(OGHeightsX2) + ShapeAdjustmentX;     
    AvgY2 = sum(OGHeightsY2)/len(OGHeightsY2) + ShapeAdjustmentY; 

    for line in OGHeights2:
        Heights2.append([(line[0]- AvgX2)*scale, (line[1] - AvgY2)*scale, line[2], line[3]])
        HeightsX2.append(line[0]- AvgX2)
        HeightsY2.append(line[1] - AvgY2)
        HeightsZ2.append(line[2])

        point2 = np.array([(line[0]- AvgX2)*scale, (line[1] - AvgY2)*scale, line[2]])

        points2 = np.vstack([points2, point2])

    #HeightsAverage = sum(HeightsZ) / len(HeightsZ)
    #HeightsMin  = min(HeightsZ)
    #HeightsMax  = max(HeightsZ)

    #HeightsAverage2 = sum(HeightsZ2) / len(HeightsZ2)
    #HeightsMin2  = min(HeightsZ2)
    #HeightsMax2  = max(HeightsZ2)
    #print(OGHeights)
    #print(OGHeights2)
    
    

            
    
    tolerance = 1.2;
    corrections = True;
    if corrections is True:
        print('This is Z average:', AvgZ)
        for point in points:
            #print(point)
            if np.abs(point[2] - AvgZ) > tolerance:
                print("!!! ALERT !!!!")
                print("Value of Point:", point, "is higher than the tolerance, Setting to Avg")
                point[2] = AvgZ ;
                print("now:", point);
                
            #if point[2] > 4:
            #    print("Value of Point:", point, "is greater than 4, setting to 3")
            #    point[2] = AvgZ2;
            #    print("now", point);
        
        if ShapePlot == False:
            for point in points2:
                #print(point)
                if np.abs(point[2] - AvgZ2) > tolerance:
                    print("Value of Point:", point, "is higher than the tolerance, Setting to Avg")
                    point[2] = AvgZ2;
                    print("now:", point);
        
                    
        print('This is Z average:', AvgZ)
        if AvgZ > 20:
            print("Moving down from Average adding 3.1");
            print("After Height Value Adjustment: ")
            for point in points:
                if ShapePlot: point[2] = point[2] - AvgZ;
                else: point[2] = point[2] - AvgZ + 3.1;
                print(point)
            
               
                
            #if point[2] > 4:
            #    print("Value of Point:", point, "is greater than 4, setting to 3")
            #    point[2] = AvgZ2;
            #    print("now", point);
        if AvgZ2 > 20:
            if not ShapePlot: print("Moving down from Average adding 3.1");
            for point in points2:
                point[2] = point[2] - AvgZ + 3.1;
                
    # Extract x, y, z coordinates
    
    X = points[:, 0]
    Y = points[:, 1]
    Z = points[:, 2]
    print("Max value:", max(Z))
    print("Min value:", min(Z))
    
    #print("---")
    #print(OGHeights)
    
    #print("---")
    #print(Heights)
    
    #TEST ARRAY
    #X.fill(4)
    #Y.fill(4)
    
    #Z = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0] #25 points center bowl
    #Z = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0] #21 points center bowl
    #print(X,Y,Z)
    
    #X2 = points2[:, 0]
    #Y2 = points2[:, 1]
    Z2 = points2[:, 2]
    print("Max value:", max(Z2))
    print("Min value:", min(Z2))
    
    #print(Z);
    #print(Z2);

    DX = X;
    DY = Y;
    if ShapePlot == True:
        DZ = Z;
    else:
        DZ = Z - Z2;
        
    #DZ = Z - Z2;
    
    #test points
    #DZ[0] = 10;
    #DX[0] = 0; DY[0] = 0;
    #DX[8] = 60; DY[8] = 0;
    #DZ[8] = 10;
    #print(DX[0], DY[0], DZ[0])
    #print(DX[0], DY[0], DZ[0])


    # Create the design matrix for a higher-order polynomial
    A = np.c_[np.ones(points.shape[0]), DX, DY, DX**2, DY**2, DX*DY, DX**3, DY**3, DX**2*DY, DX*DY**2]
    # Solve for the coefficients
    C, _, _, _ = scipy.linalg.lstsq(A, DZ)
    # Calculate the fitted values
    z_fit = A @ C
    # Calculate the errors
    errors = DZ - z_fit
    
    
    FitMin  = min(z_fit)
    FitMax  = max(z_fit)
    
    #print(FitMin, FitMax)
    
    errorsMax = round(max(errors),2);
    total_error = np.sum(np.abs(errors))
    print()
    print(f" (1) Total error: {total_error}")
    print()

    #newFitMax = FitMax - FitMax; 


    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    u, v = np.meshgrid(u, v)  # Create a meshgrid for u and v
    #fn = 15 - 1 * a * np.abs(np.sin(u * 3))**g + 2

    #'LDT''HDT''LDB''LDR''LDL''LD5''LDF''HDF'
    
    #HEXAGON Formula
    if MaskShape == 'LDF' or MaskShape == 'HDF' or MaskShape == 'LD5':
    #if MaskShape == 'LDF' or MaskShape == 'HDF' or MaskShape == 'LD5' or MaskShape == 'LDR':
        
        u = np.linspace(0, 2 * np.pi, 100)   #   0, 2 * np.pi
        v = np.linspace(0, np.pi, 100)
        u, v = np.meshgrid(u, v)
        fn = 15 - 1 * a * np.abs(np.sin((u) * 3))**g + 2;
        
    elif MaskShape == 'LDR':
        u = np.linspace(-5/6*np.pi, np.pi/6, 100)
        #u = np.linspace(-np.pi/6, (5/6)*np.pi, 100)   #  -np.pi/2, np.pi/2
        v = np.linspace(0, np.pi, 100)
        u, v = np.meshgrid(u, v)
        fn = 15 - 1 * a * np.abs(np.sin((u + np.pi) * 3))**g + 2;

    elif MaskShape == 'LDL':
        
        #u = np.linspace(np.pi*5/6, 11/6*np.pi, 100)    #  np.pi/2, -np.pi/2
        u = np.linspace(np.pi/6, 7/6*np.pi,  100)
        v = np.linspace(0, np.pi, 100)
        u, v = np.meshgrid(u, v)
        fn = 15 - 1 * a * np.abs(np.sin(u * 3))**g + 2;
        
    elif MaskShape == 'LDT':
        
        u = np.linspace(-2/6*np.pi, 4/6*np.pi, 100)   # 0, np.pi
        v = np.linspace(0, np.pi, 100)
        u, v = np.meshgrid(u, v)
        fn = 15 - 1 * a * np.abs(np.sin(u * 3))**g + 2;
        
    elif MaskShape == 'LDB':
        
        u = np.linspace(1/3*np.pi, -2/3*np.pi, 100)    # np.pi, 2*np.pi
        v = np.linspace(0, np.pi, 100)
        u, v = np.meshgrid(u, v)
        fn = 15 - 1 * a * np.abs(np.sin(u * 3))**g + 2;

    elif MaskShape == 'HDT':     
        
        u = np.linspace(-2/6*np.pi, 4/6*np.pi, 100)
        #u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        u, v = np.meshgrid(u, v)
        fn = 15 - 1 * a * np.abs(np.sin(u * 3))**g + 2;
    
    elif MaskShape == 'HDB':    
        
        u = np.linspace(0, 2 * np.pi, 100)   #   0, 2 * np.pi
        v = np.linspace(0, np.pi, 100)
        u, v = np.meshgrid(u, v)
        fn = 15 - 1 * a * np.abs(np.sin((u) * 3))**g + 2;
        
        #fn[fn > threshold] = threshold
        
        #UCOMMENT IF BUNDARY DOESNT WORK
        
        
        """
        u = np.linspace(0, 2 * np.pi, 100)   # theta from 0 to 2π
        v = np.linspace(0, np.pi, 100)
        u, v = np.meshgrid(u, v)
        
        # Rotate 60 degrees to the left (counterclockwise)
        u_rot = u + np.pi / 3
        
        # Define components using rotated angle
        Y = 17 - 2 * np.abs(np.sin(u_rot * 3))**1
        T = -np.abs(np.cos(u_rot / 2 + (9 * np.pi / 12)))**25 + 1
        J = np.abs(np.cos(u_rot / 2 + (9 * np.pi / 12)))**70
        U = 20 - 10 * (np.sin(u_rot))**2
        E = 0.5 - np.sin(9 * u_rot)
        K = np.abs(np.cos(u_rot / 2 + (9 * np.pi / 12)))**20


        
        # Final function
        fn = Y * T + J * U + E * K
        """
         
    else:
        print("!!!!! ELSE !!!!!")
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        u, v = np.meshgrid(u, v)
        fn = 15 - 1 * a * np.abs(np.sin(u * 3))**g + 2;

    
    #important Do not move from here!!!!
    r = np.ones(u.shape) * fn

     #Calculate x, y, and z using the meshgrid
    if MaskShape == 'HDB': 
        x0 = 5 * (r * np.cos(u + np.pi / 3)) * np.sin(v)
        y0 = 5 * (r * np.sin(u + np.pi / 3)) * np.sin(v)
        x = y0
        y = -1*x0
    else:
        x = 5 * (r * np.cos(u + np.pi / 3)) * np.sin(v)
        y = 5 * (r * np.sin(u + np.pi / 3)) * np.sin(v)
    

        
    # Define y threshold for masking
    #y_threshold = 100  # Example threshold
    
    
    #x_masked = np.ma.masked_where(y < y_threshold, x)
    #y_masked = np.ma.masked_where(y < y_threshold, y)


    if MaskShape == 'HD Top':                            ##CHECK THAT THIS WORKS / MAKE IT WORK 
        x_min, x_max = -1000, -30;

        # Apply limits using a for loop
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                if x[i, j] < x_min or x[i, j] > x_max:
                    x[i, j] = np.nan  # Set to NaN or any other value to indicate out of bounds
                    
                    

    ############### THE FUNCTION ###########################

    min_value = np.nanmin(Z)
    max_value = np.nanmax(Z)

    if np.abs(max_value-min_value) >= 0.3:
        print("Spread is too large, ","DELTA:", (max_value-min_value))
        woc = input("Would You Like To Continue With Linear Coeficcients = 0 (t/f)?: ")
        if woc == 't':
            print(C)
            C[2] = 0     
            C[1] = 0
            C[0] = 0
            print(C)
    print();
        
  
    Z = (C[0] + C[1] * x + C[2] * y + C[3] * x**2 + C[4] *y**2 + C[5] * x * y +
         C[6] * x**3 + C[7] * y**3 + C[8] * x**2 * y + C[9] * x * y**2)

    
    Coeficient_Value = np.abs(C[1]) + np.abs(C[2])

    #spike locators
          
    spike_locations = []
    for i in range(len(HeightsX)):
        spike_locations.append((HeightsX[i], HeightsY[i]))
    #print("spike locations", spike_locations)

        
    #Locations of spikes
    #spike_heights = [0.1, 0.2, 0.3, 0.5, 0.8, 1.2, 1.6, 2.1, 2.7, 3.4, 4.2, 5.1, 6.1, 7.2, 8.4, 9.7, 11.1, 12.6, 14.2, 15.9, 17.7, 19.6, 21.6, 23.7, 25.9]  # Heights of spikes
    #spike_widths = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  # Widths of spikes
    #
    
    #for (x_spike, y_spike), height, width in zip(spike_locations, spike_heights, spike_widths):
    #    spike = height * np.exp(-((x - x_spike)**2 + (y - y_spike)**2) / (2 * width**2))
    #    Z += spike
    
    #print(spike_locations)
    
    #TURN OFF!!!!!!!!!!!!!!!!!!!!!!!!
    #This removes a slant IF NEEDED!!!
    #Z = (C[0] + C[3] * x**2 + C[4] * y**2 + C[5] * x * y + C[6] * x**3 + C[7] * y**3 + C[8] * x**2 * y + C[9] * x * y**2)
    
    #print("look for points that arent near 4:", Z)
    #for value in Z:
    #    for data in value: 
    #       if data > 6:
                 #print(data)
    
    ############ TEST POINTS #############
    #X[0] = 0; Y[0] = 0;
    #X[8] = 100; Y[8] = 0;
    #Z[8] = 3.6;
    #########################


    #print("Min and Max: ",min_value, max_value)
    #print()
    #print("DELTA:", (max_value-min_value))
    #print()
    

    dZdX = (C[1]);       dZdY = (C[2]);      dZdX2 = (2*C[3]);      dZdY2 =(2*C[4]);      dZdXdY = (C[5]);

    Curvature = np.abs((dZdY**2)*(dZdX2) - 2*(dZdX)*(dZdY)*(dZdXdY) + (dZdX**2)*(dZdY2))  /  ((dZdX**2 + dZdY**2)**(3/2))


    print("Curvature @ (x=0 , y=0): " , Curvature)

    k1 = (dZdX2 + dZdY2 + np.sqrt((dZdX2 - dZdY2)**2 + 4*(dZdXdY)**2))/2

    k2 = (dZdX2 + dZdY2 - np.sqrt((dZdX2 - dZdY2)**2 + 4*(dZdXdY)**2))/2

    S = (2/np.pi)*np.arctan((k1 + k2)/(k1 - k2))

    print("Shape Index: " , S)



    C_1 = ["{:.2e}".format(x) for x in C]

    #print(C_1)

    print(f' Z = {C_1[0]} + {C_1[1]}x + {C_1[2]}y + {C_1[3]}x^2 + {C_1[4]}y^2 + {C_1[5]}xy + {C_1[6]}x^3 + {C_1[7]}y^3 + {C_1[8]}yx^2 + {C_1[9]}xy^2')


    z_0 = Z * 0 +  FitMin*0.99# - HeightsMin;
    z_E = Z * 0 +  FitMax*1.01
    
    #print("-",np.sum(Z), "/" , len(Z)*len(Z[0]), '=', np.sum(Z)/(len(Z)*len(Z[0])));
    
    if ShapePlot: 
        NewAvg = np.sum(Z)/(len(Z)*len(Z[0]))
        #print(Z)
        Z = Z - NewAvg;
        z_0 = Z * 0 + np.min(Z)
        FitMin = np.min(Z) - 0.1;
        #print(Z)
    else: 
        NewAvg = 0;
        
    
    #print(z_0)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.axis('off')
    
    # Define the min and max values for the color scale
    #vmin = -0.5
    #vmax = 0.6

    # Plot the surface with a fixed color scale
    #NORMAILZING IS VERY IMPORTANT 
    norm = Normalize(vmin=-0.4, vmax=0.4)
    surf = ax.plot_surface(x, y, Z, cmap=cm.rainbow, norm=norm)
    
    ##### cmap=cm.rainbow
    
    
    if ShapeID  == 'HDB':
        ax.view_init(elev=0, azim=0)
        ax.set_xlim([-75, 75])
        ax.set_ylim([-75, 0])
        ax.set_zlim([-1, 1])
    else:
        ax.view_init(elev=0, azim=0)
        ax.set_xlim([-75, 75])
        ax.set_ylim([-75, 75])
        ax.set_zlim([-1, 1])
    
    # Adding a colorbar (legend) for the heightmap with consistent scale
    cbar = fig.colorbar(surf, ax=ax, orientation='vertical')
    cbar.set_label('Height (mm)')
    
    
    # Add error text below the plot
    if ShapePlot == False:
        error_message = f"Maximum Error Between Measured Difference and Fit +/-{errorsMax}mm "
    else:
        error_message = f"Maximum Error Between Measurement and Fit +/-{errorsMax}mm "
    fig.text(0.5, 0.06, error_message, ha='center', fontsize=8, color='black')
    
    
    dirs = fileloco.replace(".xls","").replace(modulename,"")

    
    filename_1 = selected_file;
    edit1 = filename_1.replace(r"C:\Users\Admin\Documents\OGPQualityControl-master\data\\", "")
    edit2 = edit1.replace(r"Full", '').replace("\\","").replace("TOP","")
    main_name = edit2.split()[0]
    
    #print("This is main name", main_name)
    
    
    #shortmodulename = modulename[14:]
    shortmodulenameedit = selected_file.replace(r"C:\Users\Admin\Documents\OGPQualityControl-master\data\HD ", "").replace(r"Full", '').replace("\\","");
    shortmodulename = shortmodulenameedit.replace('.xls','').replace(main_name, '')
    
    if ShapePlot == False:
        title = main_name + " Height Movement Plot" ;
        title2 =  modulename[:16] + " Difference Plot";
    else: 
        title = main_name + " Shape Plot " ;
        title2 = modulename[:16] + " Shape Plot";
    
    #print("DEBUGGING:",title, title2)
    
    l1 = -0.90;
    l2 = 0.90;
    
    #ax.set_zlim([FitMin - 0.3, FitMax + 2.5])
    ax.set_zlim([l1, l2])

    #ax.text(-100, -40, 0, 'CH1', color='black', fontsize=12, zorder=10)  # Bottom-left corner
    #ax.text(-100, 40, 0, 'CH8', color='black', fontsize=12, zorder=10) 
    ax.text(40, 100, FitMin, 'CH8', color='black', fontsize=12, zorder=10)  # Bottom-left corner
    ax.text(-50, 100, FitMin, 'CH1', color='black', fontsize=12, zorder=10) 

    ax.set_title(title2, fontsize=14)

    #surf = ax.plot_surface(x, y, Z, cmap=cm.rainbow, norm=norm)
    shadow = ax.plot_surface(x, y, z_0, color='k', zorder=0)
            
    
    print(FitMax, np.nanmean(z_E))
    print(FitMin, np.nanmean(z_0))
    
    if np.nanmean(z_E) > np.nanmean(z_0):
        print('the mask is on top')
    else:
        print('the mask is below')
            
    
    if ShapeID == 'HDB':
        if ShapePlot is False:
            print(' DIFFERENCE PLOT ???')   
            print(FitMax, np.nanmean(z_0))
            print(FitMin, np.nanmean(z_E))
            cutout = ax.plot_surface(u*12-20, v*80 - 80, z_E+1,
                                 color='white', shade=False, alpha=1.0, zorder=0)
            
        else:    
            cutout = ax.plot_surface(u*-40, v*60 - 60, z_E,
                                 color='white', shade=False, alpha=1.0, zorder=0)
            
            
            
            
    # Axis limits and view settings
    if ShapeID == 'LD5':
        ax.set_xlim([-75, 0])
        ax.set_ylim([-50, 50])
    else:
        ax.set_xlim([-75, 75])
        ax.set_ylim([-75, 75])
    
    l1 = FitMin - 0.3
    l2 = FitMax + 0.3
    ax.set_zlim([l1, l2])
    
    if ShapeID == 'HDB':
        ax.view_init(elev=65, azim=0)
    else:
        ax.view_init(elev=65, azim=-90)

    # Define hand-placed points
    #x_points = np.array([0, 2, -3])
    #y_points = np.array([0, 2, -3])
    #z_points = np.ones_like(x_points) * 0.3 * 4  # Points at the same height
    #ax.scatter(x_points, y_points, z_points, color='black')
    #for i in range(len(x_points)):
    #    ax.text(x_points[i], y_points[i], z_points[i], f'({x_points[i]}, {y_points[i]}, {z_points[i]})', color='black')
        

    print("Current working directory:", os.getcwd())
         
    if ShapePlot is False:
        print("saving into:", dirs , modulename + '-Minus-' + modulename2  , '.png' )
        filename = os.path.join(dirs, modulename + '-Minus-' + modulename2 + '.png')
        plt.savefig(filename)

    else:
        
        filename = os.path.join(dirs, modulename.replace(' ','') + '.png')
        print("saving into:", filename )
        plt.savefig(filename)
    #filenames.append(dirs + '\\GIFS\\tempphotos\\' + str(i) + '.png')

    #print("frame", i)
    plt.show();
    plt.close(fig)  # Clear the current figure
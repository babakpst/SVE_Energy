
###############################################################################
#
# Code developed by: Dr. Babak Poursartip
# Supervised by:     Dr. Ben R. Hodges
# 
# Start date:    07/18/2017
# Latest update: 11/20/2017
#
# Comment: This class reads the simulation data from the input file.
#
###############################################################################

class Input_Info:

    def __init__(self, argv):
        
        import Setting_Class

        setting = Setting_Class.Setting() # The default option
        self.command_line_args = {}

        self.command_line_args['DT_min'] = setting.DT_min
        self.command_line_args['DT_max'] = setting.DT_max
        self.command_line_args['Plot_at_Cell'] = setting.Plot_at_Cell
        self.command_line_args['Plot_at_Face'] = setting.Plot_at_Face
        self.command_line_args['CFLu_max'] = setting.CFLu_max
        self.command_line_args['CFLb_max'] = setting.CFLb_max
        self.command_line_args['Fr_max'] = setting.Fr_max
        self.command_line_args['depth_min'] = setting.depth_min
        self.command_line_args['time_advance'] = setting.time_advance
        self.command_line_args['Gravity'] = setting.Gravity

        arg_counter = 1

        while arg_counter < len(argv):

            option = argv[arg_counter]

            if option[0] == '-': option = option[1:] # remove 1st hyphen
            else:
                # not an option, proceed with next sys.argv entry
                arg_counter += 1
                continue

            if option[0] == '-': option = option[1:] # remove 2nd hyphen

            if option in self.command_line_args:
                # next command-line argument is the value
                arg_counter += 1
                value = float(argv[arg_counter])
                self.command_line_args[option] = value
                print(" New setting is defined in the command line:")
                print(option," is change to", value)
            else:
                print(" The entered option %s is not registered." % option)

            arg_counter += 1

    def Read_Data(self):
        import os
        import shutil

        # Input data ==========================================================
        # Read the name of the input file from address file
        print(" ============== Input Class ==============")
        Address = open("Address.txt","r")
        Temp = Address.readline().rstrip("\n")      # 1
        File = Address.readline().rstrip("\n")  # 2, Input file name
        Temp = Address.readline().rstrip("\n")  # 3
        Temp = Address.readline().rstrip("\n")  # 4
        Input_Dir = Address.readline().rstrip("\n")  # 5
        Temp = Address.readline().rstrip("\n")  # 6
        Temp = Address.readline().rstrip("\n")  # 7
        Output_Dir = Address.readline().rstrip("\n")  # 8

        # Create Input/Output directories
        self.InputFileName = os.path.join(Input_Dir, File) 
        self.Output_Dir = os.path.join(Output_Dir, os.path.splitext(File)[0])

        print(" {0} {1}".format("The input file name is:", self.InputFileName))
        print(" {0} {1}".format(" The output path is:", self.Output_Dir))

        # Check whether the input file exists 

        # Create or Clean the output directory
        if os.path.exists(self.Output_Dir):
            print(" The output folder exists! The content of this folder would be emptied.")
            Temp = input("Press Enter if it is alright, otherwise copy the content of the folder. --IS IT ALRIGHT? --")
            shutil.rmtree(self.Output_Dir, ignore_errors=True)
            os.makedirs(self.Output_Dir)

        if not os.path.exists(self.Output_Dir):
            print(" The output directory does not exist. ")
            print(" Creating the output directory ... ")
            os.makedirs(self.Output_Dir)

        # Empty memory
        Address.close()
        del Temp
        del File
        del Input_Dir

    def Read_Input(self):

        import numpy as np

        print(" Opening the input file ...")
        self.File_Input = open(self.InputFileName,"r")
        print()

        # -- Opens and Reads data from the input file
        Temp = self.File_Input.readline().rstrip("\n")
        Temp = self.File_Input.readline().rstrip("\n")
        Temp = self.File_Input.readline().rstrip("\n")
        Temp = self.File_Input.readline().rstrip("\n")
        self.Total_Time = float(Temp)  # Total simulation time
        print("{:40} {:f}".format(" The total simulation time is:", self.Total_Time))
 
        Temp = self.File_Input.readline().rstrip("\n") 
        Temp = self.File_Input.readline().rstrip("\n") 
        Temp = self.File_Input.readline().rstrip("\n") 
        self.Time_Step = float(Temp)  # Time step
        print("{:40} {:f}".format(" The time step is:", self.Time_Step))

        Temp = self.File_Input.readline().rstrip("\n")  
        Temp = self.File_Input.readline().rstrip("\n")  
        Temp = self.File_Input.readline().rstrip("\n")  
        self.Q_Up = float(Temp)  # A constant flow rate at the upstream
        print("{:40} {:f}".format(" Flow rate at the upstream is:", self.Q_Up))

        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        self.h_dw = float(Temp)  # Downstream water depth
        print("{:40} {:f}".format(" Downstream water depth is:", self.h_dw))

        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        self.V_in = float(Temp)  # Control volume at the upstream
        print("{:40} {:f}".format(" Initial Control Volume is:", self.V_in))

        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        self.V_ratio = float(Temp)  # Control volume change rate along the reach
        print("{:40} {:f}".format(" Control volume change rate along the reach is:", self.V_ratio))

        Temp = self.File_Input.readline().rstrip("\n")
        Temp = self.File_Input.readline().rstrip("\n")
        Temp = self.File_Input.readline().rstrip("\n")
        self.No_reaches  = int(Temp)  # Total number of reaches
        print("{:40} {:d}".format(" Total number of reach(es) is(are):", self.No_reaches))
        
        # Define arrays: 
        self.Reach_Length = np.zeros( self.No_reaches, dtype=np.float ) # Stores the length of each reach
        self.Reach_Disc = np.zeros( self.No_reaches, dtype=np.int   ) # Stores the no. of control volume in each reach
        self.Reach_Type = np.zeros( self.No_reaches, dtype=np.int   ) # Stores the no. of control volume in each reach
        self.Reach_Slope = np.zeros( self.No_reaches, dtype=np.float ) # Stores the slope of each reach
        self.Reach_Manning = np.zeros( self.No_reaches, dtype=np.float ) # Stores the Manning's number for each reach
        self.Reach_Width = np.zeros( self.No_reaches, dtype=np.float ) # Stores the width of each reach


        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        for ii in range(self.No_reaches): # Length of each reach
            Temp       = self.File_Input.readline().rstrip("\n")
            self.Reach_Length[ii] = float(Temp)
            print("The length of reach {:d} is {:f}".format(ii+1, self.Reach_Length[ii]))

        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        for ii in range(self.No_reaches): # Total number of control volumes in each reach/ For now we have a constant discretization in each reach.
            Temp       = self.File_Input.readline().rstrip("\n")
            self.Reach_Disc[ii] = int(Temp)
            print("No. of discretization of reach {:d} is {:f}".format(ii+1, self.Reach_Disc[ii]))

        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        for ii in range(self.No_reaches): 
            Temp       = self.File_Input.readline().rstrip("\n")
            self.Reach_Type[ii] = int(Temp)
            print("Rreach {:d} is of type: {:d}".format(ii+1, self.Reach_Type[ii]))

        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        for ii in range(self.No_reaches): # Slope of each reach
            Temp       = self.File_Input.readline().rstrip("\n")
            self.Reach_Slope[ii] = float(Temp)
            print("The slope of reach {:d} is {:f}".format(ii+1, self.Reach_Slope[ii]))

        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        for ii in range(self.No_reaches): # The Manning's number for each reach
            Temp       = self.File_Input.readline().rstrip("\n")
            self.Reach_Manning[ii] = float(Temp)
            print("The Manning's no. for reach {:d} is {:f}".format(ii+1, self.Reach_Manning[ii]))

        Temp       = self.File_Input.readline().rstrip("\n")
        Temp       = self.File_Input.readline().rstrip("\n")
        for ii in range(self.No_reaches): # The width of each reach
            Temp       = self.File_Input.readline().rstrip("\n")
            self.Reach_Width[ii] = float(Temp)
            print("The width of reach {:d} is {:f}".format(ii+1, self.Reach_Width[ii]))
        
        
        print(" ============ Input Class Ends ============")        
        print()
        print(" Closing the input file ... ")
        self.File_Input.close()
        print(" End Input_Class. ")



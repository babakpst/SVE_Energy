
#####################################################################
#
# Code developed by: Dr. Babak Poursartip
# Supervised by:     Dr. Ben R. Hodges
# 
# Start date:    08/03/2017
# Latest update: 12/27/2017
#
# Comment: This class visualizes the results using matplotlib module.
# WARNING: Different compilers may behave differently here.          
#
#####################################################################

class Visualization:
    
    def __init__(self):
        pass

    # This function plots the results only at the cell center, and not at the faces.
    @staticmethod
    def Plot_at_Cell(N, X, Z, Q, V, Eta, U, E, A, T1, T2):
        import numpy as np
        import matplotlib.pyplot as plt

        Q_Arr   = np.zeros(N, dtype = np.float64)
        V_Arr   = np.zeros(N, dtype = np.float64)
        Eta_Arr = np.zeros(N, dtype = np.float64)
        U_Arr   = np.zeros(N, dtype = np.float64)
        E_Arr   = np.zeros(N, dtype = np.float64)
        X_Arr   = np.zeros(N, dtype = np.float64)
        Z_Arr   = np.zeros(N, dtype = np.float64)
        A_Arr   = np.zeros(N, dtype = np.float64)

        Title      = T2
        Q_Arr[:]   = Q[:]
        V_Arr[:]   = V[:]
        Eta_Arr[:] = Eta[:]
        U_Arr[:]   = U[:]
        E_Arr[:]   = E[:]
        X_Arr[:]   = X[:]
        Z_Arr[:]   = Z[:]
        A_Arr[:]   = A[:]

        #plt.ion()
        fig = plt.figure()

        #plt.switch_backend('TkAgg') #TkAgg (instead Qt4Agg)
        #print('#1 Backend:',plt.get_backend())
        ax1 = fig.add_subplot(321, xlim = (X_Arr.min(),X_Arr.max()), ylim = (Q_Arr.min(), Q_Arr.max()))
        #ax1 = fig.add_subplot(321)
        ax1.grid(True, color='k')   
        ax1.plot(X_Arr, Q_Arr, label ="Flow rate" , color = "c", linewidth = 2.0)

        #plt.title("SOLUTION: Water flow"+Title, fontsize = 16)
        plt.title("Solution "+Title, fontsize = 16)
        #plt.xlabel("Distance (m)",          fontsize=12)
        plt.ylabel("Flow rate (m^3/s)",     fontsize=12)

        ax2 = fig.add_subplot(322, xlim = (X_Arr.min(),X_Arr.max()), ylim = (V_Arr.min(), V_Arr.max()))
        #ax2 = fig.add_subplot(322)
        ax2.grid()
        ax2.plot(X_Arr, V_Arr, label ="Control Volume" , color = "c", linewidth = 2.0)

        #plt.title("SOLUTION: Control Volume"+Title, fontsize = 16)
        #plt.xlabel("Distance (m)",              fontsize=12)
        plt.ylabel("Contral Volume (m^3)",      fontsize=12)

        ax3 = fig.add_subplot(323, xlim = (X_Arr.min(),X_Arr.max()), ylim = (Z_Arr.min(), Eta_Arr.max()))
        #ax3 = fig.add_subplot(323)
        ax3.grid()
        ax3.plot(X_Arr, Eta_Arr, label ="Water Elevation" ,  color = "c", linewidth = 2.0)
        ax3.plot(X_Arr, Z_Arr,   label ="Bottom Elevation" , color = "r", linewidth = 2.0)
        ax3.legend()

        #plt.title("SOLUTION: Water Elevation"+Title, fontsize = 16)
        #plt.xlabel("Distance (m)", fontsize=12)
        plt.ylabel("Elevation (m)", fontsize=12)
        #plt.legend(loc=0)

        ax4 = fig.add_subplot(324, xlim = (X_Arr.min(),X_Arr.max()), ylim = (U_Arr.min(), U_Arr.max()))
        #ax4 = fig.add_subplot(324)
        ax4.grid()
        ax4.plot(X_Arr, U_Arr, label ="Velocity" , color = "c", linewidth = 2.0)

        #plt.title("SOLUTION: Water Velocity"+Title, fontsize = 16)
        #plt.xlabel("Distance (m)", fontsize=12)
        plt.ylabel("Velocity (m/s)", fontsize=12)

        ax5 = fig.add_subplot(325, xlim = (X_Arr.min(),X_Arr.max()), ylim = (E_Arr.min(), E_Arr.max()))
        #ax5 = fig.add_subplot(325)
        ax5.grid()
        ax5.plot(X_Arr, E_Arr, label ="Energy" , color = "c", linewidth = 2.0)

        #plt.title("SOLUTION: Energy"+Title,   fontsize = 16)
        plt.xlabel("Distance (m)",  fontsize=12)
        plt.ylabel("Energy (m/s)",  fontsize=12)        

        ax6 = fig.add_subplot(326, xlim = (X_Arr.min(),X_Arr.max()), ylim = (A_Arr.min(), A_Arr.max()))
        #ax6 = fig.add_subplot(326)
        ax6.grid()
        ax6.plot(X_Arr, A_Arr, label ="Area" , color = "c", linewidth = 2.0)

        #plt.title("SOLUTION: Area"+Title,   fontsize = 16)
        plt.xlabel("Distance (m)",  fontsize=12)
        plt.ylabel("Area (m^2)",  fontsize=12)


        #mng = plt.get_current_fig_manager()
        #mng.resize(*mng.window.maxsize())

        #plt.pause(0.01)
        #plt.draw
        #plt.show(block=False) # <modify> See why the execution stops when the the command gets here. 
        plt.show() # <modify> See why the execution stops when the the command gets here. 
        FileName = T1 +'.jpg'
        #plt.savefig(FileName)
        #savefig(fname, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None)
        #plt.close(fig)  


    # This function plots the results at the cell center and at the faces, simultaneously.
    @staticmethod
    def Plot_Full_Results(iii, N, X, X_F, Z_F, V, Q, Q_F, Eta, Eta_F, U, U_F, E, E_F, A, A_F, T1,T2):
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.ticker as tkr
       
        Q_Arr   = np.zeros(N*2+1, dtype = np.float64)
        V_Arr   = np.zeros(N,     dtype = np.float64)
        Eta_Arr = np.zeros(N*2+1, dtype = np.float64)
        U_Arr   = np.zeros(N*2+1, dtype = np.float64)
        E_Arr   = np.zeros(N*2+1, dtype = np.float64)
        X_Arr   = np.zeros(N*2+1, dtype = np.float64)
        X_cell  = np.zeros(N,     dtype = np.float64)
        Z_Arr   = np.zeros(N*2+1, dtype = np.float64)
        A_Arr   = np.zeros(N*2+1, dtype = np.float64)

        Title      = T2
        X_Arr[:]   = X_F[:]
        Z_Arr[:]   = Z_F[:]
        V_Arr[:]   = V[:]
        X_cell[:]  = X[:]

        for ii in range(N):
            Q_Arr[ii*2]    = Q_F[ii]
            Q_Arr[ii*2+1]  = Q[ii]

            Eta_Arr[ii*2]  = Eta_F[ii]
            Eta_Arr[ii*2+1]= Eta[ii]

            U_Arr[ii*2]    = U_F[ii]
            U_Arr[ii*2+1]  = U[ii]
            
            E_Arr[ii*2]    = E_F[ii]
            E_Arr[ii*2+1]  = E[ii]

            A_Arr[ii*2]    = A_F[ii]
            A_Arr[ii*2+1]  = A[ii]

        Q_Arr[N*2]    = Q_F[N]
        Eta_Arr[N*2]  = Eta_F[N]
        U_Arr[N*2]    = U_F[N]
        E_Arr[N*2]    = E_F[N]
        A_Arr[N*2]    = A_F[N]

        fig = plt.figure(iii)

        ax1 = fig.add_subplot(321, xlim = (X_Arr.min(),X_Arr.max()), ylim = (Q_Arr.min(),Q_Arr.max()))
        #ax1 = fig.add_subplot(321)
        ax1.grid()
        ax1.plot(X_Arr, Q_Arr, label ="Flow rate" , color = "c", linewidth = 2.0)

        plt.title(Title, fontsize = 16)
        #plt.xlabel("Distance (m)",          fontsize=12)
        plt.ylabel("Flow rate (m^3/s)",     fontsize=12)

        ax2 = fig.add_subplot(322, xlim = (X_cell.min(),X_cell.max()), ylim = (V_Arr.min(),V_Arr.max()))
        #ax2 = fig.add_subplot(322)
        ax2.grid()
        ax2.plot(X_cell, V_Arr, label ="Control Volume (V)" , color = "c", linewidth = 2.0)

        #plt.title("Water Velocity (U)"+Title, fontsize = 16)
        #plt.xlabel("Distance (m)", fontsize=12)
        plt.ylabel("Control Volume (m^3)", fontsize=12)

        ax3 = fig.add_subplot(323, xlim = (X_Arr.min(),X_Arr.max()), ylim = (Z_Arr.min(), Eta_Arr.max()))
        #ax3 = fig.add_subplot(323)
        ax3.grid()
        ax3.plot(X_Arr, Eta_Arr, label ="Water Elevation" ,  color = "c", linewidth = 2.0)
        ax3.plot(X_Arr, Z_Arr,   label ="Bottom Elevation" , color = "r", linewidth = 2.0)

        #plt.title(Title, fontsize = 16)
        #plt.title("Water Elevation (Eta)"+Title, fontsize = 16)
        #plt.xlabel("Distance (m)", fontsize=12)
        plt.ylabel("Elevation (m)", fontsize=12)
        #plt.legend(loc=0)

        ax4 = fig.add_subplot(324, xlim = (X_Arr.min(),X_Arr.max()), ylim = (U_Arr.min(), U_Arr.max()))
        #ax4 = fig.add_subplot(324)
        ax4.grid()
        ax4.plot(X_Arr, U_Arr, label ="Velocity" , color = "c", linewidth = 2.0)

        #plt.title("SOLUTION: Water Velocity"+Title, fontsize = 16)
        #plt.xlabel("Distance (m)", fontsize=12)
        plt.ylabel("Velocity (m/s)", fontsize=12)

        ax5 = fig.add_subplot(325, xlim = (X_Arr.min(),X_Arr.max()), ylim = (E_Arr.min(), E_Arr.max()))
        #ax5 = fig.add_subplot(325)
        ax5.grid()
        ax5.plot(X_Arr, E_Arr, label ="Energy" , color = "c", linewidth = 2.0)

        #plt.title("Energy (E)"+Title,   fontsize = 16)
        plt.xlabel("Distance (m)",  fontsize=12)
        plt.ylabel("Energy (m/s)",  fontsize=12)

        ax6 = fig.add_subplot(326, xlim = (X_Arr.min(),X_Arr.max()), ylim = (A_Arr.min(), A_Arr.max()))
        #ax6 = fig.add_subplot(326)
        ax6.grid()
        ax6.plot(X_Arr, A_Arr, label ="Area" , color = "c", linewidth = 2.0)

        #plt.title("Area (A)"+Title,   fontsize = 16)
        plt.xlabel("Distance (m)",  fontsize=12)
        plt.ylabel("Area (m^2)",  fontsize=12)


        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())

        #plt.pause(0.01)
        #plt.draw
        plt.show(block=False) # <modify> See why the execution stops when the the command gets here. 
        #plt.show() # <modify> See why the execution stops when the the command gets here. 
        FileName = T1 +'.jpg'
        plt.savefig(FileName)
        #savefig(fname, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None)
        plt.close(fig)  


    @staticmethod
    def Plot_Domain(N, X, Z, T):
        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.ticker as ticker

        X_Arr = np.zeros(N, dtype = np.float64)
        Z_Arr = np.zeros(N, dtype = np.float64)

        Title = T
        X_Arr[:]   = X[:]
        Z_Arr[:]   = Z[:]

        fig, ax = plt.subplots()
        ax.plot(X_Arr, Z_Arr, label ="Domain" , color = "r", linewidth = 2.0)
        
        y_labels = ax.get_yticks()
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%15.13f'))
        plt.show()



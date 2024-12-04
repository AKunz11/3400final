class datareader:
    
    def __init__(self,path):
        self.path=path
        
    def get_data(self,lognum):
        logRG=m.MesaData(file_name=self.path+f'LOGS1/profile{lognum}.data')
        logWD=m.MesaData(file_name=self.path+f'LOGS2/profile{lognum}.data')
        binarydata = m.MesaData(file_name=self.path+'binary_history.data')
        return logRG,logWD,binarydata
    
    def plot_data(self,var1,var2,data_typ,plt_typ,lognum=8):
        '''
        This function does all the plotting and data gathering.
        
        Inputs:
        **ALL MUST BE IN STRINGS**
        var1=x variable
        var2=y variable
        data_typ=individual/binary
        plt_typ=type of plot (normal,loglog,semilogx,semilogy)
        lognum= which log files you wish to use
        
        Example:
        plot_data('zone','logT','individual','normal',lognum=3)
        logRG,logWD,binarydata=self.get_data(lognum)
        '''
        
        logRG,logWD,binarydata=self.get_data(lognum)
        
        if data_typ=='individual':
            xRG=logRG.data(var1)
            yRG=logRG.data(var2)

            xWD=logWD.data(var1)
            yWD=logWD.data(var2)
            
            if plt_typ=='normal':
                plt.plot(xRG,yRG)
                plt.plot(xWD,yWD)
                plt.xlabel(var1)
                plt.ylabel(var2)
            
            elif plt_typ=='loglog':
                plt.loglog(xRG,yRG)
                plt.loglog(xWD,yWD)
                plt.xlabel(var1)
                plt.ylabel(var2)
            
            elif plt_typ=='semilogx':
                plt.semilogx(xRG,yRG)
                plt.semilogx(xWD,yWD)
                plt.xlabel(var1)
                plt.ylabel(var2)
        
            elif plt_typ=='semilogy':
                plt.semilogy(xRG,yRG)
                plt.semilogy(xWD,yWD)
                plt.xlabel(var1)
                plt.ylabel(var2)
                
            else:
                print('Unsupported plot type')
            
        if data_typ=='binary':
            bin_x=binarydata.data(var1)
            bin_y=binarydata.data(var2)
        
            if plt_typ=='normal':
                plt.plot(bin_x,bin_y)
                plt.xlabel(var1)
                plt.ylabel(var2)

            elif plt_typ=='loglog':
                plt.loglog(bin_x,bin_y)
                plt.xlabel(var1)
                plt.ylabel(var2)

            elif plt_typ=='semilogx':
                plt.semilogx(bin_x,bin_y)
                plt.xlabel(var1)
                plt.ylabel(var2)

            elif plt_typ=='semilogy':
                plt.semilogy(bin_x,bin_y)
                plt.xlabel(var1)
                plt.ylabel(var2)

            else:
                print('Unsupported plot type')
        
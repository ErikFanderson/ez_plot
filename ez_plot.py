#!/usr/bin/env python3
import matplotlib as mpl
#mpl.interactive(True)
import matplotlib.pyplot as plt
import numpy as np
import json
import sys

def returnEZ_Data():
    '''
    Returns dictionary with all proper fields initialized
    '''
    data = {}
    data["title"] = "Default Title"
    data["xlabel"] = "Default Xlabel"
    data["ylabel"] = "Default Ylabel"
    data["rcparams"] = {}
    return data

if __name__ == '__main__':
    try:
        for filename in sys.argv[1:]:
            #Load JSON
            with open(filename,'r') as fp:
                data = json.load(fp)
            #Data
            try: 
                with mpl.rc_context(data["rcparams"]):
                    plt.plot(data['xdata'],data['ydata'])
            except KeyError:
                print("No Data!")
            #Create Figure
            axis = plt.gca()
            #Title
            try: 
                axis.set_title(data['title'])
            except KeyError:
                pass
            #Axis Labels
            try: 
                axis.set_xlabel(data['xlabel'])
            except KeyError:
                pass
            try: 
                axis.set_ylabel(data['ylabel'])
            except KeyError:
                pass
        plt.show()
    except IndexError:
        print("No Filename/s Given!")


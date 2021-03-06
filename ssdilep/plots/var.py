# encoding: utf-8
'''
var.py
description:

'''

## modules


# - - - - - - - - - - - class defs  - - - - - - - - - - - - #
#------------------------------------------------------------
class Var(object):
    '''
    class to hold variable info for plotting
    '''
    #________________________________________________________
    def __init__(self,
            name,
            hname = None,
            title = None,
            path  = None,
            rebin = None,
            rebinVar = [],
            xmin  = None,
            xmax  = None,
            ymin  = None,
            ymax  = None,     
            log   = None,
            logx  = None,
            ):
        self.name = name
        if not title: title = name
        if not hname: 
          if "cutflow" in name: hname = name
          else: hname = 'h_'+name
        self.hname = hname
        self.title = title
        self.path  = path
        self.rebin = rebin
        self.rebinVar = rebinVar
        self.xmin  = xmin
        self.xmax  = xmax
        self.ymin  = ymin
        self.ymax  = ymax
        self.log   = log
        self.logx  = logx



## EOF

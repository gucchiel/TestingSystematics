## modules
import ROOT

import histmgr
import funcs
import os

from ssdilep.samples import samples, samples_DCH
from ssdilep.plots   import vars_mumu
from ssdilep.plots   import vars
from systematics     import *

from optparse import OptionParser


#-----------------
# input
#-----------------
parser = OptionParser()
parser.add_option('-v', '--var', dest='vname',
                  help='varable name',metavar='VAR',default=None)
parser.add_option('-r', '--reg', dest='region',
                  help='region name',metavar='REG',default=None)
parser.add_option('-l', '--lab', dest='label',
                  help='region label',metavar='LAB',default=None)
parser.add_option('-c', '--icut', dest='icut',
                  help='number of cuts',metavar='ICUT',default=None)
parser.add_option('-p', '--makeplot', dest='makeplot',
                  help='make plot',metavar='MAKEPLOT',default=None)
parser.add_option('-i', '--input', dest='indir',
                  help='input directory',metavar='INDIR',default=None)
parser.add_option('-o', '--output', dest='outdir',
                  help='output directory',metavar='OUTDIR',default=None)
parser.add_option('-f', '--fakest', dest='fakest',
                  help='choose fake estimate',metavar='FAKEST',default=None)
parser.add_option('-t', '--tag', dest='tag',
                  help='outfile tag',metavar='TAG',default=None)
parser.add_option('-R', '--rebinToEq', dest='rebinToEq',
                  help='rebinToEq',metavar='REBINTOEQ',default=None)
parser.add_option('-V', '--varName', dest='varName',
                  help='varName',metavar='VARNAME',default=None)
parser.add_option('-L', '--logy', dest='logy',
                  help='logy',metavar='LOGY',default=None)

(options, args) = parser.parse_args()

#-----------------
# Configuration
#-----------------
#lumi =  18232.8
lumi =  36074.56
#lumi =  33257.2 + 3212.96
#lumi =  33257.2 #+ 3212.96

# Control regions
plotsfile = []
if options.makeplot == "False":
  plotsfile.append("hists")
plotsfile.append(options.vname)
plotsfile.append(options.region)
plotsfile.append(options.tag)

for s in plotsfile:
  if not s: plotsfile.remove(s)

plotsfile = "_".join(plotsfile)+".root"
plotsfile = os.path.join(options.outdir,plotsfile)

ROOT.gROOT.SetBatch(True)
hm = histmgr.HistMgr(basedir=options.indir,target_lumi=lumi)

#-----------------
# Samples        
#-----------------

# base samples
data    = samples.data
mc_bkg  = samples.mc_bkg
fakes   = samples.fakes

# recombined samples
recom_data     = data.copy()
recom_mc_bkg  = [ b.copy() for b in mc_bkg ]

## signals
signals = []
#signals.append(samples.all_DCH)
#signals.append(samples.DCH800)

#signals.append(samples_DCH.DCH300_HLEpMp_HLEmMm)
#signals.append(samples_DCH.DCH300_HLMpMp_HLEmMm)
#signals.append(samples_DCH.DCH300_HLEpMp_HLEmMm)
#signals.append(samples_DCH.DCH500_HLEpMp_HLEmMm)
"""
signals.append(samples_DCH.DCH250_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH300_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH350_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH400_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH500_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH550_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH600_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH650_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH700_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH750_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH800_HLEpMp_HLEmMm)
signals.append(samples_DCH.DCH850_HLEpMp_HLEmMm)
"""
#signals.append(samples_DCH.DCH900_HLEpMp_HLEmMm)
#signals.append(samples_DCH.DCH1000_HLEpMp_HLEmMm)
#signals.append(samples_DCH.DCH500_HLEpMp_HLEmEm)
#signals.append(samples_DCH.DCH500_HLEpMp_HLMmMm)
#signals.append(samples_DCH.DCH700_HLEpMp_HLEmMm)
#signals.append(samples_DCH.DCH800_HLEpMp_HLEmMm)
#signals.append(samples_DCH.DCH900_HLEpMp_HLEmMm)
#signals.append(samples_DCH.DCH1000_HLEpMp_HLEmMm)
#signals.append(samples_DCH.DCH1200_HLEpMp_HLEmMm)
#signals.append(samples_DCH.DCH500_HLEpMp_HLEmMm)
#signals.append(samples_DCH.DCH300_HLEpMp_HLEmMm)

recom_signals  = [ s.copy() for s in signals ]

#--------------
# Estimators
#--------------
for s in mc_bkg + signals + [data]: 
    histmgr.load_base_estimator(hm,s)

main_addition_regions    = []
fake_addition_regions    = []
fake_subtraction_regions = []

reg_prefix, reg_suffix = funcs.get_pref_and_suff(options.region)

if reg_suffix == "MAINREG" or "TESTING":
  
  # including all regions for fake-factor method
  # ---------------------------------------------
  if options.fakest == "AllRegions":
    main_addition_regions = ["TT","TTT","TTTT"]
    
    fake_addition_regions = []
    fake_addition_regions += ["TL","LT"]
    fake_addition_regions += ["TTL","TLT","LTT"]
    fake_addition_regions += ["LLL"]
    fake_addition_regions += ["TTTL","TTLT","TLTT","LTTT"]

    fake_subtraction_regions = []
    fake_subtraction_regions += ["LL"]
    fake_subtraction_regions += ["LLT","LTL","TLL"]
  
  # only two lepton regions
  # ---------------------------------------------
  if options.fakest == "TwoLepRegions":
    
    main_addition_regions    = ["TT"]
    fake_addition_regions    = ["TL","LT"]
    fake_subtraction_regions = ["LL"]

  # only three lepton regions
  # ---------------------------------------------
  if options.fakest == "ThreeLepRegions":
    
    main_addition_regions = ["TTT"]
    
    fake_addition_regions = []
    fake_addition_regions += ["TTL","TLT","LTT"]
    fake_addition_regions += ["LLL"]

    fake_subtraction_regions = []
    fake_subtraction_regions += ["LLT","LTL","TLL"]

  if options.fakest== "FourLepRegions":
    main_addition_regions = ["TTTT"]
    
    fake_addition_regions = []
    fake_addition_regions += ["TTTL","TTLT","LTTT","TLTT"]

    fake_subtraction_regions = []
    fake_subtraction_regions += ["LLTT","LTTL","TLLT","TTLL","TLTL","LTLT"]

else:
  
  if options.fakest == "Subtraction":
    main_addition_regions =  fake_addition_regions = ["TTTT"]
    reg_prefix            =  options.region

"""
fakes.estimator = histmgr.AddRegEstimator(
      hm                  = hm, 
      sample              = fakes,
      data_sample         = data,
      mc_samples          = mc_bkg, 
      addition_regions    = ["_".join([reg_prefix]+[suffix]).rstrip("_") for suffix in fake_addition_regions],
      subtraction_regions = ["_".join([reg_prefix]+[suffix]).rstrip("_") for suffix in fake_subtraction_regions]
      )
"""
for s in recom_mc_bkg + recom_signals + [recom_data]:
  s.estimator = histmgr.AddRegEstimator(
      hm               = hm, 
      sample           = s,
      data_sample      = data,
      mc_samples       = mc_bkg + signals, 
      addition_regions = ["_".join([reg_prefix]+[suffix]).rstrip("_") for suffix in main_addition_regions]
      )

#-----------------
# Systematics       
#-----------------
# just an example ...
mc_sys = [
    SYS1, 
    SYS2,
    ]

## set mc systematics
#for s in mc_bkg + signals:
#    s.estimator.add_systematics(mc_sys)

#fakes.estimator.add_systematics(FF)

mumu_vdict  = vars.vars_dict

#-----------------
# Plotting 
#-----------------

## order backgrounds for plots
plot_ord_bkg = []
#plot_ord_bkg.append( fakes )
plot_ord_bkg += recom_mc_bkg


if options.makeplot == "True":
 funcs.plot_hist(
    backgrounds   = plot_ord_bkg,
    signal        = recom_signals, 
    data          = recom_data,
    region        = options.region,
    label         = options.label,
    histname      = os.path.join(mumu_vdict[options.vname]['path'],mumu_vdict[options.vname]['hname']),
    xmin          = mumu_vdict[options.vname]['xmin'],
    xmax          = mumu_vdict[options.vname]['xmax'],
    rebin         = mumu_vdict[options.vname]['rebin'],
    rebinVar      = mumu_vdict[options.vname]['rebinVar'],
    log           = mumu_vdict[options.vname]['log'],
    icut          = int(options.icut),
    #sys_dict      = sys_dict,
    sys_dict      = None,
    do_ratio_plot = True,
    save_eps      = True,
    plotsfile     = plotsfile,
    )

else:
 funcs.write_hist(
         backgrounds = plot_ord_bkg,
         signal      = recom_signals, # This can be a list
         data        = recom_data,
         region      = options.region,
         icut        = int(options.icut),
         histname    = os.path.join(mumu_vdict[options.vname]['path'],mumu_vdict[options.vname]['hname']),
         rebin       = mumu_vdict[options.vname]['rebin'],
         rebinVar    = mumu_vdict[options.vname]['rebinVar'],
         sys_dict    = None, #sys_dict if DO_SYS else None,
         outname     = plotsfile,
         regName     = options.tag,
         rebinToEq   = True if options.rebinToEq=="True" else False,
         varName     = str(options.varName)
         )
 ## EOF




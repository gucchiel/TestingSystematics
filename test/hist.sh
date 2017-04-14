#!/bin/bash

## Batch

#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/EXOT12_common_v1Ntuples/merged/nominal"
INPATH="/coepp/cephfs/mel/fscutti/ssdilep/EXOT12_common_v3Ntuples/merged/nominal"
#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/EXOT12_common_v3Signal/merged/nominal"
#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/EXOT12_common_v2Ntuples/nominal"
#INPATH="/coepp/cephfs/mel/fscutti/ssdilep/HIGG3D3_v8/merged/nominal"

INSCRIPT="../ssdilep/run"

#SCRIPT="j.plotter_FF.py"
#SCRIPT="j.plotter_SR2.py"
#SCRIPT="j.plotter_FF_TMP.py"
#SCRIPT="j.plotter_STUDY.py"
#SCRIPT="j.plotter_VR_OneMuPair.py"
#SCRIPT="j.plotter_TAndP.py"
#SCRIPT="j.plotter_CRele_ttbar.py"
SCRIPT="j.plotter_SR1_MuMu.py"

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00280273.root --sampletype="data"  #--events=20000
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00302393.root --sampletype="data"  --events=20000

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00282992.root --sampletype="data" --events=20000 #--config="sys:FF_DN"
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00302380.root --sampletype="data" --events=200000 #--config="sys:FF_DN" # example of triglist probs
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00302380.root --samplename="physics_Main_00302380" --sampletype="data" --events=2000 #--config="sys:FF_DN" # example of triglist probs

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/physics_Main_00299243.root --sampletype="data" #--config="sys:FF_DN" # example of triglist probs
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_NNPDF30NNLO_Wmunu_Pt0_70_CVetoBVeto.root --sampletype="mc" --events=20000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_BFilter.root  --sampletype="mc" --events=4000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_CT10_VV_muvmuv_2000M3000.root  --sampletype="mc" --events=20000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_CT10_llvv.root  --sampletype="mc" --events=20000   #--config="sys:FF_DN" 

#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_DCH800.root  --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_DCH800_HLMpMp_HLMmMm" --events=10000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_DCH800.root  --sampletype="mc" --samplename="Pythia8EvtGen_A14NNPDF23LO_DCH800_HRMpMp_HRMmMm" --events=10000   #--config="sys:FF_DN" 

python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Sherpa_CT10_ggllll.root  --sampletype="mc" --samplename="Sherpa_CT10_ggllll" --events=10000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ0W.root  --sampletype="mc" #--events=4000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.root --sampletype="mc" --events=20000   #--config="sys:FF_DN" 
#python ${INSCRIPT}/${SCRIPT} --input ${INPATH}/PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.root --samplename="PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad" --sampletype="mc" --events=2000   #--config="sys:FF_DN" 

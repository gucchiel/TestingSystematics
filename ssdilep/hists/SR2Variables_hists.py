from histconfig import *


hist_list = []


# -------
# event
# -------
hist_list.append(h_averageIntPerXing)
hist_list.append(h_actualIntPerXing)
#hist_list.append(h_correct_mu)
hist_list.append(h_NPV)
hist_list.append(h_nmuons)
hist_list.append(h_nelectrons)
hist_list.append(h_njets)
# -------
# electrons
# -------

# leptons
hist_list.append(h_lep1_pt)
hist_list.append(h_lep1_eta)
hist_list.append(h_lep1_phi)
hist_list.append(h_lep2_pt)
hist_list.append(h_lep2_eta)
hist_list.append(h_lep2_phi)
hist_list.append(h_lep3_pt)
hist_list.append(h_lep3_eta)
hist_list.append(h_lep3_phi)
hist_list.append(h_lep4_pt)
hist_list.append(h_lep4_eta)
hist_list.append(h_lep4_phi)

# -------
# MET
# -------
hist_list.append(h_met_clus_et)
hist_list.append(h_met_clus_phi)
hist_list.append(h_met_trk_et)
hist_list.append(h_met_trk_phi)
hist_list.append(h_met_clus_sumet)
hist_list.append(h_met_trk_sumet)

# -------
# Couples
# -------

hist_list.append(h_PosCouple_mVis)
hist_list.append(h_NegCouple_mVis)
hist_list.append(h_PosCouple_dR)
hist_list.append(h_NegCouple_dR)
hist_list.append(h_Couples_mVis)
hist_list.append(h_Couples_mVis)


# EOF







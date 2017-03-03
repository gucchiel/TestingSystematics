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
hist_list.append(h_elemu_chargeprod)
hist_list.append(h_elemu_dphi)
hist_list.append(h_elemu_deta)
hist_list.append(h_elemu_mVis)
hist_list.append(h_elemu_mTtot)

# -------
# electrons
# -------

# leading lep
hist_list.append(h_leplead_pt)
hist_list.append(h_leplead_eta)
hist_list.append(h_leplead_phi)
hist_list.append(h_leplead_trkd0)
hist_list.append(h_leplead_trkd0sig)
hist_list.append(h_leplead_trkz0)
hist_list.append(h_leplead_trkz0sintheta)
hist_list.append(h_leplead_ptvarcone30)

# subleading lep
hist_list.append(h_lepsublead_pt)
hist_list.append(h_lepsublead_eta)
hist_list.append(h_lepsublead_phi)
hist_list.append(h_lepsublead_trkd0)
hist_list.append(h_lepsublead_trkd0sig)
hist_list.append(h_lepsublead_trkz0)
hist_list.append(h_lepsublead_trkz0sintheta)
hist_list.append(h_lepsublead_ptvarcone30)

# -------
# MET
# -------
hist_list.append(h_met_clus_et)
hist_list.append(h_met_clus_phi)
hist_list.append(h_met_trk_et)
hist_list.append(h_met_trk_phi)
hist_list.append(h_met_clus_sumet)
hist_list.append(h_met_trk_sumet)


# EOF







import ROOT
from DataFormats.FWLite import Events, Handle

events = Events("/cmsuf/data/store/user/kshi/WpTo3l_ZpM45/crab_WpTo3l_ZpM45_PUMix/WpTo3l_ZpM45/191104_203006/0000/WpTo3l_ZpM45_MINIAODSIM_1.root")
handle = Handle('std::vector<reco::GenParticle>')
label = ("prunedGenParticles", "", "PAT")

for count, eventNum in enumerate(events):
   if count > 1: break #only for testing purposes; don't want all ~50,000 events to run on flawed code
   eventNum.getByLabel(label,handle)
   genParticles = handle.product()
   for p in genParticles:
      print "*********************Event #" + str(count) + ", Particle ID#:" + str(p.pdgId()) + "*********************"
      print "Number of Daughters = " +str(p.numberOfDaughters())
      print "Number of Mothers = " + str(p.numberOfMothers())
      print "Number of Source Candidate Ptrs = " + str(p.numberOfSourceCandidatePtrs())
      print "Charge Value = " + str(p.charge())
      print "Three Charge Value = " + str(p.threeCharge())
      print "Momentum Magnitude = " + str(p.p())
      print "Energy = " + str(p.energy())
      print "Transverse Energy = " + str(p.et())
      print "Transverse Energy Squared = " + str(p.et2())
      print "Mass = " + str(p.mass())
      print "Mass Squared = " + str(p.massSqr())
      print "Transverse Mass = " + str(p.mt())
      print "Transverse Mass Squared = " + str(p.mtSqr())
      print "Momentum X Coordinate = " + str(p.px())
      print "Momentum Y Coordinate = " + str(p.py())
      print "Momentum Z Coordinate = " + str(p.pz())
      print "Transverse Momentum = " + str(p.pt())
      print "Phi Value = " + str(p.phi())
      print "Theta Value = " + str(p.theta())
      print "Eta Value = " + str(p.eta())
      print "Rapidity Value = " + str(p.rapidity())
      print "Y Value = " + str(p.y()) #Note: Ask what y variable measures
      print "Velocity X Coordinate = " + str(p.vx())
      print "Velocity Y Coordinate = " + str(p.vy())
      print "Velocity Z Coordinate = " + str(p.vz())
     # print "dxy Value = " + str(p.dxy())
     # print "dz Value = " + str(p.dz()) #Note: Ask what dxy and dz variables measure; terminal thinks they don't exist
      print "Chi Squared = " + str(p.vertexChi2()) #Note: Ask for further clarification of variable meaning
      print "Degrees of Freedom = " + str(p.vertexNdof())
      print "Normalized Chi Squared = " + str(p.vertexNormalizedChi2())
      if p.longLived():
         print "Is long lived"
      if p.massConstraint():
         print "Mass constrains" #Note: May not be what the variable means. Ask for further clarification
      if p.hasMasterClone():
         print "Has a reference to a master clone"
      if p.hasMasterClonePtr():
         print "Has a ptr to a master clone"
      if p.isElectron():
         print "Is an electron"
      if p.isMuon():
         print "Is a muon"
      if p.isStandAloneMuon():
         print "Is a stand alone muon"
      if p.isGlobalMuon():
         print "Is a global muon"
      if p.isTrackerMuon():
         print "Is a tracker muon"
      if p.isCaloMuon():
         print "Is a calo muon" #Note: Ask what a calo muon is
      if p.isPhoton():
         print "Is a photon"
      if p.isConvertedPhoton():
         print "Is a converted photon"
      if p.isJet():
         print "Is a jet" 
      if p.isPromptFinalState():
         print "Is a prompt final state"
      if p.isDirectPromptTauDecayProductFinalState():
         print "Is a direct decay of a prompt tau and is a final state"
      if p.fromHardProcessFinalState():
         print "Is the final state direct descendant of a hard process particle"
      if p.isDirectHardProcessTauDecayProductFinalState():
         print "Is a direct decay product of a hard process tau and is a final state"

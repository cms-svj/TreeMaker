import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/040FD832-26EA-E811-9326-001E675A68BF.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/0447102A-50EA-E811-9DCD-001E675A6653.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/0E18796B-2AEA-E811-8661-001E67D80528.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/0E4C155F-70EA-E811-9D44-00266CFFBF84.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/1466083F-46EA-E811-86AB-A4BF01025B0D.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/16BEB408-94EA-E811-8573-001517F8083C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/1A42B154-46EA-E811-99EA-90B11C08AD7D.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/1ABF9BBE-47EA-E811-9539-001E67DDC119.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/2802E032-F8E9-E811-8415-001E67DDD348.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/28F87D8B-42EA-E811-949C-00266CFFBF4C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/2A599730-26EA-E811-B2F7-001E67A4069F.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/2C7CB299-1DEA-E811-9BF4-EC0D9A0B3340.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/2E3CFE6B-C9EA-E811-8B51-008CFA05206C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/322D0669-F3E9-E811-818E-0242507DC033.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/32A2EFC9-D3EA-E811-92BB-001E67DDC051.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/3817BBA1-65EA-E811-8ED6-00266CFFBC64.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/3AAC6AF5-F8E9-E811-9C96-00266CFFBED8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/4009967B-F3E9-E811-8225-AC1F6B1AF148.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/46B0845A-50EA-E811-B23B-001517F7F6A0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/489D1870-26EA-E811-88C3-001517F7F950.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/48A89D6F-A5EA-E811-95FD-00266CFFC7E4.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/50F99A6C-98EA-E811-95AE-AC1F6B1AF1CE.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/549BA16B-42EA-E811-A6FA-AC1F6B1B23BE.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/54FDC9A6-DBEA-E811-B794-001E67A3EF48.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/5E3418DE-47EA-E811-9026-001E67DDBEDA.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/62E941D8-F7E9-E811-A801-EC0D9A0B3330.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/644E199E-11EA-E811-82A5-1CC1DE0503C0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/680EC628-DEEA-E811-B60E-C4346BC08440.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/6CB90A5B-BDEA-E811-8588-90B11C04FE38.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/744254CE-47EA-E811-871B-001E67DFF4F6.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/74735446-26EA-E811-9A64-A4BF010298CF.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/76FC47B0-42EA-E811-A26E-001E67F33451.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/7A642CC9-33EA-E811-8181-A4BF0102A5F4.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/7E021365-4BEA-E811-BBF3-001E67A3EF48.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/82C55434-46EA-E811-86BF-001E67A3E8F9.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/883C88C8-42EA-E811-8423-024248422D99.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/884ECAE6-07EA-E811-A415-001517F7F5C8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/8AEEFE0F-3AEA-E811-8177-001E67A3F3DF.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/94CCA5DB-F3E9-E811-96FA-AC1F6B1B2358.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/98148C10-F6E9-E811-BC18-024263263008.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/9859D614-3AEA-E811-AA01-001E67A404B0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/ACAF733A-26EA-E811-9A87-A4BF0102A5F4.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/B87E44FF-41EA-E811-BEB0-AC1F6B1E30B2.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/BA3D9E0A-3AEA-E811-AC34-001E67A401B3.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/C2DEC3E2-47EA-E811-8C8D-A4BF0102572F.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/C63A10CA-04EA-E811-8693-001E67E5E8B6.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/C655BF7C-69EA-E811-BEC9-0026182FD77A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/CC67083F-46EA-E811-BEE0-A4BF01025B0D.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/D4141E56-0AEA-E811-BC01-00266CFFBFC0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/D6AB5645-26EA-E811-B017-001E675A659A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/DEEA9F69-26EA-E811-BA3F-001517F7F504.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/E881A337-81EA-E811-B83D-001E67D80528.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/EA1E381D-1DEA-E811-9237-001E67DDBFF7.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/028AE215-3DEA-E811-9D1C-00266CFF0ACC.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/04B2F7F2-89EA-E811-A561-00266CFFBC64.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/0EE6690B-58EA-E811-B4D7-0242460D078C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/123FEE9C-03EA-E811-973C-008CFAF554D2.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/12DFF912-41EA-E811-A54A-AC1F6B1AEFEC.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/14D41DF6-83EA-E811-B3DF-001E67A3EC00.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/1C5BBF74-2AEA-E811-BAE4-00266CFFBF88.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/323EB6B2-24EA-E811-907A-00266CFEFDE0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/3A7ABDFF-40EA-E811-B616-008CFAEEAD4C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/4498B232-19EA-E811-BB71-001E67F336A4.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/48844CD4-3DEA-E811-97F4-001E67F336EF.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/6A936411-67EA-E811-82C8-001517F7F950.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/7229A217-67EA-E811-8C28-001517FAB928.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/8493DAA9-5CEA-E811-9FCE-AC1F6B1AEFEC.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/8AC76C4A-40EA-E811-8701-008CFAEEACDC.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/9EA15CA4-1CEA-E811-8BA5-00266CFFBF64.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/B2455F02-04EA-E811-8D24-AC1F6B1B23BE.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/BE6114DB-61EA-E811-B0F5-00266CFFC7E0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/C284CB13-96EA-E811-89C0-001E67DDC24A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/CA3A7615-27EA-E811-A1C9-AC1F6B1B23BE.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/CC1FAEDC-C2EA-E811-A3B7-EC0D9A0B3340.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/F6C0C9B4-A4EA-E811-B9FE-EC0D9A0B32F0.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/FC2D8837-F5EA-E811-8270-AC1F6B1AF144.root',
] )
import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/064/00000/D633D3A1-EE76-E711-B3B0-02163E0138C8.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/079/00000/E8DB2AA6-0077-E711-8CF2-02163E019CDD.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/087/00000/70B7998F-2677-E711-849E-02163E014777.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/101/00000/C04A7920-0F77-E711-8BBF-02163E0145E3.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/104/00000/220793BE-1077-E711-85EB-02163E0118F7.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/105/00000/B01979E1-1677-E711-A595-02163E019B9B.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/106/00000/F2AB3D20-3A77-E711-9287-02163E012704.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/107/00000/0AED47DF-4977-E711-9F3B-02163E01426E.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/117/00000/6C47D1B9-3377-E711-B95B-02163E01A1D9.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/122/00000/68CA9227-7B77-E711-B7D9-02163E011D52.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/122/00000/68EB9AA0-7477-E711-975B-02163E0144FE.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/122/00000/D2E789EA-6677-E711-ABAE-02163E01A540.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/122/00000/E08C7772-6B77-E711-A0EB-02163E01A62E.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/122/00000/F852F4B5-6377-E711-83E7-02163E019B58.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/123/00000/12D667A9-6E77-E711-B280-02163E013523.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/123/00000/1402977F-7777-E711-B1BA-02163E019D88.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/124/00000/5AF95092-9077-E711-AFDD-02163E011F50.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/155/00000/2ADDAFCC-D977-E711-AB92-02163E011926.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/155/00000/A42CFC55-C277-E711-A5B5-02163E019DD2.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/155/00000/AA126423-CE77-E711-9C8B-02163E013735.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/155/00000/C8887327-C777-E711-A957-02163E01A28B.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/156/00000/880D4A60-C377-E711-BBF2-02163E01A386.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/157/00000/0C80D40B-D877-E711-99AA-02163E014716.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/157/00000/16A1C425-EE77-E711-BDDD-02163E0133AF.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/226/00000/4470925F-EE77-E711-A348-02163E0139BB.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/226/00000/C47D6592-0078-E711-BDC4-02163E0144F1.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/233/00000/4AC16677-0578-E711-82B4-02163E019C55.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/234/00000/FEFD932F-0778-E711-8D29-02163E019B6A.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/235/00000/C288A0F6-0C78-E711-8752-02163E019E72.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/236/00000/84FE4D07-1278-E711-95A0-02163E01A49E.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/237/00000/104D89DD-3E78-E711-B4E6-02163E0142E1.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/237/00000/BAA6DC4E-3578-E711-855F-02163E011E64.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/237/00000/CCE4966D-4878-E711-810D-02163E014580.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/238/00000/685CABFC-4A78-E711-9429-02163E014772.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/239/00000/C0EFFA44-4F78-E711-BBF5-02163E014403.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/240/00000/AA050F5A-6278-E711-BB58-02163E0145AE.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/241/00000/70F7E4D8-4B78-E711-8757-02163E01A603.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/273/00000/C0665F30-BF78-E711-A59F-02163E01A61E.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/280/00000/34B1944E-1B79-E711-9B80-02163E0134D9.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/280/00000/BC753589-2F79-E711-AFDD-02163E0145C5.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/280/00000/E0093D04-2279-E711-AE3F-02163E019C0F.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/281/00000/4231256F-1879-E711-989D-02163E0133B0.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/282/00000/5AE241F1-3779-E711-9600-02163E014234.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/283/00000/982DA3DE-3C79-E711-A5E1-02163E01A66C.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/284/00000/76887667-5279-E711-B4E6-02163E019D9E.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/284/00000/9CFBD107-4A79-E711-A21E-02163E01A78B.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/308/00000/A803DBE6-5279-E711-8243-02163E01A629.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/309/00000/4CFF0018-5279-E711-8384-02163E013678.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/310/00000/D462DE8D-5979-E711-9A5E-02163E01A29F.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/312/00000/725B15BF-5F79-E711-86E5-02163E011825.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/313/00000/845C5649-6379-E711-A34A-02163E01A76E.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/314/00000/747E94E8-6479-E711-AC11-02163E012436.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/328/00000/CAAD3CE0-AD79-E711-901D-02163E01244B.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/364/00000/A09C379F-B97B-E711-BBEA-02163E0142EE.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/365/00000/D21159D6-BE7B-E711-95FC-02163E01A370.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/366/00000/A22B7A3B-9F7B-E711-B4B9-02163E019BE1.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/367/00000/D687F786-A07B-E711-B08D-02163E013595.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/368/00000/26A47AA9-A77B-E711-BF2F-02163E01A4BB.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/369/00000/3EB0429E-A37B-E711-8ED9-02163E01A3BE.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/370/00000/A0BBA068-B87B-E711-B166-02163E019D87.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/371/00000/46444F91-B27B-E711-B568-02163E019E12.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/372/00000/8C53DE78-AA7B-E711-9B2E-02163E01A6B7.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/373/00000/587F3CD2-0E7C-E711-ABB9-02163E014150.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/375/00000/3CC6B014-D37B-E711-818F-02163E019BAE.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/389/00000/325A65D6-E17B-E711-9E2D-02163E01A3C2.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/390/00000/BED65BF3-CA7B-E711-8F4B-02163E012987.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/391/00000/B05F7FF0-C07B-E711-8E10-02163E01A5E7.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/392/00000/6457DB62-C47B-E711-B81B-02163E019B4D.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/393/00000/72A00A6C-C67B-E711-9270-02163E0142D8.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/394/00000/38B7133B-C67B-E711-B533-02163E01A41F.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/395/00000/60634B28-DC7B-E711-A4ED-02163E01A63E.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/396/00000/E0AF4500-CF7B-E711-B501-02163E01A3BD.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/399/00000/B66B9FDA-D17B-E711-932D-02163E01A38E.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/400/00000/3AEBD5D0-E27B-E711-8399-02163E0121CB.root',
'/store/data/Run2017C/HTMHT/MINIAOD/PromptReco-v2/000/300/400/00000/D63DE05C-F97B-E711-85B2-02163E012987.root' ] );

import os

## need to replace these strings in the output
## WARNING: order is important -> substrings should go last !!!
mcstrings = []
mcstrings.append(["MadGraphPythia8EvtGen_A14NNPDF23LO_",""])
mcstrings.append(["Pythia8EvtGen_A14NNPDF23LO_",""])
mcstrings.append(["PowhegPy8EG_CT10nloME_AZNLOCTEQ6L1_",""])
mcstrings.append(["Sherpa_CT10_",""])
mcstrings.append(["PowhegPythiaEvtGen_P2012_",""])
mcstrings.append(["PowhegPythiaEvtGen_P2012CT10_",""])
mcstrings.append(["PowhegPythiaEvtGen_P2012radHi_",""])
mcstrings.append(["PowhegPythiaEvtGen_P2012radLo_",""])
mcstrings.append(["aMcAtNloHerwigppEvtGen_",""])

def recreplace(s=None,l=[]):
  ns = s
  for x in l: ns = ns.replace(x[0],x[1])
  return ns

def build_strings(isMC=True,channel=None,sample=None,type=None,rTag=None,pTag=None,ami=True,OUTTAG=None):
  
  dataset = []

  if isMC: dataset    += ["mc15_13TeV"]
  else:  dataset      += ["data15_13TeV"]
  if channel: dataset += [str(channel)]
  else: dataset       += ["*"]
  if sample: dataset  += ["*"+str(sample)+"*"]
  else: dataset       += ["*"]
  if type: dataset    += [str(type)]
  else: dataset       += ["*"]
  
  fname = filter(lambda i: i != "*", dataset)
  fname = "_".join(fname)
  fname = fname.replace("*","")

  string = ".".join(dataset)+"."
  
  if rTag: 
    assert isMC, "ERROR: rTag requested but sample is data"
    string += "*%s*" % rTag
    fname  +=  "_%s" % rTag
  if pTag: 
    string += "*%s*" % pTag
    fname  += "_%s" % pTag
  
  string += "*" 
  fname  += ".txt"
  
  # wildcarding in ami
  if ami:
    string = string.replace("*","%")
    while "%%" in string: string = string.replace("%%","%")
  
  if OUTTAG: fname = "_".join([OUTTAG,fname])
  
  return {"search_string":string,"file_name":fname}

{"filter":false,"title":"jsonFileHandler.py","tooltip":"/jsonFileHandler.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":11,"column":0},"end":{"row":35,"column":35},"action":"remove","lines":["import jsonFileHandler","","data = jsonFileHandler.readJsonFile('files/insulin.json')","","if data != \"\" :","    bInsulin = data['molecules']['bInsulin']","    aInsulin = data['molecules']['aInsulin']","    insulin = bInsulin + aInsulin","    molecularWeightInsulinActual = data['molecularWeightInsulinActual']","    print('bInsulin: ' + bInsulin)","    print('aInsulin: ' + aInsulin)","    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))","    # Calculating the molecular weight of insulin  ","    # Getting a list of the amino acid (AA) weights  ","    aaWeights = data['weights']","    # Count the number of each amino acids  ","    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  ","    # Multiply the count by the weights  ","    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in","    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  ","    print(\"The rough molecular weight of insulin: \" +","    str(molecularWeightInsulin))","    print(\"Percent error: \" + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))","else:","    print(\"Error. Exiting program\")"],"id":2}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":0},"end":{"row":11,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1636708906609,"hash":"4ad0da57ad80782a419cdc7fba689c9cebdf6be0"}
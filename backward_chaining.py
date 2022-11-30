factsKw=[['croaks','frog'],['eats flies','frog'],["frog","green"],
         ['chirp','canary'],['sing','canary'],["canary","yellow"]]
def check(str,factDb):
    facts=[]
    flag=True
    while flag==True:
        flag=False
        for txt in str:
            for A1 in factDb:
                if A1[1]==txt:
                    tmp=[A1[0],txt]
                    if not tmp in facts:
                        facts+=[tmp]
                        str+=[A1[0]]
                        flag=True
    return facts
result=check(['green'],factsKw)
print(result)
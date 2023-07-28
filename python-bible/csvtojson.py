import json

def csvtojson(csvstring):
    '''
    Input string is the form of k:v,k:v,...
    '''
    keyvaluepairs = csvstring.split(',')
    jsonOut = {}
    for pair in keyvaluepairs:
        key, value = pair.split(':')
        jsonOut[key] = value
    return   jsonOut



if __name__ == "__main__":
    testString1 = "a:b,c:d"
    testString2 = "a:b,c:d,e:f"
    jsonOut1 = csvtojson(testString1)
    print(jsonOut1["a"])
    jsonOut2 = csvtojson(testString2)
    print(jsonOut2)
   
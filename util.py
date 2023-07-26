import json

with open('response.json') as schema_file:
    response = json.load(schema_file)

with open('request.json') as source_file:
    request = json.load(source_file)

def map(responseDict, requestDict):
    keyValues = []
    keysTarget = []
    keysReference = []
    result = request.copy() 

    def searchTree(dictionary, callback):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                searchTree(value, callback)
            else:
                callback(key, value)

    def listKey(key, value):
        if isinstance(value, dict):
            pass
        else:
            keyValues.append((key,value))

    def getReferenceKey(key, value):
        if isinstance(value, dict):
            pass
        else:
            keysReference.append(key)
    
    def getTargetKey(key, value):
        if isinstance(value, dict):
            pass
        else:
            keysTarget.append(key)
    
    def assignValue(key, value):
        if isinstance(value, dict):
            pass
        for i in keyValues:
            if i[0] == key:
                result[key] = i[1]
    
    searchTree(responseDict, getReferenceKey)
    searchTree(requestDict, getTargetKey)
    sliced = [x for x in keysTarget if x not in keysReference]

    if len(sliced) != 0:
        message = ", "
        # print("data kurang lengkap:" + message.join(sliced))
        return

    # print(len(sliced))

    searchTree(responseDict, listKey)
    searchTree(requestDict, assignValue)

    return result

# print(map(response,request))
import json 
 
 
def beautiful_json(jsonStr): 
    data = json.dumps(jsonStr, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False) 
    return data 
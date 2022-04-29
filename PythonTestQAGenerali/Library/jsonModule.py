import json

def read_file_content(filePath):
    """
    filePath: dir with full path to json file
    return data as json object
    """
    file_data = open(filePath, 'r')
    return json.loads(file_data.read())


def remove_element_from_content(elementToRemove, inputFilePath, outputfilePath):
    """
    2. Create a python method that takes a json element
       as an argument, and removes that element from test_payload.json.
       Please verify that the method can remove either nested or non-nested elements
        (try removing "outParams" and "appdate").
       Please write the modified json to a new file.
    """
    json_input = read_file_content(inputFilePath)
    json_out = {}
    for k, v in json_input.items():
        if k != elementToRemove:
            json_out[k] = v

    with open(outputfilePath, "w") as outfile:
        json.dump(json_out, outfile)

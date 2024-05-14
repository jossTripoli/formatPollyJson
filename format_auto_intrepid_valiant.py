import json

def format_strings_to_json():
    intrepid_string = '''
{"time":3055,"type":"word","start":41,"end":45,"value":"Your"}
{"time":4242,"type":"word","start":65,"end":69,"value":"here"}
{"time":5122,"type":"word","start":71,"end":76,"value":"Below"}
{"time":5735,"type":"word","start":78,"end":84,"value":"you'll"}
{"time":5985,"type":"word","start":85,"end":89,"value":"find"}
{"time":6297,"type":"word","start":90,"end":97,"value":"options"}
{"time":6735,"type":"word","start":98,"end":100,"value":"to"}
{"time":6860,"type":"word","start":101,"end":107,"value":"either"}
{"time":7122,"type":"word","start":108,"end":114,"value":"retake"}
{"time":7547,"type":"word","start":115,"end":118,"value":"the"}
{"time":7672,"type":"word","start":119,"end":123,"value":"quiz"}
{"time":8272,"type":"word","start":125,"end":131,"value":"review"}
{"time":8572,"type":"word","start":132,"end":135,"value":"the"}
{"time":8710,"type":"word","start":136,"end":143,"value":"correct"}
{"time":9172,"type":"word","start":144,"end":151,"value":"answers"}
{"time":9747,"type":"word","start":153,"end":155,"value":"or"}
{"time":9922,"type":"word","start":156,"end":163,"value":"proceed"}
{"time":10297,"type":"word","start":164,"end":166,"value":"to"}
{"time":10447,"type":"word","start":167,"end":170,"value":"the"}
{"time":10547,"type":"word","start":171,"end":175,"value":"next"}
{"time":10835,"type":"word","start":176,"end":180,"value":"page"}
{"time":11835,"type":"word","start":176,"end":180,"value":"page"}
'''
    valiant_string = '''
{"time":2430,"type":"word","start":41,"end":45,"value":"Your"}
{"time":3430,"type":"word","start":65,"end":69,"value":"here"}
{"time":4222,"type":"word","start":71,"end":76,"value":"Below"}
{"time":4935,"type":"word","start":78,"end":84,"value":"you'll"}
{"time":5085,"type":"word","start":85,"end":89,"value":"find"}
{"time":5385,"type":"word","start":90,"end":97,"value":"options"}
{"time":5810,"type":"word","start":98,"end":100,"value":"to"}
{"time":5960,"type":"word","start":101,"end":107,"value":"either"}
{"time":6147,"type":"word","start":108,"end":114,"value":"retake"}
{"time":6547,"type":"word","start":115,"end":118,"value":"the"}
{"time":6622,"type":"word","start":119,"end":123,"value":"quiz"}
{"time":7272,"type":"word","start":125,"end":131,"value":"review"}
{"time":7585,"type":"word","start":132,"end":135,"value":"the"}
{"time":7672,"type":"word","start":136,"end":143,"value":"correct"}
{"time":8022,"type":"word","start":144,"end":151,"value":"answers"}
{"time":8697,"type":"word","start":153,"end":155,"value":"or"}
{"time":8810,"type":"word","start":156,"end":163,"value":"proceed"}
{"time":9235,"type":"word","start":164,"end":166,"value":"to"}
{"time":9335,"type":"word","start":167,"end":170,"value":"the"}
{"time":9422,"type":"word","start":171,"end":175,"value":"next"}
{"time":9672,"type":"word","start":176,"end":180,"value":"page"}
{"time":9772,"type":"word","start":176,"end":180,"value":"page"}

'''

    # INTREPID FORMATTING
    # Split the input string into individual JSON objects
    intrepid_data = [json.loads(line) for line in intrepid_string.strip().split('\n')]

    # Create a new list with modified elements
    formatted_data = [{"time": entry["time"],
                    "type": entry["type"],
                    "value": entry["value"],
                    "element": "narrate-1-page"} for entry in intrepid_data]

    # Create a dictionary with the new list
    formatted_json = {"intrepid": formatted_data}

    with open("second.json", "w", encoding="utf-8") as output_file:
        output_file.write('{"intrepid": [\n')
        for i, item in enumerate(formatted_json["intrepid"]):
            if i < len(formatted_json["intrepid"]) - 1:
                # Item not last, append comma
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
            else:
                # Last item, do not append comma
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
        output_file.write(']}\n')

    print("Formatted Intrepid JSON written to second.json")

    # VALIANT FORMATTING
    # Split the input string into individual JSON objects
    valiant_data = [json.loads(line) for line in valiant_string.strip().split('\n')]

    # Create a new list with modified elements
    formatted_data = [{"time": entry["time"],
                    "type": entry["type"],
                    "value": entry["value"],
                    "element": "narrate-1"} for entry in valiant_data]

    # Create a dictionary with the new list
    formatted_json = {"valiant": formatted_data}

    with open("third.json", "w", encoding="utf-8") as output_file:
        output_file.write('{"valiant": [\n')
        for i, item in enumerate(formatted_json["valiant"]):
            if i < len(formatted_json["valiant"]) - 1:
                # Item not last, append comma
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
            else:
                # Last item, do not append comma
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
        output_file.write(']}\n')

    print("Formatted Valiant JSON written to third.json")



# switch time and element
def switch_times_intrepid(first_json, second_json, intrepid_file):
    with open(first_json, 'r', encoding="utf-8") as file:
        data = json.load(file)

    with open(second_json, 'r', encoding="utf-8") as file:
        new_times = json.load(file)["intrepid"]

    for item, new_time in zip(data["daring"], new_times):
        item["time"] = new_time["time"]

    with open(intrepid_file, 'w', encoding="utf-8") as outfile:
        outfile.write('{"intrepid": [\n')

        # Write each item to the file, except the last, with a comma
        for item in data["daring"][:-1]:
            outfile.write(json.dumps(item, separators=(',', ': ')) + ',\n')
        # Write the last item without a comma
        if data["daring"]:  # Check if the list is not empty to avoid IndexError
            outfile.write(json.dumps(data["daring"][-1], separators=(',', ': ')))
        outfile.write('\n]}\n')

    # with open(intrepid_file, 'w', encoding="utf-8") as outfile:
    #     for item in data["daring"]:
    #         outfile.write(json.dumps(item, separators=(',', ': ')) + ',\n')

def switch_times_valiant(first_json, second_json, valiant_file):
    with open(first_json, 'r', encoding="utf-8") as file:
        data = json.load(file)

    with open(second_json, 'r', encoding="utf-8") as file:
        new_times = json.load(file)["valiant"]

    for item, new_time in zip(data["daring"], new_times):
        item["time"] = new_time["time"]

    # with open(valiant_file, 'w', encoding="utf-8") as outfile:
    #     for item in data["daring"]:
    #         outfile.write(json.dumps(item, separators=(',', ': ')) + ',\n')
 
    with open(valiant_file, 'w', encoding="utf-8") as outfile:
        outfile.write('{"valiant": [\n')

        # Write each item to the file, except the last, with a comma
        for item in data["daring"][:-1]:
            outfile.write(json.dumps(item, separators=(',', ': ')) + ',\n')
        # Write the last item without a comma
        if data["daring"]:  # Check if the list is not empty to avoid IndexError
            outfile.write(json.dumps(data["daring"][-1], separators=(',', ': ')))
            
        outfile.write('\n]}\n')

def main():
    # change strings into json
    format_strings_to_json()
    
    # Now
    # input files names
    first_json_file = "first.json"
    second_json_file = "second.json"
    third_json_file = "third.json"

    # output file names
    intrepid_json_file = "intrepid.json"
    valiant_json_file = "valiant.json"

    switch_times_intrepid(first_json_file, second_json_file, intrepid_json_file)

    print("Intrepid JSON written to " + intrepid_json_file)

    switch_times_valiant(first_json_file, third_json_file, valiant_json_file)

    print("Valiant JSON written to " + valiant_json_file)


if __name__ == "__main__":
    main()
import json

def format_strings_to_json():
    intrepid_string = '''
{"time":187,"type":"word","start":13,"end":21,"value":"Identity"}
{"time":712,"type":"word","start":22,"end":27,"value":"Theft"}
{"time":1000,"type":"word","start":28,"end":34,"value":"Basics"}
{"time":2255,"type":"word","start":48,"end":56,"value":"Identity"}
{"time":2780,"type":"word","start":57,"end":62,"value":"theft"}
{"time":3105,"type":"word","start":63,"end":65,"value":"is"}
{"time":3217,"type":"word","start":66,"end":70,"value":"when"}
{"time":3380,"type":"word","start":71,"end":75,"value":"your"}
{"time":3530,"type":"word","start":76,"end":84,"value":"personal"}
{"time":3942,"type":"word","start":85,"end":96,"value":"information"}
{"time":4580,"type":"word","start":97,"end":99,"value":"is"}
{"time":4705,"type":"word","start":100,"end":106,"value":"stolen"}
{"time":5192,"type":"word","start":107,"end":110,"value":"and"}
{"time":5330,"type":"word","start":111,"end":115,"value":"used"}
{"time":5567,"type":"word","start":116,"end":123,"value":"against"}
{"time":6017,"type":"word","start":124,"end":127,"value":"you"}
{"time":6897,"type":"word","start":141,"end":148,"value":"Example"}
{"time":7647,"type":"word","start":150,"end":153,"value":"Mr."}
{"time":8022,"type":"word","start":154,"end":161,"value":"Johnson"}
{"time":8485,"type":"word","start":162,"end":169,"value":"sharing"}
{"time":8835,"type":"word","start":170,"end":173,"value":"his"}
{"time":9085,"type":"word","start":174,"end":182,"value":"personal"}
{"time":9535,"type":"word","start":183,"end":187,"value":"info"}
{"time":10022,"type":"word","start":188,"end":192,"value":"over"}
{"time":10272,"type":"word","start":193,"end":196,"value":"the"}
{"time":10385,"type":"word","start":197,"end":202,"value":"phone"}
{"time":10660,"type":"word","start":203,"end":210,"value":"allowed"}
{"time":11022,"type":"word","start":211,"end":219,"value":"scammers"}
{"time":11522,"type":"word","start":220,"end":222,"value":"to"}
{"time":11647,"type":"word","start":223,"end":227,"value":"make"}
{"time":11947,"type":"word","start":228,"end":240,"value":"unauthorized"}
{"time":12585,"type":"word","start":241,"end":248,"value":"charges"}
'''
    valiant_string = '''
{"time":25,"type":"word","start":13,"end":21,"value":"Identity"}
{"time":425,"type":"word","start":22,"end":27,"value":"Theft"}
{"time":712,"type":"word","start":28,"end":34,"value":"Basics"}
{"time":1792,"type":"word","start":48,"end":56,"value":"Identity"}
{"time":2192,"type":"word","start":57,"end":62,"value":"theft"}
{"time":2580,"type":"word","start":63,"end":65,"value":"is"}
{"time":2730,"type":"word","start":66,"end":70,"value":"when"}
{"time":2867,"type":"word","start":71,"end":75,"value":"your"}
{"time":2955,"type":"word","start":76,"end":84,"value":"personal"}
{"time":3442,"type":"word","start":85,"end":96,"value":"information"}
{"time":3955,"type":"word","start":97,"end":99,"value":"is"}
{"time":4042,"type":"word","start":100,"end":106,"value":"stolen"}
{"time":4480,"type":"word","start":107,"end":110,"value":"and"}
{"time":4617,"type":"word","start":111,"end":115,"value":"used"}
{"time":4867,"type":"word","start":116,"end":123,"value":"against"}
{"time":5192,"type":"word","start":124,"end":127,"value":"you"}
{"time":5872,"type":"word","start":141,"end":148,"value":"Example"}
{"time":6635,"type":"word","start":150,"end":153,"value":"Mr."}
{"time":6935,"type":"word","start":154,"end":161,"value":"Johnson"}
{"time":7385,"type":"word","start":162,"end":169,"value":"sharing"}
{"time":7735,"type":"word","start":170,"end":173,"value":"his"}
{"time":7860,"type":"word","start":174,"end":182,"value":"personal"}
{"time":8322,"type":"word","start":183,"end":187,"value":"info"}
{"time":8647,"type":"word","start":188,"end":192,"value":"over"}
{"time":8797,"type":"word","start":193,"end":196,"value":"the"}
{"time":8885,"type":"word","start":197,"end":202,"value":"phone"}
{"time":9160,"type":"word","start":203,"end":210,"value":"allowed"}
{"time":9460,"type":"word","start":211,"end":219,"value":"scammers"}
{"time":9960,"type":"word","start":220,"end":222,"value":"to"}
{"time":10047,"type":"word","start":223,"end":227,"value":"make"}
{"time":10272,"type":"word","start":228,"end":240,"value":"unauthorized"}
{"time":10847,"type":"word","start":241,"end":248,"value":"charges"}
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
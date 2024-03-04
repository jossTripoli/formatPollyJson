import json

# input files names
first_json_file = "first.json"
second_json_file = "second.json"
third_json_file = "third.json"

# output file names
intrepid_json_file = "intrepid.json"
valiant_json_file = "valiant.json"

def format_strings_to_json():
    intrepid_string = '''
    {"time":187,"type":"word","start":13,"end":20,"value":"Reflect"}
    {"time":1380,"type":"word","start":34,"end":38,"value":"Take"}
    {"time":1567,"type":"word","start":39,"end":40,"value":"a"}
    {"time":1642,"type":"word","start":41,"end":47,"value":"moment"}
    {"time":2005,"type":"word","start":48,"end":50,"value":"to"}
    {"time":2130,"type":"word","start":51,"end":56,"value":"think"}
    {"time":2342,"type":"word","start":57,"end":62,"value":"about"}
    {"time":2630,"type":"word","start":63,"end":66,"value":"the"}
    {"time":2755,"type":"word","start":67,"end":76,"value":"following"}
    {"time":4727,"type":"word","start":92,"end":95,"value":"Can"}
    {"time":4902,"type":"word","start":96,"end":99,"value":"you"}
    {"time":5002,"type":"word","start":100,"end":106,"value":"recall"}
    {"time":5402,"type":"word","start":107,"end":108,"value":"a"}
    {"time":5527,"type":"word","start":109,"end":113,"value":"time"}
    {"time":5839,"type":"word","start":114,"end":118,"value":"when"}
    {"time":5964,"type":"word","start":119,"end":122,"value":"you"}
    {"time":6152,"type":"word","start":123,"end":129,"value":"shared"}
    {"time":6402,"type":"word","start":130,"end":141,"value":"information"}
    {"time":6977,"type":"word","start":142,"end":147,"value":"about"}
    {"time":7227,"type":"word","start":148,"end":156,"value":"yourself"}
    {"time":7714,"type":"word","start":157,"end":161,"value":"that"}
    {"time":7852,"type":"word","start":162,"end":165,"value":"you"}
    {"time":7977,"type":"word","start":166,"end":171,"value":"later"}
    {"time":8302,"type":"word","start":172,"end":181,"value":"regretted"}
    {"time":9444,"type":"word","start":183,"end":185,"value":"If"}
    {"time":9569,"type":"word","start":186,"end":188,"value":"so"}
    {"time":10007,"type":"word","start":190,"end":194,"value":"what"}
    {"time":10294,"type":"word","start":195,"end":203,"value":"happened"}
    {"time":11662,"type":"word","start":219,"end":224,"value":"Given"}
    {"time":11924,"type":"word","start":225,"end":229,"value":"what"}
    {"time":12099,"type":"word","start":230,"end":236,"value":"you've"}
    {"time":12287,"type":"word","start":237,"end":244,"value":"learned"}
    {"time":12537,"type":"word","start":245,"end":250,"value":"about"}
    {"time":12787,"type":"word","start":251,"end":255,"value":"what"}
    {"time":13037,"type":"word","start":256,"end":264,"value":"personal"}
    {"time":13474,"type":"word","start":265,"end":276,"value":"information"}
    {"time":14112,"type":"word","start":277,"end":285,"value":"scammers"}
    {"time":14599,"type":"word","start":286,"end":289,"value":"are"}
    {"time":14787,"type":"word","start":290,"end":295,"value":"after"}
    {"time":15362,"type":"word","start":297,"end":301,"value":"will"}
    {"time":15474,"type":"word","start":302,"end":307,"value":"there"}
    {"time":15662,"type":"word","start":308,"end":310,"value":"be"}
    {"time":15724,"type":"word","start":311,"end":312,"value":"a"}
    {"time":15849,"type":"word","start":313,"end":323,"value":"difference"}
    {"time":16274,"type":"word","start":324,"end":326,"value":"in"}
    {"time":16412,"type":"word","start":327,"end":331,"value":"what"}
    {"time":16549,"type":"word","start":332,"end":335,"value":"you"}
    {"time":16624,"type":"word","start":336,"end":340,"value":"will"}
    {"time":16849,"type":"word","start":341,"end":346,"value":"share"}
    {"time":17099,"type":"word","start":347,"end":353,"value":"online"}
    '''
    valiant_string = '''
    {"time":25,"type":"word","start":13,"end":20,"value":"Reflect"}
    {"time":1030,"type":"word","start":34,"end":38,"value":"Take"}
    {"time":1230,"type":"word","start":39,"end":40,"value":"a"}
    {"time":1267,"type":"word","start":41,"end":47,"value":"moment"}
    {"time":1592,"type":"word","start":48,"end":50,"value":"to"}
    {"time":1667,"type":"word","start":51,"end":56,"value":"think"}
    {"time":1880,"type":"word","start":57,"end":62,"value":"about"}
    {"time":2092,"type":"word","start":63,"end":66,"value":"the"}
    {"time":2167,"type":"word","start":67,"end":76,"value":"following"}
    {"time":4039,"type":"word","start":92,"end":95,"value":"Can"}
    {"time":4189,"type":"word","start":96,"end":99,"value":"you"}
    {"time":4289,"type":"word","start":100,"end":106,"value":"recall"}
    {"time":4664,"type":"word","start":107,"end":108,"value":"a"}
    {"time":4702,"type":"word","start":109,"end":113,"value":"time"}
    {"time":5064,"type":"word","start":114,"end":118,"value":"when"}
    {"time":5189,"type":"word","start":119,"end":122,"value":"you"}
    {"time":5277,"type":"word","start":123,"end":129,"value":"shared"}
    {"time":5602,"type":"word","start":130,"end":141,"value":"information"}
    {"time":6139,"type":"word","start":142,"end":147,"value":"about"}
    {"time":6402,"type":"word","start":148,"end":156,"value":"yourself"}
    {"time":6789,"type":"word","start":157,"end":161,"value":"that"}
    {"time":6952,"type":"word","start":162,"end":165,"value":"you"}
    {"time":7027,"type":"word","start":166,"end":171,"value":"later"}
    {"time":7302,"type":"word","start":172,"end":181,"value":"regretted"}
    {"time":8319,"type":"word","start":183,"end":185,"value":"If"}
    {"time":8444,"type":"word","start":186,"end":188,"value":"so"}
    {"time":9057,"type":"word","start":190,"end":194,"value":"what"}
    {"time":9207,"type":"word","start":195,"end":203,"value":"happened"}
    {"time":10287,"type":"word","start":219,"end":224,"value":"Given"}
    {"time":10587,"type":"word","start":225,"end":229,"value":"what"}
    {"time":10749,"type":"word","start":230,"end":236,"value":"you've"}
    {"time":10874,"type":"word","start":237,"end":244,"value":"learned"}
    {"time":11149,"type":"word","start":245,"end":250,"value":"about"}
    {"time":11374,"type":"word","start":251,"end":255,"value":"what"}
    {"time":11599,"type":"word","start":256,"end":264,"value":"personal"}
    {"time":12037,"type":"word","start":265,"end":276,"value":"information"}
    {"time":12549,"type":"word","start":277,"end":285,"value":"scammers"}
    {"time":13012,"type":"word","start":286,"end":289,"value":"are"}
    {"time":13162,"type":"word","start":290,"end":295,"value":"after"}
    {"time":13724,"type":"word","start":297,"end":301,"value":"will"}
    {"time":13837,"type":"word","start":302,"end":307,"value":"there"}
    {"time":13962,"type":"word","start":308,"end":310,"value":"be"}
    {"time":14137,"type":"word","start":311,"end":312,"value":"a"}
    {"time":14187,"type":"word","start":313,"end":323,"value":"difference"}
    {"time":14637,"type":"word","start":324,"end":326,"value":"in"}
    {"time":14737,"type":"word","start":327,"end":331,"value":"what"}
    {"time":14899,"type":"word","start":332,"end":335,"value":"you"}
    {"time":14987,"type":"word","start":336,"end":340,"value":"will"}
    {"time":15087,"type":"word","start":341,"end":346,"value":"share"}
    {"time":15374,"type":"word","start":347,"end":353,"value":"online"}
    '''

    # INTREPID FORMATTING
    # Split the input string into individual JSON objects
    intrepid_data = [json.loads(line) for line in intrepid_string.strip().split('\n')]

    # Create a new list with modified elements
    formatted_data_intrepid = [{"time": entry["time"],
                    "type": entry["type"],
                    "value": entry["value"],
                    "element": "narrate-1-page"} for entry in intrepid_data]

    # Create a dictionary with the new list
    global formatted_json_intrepid
    formatted_json_intrepid = {"intrepid": formatted_data_intrepid}
    

    with open("second.json", "w", encoding="utf-8") as output_file:
        output_file.write('{"intrepid": [\n')
        for i, item in enumerate(formatted_json_intrepid["intrepid"]):
            if i < len(formatted_json_intrepid["intrepid"]) - 1:
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
    formatted_data_valiant = [{"time": entry["time"],
                    "type": entry["type"],
                    "value": entry["value"],
                    "element": "narrate-1"} for entry in valiant_data]

    # Create a dictionary with the new list
    global formatted_json_valiant
    formatted_json_valiant = {"valiant": formatted_data_valiant}

    with open("third.json", "w", encoding="utf-8") as output_file:
        output_file.write('{"valiant": [\n')
        for i, item in enumerate(formatted_json_valiant["valiant"]):
            if i < len(formatted_json_valiant["valiant"]) - 1:
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

    with open(intrepid_file, 'w', encoding="utf-8") as output_file:
        output_file.write('{"intrepid": [\n')
        for i, item in enumerate(formatted_json_intrepid["intrepid"]):
            if i < len(formatted_json_intrepid["intrepid"]) - 1:
                # Item not last, append comma
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
            else:
                # Last item, do not append comma
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
        output_file.write(']}\n')
        
def switch_times_valiant(first_json, second_json, valiant_file):
    with open(first_json, 'r', encoding="utf-8") as file:
        data = json.load(file)

    with open(second_json, 'r', encoding="utf-8") as file:
        new_times = json.load(file)["valiant"]

    for item, new_time in zip(data["daring"], new_times):
        item["time"] = new_time["time"]

    with open(valiant_file, 'w', encoding="utf-8") as output_file:
        output_file.write('{"valiant": [\n')
        for i, item in enumerate(formatted_json_valiant["valiant"]):
            if i < len(formatted_json_valiant["valiant"]) - 1:
                # Item not last, append comma
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
            else:
                # Last item, do not append comma
                output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
        output_file.write(']}\n')



def main():
    # change strings into json
    format_strings_to_json()


    switch_times_intrepid(first_json_file, second_json_file, intrepid_json_file)

    print("Intrepid JSON written to " + intrepid_json_file)

    switch_times_valiant(first_json_file, third_json_file, valiant_json_file)

    print("Valiant JSON written to " + valiant_json_file)


if __name__ == "__main__":
    main()
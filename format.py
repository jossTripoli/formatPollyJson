import json

original_string = '''
{"time":1325,"type":"word","start":23,"end":27,"value":"The"}
{"time":1425,"type":"word","start":28,"end":37,"value":"Johnsons'"}
{"time":1912,"type":"word","start":38,"end":46,"value":"Identity"}
{"time":2300,"type":"word","start":47,"end":53,"value":"Stolen"}
{"time":3305,"type":"word","start":57,"end":62,"value":"Agent"}
{"time":3655,"type":"word","start":63,"end":70,"value":"Valiant"}
{"time":4042,"type":"word","start":71,"end":75,"value":"will"}
{"time":4192,"type":"word","start":76,"end":81,"value":"guide"}
{"time":4505,"type":"word","start":82,"end":85,"value":"you"}
{"time":4592,"type":"word","start":86,"end":93,"value":"through"}
{"time":4767,"type":"word","start":94,"end":97,"value":"the"}
{"time":4867,"type":"word","start":98,"end":105,"value":"Johnson"}
{"time":5305,"type":"word","start":106,"end":114,"value":"family's"}
{"time":5755,"type":"word","start":115,"end":124,"value":"encounter"}
{"time":6130,"type":"word","start":125,"end":129,"value":"with"}
{"time":6292,"type":"word","start":130,"end":138,"value":"identity"}
{"time":6680,"type":"word","start":139,"end":144,"value":"theft"}
{"time":7585,"type":"word","start":146,"end":151,"value":"Click"}
{"time":7797,"type":"word","start":152,"end":155,"value":"the"}
{"time":7960,"type":"word","start":156,"end":161,"value":"image"}
{"time":8222,"type":"word","start":162,"end":164,"value":"to"}
{"time":8310,"type":"word","start":165,"end":170,"value":"start"}
{"time":8610,"type":"word","start":171,"end":174,"value":"the"}
{"time":8672,"type":"word","start":175,"end":180,"value":"video"}
'''

# Split the input string into individual JSON objects
original_data = [json.loads(line) for line in original_string.strip().split('\n')]

# Create a new list with modified elements
formatted_data = [{"time": entry["time"],
                   "type": entry["type"],
                   "value": entry["value"],
                   "element": "narrate-1"} for entry in original_data]

# Create a dictionary with the new list
formatted_json = {"daring": formatted_data}

# with open("formatted_json.json", "w") as output_file:
#     json.dump(formatted_json, output_file, separators=(',', ':'))

# Write the formatted JSON to a new file with each item on a new line and a trailing comma
# with open("formatted_output.json", "w") as output_file:
#     output_file.write('{"daring": [\n')
#     for item in formatted_json["daring"]:
#         output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
#     output_file.write(']\n}\n')

with open("formatted_output.json", "w") as output_file:
    output_file.write('{"daring": [\n')
    for i, item in enumerate(formatted_json["daring"]):
        if i < len(formatted_json["daring"]) - 1:
            # Item not last, append comma
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
        else:
            # Last item, do not append comma
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
    output_file.write(']}\n')

print("Formatted JSON written to formatted_json.json")

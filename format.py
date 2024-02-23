import json

original_string = '''
{"time":25,"type":"word","start":13,"end":28,"value":"Congratulations"}
{"time":1492,"type":"word","start":42,"end":48,"value":"You've"}
{"time":1667,"type":"word","start":49,"end":58,"value":"completed"}
{"time":2092,"type":"word","start":59,"end":62,"value":"the"}
{"time":2167,"type":"word","start":63,"end":72,"value":"Challenge"}
{"time":2630,"type":"word","start":73,"end":76,"value":"and"}
{"time":2705,"type":"word","start":77,"end":83,"value":"earned"}
{"time":2867,"type":"word","start":84,"end":85,"value":"a"}
{"time":2905,"type":"word","start":86,"end":92,"value":"bronze"}
{"time":3292,"type":"word","start":93,"end":98,"value":"badge"}
{"time":4434,"type":"word","start":125,"end":128,"value":"You"}
{"time":4547,"type":"word","start":129,"end":133,"value":"have"}
{"time":4684,"type":"word","start":134,"end":136,"value":"an"}
{"time":4747,"type":"word","start":137,"end":145,"value":"Identity"}
{"time":5184,"type":"word","start":146,"end":151,"value":"Theft"}
{"time":5497,"type":"word","start":152,"end":162,"value":"Resilience"}
{"time":5934,"type":"word","start":163,"end":168,"value":"score"}
{"time":6209,"type":"word","start":169,"end":174,"value":"shown"}
{"time":6497,"type":"word","start":175,"end":179,"value":"here"}
{"time":7577,"type":"word","start":206,"end":208,"value":"To"}
{"time":7702,"type":"word","start":209,"end":214,"value":"build"}
{"time":8002,"type":"word","start":215,"end":219,"value":"your"}
{"time":8114,"type":"word","start":220,"end":230,"value":"resilience"}
{"time":8702,"type":"word","start":231,"end":234,"value":"and"}
{"time":8789,"type":"word","start":235,"end":239,"value":"earn"}
{"time":8939,"type":"word","start":240,"end":244,"value":"more"}
{"time":9139,"type":"word","start":245,"end":251,"value":"badges"}
{"time":9889,"type":"word","start":253,"end":261,"value":"continue"}
{"time":10327,"type":"word","start":262,"end":264,"value":"to"}
{"time":10439,"type":"word","start":265,"end":268,"value":"the"}
{"time":10527,"type":"word","start":269,"end":273,"value":"next"}
{"time":10764,"type":"word","start":274,"end":281,"value":"section"}
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
with open("formatted_output.json", "w") as output_file:
    output_file.write('{"daring": [\n')
    for item in formatted_json["daring"]:
        output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
    output_file.write(']\n}\n')

print("Formatted JSON written to formatted_json.json")

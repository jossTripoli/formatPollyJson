import json

original_string = '''
{"time":25,"type":"word","start":1,"end":16,"value":"Congratulations"}
{"time":987,"type":"word","start":17,"end":19,"value":"on"}
{"time":1112,"type":"word","start":20,"end":30,"value":"completing"}
{"time":1600,"type":"word","start":31,"end":34,"value":"the"}
{"time":1675,"type":"word","start":35,"end":39,"value":"quiz"}
{"time":2730,"type":"word","start":41,"end":45,"value":"Your"}
{"time":2842,"type":"word","start":46,"end":51,"value":"score"}
{"time":3205,"type":"word","start":52,"end":54,"value":"is"}
{"time":3380,"type":"word","start":55,"end":64,"value":"displayed"}
{"time":3830,"type":"word","start":65,"end":69,"value":"here"}
{"time":4697,"type":"word","start":71,"end":76,"value":"Below"}
{"time":5335,"type":"word","start":78,"end":84,"value":"you'll"}
{"time":5497,"type":"word","start":85,"end":89,"value":"find"}
{"time":5822,"type":"word","start":90,"end":97,"value":"options"}
{"time":6347,"type":"word","start":98,"end":100,"value":"to"}
{"time":6447,"type":"word","start":101,"end":107,"value":"either"}
{"time":6735,"type":"word","start":108,"end":114,"value":"retake"}
{"time":7135,"type":"word","start":115,"end":118,"value":"the"}
{"time":7197,"type":"word","start":119,"end":123,"value":"quiz"}
{"time":7872,"type":"word","start":125,"end":131,"value":"review"}
{"time":8160,"type":"word","start":132,"end":135,"value":"the"}
{"time":8260,"type":"word","start":136,"end":143,"value":"correct"}
{"time":8647,"type":"word","start":144,"end":151,"value":"answers"}
{"time":9360,"type":"word","start":153,"end":155,"value":"or"}
{"time":9485,"type":"word","start":156,"end":163,"value":"proceed"}
{"time":9960,"type":"word","start":164,"end":166,"value":"to"}
{"time":10072,"type":"word","start":167,"end":170,"value":"the"}
{"time":10160,"type":"word","start":171,"end":175,"value":"next"}
{"time":10560,"type":"word","start":176,"end":180,"value":"page"}
'''

# Split the input string into individual JSON objects
original_data = [json.loads(line) for line in original_string.strip().split('\n')]

# Create a new list with modified elements
formatted_data = [{"time": entry["time"],
                   "type": entry["type"],
                   "value": entry["value"],
                   "element": "narrate-1-page"} for entry in original_data]

# Create a dictionary with the new list
formatted_json = {"daring": formatted_data}

with open("daring.json", "w", encoding="utf-8") as output_file:
    output_file.write('{"daring": [\n')
    for i, item in enumerate(formatted_json["daring"]):
        if i < len(formatted_json["daring"]) - 1:
            # Item not last, append comma
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
        else:
            # Last item, do not append comma
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
    output_file.write(']}\n')

print("Formatted Daring JSON written to daring.json. Next fill in the elements and paste into first.json. Then paste daring and valiant strings into switch_times.py and run the script.")

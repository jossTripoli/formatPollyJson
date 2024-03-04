import json

original_string = '''
{"time":25,"type":"word","start":13,"end":28,"value":"Congratulations"}
{"time":1667,"type":"word","start":42,"end":48,"value":"You've"}
{"time":1842,"type":"word","start":49,"end":58,"value":"completed"}
{"time":2280,"type":"word","start":60,"end":68,"value":"Concepts"}
{"time":2955,"type":"word","start":70,"end":73,"value":"and"}
{"time":3067,"type":"word","start":74,"end":80,"value":"earned"}
{"time":3330,"type":"word","start":81,"end":82,"value":"a"}
{"time":3380,"type":"word","start":83,"end":89,"value":"bronze"}
{"time":3792,"type":"word","start":90,"end":95,"value":"badge"}
{"time":5022,"type":"word","start":122,"end":125,"value":"You"}
{"time":5197,"type":"word","start":126,"end":129,"value":"now"}
{"time":5434,"type":"word","start":130,"end":134,"value":"know"}
{"time":6072,"type":"word","start":150,"end":153,"value":"The"}
{"time":6147,"type":"word","start":154,"end":160,"value":"basics"}
{"time":6672,"type":"word","start":161,"end":163,"value":"of"}
{"time":6772,"type":"word","start":164,"end":172,"value":"identity"}
{"time":7222,"type":"word","start":173,"end":178,"value":"theft"}
{"time":7847,"type":"word","start":193,"end":197,"value":"What"}
{"time":7997,"type":"word","start":198,"end":209,"value":"information"}
{"time":8647,"type":"word","start":210,"end":218,"value":"scammers"}
{"time":9147,"type":"word","start":219,"end":222,"value":"are"}
{"time":9297,"type":"word","start":223,"end":228,"value":"after"}
{"time":9947,"type":"word","start":243,"end":249,"value":"Online"}
{"time":10409,"type":"word","start":250,"end":258,"value":"identity"}
{"time":10822,"type":"word","start":259,"end":269,"value":"management"}
{"time":12177,"type":"word","start":295,"end":297,"value":"To"}
{"time":12302,"type":"word","start":298,"end":303,"value":"build"}
{"time":12577,"type":"word","start":304,"end":308,"value":"your"}
{"time":12702,"type":"word","start":309,"end":319,"value":"resilience"}
{"time":13414,"type":"word","start":320,"end":323,"value":"and"}
{"time":13564,"type":"word","start":324,"end":328,"value":"earn"}
{"time":13714,"type":"word","start":329,"end":333,"value":"more"}
{"time":13914,"type":"word","start":334,"end":340,"value":"badges"}
{"time":14664,"type":"word","start":342,"end":350,"value":"continue"}
{"time":15164,"type":"word","start":351,"end":353,"value":"to"}
{"time":15302,"type":"word","start":354,"end":357,"value":"the"}
{"time":15389,"type":"word","start":358,"end":362,"value":"next"}
{"time":15752,"type":"word","start":363,"end":370,"value":"section"}
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

with open("first.json", "w", encoding="utf-8") as output_file:
    output_file.write('{"daring": [\n')
    for i, item in enumerate(formatted_json["daring"]):
        if i < len(formatted_json["daring"]) - 1:
            # Item not last, append comma
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + ',\n')
        else:
            # Last item, do not append comma
            output_file.write('\t' + json.dumps(item, separators=(',', ': ')) + '\n')
    output_file.write(']}\n')

print("Formatted JSON written to first.json")

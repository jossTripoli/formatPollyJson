import json

original_string = '''
{"time":25,"type":"word","start":13,"end":20,"value":"Reflect"}
{"time":1130,"type":"word","start":34,"end":38,"value":"Take"}
{"time":1367,"type":"word","start":39,"end":40,"value":"a"}
{"time":1417,"type":"word","start":41,"end":47,"value":"moment"}
{"time":1817,"type":"word","start":48,"end":50,"value":"to"}
{"time":1917,"type":"word","start":51,"end":56,"value":"think"}
{"time":2192,"type":"word","start":57,"end":62,"value":"about"}
{"time":2455,"type":"word","start":63,"end":66,"value":"the"}
{"time":2530,"type":"word","start":67,"end":76,"value":"following"}
{"time":3597,"type":"word","start":78,"end":91,"value":"            -"}
{"time":4452,"type":"word","start":92,"end":95,"value":"Can"}
{"time":4602,"type":"word","start":96,"end":99,"value":"you"}
{"time":4727,"type":"word","start":100,"end":106,"value":"recall"}
{"time":5089,"type":"word","start":107,"end":108,"value":"a"}
{"time":5139,"type":"word","start":109,"end":113,"value":"time"}
{"time":5539,"type":"word","start":114,"end":118,"value":"when"}
{"time":5677,"type":"word","start":119,"end":122,"value":"you"}
{"time":5764,"type":"word","start":123,"end":129,"value":"shared"}
{"time":6052,"type":"word","start":130,"end":141,"value":"information"}
{"time":6639,"type":"word","start":142,"end":147,"value":"about"}
{"time":6877,"type":"word","start":148,"end":156,"value":"yourself"}
{"time":7314,"type":"word","start":157,"end":161,"value":"that"}
{"time":7452,"type":"word","start":162,"end":165,"value":"you"}
{"time":7577,"type":"word","start":166,"end":171,"value":"later"}
{"time":7839,"type":"word","start":172,"end":181,"value":"regretted"}
{"time":8807,"type":"word","start":183,"end":185,"value":"If"}
{"time":8944,"type":"word","start":186,"end":188,"value":"so"}
{"time":9494,"type":"word","start":190,"end":194,"value":"what"}
{"time":9657,"type":"word","start":195,"end":203,"value":"happened"}
{"time":10282,"type":"word","start":205,"end":218,"value":"            -"}
{"time":10887,"type":"word","start":219,"end":224,"value":"Given"}
{"time":11162,"type":"word","start":225,"end":229,"value":"what"}
{"time":11337,"type":"word","start":230,"end":236,"value":"you've"}
{"time":11537,"type":"word","start":237,"end":244,"value":"learned"}
{"time":11862,"type":"word","start":245,"end":250,"value":"about"}
{"time":12124,"type":"word","start":251,"end":255,"value":"what"}
{"time":12299,"type":"word","start":256,"end":264,"value":"personal"}
{"time":12749,"type":"word","start":265,"end":276,"value":"information"}
{"time":13337,"type":"word","start":277,"end":285,"value":"scammers"}
{"time":13799,"type":"word","start":286,"end":289,"value":"are"}
{"time":13937,"type":"word","start":290,"end":295,"value":"after"}
{"time":14612,"type":"word","start":297,"end":301,"value":"will"}
{"time":14699,"type":"word","start":302,"end":307,"value":"there"}
{"time":14862,"type":"word","start":308,"end":310,"value":"be"}
{"time":15012,"type":"word","start":311,"end":312,"value":"a"}
{"time":15087,"type":"word","start":313,"end":323,"value":"difference"}
{"time":15537,"type":"word","start":324,"end":326,"value":"in"}
{"time":15649,"type":"word","start":327,"end":331,"value":"what"}
{"time":15787,"type":"word","start":332,"end":335,"value":"you"}
{"time":15912,"type":"word","start":336,"end":340,"value":"will"}
{"time":16012,"type":"word","start":341,"end":346,"value":"share"}
{"time":16287,"type":"word","start":347,"end":353,"value":"online"}
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

print("Formatted JSON written to formatted_json.json")

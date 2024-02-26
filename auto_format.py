import json
import pyperclip

# Prompt the user for the input string
original_string = input("Please enter the JSON string: ")

# Split the input string into individual JSON objects
original_data = [json.loads(line) for line in original_string.strip().split('\n')]

# Create a new list with modified elements
formatted_data = [{"time": entry["time"],
                   "type": entry["type"],
                   "value": entry["value"],
                   "element": "narrate-1"} for entry in original_data]

# Create a dictionary with the new list
formatted_json = {"daring": formatted_data}

# Prepare the JSON string for writing to file and copying to clipboard
formatted_json_str = '{"daring": [\n'
for i, item in enumerate(formatted_json["daring"]):
    if i < len(formatted_json["daring"]) - 1:
        # Item not last, append comma
        formatted_json_str += '\t' + json.dumps(item, separators=(',', ': ')) + ',\n'
    else:
        # Last item, do not append comma
        formatted_json_str += '\t' + json.dumps(item, separators=(',', ': ')) + '\n'
formatted_json_str += ']}\n'

# Write the formatted JSON to a new file
with open("formatted_output.json", "w") as output_file:
    output_file.write(formatted_json_str)

# Copy the formatted JSON string to the clipboard
pyperclip.copy(formatted_json_str)

print("Formatted JSON written to formatted_output.json and copied to clipboard.")

import json
input_file=open('latest_data.json', 'r')
output_file=open('test.json', 'w')
json_decode=json.load(input_file)
result = []
for item in json_decode:
    my_dict={}
    my_dict['created_at']=item.get('created_at')
    print(my_dict)
    result.append(my_dict)
back_json=json.dumps(result, output_file)
output_file.write(back_json)
output_file.close() 

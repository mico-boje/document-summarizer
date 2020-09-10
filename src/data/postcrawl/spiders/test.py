# import json
#
# json_data = []
# json_file = open('links.json')
#
# for line in json_file:
#     json_data.append(line)
#
# counter = 1
# links_list = []
# while counter < len(json_data) -1:
#     if json_data[counter][-2] == ',':
#         json_data[counter] = json_data[counter][:-2]
#     temp_json = json.loads(json_data[counter])
#   #  del temp_json['link'][-1]
#     for i, k in enumerate(temp_json['link']):
#         if k[:5] == 'https':
#             print(temp_json['link'][i])
#             links_list.append(temp_json['link'][i])
#     counter += 1
# links_list = list(dict.fromkeys(links_list))
# print(links_list)
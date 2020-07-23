import json
import sys

class JsonMapper():

    def __init__(self):
        pass

    def recurse_json(self, json_obj, node_level_counter=0):
        if node_level_counter == 0 and type(json_obj) == str:
            json.loads(json_obj)

        primitive_types = [str, int, float, bool, type(None)]

        type_lookup_dict = {
            str: "string",
            int: "long",
            float: "double",
            bool: "boolean",
            type(None): "null",
            dict: "Object",
            list: "Array"
        }

        if type(json_obj) == dict:
            node_levels = {k: node_level_counter for k in list(json_obj.keys())}
            for k in list(json_obj.keys()):
                if type(json_obj[k]) in primitive_types:
                    print(f"Termination at node level {node_levels[k]} | key - '{k}', fieldType - {type_lookup_dict[type(json_obj[k])]}, value {json_obj[k]}")
                elif type(json_obj[k]) == list:
                    print(f"-----{type_lookup_dict[type(json_obj[k])]}-----")
                    print(f"Type {type_lookup_dict[type(json_obj[k])]} under key - '{k}' encountered at node level {node_levels[k]}")
                    index_counter = 0
                    for i, element in enumerate(json_obj[k]):
                        elem_type = type(element)
                        if elem_type in primitive_types:
                            print(f"Termination within Array(index:{i}) at node level {node_levels[k]} | key - '{k}', fieldType - {type_lookup_dict[elem_type]}, value {element}")
                        else:
                            print(f"-----{type_lookup_dict[elem_type]}-----")
                            print(f"Type {type_lookup_dict[elem_type]} in list under key - '{k}' at list index {index_counter} encountered at node level {node_level_counter}")
                            index_counter += 1
                            self.recurse_json(element, node_level_counter)

                else:
                    print(f"-----{type_lookup_dict[type(json_obj[k])]}-----")
                    print(f"Type {type_lookup_dict[type(json_obj[k])]} under key - '{k}' encountered at node level {node_levels[k]}")
                    node_level_counter += 1
                    self.recurse_json(json_obj[k], node_level_counter)

        elif type(json_obj) == list:
            if node_level_counter == 0:
                k = "root"
            node_levels = {str(e): node_level_counter for e in json_obj}
            node_levels["root"] = 0
            for list_element in json_obj:
                if type(list_element) in primitive_types:
                    print(f"Termination at node level {node_levels[k]} | key - '{k}', fieldType - {type_lookup_dict[type(list_element)]}, value {list_element}")
                elif type(list_element) == list:
                    print(f"-----{type_lookup_dict[type(list_element)]}-----")
                    print(f"Type {type_lookup_dict[type(list_element)]} under key - '{k}' encountered at node level {node_levels[str(list_element)]}")
                    index_counter = 0
                    for i, element in enumerate(list_element):
                        elem_type = type(element)
                        if elem_type in primitive_types:
                            print(f"Termination within Array(index:{i} at node level {node_levels[k]} | key - '{k}', fieldType - {type_lookup_dict[elem_type]}, value {element}")
                        else:
                            print(f"-----{type_lookup_dict[elem_type]}-----")
                            print(f"Type {type_lookup_dict[type(json_obj[k])]} in list under key - '{k}' at list index {index_counter} encountered at node level {node_levels[str(list_element)]}")
                            index_counter += 1
                            self.recurse_json(element, node_level_counter)

                else:
                    elem_type = dict
                    print(f"-----{type_lookup_dict[elem_type]}-----")
                    print(f"Type {type_lookup_dict[elem_type]} under key - '{k}' encountered at node level {node_levels[str(list_element)]}")
                    node_level_counter += 1
                    self.recurse_json(list_element, node_level_counter)


if __name__ == "__main__":
    ### Example usage from file

    # fp = r"C:\Users\MyUser\Path\to\Json.json"
    # with open(fp) as f:
    #     input_json = json.loads(f.read())
    ####

    jm = JsonMapper()
    input_json = json.loads(sys.stdin.read())
    jm.recurse_json(input_json)
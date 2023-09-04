def overall(value,netlist_file):
    import networkx as nxṇ
    import matplotlib.pyplot as plt
    import re
    with open(netlist_file, 'r') as file:
        netlist = file.read()
    split_lines = netlist.split(';')
    # print(split_lines)
    cleaned_lines = []
    for line in split_lines:
        cleaned_line = line.strip()
        cleaned_lines.append(cleaned_line)
    token=[]
    for line in cleaned_lines:
        line.split()
        token.append(line.split())
    gate=[]
    after_gate=[]
    input_s=[]
    output_s=[]
    wire_s=[]
    for sublist in token:
        if sublist[0]!='module' and sublist[0]!='input' and sublist[0]!='output' and sublist[0]!='wire':
            if sublist[0]=='endmodule':
                continue
            else:
                gate.append(sublist[0])
                after_gate.append(sublist[1])
        else:
            if sublist[0]=='input':
                input_s.append(sublist[1])
            else:
                if sublist[0]=='wire':
                    wire_s.append(sublist[1])
                else:
                    if sublist[0]=='output':
                        output_s.append(sublist[1])

    wire_s = wire_s[0].split(',')
    # print(wire_s)
    output_s = output_s[0].split(',')
    # print(output_s)
    input_s = input_s[0].split(',')
    # print(input_s)

    values=value
    input_dictionary = {input_s[i]: values[i] for i in range(len(input_s))}
    # print(values)
    # print(input_dictionary)

    # print(input_dictionary)
    # print(gate)
    # print(after_gate)
    # hold_input_dictionary=input_dictionary
    expressions = after_gate
    def extract_elements_and_gates(expression):
        start_index = expression.find('(') + 1
        end_index = expression.find(')')
        elements_inside_brackets = expression[start_index:end_index]
        elements_list = elements_inside_brackets.split(',')
        gate_name = expression.split('(')[0].strip()
        return elements_list, gate_name

    all_elements_list = []
    all_gate_names = []
    for expression in expressions:
        elements_list, gate_name = extract_elements_and_gates(expression)
        all_elements_list.append(elements_list)
        all_gate_names.append(gate_name)
    # print(all_gate_names)
    # print(gate)
    # print(all_elements_list)
    new_all_gate_names = [item.split('_')[0] for item in all_gate_names]
    # print(new_all_gate_names)
    for i in range(0,len(new_all_gate_names)):
        each_element=all_elements_list[i]
        if new_all_gate_names[i]=='NOT1':
            input_dictionary[each_element[0]] = int(not input_dictionary[each_element[1]])
        elif new_all_gate_names[i]=='NOT':
            input_dictionary[each_element[0]] = int(not input_dictionary[each_element[1]])
        elif new_all_gate_names[i]=='AND2':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]])
        elif new_all_gate_names[i]=='OR2':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]] or input_dictionary[each_element[2]])
        elif new_all_gate_names[i]=='OR3':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]] or input_dictionary[each_element[2]] or input_dictionary[each_element[3]])
        elif new_all_gate_names[i]=='NAND2':
            x = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]])
            input_dictionary[each_element[0]] = int(not x)
        elif new_all_gate_names[i]=='AND4':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]] and input_dictionary[each_element[3]] and input_dictionary[each_element[4]])
        elif new_all_gate_names[i]=='AND5':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]] and input_dictionary[each_element[3]] and input_dictionary[each_element[4]] and input_dictionary[each_element[5]])
        elif new_all_gate_names[i]=='AND8':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]] and input_dictionary[each_element[3]] and input_dictionary[each_element[4]] and input_dictionary[each_element[5]] and input_dictionary[each_element[6]] and input_dictionary[each_element[7]] and input_dictionary[each_element[8]])
        elif new_all_gate_names[i]=='NAND8':
            x = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]] and input_dictionary[each_element[3]] and input_dictionary[each_element[4]] and input_dictionary[each_element[5]] and input_dictionary[each_element[6]] and input_dictionary[each_element[7]] and input_dictionary[each_element[8]])
            input_dictionary[each_element[0]] = int(not x)
        elif new_all_gate_names[i]=='NAND4':
            x = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]] and input_dictionary[each_element[3]] and input_dictionary[each_element[4]])
            input_dictionary[each_element[0]] = int(not x)
        elif new_all_gate_names[i]=='NAND3':
            x = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]] and input_dictionary[each_element[3]])
            input_dictionary[each_element[0]] = int(not x)
        elif new_all_gate_names[i]=='NAND5':
            x = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]] and input_dictionary[each_element[3]] and input_dictionary[each_element[4]] and input_dictionary[each_element[5]])
            input_dictionary[each_element[0]] = int(not x)
        elif new_all_gate_names[i]=='OR4':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]] or input_dictionary[each_element[2]] or input_dictionary[each_element[3]] or input_dictionary[each_element[4]])
        elif new_all_gate_names[i]=='OR5':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]] or input_dictionary[each_element[2]] or input_dictionary[each_element[3]] or input_dictionary[each_element[4]] or input_dictionary[each_element[5]])
        elif new_all_gate_names[i]=='BUFF1':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]])
        elif new_all_gate_names[i]=='AND3':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]] and input_dictionary[each_element[3]])
        elif new_all_gate_names[i]=='NOR2':
            x = int(input_dictionary[each_element[1]] or input_dictionary[each_element[2]])
            input_dictionary[each_element[0]] = int(not x)
        elif new_all_gate_names[i]=='NOR3':
            x = int(input_dictionary[each_element[1]] or input_dictionary[each_element[2]] or input_dictionary[each_element[3]])
            input_dictionary[each_element[0]] = int(not x)
        elif new_all_gate_names[i]=='NOR4':
            x = int(input_dictionary[each_element[1]] or input_dictionary[each_element[2]] or input_dictionary[each_element[3]] or input_dictionary[each_element[4]])
            input_dictionary[each_element[0]] = int(not x)
        elif new_all_gate_names[i]=='NOR8':
            x = int(input_dictionary[each_element[1]] or input_dictionary[each_element[2]] or input_dictionary[each_element[3]] or input_dictionary[each_element[4]] or input_dictionary[each_element[5]] or input_dictionary[each_element[6]] or input_dictionary[each_element[7]] or input_dictionary[each_element[8]])
            input_dictionary[each_element[0]] = int(not x)
        elif new_all_gate_names[i]=='AND9':
            input_dictionary[each_element[0]] = int(input_dictionary[each_element[1]] and input_dictionary[each_element[2]] and input_dictionary[each_element[3]] and input_dictionary[each_element[4]] and input_dictionary[each_element[5]] and input_dictionary[each_element[6]] and input_dictionary[each_element[7]] and input_dictionary[each_element[8]] and input_dictionary[each_element[9]])
    # print(input_dictionary)


    wire_list=[]
    for i in wire_s:
        if i in input_dictionary:
            wire_list.append(input_dictionary[i])

    # print(wire_list)
    return wire_list,wire_s

def calculation(test_vectors,netlist,rare_node_threshold,rare_switching_threshold):
    # Create an empty list to store the lines
    lines_list = []

    # Open the text file in read mode
    with open(test_vectors, 'r') as file:
        # Read each line of the file
        for line in file:
            # Remove any leading or trailing whitespace characters (like newline)
            line = line.strip()
            # Split the line into individual characters
            digits = list(line)
            # Convert each character to an integer and append to the inner list
            integers_list = [int(digit) for digit in digits]
            # Append the inner list to the outer list
            lines_list.append(integers_list)

    total_space=[]
    rare_node=[]
    number_of_1s=[]
    save=[]
    count=0
    for i in range(0,len(lines_list)):
        wire_list,wire_s=overall(lines_list[i],netlist)
        total_space.append(wire_list)


    #print(total_space)
    # Input list
    input_list = total_space
    # print(input_list)

    # Use the zip function to group elements by their positions
    grouped_elements = list(zip(*input_list))

    # Convert each group of elements into a list
    result_list = [list(group) for group in grouped_elements]

    for item in result_list:
        for i in item:
            if i==1:
                count=count+1
        number_of_1s.append(count)
        count=0

    number_of_0s = [len(lines_list) - x for x in number_of_1s]

    # Rare Node for 1
    rare_Node_for_1=[]
    for i in range(0,len(number_of_0s)):
        if number_of_0s[i]>rare_node_threshold:
            rare_Node_for_1.append(wire_s[i])
    # print("rare_Node_for_1")
    # print(rare_Node_for_1)
    # Rare Node for 0
    rare_Node_for_0=[]
    for i in range(0,len(number_of_1s)):
        if number_of_1s[i]>rare_node_threshold:
            rare_Node_for_0.append(wire_s[i])
    # print("rare_Node_for_0")
    # print(len(rare_Node_for_0))

    # Rare Switching Node
    corresponding_rare_switching_values={}
    rare_count=0
    rare_switching_nodes=[]
    for index, k in enumerate(result_list):
        for i, j in zip(range(0,len(k)), range(1, len(k))):
            if k[j]!=k[i]:
                rare_count=rare_count+1
        corresponding_rare_switching_values[wire_s[index]]=rare_count
        if rare_count<rare_switching_threshold:
            rare_switching_nodes.append(wire_s[index])
        rare_count=0
    # print(corresponding_rare_switching_values)
    # print("rare_switching_node")
    # print(rare_switching_nodes)
    # print(corresponding_rare_switching_values)
    # print(number_of_1s)


    corresponding_1_values={wire_s[i]: number_of_1s[i] for i in range(len(wire_s))}
    corresponding_0_values={wire_s[i]: number_of_0s[i] for i in range(len(wire_s))}
    # print("Value '1' at nodes")
    # print(corresponding_1_values)
    # print("Value '0' at nodes")
    # print(corresponding_0_values)
    # print("Value of switching")
    # print(corresponding_rare_switching_values)

    #Writting to a file
    # import json

    # with open('corresponding_values.txt','w') as f:
    #     f.write("Values of 1's at nodes")
    #     json.dump(corresponding_1_values,f)
    #     f.write("Values of 0's at nodes")
    #     json.dump(corresponding_0_values,f)
    #     f.write("Values ofss switching at nodes")
    #     json.dump(corresponding_rare_switching_values,f)

    # for key, value in corresponding_1_values.items():
    #     print(f"'{key}': {value}")
    #     # if value>95:
    #     #     print(key)
    return corresponding_1_values,corresponding_0_values,rare_switching_nodes,rare_Node_for_1,rare_Node_for_0,number_of_1s,number_of_0s,total_space,lines_list,result_list,wire_s

def calculation_mero(lines_list,netlist):
    wire_list,wire_s=overall(lines_list,netlist)
    return wire_list,wire_s

def MERO(N,RV,netlist,RV_for_RN,rare_node_threshold,rare_switching_threshold):
    corresponding_1_values,corresponding_0_values,rare_switching_nodes,rare_Node_for_1,rare_Node_for_0,number_of_1s,number_of_0s,total_space,lines_list,result_list,wire_s=calculation(RV_for_RN,netlist,rare_node_threshold,rare_switching_threshold)

    #SORTING VECTORS IN THEIR MAXIMUM RARE NODE TRIGGERING ORDER
    lines_dict_sort={}
    # count_1=0
    # wire_list,wire_s=calculation_mero(lines_list[0],'c1355.v')
    # my_dict_sort = dict(zip(wire_s, wire_list))
    # for x in rare_Node_for_1:
    #     if my_dict_sort[x]==1:
    #         count_1=count_1+1
    # for y in rare_Node_for_0:
    #     if my_dict_sort[y]==0:
    #         count_1=count_1+1
    # my_tuple = tuple(lines_list[0])
    # lines_dict_sort[my_tuple]=count_1

    # Open the text file in read mode
    with open(RV, 'r') as file:
        # Read each line (sentence) from the file
        sentences = [line.strip() for line in file]

    # Convert each sentence to a list and create a list of lists
    list_of_lists = [[int(digit) for digit in sentence] for sentence in sentences]

    lines_list_overall=lines_list+list_of_lists
    # print(len(rare_Node_for_0))
    # print(len(rare_Node_for_1))
    # print(len(wire_s))
    # print(lines_list_overall)
    # print(lines_list_overall)

    # Print the resulting list of lists
    # print(len(lines_list_overall))
    count_1=0
    for i in lines_list_overall:
        # print(i)
        wire_list,wire_s=calculation_mero(i,netlist)
        my_dict_sort = dict(zip(wire_s, wire_list))
        for x in rare_Node_for_1:
            if my_dict_sort[x]==1:
                count_1=count_1+1
        for y in rare_Node_for_0:
            if my_dict_sort[y]==0:
                count_1=count_1+1
        # print(count_1)
        my_tuple = tuple(i)
        lines_dict_sort[my_tuple]=count_1
        count_1=0
    lines_dict_sorted = dict(sorted(lines_dict_sort.items(), key=lambda item: (item[1], item[0]), reverse=True))
    # lines_dict_sorted = dict(sorted(lines_dict_sort.items(), key=lambda item: item[1], reverse=True))

    # for key,value in lines_dict_sort.items():
    #     print(key,value)                                      #<<<<<<<<<<---------
    # print(len(lines_dict_sorted))
    # for key,value in lines_dict_sorted.items():
    #     print(key,value)
    keys_list = []
    values_list = []
    for key, value in lines_dict_sorted.items():
        # print(key,value)
        keys_list.append(list(key))
        values_list.append(value)

    # print(keys_list)
    # print(values_list)

    # Set number of times node satisfies rare value (AR) to 0
    ar_dict_rare_Node_for_1={}
    for item in rare_Node_for_1:
        ar_dict_rare_Node_for_1[item] = 0
    # print(ar_dict_rare_Node_for_1)

    ar_dict_rare_Node_for_0={}
    for item in rare_Node_for_0:
        ar_dict_rare_Node_for_0[item] = 0
    # print(ar_dict_rare_Node_for_0)

    # Applying bit flipping algorithm
    # NOW SORTED TEST VECTORS LIST IS "lines_list_new"
    # Flipping and checking
    count=0
    flag=0
    ATG={}
    temp_dict={}
    combined_temp_dict={}
    iterations=0
    for i in keys_list:
        combined_temp_dict={}
        k=i
        # print(k)
        # print(i)
        temp_dict[tuple(i)]=lines_dict_sorted[tuple(i)]
        # print(temp_dict)
        for j in range(len(i)):
            iterations=iterations+1
            flipped_list = i.copy()
            flipped_list[j] = 1 - flipped_list[j]
            # print(flipped_list)
            wire_list,wire_s=calculation_mero(flipped_list,netlist)
            my_dict = dict(zip(wire_s, wire_list))
            # print(my_dict)
            for x in rare_Node_for_1:
                if my_dict[x]==1:
                    count=count+1
            for y in rare_Node_for_0:
                if my_dict[y]==0:
                    count=count+1
            # print(count)
            if count>temp_dict[tuple(k)]:
                del temp_dict[tuple(k)]
                temp_dict[tuple(flipped_list)] = count
                k=flipped_list
                # ATG[tuple(flipped_list)]=count
            count=0
        # print(temp_dict)
        keys_list_1 = []
        values_list_1 = []
        for key, value in temp_dict.items():
            keys_list_1.append(list(key))
            values_list_1.append(value)
        # print(keys_list_1,values_list_1)
        wire_list,wire_s=calculation_mero(keys_list_1[0],netlist)
        my_dict = dict(zip(wire_s, wire_list))
            # print(my_dict)
        for x in ar_dict_rare_Node_for_1:
            if my_dict[x]==1:
                ar_dict_rare_Node_for_1[x]=ar_dict_rare_Node_for_1[x]+1
        for y in ar_dict_rare_Node_for_0:
            if my_dict[y]==0:
                ar_dict_rare_Node_for_0[y]=ar_dict_rare_Node_for_0[y]+1
        ATG.update(temp_dict)
        temp_dict.clear()
        combined_temp_dict=ar_dict_rare_Node_for_0
        for z in ar_dict_rare_Node_for_0:
            combined_temp_dict[z]=ar_dict_rare_Node_for_0[z]
        # combined_temp_dict.update(ar_dict_rare_Node_for_1)
        # print(combined_temp_dict)
        for value in combined_temp_dict.values():
            if value < N:
                flag=0
                break
            else:
                flag=1
        # combined_temp_dict.clear()
        # print(flag)
        if flag==0:
            continue
        else:
            break

    # print(ar_dict_rare_Node_for_1)
    # print(ar_dict_rare_Node_for_0)
    ATG_sorted = dict(sorted(ATG.items(), key=lambda item: (item[1], item[0]), reverse=True))
    ATG_sorted_0_TRIGGERED_REMOVED = {key: value for key, value in ATG_sorted.items() if value != 0}
    # for key,value in ATG_sorted.items():
    #     print(key,value)
    print(iterations)
    # print(rare_Node_for_0)
    # print(rare_Node_for_1)

    return ar_dict_rare_Node_for_1,ar_dict_rare_Node_for_0,ATG_sorted,len(ATG_sorted),wire_s,ATG_sorted_0_TRIGGERED_REMOVED


# MERO(value of N,RV Set,netlist,RV set to detect rare nodes,rare_node_threshold,rare_switching_threshold)
ar_dict_rare_Node_for_1,ar_dict_rare_Node_for_0,ATG_Set_by_MERO,length,wire_s,ATG_sorted_0_TRIGGERED_REMOVED=MERO(100,'testvectors_c2670_x.txt','c2670.v','testvectors_c2670.txt',95,5)
for key,value in ATG_sorted_0_TRIGGERED_REMOVED.items():
    print(key,value)
print(len(ATG_sorted_0_TRIGGERED_REMOVED))
# print(len(wire_s))
# print(ar_dict_rare_Node_for_0)
# print(ar_dict_rare_Node_for_1)

import json
with open('dictionary.txt', 'w') as file:
        for key,value in ATG_sorted_0_TRIGGERED_REMOVED.items():
            file.write(key,value)

# # Your dictionary

# # Specify the file name and open it in write mode
# file_name = 'dictionary.txt'

# with open(file_name, 'w') as json_file:
#     # Use the json.dump() function to write the dictionary to the file
#     json.dump(ATG_sorted_0_TRIGGERED_REMOVED, json_file)

# print(f'Dictionary has been written to {file_name}')
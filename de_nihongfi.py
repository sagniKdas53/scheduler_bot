import csv


def make_list(file):
    list_name = []
    with open('names.txt', 'r') as make_ls:
        for nm in make_ls:
            list_name.append(str(nm).strip())
    with open(file, 'r') as sch:
        reader = csv.DictReader(sch)
        for row in reader:
            data = row['NAME']
            list_name.append(str(data))
    unique_name = set(list_name)
    list_name = list(unique_name)
    print(list_name)
    with open('names_test.txt', 'w') as make_ls_w:
        for idl in list_name:
            make_ls_w.write(str(idl) + '\n')


def translate_export(file, orig, tran):
    uni = open(orig, 'r')
    list_og_names = uni.readlines()
    uni.close()
    name_list = []
    uni_t = open(tran, 'r')
    list_trans = uni_t.readlines()
    uni_t.close()
    for ele in range(len(list_og_names)):
        name_list.append([list_og_names[ele].strip(), list_trans[ele].strip()])
    # print(name_list)
    final = open(file,'r')
    total_data = final.readlines()
    final.close()
    # for name_data in name_list:
    # print(name_data[0],'\t',name_data[1])
    dict_name = dict(name_list)  # idk how to fix this
    for key, val in dict_name.items():
        for idx, ele in enumerate(total_data):
            if key in ele:
                total_data[idx] = ele.replace(key, val)
    write_it = open('export_translated.csv','w')
    write_it.writelines(total_data)
    write_it.close()

# make_list('export.csv')
# translate_export('export_local.csv', 'names.txt', 'translate_names.txt')

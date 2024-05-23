import sys
prevPos = 0
def write_element(lvl, type, content, open):
    
    if (not open):
        str = ""
        for i in range(lvl):
            str+=('\t')
            pass
        str+=("<" + type + ">\n")
        for i in range(lvl + 1):
            str+=('\t');
            pass
        str+=(content + "\n");
        for i in range(lvl):
            str+=('\t')
            pass
    else:
            str+=("</"+type + ">\n");
    return str;
    
def build_dectionary(file):
    dictionaire = {}
    for line in file:
        spliter = [s.strip() for s in line.split('=')]
        name = spliter[0];
        my_list = [s.strip() for s in spliter[1].split(',')] # ['position:11', 'number:112', 'small: Cn', 'molar:285', 'electron:2 8 18 32 32 18 2']
        my_list.insert(0, 'name:'+name)
        sub_dictionaire = {};
        for s in my_list :
            sub_dict_element_split = s.split(":");
            sub_dict_element = [ss.strip() for ss in sub_dict_element_split]
            sub_dictionaire[sub_dict_element[0]] = sub_dict_element[1];
            pass
        dictionaire[sub_dictionaire['number']] = sub_dictionaire
    return dictionaire;
    pass

# --*-- Main  --*--
if __name__ == '__main__' :
    read_file = open('periodic_table.txt', 'r');
    output_file = open('periodic_table.html', 'w')
    dictionaire = build_dectionary(read_file);
    output_file.write('<table>\n')
    for key, value in dictionaire.items():
        name = value.get('name')
        number = value.get('number')
        small = value.get('small')
        molar = value.get('molar')
        electron = value.get('electron')
        position = value.get('position')
        lvl = 1
        beginn = "<tr>\n" if value.get('position') == '0' else ""
        endd = "</tr>\n" if value.get('position') == '17' else ""
        if (int(position) > prevPos + 1 and not beginn):
            print(prevPos + 1, int(position))
            for i in range(int(position) - prevPos - 1):
                output_file.write(f'\
    <td style="border: 1px solid black; padding:10px">\n\
        <h4></h4>\n\
        <ul>\n\
        </ul>\n\
    </td>\n\
            ')
            pass;
        output_file.write(f'\
    '+beginn+'\n\
    <td style="border: 1px solid black; padding:10px">\n\
        <h4>'+ name +'</h4>\n\
        <ul>\n\
            <li>No '+ number+  '</li>\n\
            <li>'+ small+  '</li>\n\
            <li>'+ molar+  '</li>\n\
            <li>'+ electron+  'electron</li>\n\
        </ul>\n\
    </td>\n\
    '+endd+'\
            ')
        prevPos = int(value.get('position'))
        pass
    output_file.write('</table>')
    output_file.close();
    read_file.close();
    
import os, glob, csv, re, pprint
from locale import getpreferredencoding

file_for_write = os.path.join(os.getcwd(), 'main_data.txt')

def get_txt():
    return glob.glob(os.path.join(os.getcwd(), '*.txt'))

def get_data():
    files = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []
    encoding = getpreferredencoding()
    #print(get_txt())
    for filename in get_txt():
        #print(len(get_txt()))
        #print(os.listdir('.'))
        if 'main_data.txt' in re.split(r'\\', filename):
            continue
        else:
            files.append(filename)
#             print(filename)
            with open(filename, encoding=encoding) as f_n:
                f_n_reader = csv.reader(f_n)
                for row in f_n_reader:
                    
                    if re.search(r'Изготовитель системы', str(row)):
                        os_prod_list.append(re.search(r'[A-Z]{4,}', str(row)).group(0))
                        
                    elif re.search(r'Название ОС', str(row)):
                        os_name_list.append(re.search(r'([A-Z].*?\')', str(row)).group(0))
                        
                    elif re.search(r'Код продукта', str(row)):
                        os_code_list.append(re.search(r'\d{5}.....\d{7}.\d{5}', str(row)).group(0))
                        
                    elif re.search(r'Тип системы', str(row)):
                        os_type_list.append(re.sub(r':\s+', ':', str(row).strip(\[\]\'\')).split(':'))
                    
    main_data.append(['Изготовитель системы','Название ОС','Код продукта','Тип системы'])
    for item in range(len(files)):
        main_data.append([
                    os_prod_list[item],
                    os_name_list[item],
                    os_code_list[item],
                    os_type_list[item]
                    ])        
            
        #print(main_data, os_prod_list, os_name_list, os_code_list, os_type_list)
    return main_data

print(get_data())

def write_to_csv(file, data):
    encoding = getpreferredencoding()
    with open(file, 'w', encoding=encoding) as f_n:
        f_n_writer = csv.writer(f_n)
        for row in data:
            f_n_writer.writerow(row)
    print(f_n)

# write_to_csv(file_for_write, get_data())
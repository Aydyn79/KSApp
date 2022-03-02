import os, glob, csv, re, chardet

path = 'C:\\Users\\Администратор\\Desktop\\Студентам для решения домашнего задания'
file_for_write = 'C:\\Users\\Администратор\\Desktop\\Студентам для решения домашнего задания\\main_data.txt'

def get_data(path):
    files = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for filename in glob.glob(os.path.join(path, '*.txt')):
        if re.match(r'main_data',file_for_write):
            continue
        else:
            files.append(filename)
            
            with open(filename) as f_n:
                f_n_reader = csv.reader(f_n)
                for row in f_n_reader:
                    
                    row =[x.encode('utf-8').decode('utf-8') for x in row]
                    
                    if re.search(r'Изготовитель системы', str(row)):
                        os_prod_list.append(re.search(r'[A-Z]\w+',str(row)).group())
                        
                    elif re.search(r'Название ОС', str(row)):
                        os_name_list.append(re.sub(r'([\[\]\"\'])','', str(row)[36:72:]))
                        
                    elif re.search(r'Код продукта', str(row)):
                        os_code_list.append(re.sub(r'([\[\]\"\'])','', str(row)[36::]))
                        
                    elif re.search(r'Тип системы', str(row)):
                        os_type_list.append(re.sub(r'([\[\]\"\'])','', str(row)[36::]))
                    
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

print(get_data(path))

def write_to_csv(file, data):
    with open(file, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in data:
            f_n_writer.writerow(row)
    print(f_n)

write_to_csv(file_for_write, get_data('C:\\Users\\Администратор\\Desktop\\Студентам для решения домашнего задания'))
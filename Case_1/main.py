import os, glob, csv, re, chardet


def get_txt():
    return glob.glob(os.path.join(os.getcwd(), '*.txt'))


def get_encoding(filename):
    with open(filename, 'br') as f_n:
        detector = chardet.UniversalDetector()
        for row in f_n:
            detector.feed(row)
            if detector.done:
                break
        detector.close()
    return detector.result.get('encoding')


def get_data():
    files = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for filename in get_txt():
        if 'main_data.txt' in re.split(r'\\', filename):
            continue
        else:
            files.append(filename)
            encoding = get_encoding(filename)
            with open(filename, encoding=encoding) as f_n:
                f_n_reader = csv.reader(f_n)
                for row in f_n_reader:
                    if re.search(r'Изготовитель системы', str(row)):
                        os_prod_list.append(re.search(r'[A-Z]{4,}', str(row)).group(0))
                    elif re.search(r'Название ОС', str(row)):
                        os_name_list.append(re.search(r'([A-Z].*)', str(row).strip("[]'")).group(0))
                    elif re.search(r'Код продукта', str(row)):
                        os_code_list.append(re.search(r'\d{5}.....\d{7}.\d{5}', str(row)).group(0))
                    elif re.search(r'Тип системы', str(row)):
                        os_type_list.append(re.search(r'[a-z].*$', str(row).strip("[]'")).group(0))

    main_data.append(['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'])
    for item in range(len(files)):
        main_data.append([
            os_prod_list[item],
            os_name_list[item],
            os_code_list[item],
            os_type_list[item]
        ])
    return main_data


def write_to_csv(csv_file_path):
    with open(csv_file_path, 'w', encoding='utf-8') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in get_data():
            f_n_writer.writerow(row)

if __name__ == "__main__":
    csv_file_path = os.path.join(os.getcwd(), 'main_data.csv')
    write_to_csv(csv_file_path)

    with open('main_data.csv', encoding='utf-8') as f_n:
        print(f_n.read())



from glob import iglob;
import sys;
import json
import csv

def flatten_json(nested_json):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

def write_to_csv(path):
    encodings = ['utf-8-sig', 'utf-16', 'utf-16-le', 'utf-16-be']
    data = {}
    for encoding in encodings:
        try:
            with open(path, 'r', encoding=encoding) as file:
                content = file.read()
                try:
                    if content.strip():
                        data = json.loads(content);
                    else:
                        print(f"{path} is empty")
                except json.JSONDecodeError as e:
                    continue
        except UnicodeDecodeError as e:
            continue
    flattened_json = flatten_json(data)
    csv_file_name = path.split("\\")[-1].split('.')[0]
    with open(f"{sys.path[0]}"+f"/csv/{csv_file_name}.csv", 'w', newline = '') as csv_f:
        writer = csv.DictWriter(csv_f, fieldnames=flattened_json.keys());

        writer.writeheader();

        writer.writerow(flattened_json);


if __name__ == "__main__":
    links = []
    for item in iglob(pathname=f"{sys.path[0]}/data/**/*.json", recursive=True):

        links.append(item)
    for i in links:
        write_to_csv(i)

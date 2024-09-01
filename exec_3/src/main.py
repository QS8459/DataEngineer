import requests;
import gzip;
import json;
import io
import os;
def get_zip_file(url):
    request = requests.get(url);
    compressed_file = io.BytesIO(request.content);
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)
    file_cont = decompressed_file.read()
    decode = file_cont.decode('utf-8')
    return decode;

def get_file_itself(url):
    request = requests.get(url, stream=True, timeout=60)
    if request.ok:
        compressed_file = gzip.GzipFile(fileobj=request.raw);
        for line in compressed_file:
            decoded = line.decode('utf-8');
            yield decoded
    else:
        print("Status code is: ", request.status_code);

def write_stream_to_file(file_path,  content_stream):
    with open(f"{os.getcwd()}/{file_path}", 'w', encoding='utf-8') as f:
        for line in content_stream:
            f.write(line)

if __name__ == "__main__":
    original_url = 'https://data.commoncrawl.org'
    file_to_get_url = 'crawl-data/CC-MAIN-2022-05/wet.paths.gz'

    file=get_zip_file(f"{original_url}/{file_to_get_url}").split('\n')[0]
    write_stream_to_file('title.txt',get_file_itself(f"{original_url}/{file}"))


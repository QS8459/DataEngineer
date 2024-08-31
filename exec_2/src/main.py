#from lxml import html;
#import requests;
#import sys;
#import pandas as pd

if __name__ == "__main__":
     print("Hello World!");
   # url = sys.argv[1]
   # response = requests.get(url);
   # tree = html.fromstring(response.text);

    #files = tree.xpath('//table/tr[position()>3]/td[1]/a/text()');
    #date = tree.xpath('//table/tr[position()>3]/td[2]/text()');
    #index_i_need = 0;
    #for i in range(len(date)):
    #   if i == '2022-02-07 14:03':
    #        index_i_need = i;

    #file_name = files[index_i_need]

    #csv_file = requests.get(f'{url}{file_name}');

    #with open(f"{sys.path[0]}/{file_name}", 'wb') as file:
    #    file.write(csv_file.content);
    #data = pd.read_csv(f'{sys.path[0]}/01001099999.csv', dtype= {
#        'HourlyDryBulbTemperature': 'string'
    #});
    #non_numeric_values = data[~data['HourlyDryBulbTemperature'].str.replace('.', '', 1).str.isdigit()]
    #data['HourlyDryBulbTemperature'] = pd.to_numeric(data['HourlyDryBulbTemperature'], errors='coerce')
    #a = data.HourlyDryBulbTemperature.max();
    #print(data.query('HourlyDryBulbTemperature == @a'));


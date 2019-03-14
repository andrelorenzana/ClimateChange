import re

regex1 = re.compile(r'\s+')
regex2 = re.compile(r'\s{2,}')

def parse_station_file():
    

    with open('ghcnd-stations.txt', 'r') as f:

        output_csv = open('ghcnd-stations.csv', 'w')
        columns = 'ID,LATITUDE,LONGITUDE,ELEVATION,STATE,NAME,GSN-FLAG,HCN/CRN-FLAG,WMO-ID\n'
        output_csv.write(columns)

        for line in f:

            station_id = regex1.sub('', line[0:11])
            latitude = regex1.sub('', line[12:20])
            longitude = regex1.sub('', line[21:30])
            elevation = regex1.sub('', line[31:37])
            state = regex1.sub('', line[38:40])
            name = regex2.sub('', line[41:71])
            gsn_flag = regex1.sub('', line[72:75])
            hcn_crn_flag = regex1.sub('', line[76:79])
            wmo_id = regex1.sub('', line[80:85])

            result = station_id + ',' + latitude + ',' + longitude + ',' + elevation + ',' + state + ',' + name + ',' + gsn_flag + ',' + \
                hcn_crn_flag + ',' + wmo_id + '\n'

            output_csv.write(result)

def insert_column_name(filepath):
    with open(filepath, 'r') as original: data = original.read()
    
    column_names = 'ID,DATE,TYPE,VALUE'

    with open(filepath, 'w') as modified: modified.write(column_names + "\n" + data)
        
def clean_csv(filepath, output_path):
    with open(filepath, 'r') as f:

        output_csv = open(output_path, 'w')
        column_names = 'ID,DATE,TYPE,VALUE\n'
        output_csv.write(column_names)

        for line in f:
            variables = line.split(',')
            result = f'{variables[0]},{variables[1]},{variables[2]},{variables[3]}\n'
            output_csv.write(result)
    

        
def main():
    clean_csv('raw_data/2018.csv', 'clean_data/2018.csv')

if __name__ == "__main__":
    main()
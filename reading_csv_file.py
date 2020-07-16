import csv



def getting_smtp_server(domain):
    print ("Readig file csv list")
    with open('smtp_servers_list.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        smtp_server = "none"
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are: {", ".join(row)}')
                line_count += 1
            elif row[0].lower() == domain.lower() or row[1].lower() == domain.lower():
                #print(f'\t{row[0]} | {row[1]} | {row[2]}.')
                smtp_server = row[2]
            #else:
                #print ("There is no smtp listed for this email")
                #print(f'\t{row[0]} | {row[1]} | {row[2]}.')
                #line_count += 1
        #print(f'Processed {line_count} lines.')
        print ("Getting the SMTP server")
        return smtp_server
        

smtp_server_defined = getting_smtp_server("fgdfgdf.com")

print ("SMTP Server: " + smtp_server_defined)
import csv

""" Script to create the csv file required for the interface configuration"""
source_file = "router_interfaces.csv"

columns = ['Interface','Network','IP_Address','Subnet_Mask','Description','Routing_Protocol']

data = [
    ['E0/0','10.0.0.0','10.0.0.1','255.255.255.0','Red interna','OSPF'],
    ['E0/1','10.0.1.0','10.0.1.1','255.255.255.252','WAN','static'],
    ['E0/2','10.0.2.0','10.0.2.1','255.255.255.0','Invitados','RIP'],
    ['E0/3','10.0.3.0','10.0.3.1','255.255.255.0','Personal externo','EIGRP']
]

with open(source_file,mode='w',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(columns)
    csv_writer.writerows(data)

print("Archivo CSV de interfaces de router creado con exito.")


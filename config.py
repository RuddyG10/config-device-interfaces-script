import csv
from jinja2 import Template
from nornir import InitNornir
from nornir_netmiko import netmiko_send_config, netmiko_send_command
from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result, print_title

# Router interfaces CSV path
source_file = "router_interfaces.csv"
#Template path
interface_template_file = "interface-template.j2"

# saving device configurations
interface_configs=""

# Read the Template file and saving it into a Template object
with open(interface_template_file) as f:
    interface_template = Template(f.read(),keep_trailing_newline=True)

#Read the CSV file
with open(source_file) as f:
    reader = csv.DictReader(f)

    # Save each row of the CSV in a variable and adding it into interface_configs
    for row in reader:
        interface_config = interface_template.render(
            interface = row["Interface"],
            description = row["Description"],
            ip_address= row["IP_Address"],
            subnet_mask = row["Subnet_Mask"],
            routing_protocol = row["Routing_Protocol"],
            network = row["Network"]
        )

        interface_configs += interface_config

# Save interface_configs in a text file
with open("router_interface_config.txt","w") as f:
    f.write(interface_configs)
print("Archivo de configuracion de las interfaces del router generado con exito!")

# Initialize nornir
nr = InitNornir(config_file="config.yaml")

#Function to send all configurations saved in the textfile to all devices
def config(task):

    task.run(
        task=netmiko_send_config,
        config_file="router_interface_config.txt"
    )

#Filter devices per group
devices = nr.filter(F(groups__contains="Ruddy") and F(groups__contains="Routers"))

# Run the script
results = devices.run(task=config)

print_title("Realizando la configuracion...")

#Print all results
print_result(results)
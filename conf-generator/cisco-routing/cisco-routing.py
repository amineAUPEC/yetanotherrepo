
import ipaddress


# main variables def
address="192.168.2.1"
mask="255.255.255.0"



# get last ip for network
def get_last_ip(address, wildcard_mask):
    network = ipaddress.IPv4Network(address+"/"+wildcard_mask, strict=False)
    last_ip=str(network.broadcast_address)
    print("address is : "+address)
    print("wildcard_mask is : "+wildcard_mask)
    print("last_ip is : "+last_ip)
    return last_ip

# get last ip adress
# function for from a mask get wildcard mask
def get_wildcard_mask(mask):
    mask_list=mask.split(".")
    wildcard_mask_list=[]
    for i in mask_list:
        if i == "255":
            wildcard_mask_list.append("0")
        elif i == "0":
            wildcard_mask_list.append("255")
        else:
            wildcard_mask_list.append(i)
    wildcard=".".join(wildcard_mask_list)
    return wildcard

# create a function to get network_address from address and mask
def get_network_address(address, mask):
    network = ipaddress.IPv4Network(address+"/"+mask, strict=False)
    network=str(network.network_address)
    return network

network_address=get_network_address(address, mask)
wildcard_mask=get_wildcard_mask(mask)
print("wildcard_mask: "+wildcard_mask)

# function print_params
def print_params():
    print("parameters : below :  ")
    print("*"*16)
    print("address: "+address)
    print("network_address: "+network_address)
    print("wildcard_mask: "+wildcard_mask)
    print("*"*16)
# create a function  cisco_routing for ospf
def cisco_routing(router_name, mask, address, interface, ospf_process_id, area_id, network_address, wildcard_mask):
    if mask =="": 
        default_mask="255.255.255.0"
        mask=default_mask
    else:
        mask=mask


        print("en")
        print("conf t")
        print("hostname "+router_name)
        print("int "+interface)
        print("ip addr "+address+" "+mask)
        print("ip ospf "+ospf_process_id+ " area "+area_id)
        print("no shutdown")
        print("end")


        print("en")
        print("conf t")
        print("router ospf "+ospf_process_id)
        print("network "+network_address+" "+ wildcard_mask+" area "+area_id)
        print("wildcard "+wildcard_mask + " end")
        # print("network 192.168.2.0 0.0.0.255 area 3")
        # print("network 192.168.2.0 0.0.0.255 area 2")
        # print("network 192.168.3.0 0.0.0.255 area 2")
        print("end")
        return None






def set_address(interface, address, mask):
    print("#set_address :")
    print("#***********************************************************")
    print("en")
    print("conf t ")
    print("int "+ interface)
    print("ip addr "+ " "+ address +" "+mask)
    print("no shutdown")
    print("end")
    print("#***********************************************************")
    return None





list_address=["192.168.1.1", "192.168.1.250"]


def add_address(address, list_address=list_address):
    print("#add_address :")
    print("#***********************************************************")
    print("adding "+ address)
    list_address.append(address)
    print("#***********************************************************")

def generate_vlan(vlan_id, name="vlan_name", optionnal="no"):
    print("#generate_vlan :")
    print("#***********************************************************")
    if optionnal == "no":
        print("en")
        print("conf t")
    print("vlan "+vlan_id)
    print("name "+name)
    print("end")
    print("#***********************************************************")
    return None



def ping_address(list_address):
    print("#ping_address :")
    print("#***********************************************************")
    for i in list_address:
        print("ping "+i)
    print("#***********************************************************")
    return None



def enable_spanning_tree(interface, mode="access", vlan_id="10", protection="true"):
    print("#enable_spanning_tree :")
    print("#***********************************************************")
    print("en")
    print("conf t")
    print("int "+interface)
    print("switchport mode "+mode)
    print("switchport access vlan "+vlan_id)
    if protection == "true":
        print("spanning-tree portfast")
        print("spanning-tree bpduguard enable")
    print("end")
    print("#***********************************************************")
    return None


# calling 
# set_address("gi0/1","209.165.201.1", "255.255.255.224")
# add_address("172.16.1.1",list_address)
# add_address("172.16.1.254")
# ping_address(list_address)
# cisco_routing("R1", mask,address, "s0/1/1", "100", "3", network_address, wildcard_mask)
print_params()


get_last_ip(address, wildcard_mask)

# enable_spanning_tree("s0/1/1")
# enable_spanning_tree("s0/1/1","trunk", "10", "false")


print("getting")

get_network_address("88.200.10.5","255.255.254.0")

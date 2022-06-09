usb_counter = 1


def usb_info(string):
    print(string)
    print("Vendor: " + string.split("Ven_")[1].split("&Prod_")[0])
    print("Product: " + string.split("&Prod_")[1].split("&Rev_")[0])
    print("Serial: " + string.split("#")[2].split("#")[0])


with open("sy.txt") as f:
    for i in f:
        if i.find("Device Install (Hardware initiated)") != -1 and i.find("Ven_") != -1:
            # print(str(usb_counter) + i)
            print(str(usb_counter))
            usb_info(i)
            print(next(f))
            print("-"*165 + "\n")
            usb_counter += 1

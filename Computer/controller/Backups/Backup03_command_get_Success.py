"""
Handling raw data inputs example
Version 0.0.3

Ben Camp
Modified from example
"""
from time import sleep
from msvcrt import kbhit
import re
import pywinusb.hid as hid

#Regex seems to have done the deed.
#Added an output file to see what the raw data is doing.
def sample_handler(data):
    stuff_from_data = format(data)
    numbers_from_data = re.findall(r'\d+', stuff_from_data)
    print numbers_from_data
    size_n = numbers_from_data.__len__() - 1
    x = 0
    while x < size_n:
        file_output.write(numbers_from_data[x])
        file_output.write(', ')
        x += 1
    file_output.write('\n')
    
def raw_test():
    # simple test
    # browse devices...
    all_hids = hid.find_all_hid_devices()
    if all_hids:
        while True:
            print("Choose a device to monitor raw input reports:\n")
            print("0 => Exit")
            for index, device in enumerate(all_hids):
            
                device_name = unicode("{0.vendor_name} {0.product_name}" \
                        "(vID=0x045e, pID=0x02d1)"\
                        "".format(device, device.vendor_id, device.product_id))
                print("{0} => {1}".format(index+1, device_name))
            print("\n\tDevice ('0' to '%d', '0' to exit?) " \
                    "[press enter after number]:" % len(all_hids))
            index_option = raw_input()
            if index_option.isdigit() and int(index_option) <= len(all_hids):
                # invalid
                break;
        int_option = int(index_option)
        if int_option:
            device = all_hids[int_option-1]
            try:
                device.open()

                #set custom raw data handler
                device.set_raw_data_handler(sample_handler)
                
                print("\nWaiting for data...\nPress any (system keyboard) key to stop...")
                while not kbhit() and device.is_plugged():
                    #just keep the device opened to receive events
                    sleep(2)
                return
            finally:
                device.close()
    else:
        print("There's not any non system HID class device available")
#
if __name__ == '__main__':
    # first be kind with local encodings
    import sys
    if sys.version_info >= (3,):
        # as is, don't handle unicodes
        unicode = str
        raw_input = input
    else:
        # allow to show encoded strings
        import codecs
        sys.stdout = codecs.getwriter('mbcs')(sys.stdout)
    file_output = open('output.txt', 'a')
    raw_test()
    file_output.close()
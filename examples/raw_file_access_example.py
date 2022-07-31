
from fisher_py.data import Device, TrayShape
from fisher_py.raw_file_reader import RawFileReaderAdapter


if __name__ == '__main__':
    # Check to see if the RAW file name was supplied as an argument to the program
    filename = "my_file.raw"
    
    # Create the RawFileAccess object for accessing the RAW file
    raw_file = RawFileReaderAdapter.file_factory(filename)
    
    raw_file.select_instrument(Device.MS, 1)
    
    print(f'User labels: {", ".join(raw_file.user_label)}')
    print(raw_file.scan_events)
    print(raw_file)
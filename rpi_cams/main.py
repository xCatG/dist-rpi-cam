
# def parse_config():
#     TODO()
#
# def init_cam():
#     TODO()
#
# def
#

def main():
    # parse config to grab saving location, log location, schedule, frequency and file saving pattern
    config = parse_config()
    # initialize camera; should stop if cam module has trouble and write error to specific location
    init_cam()

    # main loop to save pictures
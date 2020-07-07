import getopt
import socket
import subprocess
import sys
import threading

# Settings
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
    print("""
    BHP Net Tool
    
    Usage: net_tool.py -t TARGET_HOST -p PORT
    
    -l --listen                     - listen for incoming connections
    -e --execute=file               - execute the given file upon receiving connection
    -c --command                    - initialize a command shell
    -u --upload=destination         - upload a file to the destination upon receiving connection
    """)
    sys.exit(0)


def client_sender(buffer):
    pass


def server_loop():
    pass


if __name__ == '__main__':
    global listen
    global execute
    global command
    global upload_destination
    global target
    global port

    if len(sys.argv) > 1:
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for opt, arg in opts:
        if opt == "-h" or opt == "--help":
            usage()
        elif opt == "-l" or opt == "--listen":
            listen = True
        elif opt == "-e" or opt == "--execute":
            execute = arg
        elif opt == "-c" or opt == "--command":
            command = True
        elif opt == "-u" or opt == "--upload":
            upload_destination = arg
        elif opt == "-t" or opt == "--target":
            target = arg
        elif opt == "-p" or opt == "--port":
            port = int(arg)
        else:
            raise Exception(f"Unknown option: {opt}")

    if not listen and len(target) and port:
        buffer = sys.stdin.read()
        client_sender(buffer)

    if listen:
        server_loop()

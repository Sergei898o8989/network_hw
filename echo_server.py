import socket
import re
import http.client
from urllib.parse import urlparse, parse_qs


def handle_request(client_socket, client_address):
    request = client_socket.recv(1024).decode()
    print(f"Received request from {client_address}:\n{request}")

    # Request parsing
    request_line = request.split("\r\n")[0]
    request_method, request_uri, _ = request_line.split(" ")
    parsed_url = urlparse(request_uri)
    query_params = parse_qs(parsed_url.query)
    status_code = query_params.get('status', [200])[0]

    try:
        status_code = int(status_code)
        status_message = http.client.responses.get(status_code, 'Unknown Status Code')
        status_line = f"{status_code} {status_message}"
    except ValueError:
        status_line = "200 OK"

    # Response creation
    response_headers = [
        f"Request Method: {request_method}",
        f"Request Source: {client_address}",
        f"Response Status: {status_line}",
    ]

    for header_line in request.split("\r\n")[1:]:
        if header_line and ':' in header_line:
            response_headers.append(header_line)

    response_body = "\r\n".join(response_headers)
    response = f"HTTP/1.1 {status_line}\r\nContent-Type: text/plain\r\nContent-Length: " \
               f"{len(response_body)}\r\n\r\n{response_body}"
    client_socket.sendall(response.encode())


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)

    print("Server is listening on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection accepted from {client_address}")
        handle_request(client_socket, client_address)
        client_socket.close()


if __name__ == "__main__":
    main()

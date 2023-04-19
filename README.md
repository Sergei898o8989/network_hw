# network_hw

To connect to the server via a browser, follow these steps:

Make sure your Python echo server is running. 
Start it by running the script that you implemented in the previous answer.

Open your preferred web browser.

In the address bar, type the server's address and port number, then press Enter. 
Since the server is listening on port 8080 and bound to '0.0.0.0', you can use the 
following address if you're connecting from the same machine:

http://localhost:8080
If you're connecting from another machine on the same local network, replace "localhost" with the IP address
of the machine running the echo server. For example:

http://192.168.1.100:8080
To test the status code functionality, you can add the status parameter to the URL, like this:

http://localhost:8080/?status=404
This will make the server return a 404 Not Found status.

Press Enter to send the request to the server. 
The browser should display the headers and status code that the server received and processed.
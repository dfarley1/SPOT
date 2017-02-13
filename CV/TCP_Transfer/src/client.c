//-------------------------------------------------------------------------------------------------
//  Auth: David Chalco (0xDC)
//  Desc: The intention of this script is to transfer files through TCP to a LAN server
//  Date: 01-22-2017
//-------------------------------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>

#define BUFFER_SIZE 1024

int main(int argc, char *argv[]) {
    int clientSocket;
    int com_port;
    char *fin_name;
    char *server_ip;
    struct sockaddr_in serverAddr;
    socklen_t addr_size;

    // Verify/Parse input
    if(argc < 4) {
        fprintf(stderr, "Usage: ./client port_number server_ip input_file\n");
        exit(1);
    } else {
        com_port  = atoi(argv[1]);
        server_ip = argv[2];
        fin_name  = argv[3];
    }

    // Create a new socket
    clientSocket = socket(PF_INET, SOCK_STREAM, 0);

    // Configure server settings
    fprintf(stdout, "Configuring server settings:\n\tPORT %d\n\tIP %s\n", com_port, server_ip);
    serverAddr.sin_family = AF_INET;   // Use IP 
    serverAddr.sin_port = htons(com_port);
    serverAddr.sin_addr.s_addr = inet_addr(server_ip);
    memset(serverAddr.sin_zero, '\0', sizeof(serverAddr.sin_zero));

    // Establish socket connection
    fprintf(stdout, "Attempting to connect...\n\n");
    addr_size = sizeof(serverAddr);
    connect(clientSocket, (struct sockaddr*)&serverAddr, addr_size);
    
    // Prepare file descriptor
    char fin_buf[BUFFER_SIZE] = {0};
    FILE *fin = fopen(fin_name, "r");
    if(fin == NULL) {
        fprintf(stderr, "ERROR: Could not open file\n");
        exit(1);
    }

    int byte_count   = 0;
    int bytes_recvd  = 0;
    int bytes_sent   = 0;
    
    // Send/Echo the contents of the file to the server
    while(fgets(fin_buf, sizeof(fin_buf), fin)) {
        // Send and echo a line
        byte_count = send(clientSocket, fin_buf, strlen(fin_buf)+1, 0);
        fprintf(stdout, "\t[Client]: %s", fin_buf);
        
        // Aesthetics
        if(fin_buf[strlen(fin_buf)] != '\n') fprintf(stdout, "\n");
        bytes_sent += byte_count;

        // Reset the buffer
        memset(fin_buf,0,sizeof(fin_buf));
    }

    fprintf(stdout, "Transfer complete.\n");
    fprintf(stdout, "\tRECVD: %d B\n\tSENT : %d\n", bytes_recvd, bytes_sent);
    fclose(fin);
    close(clientSocket);

    //#define SEND_RECV_EXAMPLE
    #ifdef SEND_RECV_EXAMPLE
    char buffer[1024];
    
    // Receive data from server
    recv(clientSocket, buffer, 1024, 0);
    fprintf(stdout, "\t[Server]: %s", buffer);

    // Send data to the server
    memset(buffer,0,sizeof(buffer));
    strcpy(buffer, "This is a message from the client\n");
    send(clientSocket, buffer, strlen(buffer)+1, 0);
    fprintf(stdout, "\t[Client]: %s", buffer);
   
    fprintf(stdout, "\nTransfer complete. Exiting...\n");
    #endif 
    
    fprintf(stdout, "Exiting...\n");
    exit(0);
}

//-------------------------------------------------------------------------------------------------
// Auth: David Chalco (0xDC)
// Desc: The intention of this program is to receive the contents of a client file over TCP and
//       reconstruct/save it locally
// Date: 01-22-2017
// Note:                                  TRANSMISSION PROTOCOL
//                              CLIENT                               SERVER
//                      
//                      Packet[0] = device_ID       ---->           Save ID
//                                .
//                                .
//                      Packet[i] = data[1024]      ---->         Append to file
//                                .
//                                .
//                    Packet[n-1] = "END TRANSMIT"  ---->   Cues end of transmission
//
// TODO: Need to add options to make command more user friendly. Add output suppression 
//       flag capability


#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>

#define BUFFER_SIZE 1024

int main(int argc, char *argv[]){
  int com_port;
  char *server_ip;
  char *fout_name;
  char fout_buf[BUFFER_SIZE];
  int welcomeSocket, newSocket;
  struct sockaddr_in serverAddr;
  struct sockaddr_storage serverStorage;
  socklen_t addr_size;

  // Check for command line input
  if(argc < 4) {
      fprintf(stderr, "Usage ./server port_number server_ip output_file\n");
      exit(1);
  } else {
      com_port  = atoi(argv[1]);
      server_ip = argv[2];
      fout_name = argv[3];
  }
  
  welcomeSocket = socket(PF_INET, SOCK_STREAM, 0);
  // Configure the server settings
  fprintf(stdout, "Attempting to configure server:\n\tPORT %d\n\tIP %s\n", com_port, server_ip);
  serverAddr.sin_family = AF_INET;                                // Configure IP
  serverAddr.sin_port = htons(com_port);                          // Set TCP port
  serverAddr.sin_addr.s_addr = inet_addr(server_ip);              // Set Server IPv4
  memset(serverAddr.sin_zero, '\0', sizeof serverAddr.sin_zero);  

  // Bind communication
  bind(welcomeSocket, (struct sockaddr *) &serverAddr, sizeof(serverAddr));

  // Listen, with a queue of size 5
  if(listen(welcomeSocket,5)==0) {
      fprintf(stdout, "Listening for incoming connections...\n\n");
  } else {
      fprintf(stderr, "ERROR: Failed to listen\n");
      exit(1);
  }

  // Accept new client connection
  addr_size = sizeof serverStorage;
  newSocket = accept(welcomeSocket, (struct sockaddr *) &serverStorage, &addr_size);
  
  // Prepare file descriptors
  FILE *fout = fopen(fout_name, "a+");
  if(fout == NULL) {
      fprintf(stderr, "ERROR: Could not create output file\n");
      exit(1);
  }
  int byte_count  = 0;
  int bytes_recvd = 0;
  int bytes_sent  = 0;

  while(1) {
      // Receive data
      byte_count = recv(newSocket, fout_buf, BUFFER_SIZE, 0);

      // Check for end of transmission
      if(byte_count == 0) {
          fprintf(stdout, "Communication mutually ended\n");
          break;
      } else if(byte_count < 0) {
          fprintf(stderr, "ERROR: Bad packets\n");
          exit(1);
      }


      // Echo to terminal
      fout_buf[byte_count] = '\0';
      fprintf(stdout, "\t[Client]: %s\n", fout_buf);

      bytes_recvd += byte_count;
  }
  /*
  while((byte_count = recv(newSocket, fout_buf, sizeof(fout_buf), 0)) > 0) {
      fprintf(stdout, "bytes = %d\n", byte_count);
      
      // Append to the output file and echo
      fprintf(fout, "%.*s", byte_count, fout_buf);  
      fprintf(stdout, "\t[Client]: %.*s", byte_count, fout_buf);
      //if(fout_buf[strlen(fout_buf)] != '\n') fprintf(stdout, "\n");

      bytes_recvd += byte_count;
  }*/

  // Report any errors
  if(byte_count < 0) {
      fprintf(stderr, "ERROR: Bad packet reception\n");
      exit(1);
  }

  //#define SEND_RECV_EXAMPLE
  #ifdef SEND_RECV_EXAMPLE
  char buffer[1024] = {0};
  // Send message to client
  strcpy(buffer,"Hi client, how are you?\n");
  send(newSocket,buffer,strlen(buffer)+1,0);
  fprintf(stdout, "\t[Server]: %s", buffer);

  // Receive a message fromt the client and echo
  memset(buffer,0,sizeof(buffer));
  recv(newSocket, buffer, sizeof(buffer), 0);
  fprintf(stdout, "\t[Client]: %s", buffer);
  #endif

  // Destroy connections
  close(newSocket);
  close(welcomeSocket);
  fclose(fout);

  fprintf(stdout, "\nTransfer complete.\n\tRECVD: %d B\n\tSENT : %d B\nExiting...\n", bytes_recvd, bytes_sent);
  exit(0);
}

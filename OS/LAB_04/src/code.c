#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main()
{
    int fd;
    char buffer[80];
    static char message[] = "Name: Hassan Rehman\nReg No: BSE203029\nProgram: BSE";
    fd = open("myfile.txt", O_RDWR);
    if (fd != -1)
    {
        printf("My file opened for read/write access\n");
        write(fd, message, sizeof(message));
        lseek(fd, 0, 0); // Makes the cursor go back to start of the message
        read(fd, buffer, sizeof(buffer));
        printf("%s was written in my file\n", buffer);
        close(fd);
    }
    else
        printf("Error");
}
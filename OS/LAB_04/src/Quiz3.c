#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main()
{
    int fd;
    char buffer[80];
    static char message[] = "Name: Hassan Rehman\nCard No: N/A\nDate Of issue: 1-1-2021\nDate of Expiry: 2-2-2025\nBank Name: Bank Alfalah\n";
    printf("%ld\n", message[0] / sizeof(message));
    for (int i = 0; i < message[0] / sizeof(message); i++)
        buffer[i] = message[i];
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
        printf("Error\n");

    return 0;
}
#include <stdio.h>
#include <errno.h>
#include <fcntl.h>

extern int errno;

int main()
{
    int fd = access("text/myfile.txt", F_OK);
    if (fd == -1)
    {
        printf("Error Number: %d\n", errno);
        perror("Error Description: ");
    }
    else
        printf("No error\n");

    return 0;
}
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/syscall.h>
#include <sys/stat.h>
#include <fcntl.h>

extern int errno;
int main()
{
    int fd = access("myfile.txt", F_OK);
    if (fd == -1)
    {
        printf("Error Number: %d\n", errno);
        perror("Error Description: ");
    }
    else
    {
        printf("The file is present in the system\n");
        int fd = open("myfile.txt", O_RDONLY);
        if (fd == -1)
            printf("No permission to open the file\n");
        else
            printf("We have the permission to access the file\n");
    }
}
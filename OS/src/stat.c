#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>

void sfile(char const filename[]);

int main()
{
    ssize_t read;
    char *buffer = 0;
    size_t buff_size = 0;
    printf("Enter the name of the file to check: ");
    read = getline(&buffer, &buff_size, stdin);
    if (read <= 0)
    {
        printf("Getline Failed\n");
        exit(1);
    }

    if (buffer[read - 1] == '\n')
        buffer[read - 1] = 0;

    int s = open(buffer, O_RDONLY);
    if (s == -1)
    {
        printf("File doesn't exist\n");
        exit(1);
    }
    else
        sfile(buffer);

    free(buffer);
    return 0;
}

void sfile(char const filename[])
{
    struct stat sfile;
    if (stat(filename, &sfile) == -1)
        printf("Error Occurred\n");


    // Accessing data members of stat struct
    printf("File st_uid %d", sfile.st_uid);
    printf("\nFile st_blksize %ld", sfile.st_blksize);
    printf("\nFile st_gid %d", sfile.st_gid);
    printf("\nFile st_blocks %ld", sfile.st_blocks);
    printf("\nFile st_size %ld", sfile.st_size);
    printf("\nFile st_nlink %u", (unsigned int)sfile.st_nlink);
    printf("\nFile Permissions User ");
    printf((sfile.st_mode & S_IRUSR) ? "r" : "-");
    printf((sfile.st_mode & S_IWUSR) ? "w" : "-");
    printf((sfile.st_mode & S_IXUSR) ? "x" : "-");
    printf("\nFile Permissions Group ");
    printf((sfile.st_mode & S_IRGRP) ? "r" : "-");
    printf((sfile.st_mode & S_IWGRP) ? "w" : "-");
    printf((sfile.st_mode & S_IXGRP) ? "x" : "-");
    printf("\nFile Permissions Other ");
    printf((sfile.st_mode & S_IROTH) ? "r" : "-");
    printf((sfile.st_mode & S_IWOTH) ? "w" : "-");
    printf((sfile.st_mode & S_IXOTH) ? "x" : "-");
    printf("\n");
    
}
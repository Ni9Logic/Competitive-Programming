#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/file.h>
#include <sys/sendfile.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/fcntl.h>

#define BUFFER_SIZE 67108864

int main()
{
    printf("I/O test with send file and related system calls.\n\n");
    printf("Allocating 64 MB buffer: ");
    char *buffer = (char *)malloc(BUFFER_SIZE); //? This buffer will contain random data in it, We don't care about that.
    printf("Done\n");

    //? Writing the buffer to file out.
    printf("Writing data to the first buffer: ");
    int fout = open("buffer1", O_RDONLY);
    write(fout, &buffer, BUFFER_SIZE);
    close(fout);
    printf("Done\n");

    //? Copying data from first to second.
    int fin = open("buffer1", O_RDONLY);
    fout = open("buffer2", O_RDONLY);
    sendfile(fout, fin, 0, BUFFER_SIZE);
    close(fin);
    close(fout);
    printf("Done\n");

    //? Clearing memory
    printf("Freeing buffer 1: ");
    free(buffer);
    printf("Done\n");

    //? Deleting files
    printf("Deleting Files: ");
    unlink("buffer1");
    unlink("buffer2");
    printf("Done\n");
    return 0;
}
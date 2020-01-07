#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>

uid_t getuid()
{
        printf("SUPER LE SUID\n");
        return 4242;
}

uid_t geteuid()
{
        return 4242;
}


#include <unistd.h>
#include <sys/types.h>

uid_t getuid()
{
        return 4242;
}

uid_t geteuid()
{
        return 4242;
}


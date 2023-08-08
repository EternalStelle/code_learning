#include <stdio.h>
#include <inttypes.h>//inttypes.h支持可移植类型
int main(void)
{
    int32_t me32;
    me32 = 45933945;
    printf("First assume int32_t is int: ");
    printf("%d\n", me32);
    printf("Next let's not make any assumptions.\n");
    printf("Instead, use a \"macro\" from inttypes.h\n");
    //参数PRId32被inttypes.h的d替换，相当于%d
    printf("me32=%" PRId32 "\n", me32);
    return 0;
}
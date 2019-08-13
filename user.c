#include<stdio.h>

#include<string.h>


int main()
{
    
    int x = 3;
    
    char * s1 = "arad";
    
    char * s2 = "arae";
    
    int cmp = strcmp(s1, s2);
    
    printf("%d\n", cmp);
    
    return 0;
}
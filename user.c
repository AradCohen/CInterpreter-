#include<stdio.h>

#include<string.h>


int main()
{
    
    int x = 3;
    
    char *s1 = "aaa";
    
    char *s2 = "bbb";
    
    int cmp = strcmp(s1, s2);
    
    printf("%d", cmp);
    
    return 0;
}
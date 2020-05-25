#include<stdio.h>
#include<stdlib.h>
void main()
{
    int n,s,i;
    printf("Enter the length of the series : ");
    scanf("%d",&n);
    for( i=0;i<n;i++)
    {
        s=i*(i+1)/2;
        printf("%d ",s);
    }
}

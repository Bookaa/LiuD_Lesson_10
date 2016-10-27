#include <stdio.h>

#if 0
long a=10000,b,c=2800,d,e,f[2801],g;
main()
{
    for(;b-c;)
        f[b++]=a/5;
    for(;d=0,g=c*2;c-=14,printf("%.4d",e+d/a),e=d%a)
        for(b=c;d+=f[b]*a,f[b]=d%--g,d/=g--,--b;d*=b);
}
#endif

int main()
{
    int c=2800,f[2801];
    for (int b = 0; b < c; b++)
        f[b] = 10000 / 5;
    f[c] = 0;
    int e = 0;
    while (c != 0) {
        int d = 0;
        int b = c;
        while (1) {
            d += f[b] * 10000;
            f[b] = d % (b * 2 - 1);
            d /= (b * 2 - 1);
            b--;
            if (b == 0)
                break;
            d *= b;
        }
        c -= 14;
        printf("%.4d", e + d / 10000);
        e = d % 10000;
    }
    printf("\n");
    return 0;
}


# LiuD_Lesson_10
LiuD lesson ten

I find a simple C code to get PI:

    #include <stdio.h>

    long a=10000,b,c=2800,d,e,f[2801],g;
    main()
    {
        for(;b-c;)
            f[b++]=a/5;
        for(;d=0,g=c*2;c-=14,printf("%.4d",e+d/a),e=d%a)
            for(b=c;d+=f[b]*a,f[b]=d%--g,d/=g--,--b;d*=b);
    }

I reformat it to:

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

Lets try to parse it.

Its LiuD describe:

    option.prefix = CPP
    states.skip = crlf
    basic.CSTR = '"[^"\\]*(?:\\.[^"\\]*)*"'

    main = gstmt*

    gstmt := funcdef | declare
        funcdef = datatype NAME '(' params? ')' '{' stmt* '}'
        params = param ^* ','
        param = datatype NAME

    declare0 = datatype newvars
        newvars = declvar ^* ','
    declare = declare0 ';'
    declvar := declvar_array | declvar_assign | litname
        declvar_array = NAME '[' NUMBER ']'
        declvar_assign = NAME '=' value

    stmt_0 := declare0 | assign | augassign | vpp | value
        augassign = dest ('+=' | '-=' | '/=' | '*=') value
        assign = dest '=' value
        dest := dest_array | litname
            dest_array = NAME '[' value ']'
        vpp = NAME ('++' | '--')
    stmt_2 = stmt_0? ';'
    stmt := if_stmt | while_stmt | for_stmt | stmt_2 | return_stmt
        if_stmt = 'if' '(' value ')' block else_part?
            else_part = 'else' block
        while_stmt = 'while' '(' value ')' block
        for_stmt = 'for' '(' stmt_0? ';' value? ';' stmt_0? ')' block
        return_stmt = 'return' value ';'

    block := stmt | enclosedblock
        enclosedblock = '{' stmt* '}'

    datatype = 'int' | 'long'

    value0 = NUMBER | NAME | CSTR
    value1 := enclosed | funccall | array_index | value0
        enclosed = '(' value ')'
        funccall = NAME '(' arg? ')'
            arg = value ^* ','
        array_index = NAME '[' value ']'
    value2 := signed | value1
        signed = ('-' | '+') value1
    binvalue = value2, (, ('*' '/') ('+' '-') '%' ('>=' '>' '<=' '<' '==' '!=')) value1
    value := binvalue

    litname = NAME

some new GDL syntax need,

    basic.NAME = STRING
    jiad = NAME '^*' STRING     means ABAB...A, that is A separated by B, at least one A
    itemq = value1 '?'          means can have a item or not


Even more, I write the PI in Python format, and parse it:

    def main():
        c = 2800
        f = [10000 / 5] * 2801
        f[c] = 0
        e = 0
        while c != 0:
            d = 0
            b = c
            while True:
                d += f[b] * 10000
                f[b] = d % (b * 2 - 1)
                d /= (b * 2 - 1)
                b -= 1
                if b == 0:
                    break
                d *= b

            c -= 14
            print '%04d' % (e + d / 10000),
            e = d % 10000

        print

    main()


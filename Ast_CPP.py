# auto generated

# LiuD syntax :

# option.prefix = CPP
#     states.skip = crlf
#     basic.CSTR = '"[^"\\]*(?:\\.[^"\\]*)*"'
# 
#     main = gstmt*
# 
#     gstmt := funcdef | declare
#         funcdef = datatype NAME '(' params? ')' '{' stmt* '}'
#         params = param ^* ','
#         param = datatype NAME
# 
#     declare0 = datatype newvars
#         newvars = declvar ^* ','
#     declare = declare0 ';'
#     declvar := declvar_array | declvar_assign | litname
#         declvar_array = NAME '[' NUMBER ']'
#         declvar_assign = NAME '=' value
# 
#     stmt_0 := declare0 | assign | augassign | vpp | value
#         augassign = dest ('+=' | '-=' | '/=' | '*=') value
#         assign = dest '=' value
#         dest := dest_array | litname
#             dest_array = NAME '[' value ']'
#         vpp = NAME ('++' | '--')
#     stmt_2 = stmt_0? ';'
#     stmt := if_stmt | while_stmt | for_stmt | stmt_2 | return_stmt
#         if_stmt = 'if' '(' value ')' block else_part?
#             else_part = 'else' block
#         while_stmt = 'while' '(' value ')' block
#         for_stmt = 'for' '(' stmt_0? ';' value? ';' stmt_0? ')' block
#         return_stmt = 'return' value ';'
# 
#     block := stmt | enclosedblock
#         enclosedblock = '{' stmt* '}'
# 
#     datatype = 'int' | 'long'
# 
#     value0 = NUMBER | NAME | CSTR
#     value1 := enclosed | funccall | array_index | value0
#         enclosed = '(' value ')'
#         funccall = NAME '(' arg? ')'
#             arg = value ^* ','
#         array_index = NAME '[' value ']'
#     value2 := signed | value1
#         signed = ('-' | '+') value1
#     binvalue = value2, (, ('*' '/') ('+' '-') '%' ('>=' '>' '<=' '<' '==' '!=')) value1
#     value := binvalue
# 
#     litname = NAME
#     

from GDL_common import *

class CPP_main:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_main(self)

class CPP_funcdef:
    def __init__(self, v, s, vq, vlst):
        self.v = v
        self.s = s
        self.vq = vq
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_funcdef(self)

class CPP_params:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_params(self)

class CPP_param:
    def __init__(self, v, s):
        self.v = v
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_param(self)

class CPP_declare0:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_declare0(self)

class CPP_newvars:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_newvars(self)

class CPP_declare:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_declare(self)

class CPP_declvar_array:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def walkabout(self, visitor):
        return visitor.visit_declvar_array(self)

class CPP_declvar_assign:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_declvar_assign(self)

class CPP_augassign:
    def __init__(self, v1, s, v2):
        self.v1 = v1
        self.s = s
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_augassign(self)

class CPP_assign:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_assign(self)

class CPP_dest_array:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_dest_array(self)

class CPP_vpp:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def walkabout(self, visitor):
        return visitor.visit_vpp(self)

class CPP_stmt_2:
    def __init__(self, vq):
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_stmt_2(self)

class CPP_if_stmt:
    def __init__(self, v1, v2, vq):
        self.v1 = v1
        self.v2 = v2
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_if_stmt(self)

class CPP_else_part:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_else_part(self)

class CPP_while_stmt:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_while_stmt(self)

class CPP_for_stmt:
    def __init__(self, vq1, vq2, vq3, v):
        self.vq1 = vq1
        self.vq2 = vq2
        self.vq3 = vq3
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_for_stmt(self)

class CPP_return_stmt:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_return_stmt(self)

class CPP_enclosedblock:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_enclosedblock(self)

class CPP_datatype:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_datatype(self)

class CPP_value0:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_value0(self)

class CPP_enclosed:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_enclosed(self)

class CPP_funccall:
    def __init__(self, s, vq):
        self.s = s
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_funccall(self)

class CPP_arg:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_arg(self)

class CPP_array_index:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_array_index(self)

class CPP_signed:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_signed(self)

class CPP_binvalue:
    def __init__(self, v1, s, v2):
        self.v1 = v1
        self.s = s
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_binvalue(self)

class CPP_litname:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_litname(self)

class CPP_Parser(Parser00):
    def handle_CSTR(self):
        pattn = r'"[^"\\]*(?:\\.[^"\\]*)*"'
        return self.handle_basic(pattn)

    def handle_main(self):
        v = self.hdl_gstmt()
        if not v:
            return None
        savpos = self.pos
        vlst = [v]
        while True:
            self.skipspacecrlf()
            v = self.hdl_gstmt()
            if not v:
                break
            vlst.append(v)
            savpos = self.pos
        self.restorepos(savpos)
        return CPP_main(vlst)

    def hdl_gstmt(self):
        v = self.handle_funcdef()
        if not v:
            v = self.handle_declare()
        if not v:
            return None
        return v

    def handle_funcdef(self):
        savpos = self.pos
        v = self.handle_datatype()
        if not v:
            return None
        self.skipspacecrlf()
        s = self.handle_NAME()
        if not s:
            return self.restorepos(savpos)
        self.skipspacecrlf()
        if not self.handle_str('('):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        vq = self.handle_params()
        self.skipspacecrlf()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        if not self.handle_str('{'):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        vlst = []
        savpos2 = self.pos
        while True:
            v_ = self.hdl_stmt()
            if not v_:
                break
            vlst.append(v_)
            savpos2 = self.pos
            self.skipspacecrlf()
        self.restorepos(savpos2)
        self.skipspacecrlf()
        if not self.handle_str('}'):
            return self.restorepos(savpos)
        return CPP_funcdef(v, s, vq, vlst)

    def handle_params(self):
        s = self.handle_param()
        if not s:
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspacecrlf()
            if not self.handle_str(','):
                break
            self.skipspacecrlf()
            s = self.handle_param()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        return CPP_params(vlst)

    def handle_param(self):
        savpos = self.pos
        v = self.handle_datatype()
        if not v:
            return None
        self.skipspacecrlf()
        s = self.handle_NAME()
        if not s:
            return self.restorepos(savpos)
        return CPP_param(v, s)

    def handle_declare0(self):
        savpos = self.pos
        v1 = self.handle_datatype()
        if not v1:
            return None
        self.skipspacecrlf()
        v2 = self.handle_newvars()
        if not v2:
            return self.restorepos(savpos)
        return CPP_declare0(v1, v2)

    def handle_newvars(self):
        s = self.hdl_declvar()
        if not s:
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspacecrlf()
            if not self.handle_str(','):
                break
            self.skipspacecrlf()
            s = self.hdl_declvar()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        return CPP_newvars(vlst)

    def handle_declare(self):
        savpos = self.pos
        v = self.handle_declare0()
        if not v:
            return None
        self.skipspacecrlf()
        if not self.handle_str(';'):
            return self.restorepos(savpos)
        return CPP_declare(v)

    def hdl_declvar(self):
        v = self.handle_declvar_array()
        if not v:
            v = self.handle_declvar_assign()
        if not v:
            v = self.handle_litname()
        if not v:
            return None
        return v

    def handle_declvar_array(self):
        savpos = self.pos
        s1 = self.handle_NAME()
        if not s1:
            return None
        self.skipspacecrlf()
        if not self.handle_str('['):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        s2 = self.handle_NUMBER()
        if not s2:
            return self.restorepos(savpos)
        self.skipspacecrlf()
        if not self.handle_str(']'):
            return self.restorepos(savpos)
        return CPP_declvar_array(s1, s2)

    def handle_declvar_assign(self):
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            return None
        self.skipspacecrlf()
        if not self.handle_str('='):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        return CPP_declvar_assign(s, v)

    def hdl_stmt_0(self):
        v = self.handle_declare0()
        if not v:
            v = self.handle_assign()
        if not v:
            v = self.handle_augassign()
        if not v:
            v = self.handle_vpp()
        if not v:
            v = self.hdl_value()
        if not v:
            return None
        return v

    def handle_augassign(self):
        savpos = self.pos
        v1 = self.hdl_dest()
        if not v1:
            return None
        self.skipspacecrlf()
        s = self.handle_str('+=')
        if not s:
            s = self.handle_str('-=')
        if not s:
            s = self.handle_str('/=')
        if not s:
            s = self.handle_str('*=')
        if not s:
            return self.restorepos(savpos)
        self.skipspacecrlf()
        v2 = self.hdl_value()
        if not v2:
            return self.restorepos(savpos)
        return CPP_augassign(v1, s, v2)

    def handle_assign(self):
        savpos = self.pos
        v1 = self.hdl_dest()
        if not v1:
            return None
        self.skipspacecrlf()
        if not self.handle_str('='):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        v2 = self.hdl_value()
        if not v2:
            return self.restorepos(savpos)
        return CPP_assign(v1, v2)

    def hdl_dest(self):
        v = self.handle_dest_array()
        if not v:
            v = self.handle_litname()
        if not v:
            return None
        return v

    def handle_dest_array(self):
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            return None
        self.skipspacecrlf()
        if not self.handle_str('['):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        self.skipspacecrlf()
        if not self.handle_str(']'):
            return self.restorepos(savpos)
        return CPP_dest_array(s, v)

    def handle_vpp(self):
        savpos = self.pos
        s1 = self.handle_NAME()
        if not s1:
            return None
        self.skipspacecrlf()
        s2 = self.handle_str('++')
        if not s2:
            s2 = self.handle_str('--')
        if not s2:
            return self.restorepos(savpos)
        return CPP_vpp(s1, s2)

    def handle_stmt_2(self):
        savpos = self.pos
        vq = self.hdl_stmt_0()
        self.skipspacecrlf()
        if not self.handle_str(';'):
            return self.restorepos(savpos)
        return CPP_stmt_2(vq)

    def hdl_stmt(self):
        v = self.handle_if_stmt()
        if not v:
            v = self.handle_while_stmt()
        if not v:
            v = self.handle_for_stmt()
        if not v:
            v = self.handle_stmt_2()
        if not v:
            v = self.handle_return_stmt()
        if not v:
            return None
        return v

    def handle_if_stmt(self):
        savpos = self.pos
        if not self.handle_str('if'):
            return None
        self.skipspacecrlf()
        if not self.handle_str('('):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        v1 = self.hdl_value()
        if not v1:
            return self.restorepos(savpos)
        self.skipspacecrlf()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        v2 = self.hdl_block()
        if not v2:
            return self.restorepos(savpos)
        self.skipspacecrlf()
        vq = self.handle_else_part()
        return CPP_if_stmt(v1, v2, vq)

    def handle_else_part(self):
        savpos = self.pos
        if not self.handle_str('else'):
            return None
        self.skipspacecrlf()
        v = self.hdl_block()
        if not v:
            return self.restorepos(savpos)
        return CPP_else_part(v)

    def handle_while_stmt(self):
        savpos = self.pos
        if not self.handle_str('while'):
            return None
        self.skipspacecrlf()
        if not self.handle_str('('):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        v1 = self.hdl_value()
        if not v1:
            return self.restorepos(savpos)
        self.skipspacecrlf()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        v2 = self.hdl_block()
        if not v2:
            return self.restorepos(savpos)
        return CPP_while_stmt(v1, v2)

    def handle_for_stmt(self):
        savpos = self.pos
        if not self.handle_str('for'):
            return None
        self.skipspacecrlf()
        if not self.handle_str('('):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        vq1 = self.hdl_stmt_0()
        self.skipspacecrlf()
        if not self.handle_str(';'):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        vq2 = self.hdl_value()
        self.skipspacecrlf()
        if not self.handle_str(';'):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        vq3 = self.hdl_stmt_0()
        self.skipspacecrlf()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        v = self.hdl_block()
        if not v:
            return self.restorepos(savpos)
        return CPP_for_stmt(vq1, vq2, vq3, v)

    def handle_return_stmt(self):
        savpos = self.pos
        if not self.handle_str('return'):
            return None
        self.skipspacecrlf()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        self.skipspacecrlf()
        if not self.handle_str(';'):
            return self.restorepos(savpos)
        return CPP_return_stmt(v)

    def hdl_block(self):
        v = self.hdl_stmt()
        if not v:
            v = self.handle_enclosedblock()
        if not v:
            return None
        return v

    def handle_enclosedblock(self):
        savpos = self.pos
        if not self.handle_str('{'):
            return None
        self.skipspacecrlf()
        vlst = []
        savpos2 = self.pos
        while True:
            v_ = self.hdl_stmt()
            if not v_:
                break
            vlst.append(v_)
            savpos2 = self.pos
            self.skipspacecrlf()
        self.restorepos(savpos2)
        self.skipspacecrlf()
        if not self.handle_str('}'):
            return self.restorepos(savpos)
        return CPP_enclosedblock(vlst)

    def handle_datatype(self):
        s = self.handle_str('int')
        if not s:
            s = self.handle_str('long')
        if not s:
            return None
        return CPP_datatype(s)

    def handle_value0(self):
        s = self.handle_NUMBER()
        if not s:
            s = self.handle_NAME()
        if not s:
            s = self.handle_CSTR()
        if not s:
            return None
        return CPP_value0(s)

    def hdl_value1(self):
        v = self.handle_enclosed()
        if not v:
            v = self.handle_funccall()
        if not v:
            v = self.handle_array_index()
        if not v:
            v = self.handle_value0()
        if not v:
            return None
        return v

    def handle_enclosed(self):
        savpos = self.pos
        if not self.handle_str('('):
            return None
        self.skipspacecrlf()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        self.skipspacecrlf()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        return CPP_enclosed(v)

    def handle_funccall(self):
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            return None
        self.skipspacecrlf()
        if not self.handle_str('('):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        vq = self.handle_arg()
        self.skipspacecrlf()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        return CPP_funccall(s, vq)

    def handle_arg(self):
        s = self.hdl_value()
        if not s:
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspacecrlf()
            if not self.handle_str(','):
                break
            self.skipspacecrlf()
            s = self.hdl_value()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        return CPP_arg(vlst)

    def handle_array_index(self):
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            return None
        self.skipspacecrlf()
        if not self.handle_str('['):
            return self.restorepos(savpos)
        self.skipspacecrlf()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        self.skipspacecrlf()
        if not self.handle_str(']'):
            return self.restorepos(savpos)
        return CPP_array_index(s, v)

    def hdl_value2(self):
        v = self.handle_signed()
        if not v:
            v = self.hdl_value1()
        if not v:
            return None
        return v

    def handle_signed(self):
        savpos = self.pos
        s = self.handle_str('-')
        if not s:
            s = self.handle_str('+')
        if not s:
            return None
        self.skipspacecrlf()
        v = self.hdl_value1()
        if not v:
            return self.restorepos(savpos)
        return CPP_signed(s, v)

    def handle_binvalue(self):
        v1 = self.hdl_value2()
        if not v1:
            return None
        def multiop1(v1):
            while True:
                savpos = self.pos
                self.skipspacecrlf()
                for s in ['*', '/']:
                    if self.handle_str(s):
                        break
                else:
                    self.restorepos(savpos)
                    return v1
                self.skipspacecrlf()
                v2 = self.hdl_value1()
                if not v2:
                    self.restorepos(savpos)
                    return v1
                v1 = CPP_binvalue(v1, s, v2)
        def multiop2(v1):
            v1 = multiop1(v1)
            while True:
                savpos = self.pos
                self.skipspacecrlf()
                for s in ['+', '-']:
                    if self.handle_str(s):
                        break
                else:
                    self.restorepos(savpos)
                    return v1
                self.skipspacecrlf()
                v2 = self.hdl_value1()
                if not v2:
                    self.restorepos(savpos)
                    return v1
                v2 = multiop1(v2)
                v1 = CPP_binvalue(v1, s, v2)
        def multiop3(v1):
            v1 = multiop2(v1)
            while True:
                savpos = self.pos
                self.skipspacecrlf()
                for s in ['%']:
                    if self.handle_str(s):
                        break
                else:
                    self.restorepos(savpos)
                    return v1
                self.skipspacecrlf()
                v2 = self.hdl_value1()
                if not v2:
                    self.restorepos(savpos)
                    return v1
                v2 = multiop2(v2)
                v1 = CPP_binvalue(v1, s, v2)
        def multiop4(v1):
            v1 = multiop3(v1)
            while True:
                savpos = self.pos
                self.skipspacecrlf()
                for s in ['>=', '>', '<=', '<', '==', '!=']:
                    if self.handle_str(s):
                        break
                else:
                    self.restorepos(savpos)
                    return v1
                self.skipspacecrlf()
                v2 = self.hdl_value1()
                if not v2:
                    self.restorepos(savpos)
                    return v1
                v2 = multiop3(v2)
                v1 = CPP_binvalue(v1, s, v2)
        return multiop4(v1)

    def hdl_value(self):
        v = self.handle_binvalue()
        if not v:
            return None
        return v

    def handle_litname(self):
        s = self.handle_NAME()
        if not s:
            return None
        return CPP_litname(s)

class CPP_output:
    def __init__(self, outp):
        self.outp = outp
    def visit_main(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_gstmt(self, node):
        node.v.walkabout(self)
    def visit_funcdef(self, node):
        node.v.walkabout(self)
        self.outp.puts(node.s)
        self.outp.puts('(')
        if node.vq:
            node.vq.walkabout(self)
        self.outp.puts(')')
        self.outp.puts('{')
        for v in node.vlst:
            v.walkabout(self)
        self.outp.puts('}')
    def visit_params(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_param(self, node):
        node.v.walkabout(self)
        self.outp.puts(node.s)
    def visit_declare0(self, node):
        node.v1.walkabout(self)
        node.v2.walkabout(self)
    def visit_newvars(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_declare(self, node):
        node.v.walkabout(self)
        self.outp.puts(';')
    def visit_declvar(self, node):
        node.v.walkabout(self)
    def visit_declvar_array(self, node):
        self.outp.puts(node.s1)
        self.outp.puts('[')
        self.outp.puts(node.s2)
        self.outp.puts(']')
    def visit_declvar_assign(self, node):
        self.outp.puts(node.s)
        self.outp.puts('=')
        node.v.walkabout(self)
    def visit_stmt_0(self, node):
        node.v.walkabout(self)
    def visit_augassign(self, node):
        node.v1.walkabout(self)
        self.outp.puts(node.s)
        node.v2.walkabout(self)
    def visit_assign(self, node):
        node.v1.walkabout(self)
        self.outp.puts('=')
        node.v2.walkabout(self)
    def visit_dest(self, node):
        node.v.walkabout(self)
    def visit_dest_array(self, node):
        self.outp.puts(node.s)
        self.outp.puts('[')
        node.v.walkabout(self)
        self.outp.puts(']')
    def visit_vpp(self, node):
        self.outp.puts(node.s1)
        self.outp.puts(node.s2)
    def visit_stmt_2(self, node):
        if node.vq:
            node.vq.walkabout(self)
        self.outp.puts(';')
    def visit_stmt(self, node):
        node.v.walkabout(self)
    def visit_if_stmt(self, node):
        self.outp.puts('if')
        self.outp.puts('(')
        node.v1.walkabout(self)
        self.outp.puts(')')
        node.v2.walkabout(self)
        if node.vq:
            node.vq.walkabout(self)
    def visit_else_part(self, node):
        self.outp.puts('else')
        node.v.walkabout(self)
    def visit_while_stmt(self, node):
        self.outp.puts('while')
        self.outp.puts('(')
        node.v1.walkabout(self)
        self.outp.puts(')')
        node.v2.walkabout(self)
    def visit_for_stmt(self, node):
        self.outp.puts('for')
        self.outp.puts('(')
        if node.vq1:
            node.vq1.walkabout(self)
        self.outp.puts(';')
        if node.vq2:
            node.vq2.walkabout(self)
        self.outp.puts(';')
        if node.vq3:
            node.vq3.walkabout(self)
        self.outp.puts(')')
        node.v.walkabout(self)
    def visit_return_stmt(self, node):
        self.outp.puts('return')
        node.v.walkabout(self)
        self.outp.puts(';')
    def visit_block(self, node):
        node.v.walkabout(self)
    def visit_enclosedblock(self, node):
        self.outp.puts('{')
        for v in node.vlst:
            v.walkabout(self)
        self.outp.puts('}')
    def visit_datatype(self, node):
        self.outp.puts(node.s)
    def visit_value0(self, node):
        self.outp.puts(node.s)
    def visit_value1(self, node):
        node.v.walkabout(self)
    def visit_enclosed(self, node):
        self.outp.puts('(')
        node.v.walkabout(self)
        self.outp.puts(')')
    def visit_funccall(self, node):
        self.outp.puts(node.s)
        self.outp.puts('(')
        if node.vq:
            node.vq.walkabout(self)
        self.outp.puts(')')
    def visit_arg(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_array_index(self, node):
        self.outp.puts(node.s)
        self.outp.puts('[')
        node.v.walkabout(self)
        self.outp.puts(']')
    def visit_value2(self, node):
        node.v.walkabout(self)
    def visit_signed(self, node):
        self.outp.puts(node.s)
        node.v.walkabout(self)
    def visit_binvalue(self, node):
        node.v1.walkabout(self)
        self.outp.puts(node.s)
        node.v2.walkabout(self)
    def visit_value(self, node):
        node.v.walkabout(self)
    def visit_litname(self, node):
        self.outp.puts(node.s)

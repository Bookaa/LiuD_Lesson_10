# auto generated

# LiuD syntax :

# option.prefix = PY
#     states.skip = no
#     stmts = (IDENT stmt)*
#     deepstmts = IDENTIN stmts IDENTOUT
# 
#     states.skip = space
# 
#     main = stmts
# 
#     stmt := if_stmt | while_stmt | return_stmt | print_stmt | funcdef | assign | augassign | value
#         if_stmt = 'if' value ':' deepstmts else_part?
#             else_part = IDENT 'else' ':' deepstmts
#         while_stmt = 'while' value ':' deepstmts else_part?
#         return_stmt = 'return' value
#         funcdef = 'def' NAME '(' params? ')' ':' deepstmts
#             params = NAME ^* ','
#         augassign = dest ('+=' | '-=' | '/=' | '*=') value
#         assign = dest '=' value
#         dest := dest_array | litname
#             dest_array = NAME '[' value ']'
#         print_stmt = 'print' args? ','?
#             args = value ^* ','
# 
#     value_bool = 'True' | 'False'
#     value0 = NUMBER | NAME | STRING
#     value1 := enclosed | funccall | array_index | value_bool | value0
#         enclosed = '(' value ')'
#         funccall = NAME '(' arg? ')'
#             arg = value ^* ','
#         array_index = NAME '[' value ']'
#     value2 := signed | array | value1
#         signed = ('-' | '+') value1
#         array = '[' arg? ','? ']'
#     binvalue = value2, (, ('*' '/') ('+' '-') '%' ('>=' '>' '<=' '<' '==' '!=')) value1
#     value := binvalue
# 
#     litname = NAME
#     

from GDL_common import *

class PY_stmts:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_stmts(self)

class PY_deepstmts:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_deepstmts(self)

class PY_main:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_main(self)

class PY_if_stmt:
    def __init__(self, v1, v2, vq):
        self.v1 = v1
        self.v2 = v2
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_if_stmt(self)

class PY_else_part:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_else_part(self)

class PY_while_stmt:
    def __init__(self, v1, v2, vq):
        self.v1 = v1
        self.v2 = v2
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_while_stmt(self)

class PY_return_stmt:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_return_stmt(self)

class PY_funcdef:
    def __init__(self, s, vq, v):
        self.s = s
        self.vq = vq
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_funcdef(self)

class PY_params:
    def __init__(self, slst):
        self.slst = slst
    def walkabout(self, visitor):
        return visitor.visit_params(self)

class PY_augassign:
    def __init__(self, v1, s, v2):
        self.v1 = v1
        self.s = s
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_augassign(self)

class PY_assign:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_assign(self)

class PY_dest_array:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_dest_array(self)

class PY_print_stmt:
    def __init__(self, vq, sq):
        self.vq = vq
        self.sq = sq
    def walkabout(self, visitor):
        return visitor.visit_print_stmt(self)

class PY_args:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_args(self)

class PY_value_bool:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_value_bool(self)

class PY_value0:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_value0(self)

class PY_enclosed:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_enclosed(self)

class PY_funccall:
    def __init__(self, s, vq):
        self.s = s
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_funccall(self)

class PY_arg:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_arg(self)

class PY_array_index:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_array_index(self)

class PY_signed:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_signed(self)

class PY_array:
    def __init__(self, vq, sq):
        self.vq = vq
        self.sq = sq
    def walkabout(self, visitor):
        return visitor.visit_array(self)

class PY_binvalue:
    def __init__(self, v1, s, v2):
        self.v1 = v1
        self.s = s
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_binvalue(self)

class PY_litname:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_litname(self)

class PY_Parser(Parser00):

    def handle_stmts(self):
        vlst = []
        savpos = self.pos
        while True:
            if not self.handle_IDENT():
                break
            v = self.hdl_stmt()
            if not v:
                break
            vlst.append(v)
            savpos = self.pos
        self.restorepos(savpos)
        if not vlst:
            return None
        return PY_stmts(vlst)

    def handle_deepstmts(self):
        savpos = self.pos
        if not self.handle_IDENTIN():
            return None
        v = self.handle_stmts()
        if not v:
            return self.restorepos(savpos)
        if not self.handle_IDENTOUT():
            return self.restorepos(savpos)
        return PY_deepstmts(v)

    def handle_main(self):
        v = self.handle_stmts()
        if not v:
            return None
        return PY_main(v)

    def hdl_stmt(self):
        v = self.handle_if_stmt()
        if not v:
            v = self.handle_while_stmt()
        if not v:
            v = self.handle_return_stmt()
        if not v:
            v = self.handle_print_stmt()
        if not v:
            v = self.handle_funcdef()
        if not v:
            v = self.handle_assign()
        if not v:
            v = self.handle_augassign()
        if not v:
            v = self.hdl_value()
        if not v:
            return None
        return v

    def handle_if_stmt(self):
        savpos = self.pos
        if not self.handle_str('if'):
            return None
        self.skipspace()
        v1 = self.hdl_value()
        if not v1:
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.handle_deepstmts()
        if not v2:
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_else_part()
        return PY_if_stmt(v1, v2, vq)

    def handle_else_part(self):
        savpos = self.pos
        if not self.handle_IDENT():
            return None
        self.skipspace()
        if not self.handle_str('else'):
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            return self.restorepos(savpos)
        self.skipspace()
        v = self.handle_deepstmts()
        if not v:
            return self.restorepos(savpos)
        return PY_else_part(v)

    def handle_while_stmt(self):
        savpos = self.pos
        if not self.handle_str('while'):
            return None
        self.skipspace()
        v1 = self.hdl_value()
        if not v1:
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.handle_deepstmts()
        if not v2:
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_else_part()
        return PY_while_stmt(v1, v2, vq)

    def handle_return_stmt(self):
        savpos = self.pos
        if not self.handle_str('return'):
            return None
        self.skipspace()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        return PY_return_stmt(v)

    def handle_funcdef(self):
        savpos = self.pos
        if not self.handle_str('def'):
            return None
        self.skipspace()
        s = self.handle_NAME()
        if not s:
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str('('):
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_params()
        self.skipspace()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            return self.restorepos(savpos)
        self.skipspace()
        v = self.handle_deepstmts()
        if not v:
            return self.restorepos(savpos)
        return PY_funcdef(s, vq, v)

    def handle_params(self):
        s = self.handle_NAME()
        if not s:
            return None
        savpos = self.pos
        slst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.handle_NAME()
            if not s:
                break
            slst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        return PY_params(slst)

    def handle_augassign(self):
        savpos = self.pos
        v1 = self.hdl_dest()
        if not v1:
            return None
        self.skipspace()
        s = self.handle_str('+=')
        if not s:
            s = self.handle_str('-=')
        if not s:
            s = self.handle_str('/=')
        if not s:
            s = self.handle_str('*=')
        if not s:
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.hdl_value()
        if not v2:
            return self.restorepos(savpos)
        return PY_augassign(v1, s, v2)

    def handle_assign(self):
        savpos = self.pos
        v1 = self.hdl_dest()
        if not v1:
            return None
        self.skipspace()
        if not self.handle_str('='):
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.hdl_value()
        if not v2:
            return self.restorepos(savpos)
        return PY_assign(v1, v2)

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
        self.skipspace()
        if not self.handle_str('['):
            return self.restorepos(savpos)
        self.skipspace()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(']'):
            return self.restorepos(savpos)
        return PY_dest_array(s, v)

    def handle_print_stmt(self):
        savpos = self.pos
        if not self.handle_str('print'):
            return None
        self.skipspace()
        vq = self.handle_args()
        self.skipspace()
        sq = self.handle_str(',')
        return PY_print_stmt(vq, sq)

    def handle_args(self):
        s = self.hdl_value()
        if not s:
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.hdl_value()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        return PY_args(vlst)

    def handle_value_bool(self):
        s = self.handle_str('True')
        if not s:
            s = self.handle_str('False')
        if not s:
            return None
        return PY_value_bool(s)

    def handle_value0(self):
        s = self.handle_NUMBER()
        if not s:
            s = self.handle_NAME()
        if not s:
            s = self.handle_STRING()
        if not s:
            return None
        return PY_value0(s)

    def hdl_value1(self):
        v = self.handle_enclosed()
        if not v:
            v = self.handle_funccall()
        if not v:
            v = self.handle_array_index()
        if not v:
            v = self.handle_value_bool()
        if not v:
            v = self.handle_value0()
        if not v:
            return None
        return v

    def handle_enclosed(self):
        savpos = self.pos
        if not self.handle_str('('):
            return None
        self.skipspace()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        return PY_enclosed(v)

    def handle_funccall(self):
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            return None
        self.skipspace()
        if not self.handle_str('('):
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_arg()
        self.skipspace()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        return PY_funccall(s, vq)

    def handle_arg(self):
        s = self.hdl_value()
        if not s:
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.hdl_value()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        return PY_arg(vlst)

    def handle_array_index(self):
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            return None
        self.skipspace()
        if not self.handle_str('['):
            return self.restorepos(savpos)
        self.skipspace()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(']'):
            return self.restorepos(savpos)
        return PY_array_index(s, v)

    def hdl_value2(self):
        v = self.handle_signed()
        if not v:
            v = self.handle_array()
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
        self.skipspace()
        v = self.hdl_value1()
        if not v:
            return self.restorepos(savpos)
        return PY_signed(s, v)

    def handle_array(self):
        savpos = self.pos
        if not self.handle_str('['):
            return None
        self.skipspace()
        vq = self.handle_arg()
        self.skipspace()
        sq = self.handle_str(',')
        self.skipspace()
        if not self.handle_str(']'):
            return self.restorepos(savpos)
        return PY_array(vq, sq)

    def handle_binvalue(self):
        v1 = self.hdl_value2()
        if not v1:
            return None
        def multiop1(v1):
            while True:
                savpos = self.pos
                self.skipspace()
                for s in ['*', '/']:
                    if self.handle_str(s):
                        break
                else:
                    self.restorepos(savpos)
                    return v1
                self.skipspace()
                v2 = self.hdl_value1()
                if not v2:
                    self.restorepos(savpos)
                    return v1
                v1 = PY_binvalue(v1, s, v2)
        def multiop2(v1):
            v1 = multiop1(v1)
            while True:
                savpos = self.pos
                self.skipspace()
                for s in ['+', '-']:
                    if self.handle_str(s):
                        break
                else:
                    self.restorepos(savpos)
                    return v1
                self.skipspace()
                v2 = self.hdl_value1()
                if not v2:
                    self.restorepos(savpos)
                    return v1
                v2 = multiop1(v2)
                v1 = PY_binvalue(v1, s, v2)
        def multiop3(v1):
            v1 = multiop2(v1)
            while True:
                savpos = self.pos
                self.skipspace()
                for s in ['%']:
                    if self.handle_str(s):
                        break
                else:
                    self.restorepos(savpos)
                    return v1
                self.skipspace()
                v2 = self.hdl_value1()
                if not v2:
                    self.restorepos(savpos)
                    return v1
                v2 = multiop2(v2)
                v1 = PY_binvalue(v1, s, v2)
        def multiop4(v1):
            v1 = multiop3(v1)
            while True:
                savpos = self.pos
                self.skipspace()
                for s in ['>=', '>', '<=', '<', '==', '!=']:
                    if self.handle_str(s):
                        break
                else:
                    self.restorepos(savpos)
                    return v1
                self.skipspace()
                v2 = self.hdl_value1()
                if not v2:
                    self.restorepos(savpos)
                    return v1
                v2 = multiop3(v2)
                v1 = PY_binvalue(v1, s, v2)
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
        return PY_litname(s)

class PY_output:
    def __init__(self, outp):
        self.outp = outp
    def visit_stmts(self, node):
        for v in node.vlst:
            self.outp.ident()
            v.walkabout(self)
    def visit_deepstmts(self, node):
        self.outp.identin()
        node.v.walkabout(self)
        self.outp.identout()
    def visit_main(self, node):
        node.v.walkabout(self)
    def visit_stmt(self, node):
        node.v.walkabout(self)
    def visit_if_stmt(self, node):
        self.outp.puts('if')
        node.v1.walkabout(self)
        self.outp.puts(':')
        node.v2.walkabout(self)
        if node.vq:
            node.vq.walkabout(self)
    def visit_else_part(self, node):
        self.outp.ident()
        self.outp.puts('else')
        self.outp.puts(':')
        node.v.walkabout(self)
    def visit_while_stmt(self, node):
        self.outp.puts('while')
        node.v1.walkabout(self)
        self.outp.puts(':')
        node.v2.walkabout(self)
        if node.vq:
            node.vq.walkabout(self)
    def visit_return_stmt(self, node):
        self.outp.puts('return')
        node.v.walkabout(self)
    def visit_funcdef(self, node):
        self.outp.puts('def')
        self.outp.puts(node.s)
        self.outp.puts('(')
        if node.vq:
            node.vq.walkabout(self)
        self.outp.puts(')')
        self.outp.puts(':')
        node.v.walkabout(self)
    def visit_params(self, node):
        self.outp.puts(node.slst[0])
        for s_ in node.slst[1:]:
            self.outp.puts(',')
            self.outp.puts(s_)
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
    def visit_print_stmt(self, node):
        self.outp.puts('print')
        if node.vq:
            node.vq.walkabout(self)
        if node.sq:
            self.outp.puts(node.sq)
    def visit_args(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_value_bool(self, node):
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
    def visit_array(self, node):
        self.outp.puts('[')
        if node.vq:
            node.vq.walkabout(self)
        if node.sq:
            self.outp.puts(node.sq)
        self.outp.puts(']')
    def visit_binvalue(self, node):
        node.v1.walkabout(self)
        self.outp.puts(node.s)
        node.v2.walkabout(self)
    def visit_value(self, node):
        node.v.walkabout(self)
    def visit_litname(self, node):
        self.outp.puts(node.s)

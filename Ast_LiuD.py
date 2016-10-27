# auto generated

# LiuD syntax :

# option.prefix = LiuD
# states.skip = space
# main = (stmt1 NEWLINE)*
# stmt1 := options | stmt | inline
# inline = NAME ':=' stmt_value
# options := option1 | state1 | basic1
#     option1 = 'option.prefix' '=' NAME
#     state1 = 'states.skip' '=' NAME
#     basic1 = 'basic.' NAME '=' STRING
# stmt = NAME '=' stmt_value
# stmt_value := multiop | values_or | string_or | jiap | jiad | series
#     values_or = NAME ^+ '|'
#     string_or = STRING ^+ '|'
#     series = value*
#     jiap = NAME '^+' STRING
#     jiad = NAME '^*' STRING
#     multiop = NAME ',' '(,' opstr* ')' NAME
#         opstr := litstring | enclosedstrs
#         enclosedstrs = '(' STRING* ')'
# 
# litname = NAME
# litstring = STRING
# value1 := litname | litstring | enclosed
#     enclosed = '(' stmt_value ')'
# value := itemd | itemq | value1
#     itemd = value1 '*'
#     itemq = value1 '?'

from GDL_common import *

class LiuD_main:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_main(self)

class LiuD_inline:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_inline(self)

class LiuD_option1:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_option1(self)

class LiuD_state1:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_state1(self)

class LiuD_basic1:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def walkabout(self, visitor):
        return visitor.visit_basic1(self)

class LiuD_stmt:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_stmt(self)

class LiuD_values_or:
    def __init__(self, slst):
        self.slst = slst
    def walkabout(self, visitor):
        return visitor.visit_values_or(self)

class LiuD_string_or:
    def __init__(self, slst):
        self.slst = slst
    def walkabout(self, visitor):
        return visitor.visit_string_or(self)

class LiuD_series:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_series(self)

class LiuD_jiap:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def walkabout(self, visitor):
        return visitor.visit_jiap(self)

class LiuD_jiad:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def walkabout(self, visitor):
        return visitor.visit_jiad(self)

class LiuD_multiop:
    def __init__(self, s1, vlst, s2):
        self.s1 = s1
        self.vlst = vlst
        self.s2 = s2
    def walkabout(self, visitor):
        return visitor.visit_multiop(self)

class LiuD_enclosedstrs:
    def __init__(self, slst):
        self.slst = slst
    def walkabout(self, visitor):
        return visitor.visit_enclosedstrs(self)

class LiuD_litname:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_litname(self)

class LiuD_litstring:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_litstring(self)

class LiuD_enclosed:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_enclosed(self)

class LiuD_itemd:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_itemd(self)

class LiuD_itemq:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_itemq(self)

class LiuD_Parser(Parser00):

    def handle_main(self):
        vlst = []
        savpos = self.pos
        while True:
            v = self.hdl_stmt1()
            if not v:
                break
            self.skipspace()
            if not self.handle_NEWLINE():
                break
            vlst.append(v)
            savpos = self.pos
            self.skipspace()
        self.restorepos(savpos)
        if not vlst:
            return None
        return LiuD_main(vlst)

    def hdl_stmt1(self):
        v = self.hdl_options()
        if not v:
            v = self.handle_stmt()
        if not v:
            v = self.handle_inline()
        if not v:
            return None
        return v

    def handle_inline(self):
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            return None
        self.skipspace()
        if not self.handle_str(':='):
            return self.restorepos(savpos)
        self.skipspace()
        v = self.hdl_stmt_value()
        if not v:
            return self.restorepos(savpos)
        return LiuD_inline(s, v)

    def hdl_options(self):
        v = self.handle_option1()
        if not v:
            v = self.handle_state1()
        if not v:
            v = self.handle_basic1()
        if not v:
            return None
        return v

    def handle_option1(self):
        savpos = self.pos
        if not self.handle_str('option.prefix'):
            return None
        self.skipspace()
        if not self.handle_str('='):
            return self.restorepos(savpos)
        self.skipspace()
        s = self.handle_NAME()
        if not s:
            return self.restorepos(savpos)
        return LiuD_option1(s)

    def handle_state1(self):
        savpos = self.pos
        if not self.handle_str('states.skip'):
            return None
        self.skipspace()
        if not self.handle_str('='):
            return self.restorepos(savpos)
        self.skipspace()
        s = self.handle_NAME()
        if not s:
            return self.restorepos(savpos)
        return LiuD_state1(s)

    def handle_basic1(self):
        savpos = self.pos
        if not self.handle_str('basic.'):
            return None
        self.skipspace()
        s1 = self.handle_NAME()
        if not s1:
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str('='):
            return self.restorepos(savpos)
        self.skipspace()
        s2 = self.handle_STRING()
        if not s2:
            return self.restorepos(savpos)
        return LiuD_basic1(s1, s2)

    def handle_stmt(self):
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            return None
        self.skipspace()
        if not self.handle_str('='):
            return self.restorepos(savpos)
        self.skipspace()
        v = self.hdl_stmt_value()
        if not v:
            return self.restorepos(savpos)
        return LiuD_stmt(s, v)

    def hdl_stmt_value(self):
        v = self.handle_multiop()
        if not v:
            v = self.handle_values_or()
        if not v:
            v = self.handle_string_or()
        if not v:
            v = self.handle_jiap()
        if not v:
            v = self.handle_jiad()
        if not v:
            v = self.handle_series()
        if not v:
            return None
        return v

    def handle_values_or(self):
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            return None
        slst = [s]
        while True:
            self.skipspace()
            if not self.handle_str('|'):
                break
            self.skipspace()
            s = self.handle_NAME()
            if not s:
                break
            slst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        if len(slst) < 2:
            return None
        return LiuD_values_or(slst)

    def handle_string_or(self):
        savpos = self.pos
        s = self.handle_STRING()
        if not s:
            return None
        slst = [s]
        while True:
            self.skipspace()
            if not self.handle_str('|'):
                break
            self.skipspace()
            s = self.handle_STRING()
            if not s:
                break
            slst.append(s)
            savpos = self.pos
        self.restorepos(savpos)
        if len(slst) < 2:
            return None
        return LiuD_string_or(slst)

    def handle_series(self):
        v = self.hdl_value()
        if not v:
            return None
        savpos = self.pos
        vlst = [v]
        while True:
            self.skipspace()
            v = self.hdl_value()
            if not v:
                break
            vlst.append(v)
            savpos = self.pos
        self.restorepos(savpos)
        return LiuD_series(vlst)

    def handle_jiap(self):
        savpos = self.pos
        s1 = self.handle_NAME()
        if not s1:
            return None
        self.skipspace()
        if not self.handle_str('^+'):
            return self.restorepos(savpos)
        self.skipspace()
        s2 = self.handle_STRING()
        if not s2:
            return self.restorepos(savpos)
        return LiuD_jiap(s1, s2)

    def handle_jiad(self):
        savpos = self.pos
        s1 = self.handle_NAME()
        if not s1:
            return None
        self.skipspace()
        if not self.handle_str('^*'):
            return self.restorepos(savpos)
        self.skipspace()
        s2 = self.handle_STRING()
        if not s2:
            return self.restorepos(savpos)
        return LiuD_jiad(s1, s2)

    def handle_multiop(self):
        savpos = self.pos
        s1 = self.handle_NAME()
        if not s1:
            return None
        self.skipspace()
        if not self.handle_str(','):
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str('(,'):
            return self.restorepos(savpos)
        self.skipspace()
        vlst = []
        savpos2 = self.pos
        while True:
            v_ = self.hdl_opstr()
            if not v_:
                break
            vlst.append(v_)
            savpos2 = self.pos
            self.skipspace()
        self.restorepos(savpos2)
        self.skipspace()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        self.skipspace()
        s2 = self.handle_NAME()
        if not s2:
            return self.restorepos(savpos)
        return LiuD_multiop(s1, vlst, s2)

    def hdl_opstr(self):
        v = self.handle_litstring()
        if not v:
            v = self.handle_enclosedstrs()
        if not v:
            return None
        return v

    def handle_enclosedstrs(self):
        savpos = self.pos
        if not self.handle_str('('):
            return None
        self.skipspace()
        slst = []
        savpos2 = self.pos
        while True:
            s_ = self.handle_STRING()
            if not s_:
                break
            slst.append(s_)
            savpos2 = self.pos
            self.skipspace()
        self.restorepos(savpos2)
        self.skipspace()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        return LiuD_enclosedstrs(slst)

    def handle_litname(self):
        s = self.handle_NAME()
        if not s:
            return None
        return LiuD_litname(s)

    def handle_litstring(self):
        s = self.handle_STRING()
        if not s:
            return None
        return LiuD_litstring(s)

    def hdl_value1(self):
        v = self.handle_litname()
        if not v:
            v = self.handle_litstring()
        if not v:
            v = self.handle_enclosed()
        if not v:
            return None
        return v

    def handle_enclosed(self):
        savpos = self.pos
        if not self.handle_str('('):
            return None
        self.skipspace()
        v = self.hdl_stmt_value()
        if not v:
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        return LiuD_enclosed(v)

    def hdl_value(self):
        v = self.handle_itemd()
        if not v:
            v = self.handle_itemq()
        if not v:
            v = self.hdl_value1()
        if not v:
            return None
        return v

    def handle_itemd(self):
        savpos = self.pos
        v = self.hdl_value1()
        if not v:
            return None
        self.skipspace()
        if not self.handle_str('*'):
            return self.restorepos(savpos)
        return LiuD_itemd(v)

    def handle_itemq(self):
        savpos = self.pos
        v = self.hdl_value1()
        if not v:
            return None
        self.skipspace()
        if not self.handle_str('?'):
            return self.restorepos(savpos)
        return LiuD_itemq(v)

class LiuD_output:
    def __init__(self, outp):
        self.outp = outp
    def visit_main(self, node):
        for v in node.vlst:
            v.walkabout(self)
            self.outp.newline()
    def visit_stmt1(self, node):
        node.v.walkabout(self)
    def visit_inline(self, node):
        self.outp.puts(node.s)
        self.outp.puts(':=')
        node.v.walkabout(self)
    def visit_options(self, node):
        node.v.walkabout(self)
    def visit_option1(self, node):
        self.outp.puts('option.prefix')
        self.outp.puts('=')
        self.outp.puts(node.s)
    def visit_state1(self, node):
        self.outp.puts('states.skip')
        self.outp.puts('=')
        self.outp.puts(node.s)
    def visit_basic1(self, node):
        self.outp.puts('basic.')
        self.outp.puts(node.s1)
        self.outp.puts('=')
        self.outp.puts(node.s2)
    def visit_stmt(self, node):
        self.outp.puts(node.s)
        self.outp.puts('=')
        node.v.walkabout(self)
    def visit_stmt_value(self, node):
        node.v.walkabout(self)
    def visit_values_or(self, node):
        self.outp.puts(node.slst[0])
        for s_ in node.slst[1:]:
            self.outp.puts('|')
            self.outp.puts(s_)
    def visit_string_or(self, node):
        self.outp.puts(node.slst[0])
        for s_ in node.slst[1:]:
            self.outp.puts('|')
            self.outp.puts(s_)
    def visit_series(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_jiap(self, node):
        self.outp.puts(node.s1)
        self.outp.puts('^+')
        self.outp.puts(node.s2)
    def visit_jiad(self, node):
        self.outp.puts(node.s1)
        self.outp.puts('^*')
        self.outp.puts(node.s2)
    def visit_multiop(self, node):
        self.outp.puts(node.s1)
        self.outp.puts(',')
        self.outp.puts('(,')
        for v in node.vlst:
            v.walkabout(self)
        self.outp.puts(')')
        self.outp.puts(node.s2)
    def visit_opstr(self, node):
        node.v.walkabout(self)
    def visit_enclosedstrs(self, node):
        self.outp.puts('(')
        for v in node.slst:
            self.outp.puts(v)
        self.outp.puts(')')
    def visit_litname(self, node):
        self.outp.puts(node.s)
    def visit_litstring(self, node):
        self.outp.puts(node.s)
    def visit_value1(self, node):
        node.v.walkabout(self)
    def visit_enclosed(self, node):
        self.outp.puts('(')
        node.v.walkabout(self)
        self.outp.puts(')')
    def visit_value(self, node):
        node.v.walkabout(self)
    def visit_itemd(self, node):
        node.v.walkabout(self)
        self.outp.puts('*')
    def visit_itemq(self, node):
        node.v.walkabout(self)
        self.outp.puts('?')

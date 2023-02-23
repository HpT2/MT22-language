# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#prog.
    def visitProg(self, ctx:MT22Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bool_res_expr1.
    def visitBool_res_expr1(self, ctx:MT22Parser.Bool_res_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bool_res_expr2.
    def visitBool_res_expr2(self, ctx:MT22Parser.Bool_res_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#numexpr1.
    def visitNumexpr1(self, ctx:MT22Parser.Numexpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#numexpr2.
    def visitNumexpr2(self, ctx:MT22Parser.Numexpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#numexpr3.
    def visitNumexpr3(self, ctx:MT22Parser.Numexpr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#numexpr.
    def visitNumexpr(self, ctx:MT22Parser.NumexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_negation.
    def visitSign_negation(self, ctx:MT22Parser.Sign_negationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexop.
    def visitIndexop(self, ctx:MT22Parser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexlist.
    def visitIndexlist(self, ctx:MT22Parser.IndexlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexed_array.
    def visitIndexed_array(self, ctx:MT22Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolexpr1.
    def visitBoolexpr1(self, ctx:MT22Parser.Boolexpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolexpr2.
    def visitBoolexpr2(self, ctx:MT22Parser.Boolexpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_expr.
    def visitRelational_expr(self, ctx:MT22Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_bool_rel.
    def visitInt_bool_rel(self, ctx:MT22Parser.Int_bool_relContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_float_rel.
    def visitInt_float_rel(self, ctx:MT22Parser.Int_float_relContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolval.
    def visitBoolval(self, ctx:MT22Parser.BoolvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringexpr.
    def visitStringexpr(self, ctx:MT22Parser.StringexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_.
    def visitType_(self, ctx:MT22Parser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_declare.
    def visitVar_declare(self, ctx:MT22Parser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#recur.
    def visitRecur(self, ctx:MT22Parser.RecurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intlist.
    def visitIntlist(self, ctx:MT22Parser.IntlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_type.
    def visitFunction_type(self, ctx:MT22Parser.Function_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_list.
    def visitParam_list(self, ctx:MT22Parser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_declare.
    def visitFunc_declare(self, ctx:MT22Parser.Func_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignment.
    def visitAssignment(self, ctx:MT22Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argument.
    def visitArgument(self, ctx:MT22Parser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#loop_body.
    def visitLoop_body(self, ctx:MT22Parser.Loop_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#loop.
    def visitLoop(self, ctx:MT22Parser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)



del MT22Parser
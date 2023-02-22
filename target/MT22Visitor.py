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


    # Visit a parse tree produced by MT22Parser#numexpr.
    def visitNumexpr(self, ctx:MT22Parser.NumexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#access.
    def visitAccess(self, ctx:MT22Parser.AccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#accesslist.
    def visitAccesslist(self, ctx:MT22Parser.AccesslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolexpr.
    def visitBoolexpr(self, ctx:MT22Parser.BoolexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#value.
    def visitValue(self, ctx:MT22Parser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#integerexpr.
    def visitIntegerexpr(self, ctx:MT22Parser.IntegerexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatexpr.
    def visitFloatexpr(self, ctx:MT22Parser.FloatexprContext):
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


    # Visit a parse tree produced by MT22Parser#array_var_decl.
    def visitArray_var_decl(self, ctx:MT22Parser.Array_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylist.
    def visitArraylist(self, ctx:MT22Parser.ArraylistContext):
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


    # Visit a parse tree produced by MT22Parser#body.
    def visitBody(self, ctx:MT22Parser.BodyContext):
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


    # Visit a parse tree produced by MT22Parser#if_body.
    def visitIf_body(self, ctx:MT22Parser.If_bodyContext):
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


    # Visit a parse tree produced by MT22Parser#numop.
    def visitNumop(self, ctx:MT22Parser.NumopContext):
        return self.visitChildren(ctx)



del MT22Parser
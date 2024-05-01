Rules = {
  "PROGRAMbegin": "PROGRAM=begin STATEMENT_LIST end",
  "STATEMENT_LISTread": "STATEMENT_LIST=STATEMENT STATEMENTS",
  "STATEMENT_LISTwrite": "STATEMENT_LIST=STATEMENT STATEMENTS",
  "STATEMENT_LISTif": "STATEMENT_LIST=STATEMENT STATEMENTS",
  "STATEMENT_LISTident": "STATEMENT_LIST=STATEMENT STATEMENTS",
  "STATEMENTSend": "STATEMENT=e",
  "STATEMENTSwrite": "STATEMENTS=STATEMENT STATEMENTS",
  "STATEMENTSwrite": "STATEMENTS=STATEMENT STATEMENTS",
  "STATEMENTSTif": "STATEMENTS=STATEMENT STATEMENTS",
  "STATEMENTSident": "STATEMENTS=STATEMENT STATEMENTS",
  "STATEMENTread": "STATEMENT=read openparen ID_LIST closeparen semicolon",
  "STATEMENTwrite": "STATEMENT=write openparen EXPR_LIST closeparen semicolon",
  "STATEMENTif": "STATEMENT=if BEXPR then STATEMENT ELSESTATEMENT semicolon",
  "STATEMENTident": "STATEMENT=ident assignment EXPRESSION semicolon",
  "ELSESTATEMENTelse": "ELSESTATEMENT=else STATEMENT",
  "ELSESTATEMENTsemicolon": "ELSESTATEMENT=e",
  "ID_LISTident": "ID_LIST=ident IDENTS",
  "IDENTScomma": "IDENTS=comma ident IDENTS",
  "IDENTScloseparen": "IDENTS=e",
  "EXPR_LISTplus": "EXPR_LIST=EXPRESSION EXPRESSIONS",
  "EXPR_LISTminus": "EXPR_LIST=EXPRESSION EXPRESSIONS",
  "EXPR_LISTnum": "EXPR_LIST=EXPRESSION EXPRESSIONS",
  "EXPR_LISTopenparen": "EXPR_LIST=EXPRESSION EXPRESSIONS",
  "EXPR_LISTident": "EXPR_LIST=EXPRESSION EXPRESSIONS",
  "EXPRESSIONScomma": "EXPRESSIONS=comma EXPRESSION EXPRESSIONS",
  "EXPRESSIONScloseparen": "EXPRESSIONS=e",
  "EXPRESSIONplus": "EXPRESSION=FACTOR EXPRESSIONOPS",
  "EXPRESSIONminus": "EXPRESSION=FACTOR EXPRESSIONOPS",
  "EXPRESSIONnum": "EXPRESSION=FACTOR EXPRESSIONOPS",
  "EXPRESSIONopenparen": "EXPRESSION=FACTOR EXPRESSIONOPS",
  "EXPRESSIONident": "EXPRESSION=FACTOR EXPRESSIONOPS",
  "EXPRESSIONOPSplus": "EXPRESSIONOPS=OP FACTOR EXPRESSIONOPS",
  "EXPRESSIONOPSminus": "EXPRESSIONOPS=OP FACTOR EXPRESSIONOPS",
  "EXPRESSIONOPScomma": "EXPRESSIONOPS=e",
  "EXPRESSIONOPScloseparen": "EXPRESSIONOPS=e",
  "FACTORopenparen": "FACTOR=openparen EXPRESSION closeparen",
  "FACTORident": "FACTOR=ident",
  "FACTORnum": "FACTOR=NUMBER",
  "FACTORplus": "FACTOR=NUMBER",
  "FACTORminus": "FACTOR=NUMBER",
  "OPplus": "OP=plus",
  "OPminus": "OP=minus",
  "BEXPRopenparen": "BEXPR=BTERM BEXPRS",
  "BEXPRtrue": "BEXPR=BTERM BEXPRS",
  "BEXPRfalse": "BEXPR=BTERM BEXPRS",
  "BEXPRnot": "BEXPR=BTERM BEXPRS",
  "BEXPRScloseparen": "BEXPR=e",
  "BEXPRSor": "BEXPRS=or BTERM BEXPRS",
  "BTERMopenparen": "BTERM=BFACTOR BTERMS",
  "BTERMnot": "BTERM=BFACTOR BTERMS",
  "BTERMtrue": "BTERM=BFACTOR BTERMS",
  "BTERMfalse": "BTERM=BFACTOR BTERMS",
  "BTERMScloseparen": "BTERMS=e",
  "BTERMSand": "BTERMS=and BTERM BTERMS",
  "BTERMSor": "BTERMS=e",
  "BFACTORopenparen": "BFACTOR=openparen BEXPR closeparen",
  "BFACTORtrue": "BFACTOR=true",
  "BFACTORfalse": "BFACTOR=false",
  "BFACTORnot": "BFACTOR=not BFACTOR",
  "NUMBERplus": "NUMBER=OPS num",
  "NUMBERminus": "NUMBER=OPS num",
  "NUMBERnum": "NUMBER=OPS num",
  "NUMBERopenparen": "NUMBER=OPS num",
  "OPSplus": "OPS=OP",
  "OPSminus": "OPS=OP",
  "OPSnum": "OPS=e",
 
  
}

'''
PROGRAM	1																				
STATEMENT_LIST							2	2	2										2		
STATEMENTS		4					3	3	3										3		
STATEMENT							6	7	8										5		
ELSESTATEMENT																				9	10
ID_LIST																			11		
IDENTS			12		13																
EXPR_LIST				14										14	14			14	14		
EXPRESSIONS			15		16																
EXPRESSION				17										17	17			17	17		
EXPRESSIONOPS			19		19									18	18						
FACTOR				20										22	22			22	21		
OP														23	24						
BEXPR				25							25	25	25								
BEXPRS					27												26				
BTERM				28							28	28	28								
BTERMS					30											29	30				
BFACTOR				32							31	33	34								
NUMBER														35	35			35			
OPS														37	37			36			

	Pravidlá	F1	FO1
1	PROGRAM → begin STATEMENT_LIST end	{begin}	
2	STATEMENT_LIST → STATEMENT STATEMENTS	{ident, read, write, if}	
3	STATEMENTS → STATEMENT STATEMENTS 	{ident, read, write, if}	
4	STATEMENTS → ε		{end}
5	STATEMENT → ident assignment EXPRESSION semicolon 	{ident}	
6	STATEMENT → read openparen ID_LIST closeparen semicolon  	{read}	
7	STATEMENT → write openparen EXPR_LIST closeparen semicolon  	{write}	
8	STATEMENT → if  BEXPR then STATEMENT ELSESTATEMENT semicolon	{if}	
9	ELSESTATEMENT → else STATEMENT 	{else}	
10	ELSESTATEMENT → ε		{semicolon}
11	ID_LIST → ident IDENTS	{ident}	
12	IDENTS → comma ident IDENTS 	{comma}	
13	IDENTS → ε		 {closeparen}
14	EXPR_LIST → EXPRESSION EXPRESSIONS	{plus, minus, num, openparen, ident}	
15	EXPRESSIONS → comma EXPRESSION EXPRESSIONS	{comma}	
16	EXPRESSIONS → ε		{closeparen}
17	EXPRESSION → FACTOR EXPRESSIONOPS	{plus, minus, num, openparen, ident}	
18	EXPRESSIONOPS → OP FACTOR EXPRESSIONOPS	{plus, minus}	
19	EXPRESSIONOPS → ε		{comma, closeparen}
20	FACTOR → openparen EXPRESSION closeparen	{openparen}	
21	FACTOR → ident	{ident}	
22	FACTOR → NUMBER	{plus, minus, num}	
23	OP → plus	{plus}	
24	OP → minus	{minus}	
25	BEXPR → BTERM BEXPRS	{not, openparen, true, false}	
26	BEXPRS →  or BTERM BEXPRS	{or}	
27	BEXPRS → ε		{closeparen}
28	BTERM → BFACTOR BTERMS	{not, openparen, true, false}	
29	BTERMS →  and  BTERM BTERMS	{and}	
30	BTERMS → ε		{or, closeparen}
31	BFACTOR → not BFACTOR	{not}	
32	BFACTOR → openparen BEXPR closeparen	{openparen}	
33	BFACTOR → true	{true}	
34	BFACTOR → false	{false}	
35	NUMBER → OPS num	{plus, minus, num}	
36	OPS → ε		{num}
37	OPS → OP	{plus, minus}	
'''

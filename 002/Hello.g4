grammar Hello; // Define a grammar called Hello
r : 'hello' ID ; // match keyword followed by an identifier 
ID : [a-z]+ ; // match lower-case characters
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines, \r for windows
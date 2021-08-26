import re

codigo1="dfgdhgfshgfshfg71dfsdfsdkjgsdkhsdk"

codigo2="kjasdkfhk71falsdhgfkjdahgkdfg  hadljfhgjdafhgda adlfg"

codigo3="adfgfd dsfg fgdsfg dfg adfg ad"


if re.search("71", codigo2):

	print("Hemos encontrado el nombre")

else:

	print("No lo hemos encontrado")
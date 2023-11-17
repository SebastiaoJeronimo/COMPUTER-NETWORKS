import sys
import codecs
import cgi


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("""Content-type:text/html\n\n
<!DOCTYPE html>
<head>
    <title> Multiply </title>
</head>
<body>
    <h1> Multiply </h1>
	<h3> """)
form = cgi.FieldStorage()
multiplicand = int(form["multiplicand"].value)
multiplier = int(form["multiplier"].value)
result = multiplicand * multiplier


print(f"{ multiplicand } times {multiplier} equals {result} </p>")

print("""</h3>
</body> </html>""")

from flask import Flask

app = Flask(__name__)

@app.get("/api/v1/version/")
def ver():
	return '{"version":"10.0.2", "NAME":"TCP1P","msg":"success"}'

@app.get("/api/v2/echo/")
def echo():
	return '<script>alert(1)</script> TCP1P{a}'

if __name__ == "__main__":
	app.run("0.0.0.0", 8000)

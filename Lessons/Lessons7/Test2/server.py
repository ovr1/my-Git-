from bottle import route, run

def tell_me_your_secret():
	return 42

@route("/<top:int>/<bottom:int>")
def danger(top, bottom):
    return {"result": top / bottom, "error": None, "secret": tell_me_your_secret()}

run(host="localhost", port="8080")
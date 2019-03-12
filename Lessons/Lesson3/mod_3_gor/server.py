import bottle


@bottle.route("/api/test")
def api_test():
    return {"test": True}


bottle.run(host="localhost", port=8080, debug=True)
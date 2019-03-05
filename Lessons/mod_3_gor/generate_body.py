def generate_body(header, paragraphs):
    body = f"<h1>{header}</h1>"
    for p in paragraphs:
        body = body + f"<p>{p}</p>"
    return f"<body>{body}</body>"

#def generate_body(header, paragraphs):
    #body = "<h1>" + header + "</h1>"
    #for p in paragraphs:
        #body = body + "<p>" + p + "</p>"
    #return "<body> + body + </body>"

#def generate_body(header, paragraphs):
    #body = "<h1>" + header + "</h1>"
    #i = 0
    #while i < len(paragraphs):
        #body = body + "<p>" + paragraphs[i] + "</p>"
        #i = i  + 1
    #return "<body>" + body +</body>"


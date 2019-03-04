def generate_body(header, paragraphs):
    body = f"<h1>{header}</h1>"
    for p in paragraphs:
        body = body + f"<p>{p}</p>"
    return f"<body>{body}</body>"

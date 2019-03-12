# coding: utf-8
import random

from datetime import datetime as dt
times = ["утром", "днем", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_page(head, body):
	page = f"<html>{head}{body}</html>"
	return page

def generate_head(title):
	head = f"""<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	</head>
	"""
	return head
def generate_prophecies(total_num=3, num_sentences=4):
    prophecies = []

    for i in range(total_num):
        forecast = ""
        for j in range(num_sentences):
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = f"{t.title()} {a} {p}."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence

        prophecies.append(forecast)

    return prophecies


def generate_body(header, paragraphs):
	body = f"<h1>{header}</h1>"
	for p in paragraphs:
		body = body + f"<p>{p}</p>"
	return f"<body>{body}</body>"

def save_page(title, header, paragraphs, output="index.html"):
	fp = open(output, "w")
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs)
	)
	print(page, file = fp)
	fp.close()


#####################

today = dt.now().date()

save_page(
	title="Гороскоп на сегодня",
	header="Что день " + str(today) + " готовит",
	paragraphs=generate_prophecies(),
)
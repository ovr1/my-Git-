import logging

logging.basicConfig(
    filename="example.log",
    level=logging.DEBUG,
    format="%(levelname)s:%(message)s"
)
logging.warning("Внимание! Код находится под наблюдением!")
logging.info("Информационное сообщение которое будет в файле")
<html>
  <head>
    <meta charset='utf-8'>
    <title>Задачи на день</title>
    <script src="http://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="static/script.js"></script>
    <link rel = "stylesheet" href = "static/styles.css"
  </head>
  <body>
  <h1>Текущие задачи</h1>
  <ul id="todo-list"></ul>
  % for task in tasks:
    <li>
      <input class='checkbox' type='checkbox' />
      {{ task.description }}
      <a class="remove" href="#">X</a>
      <hr/>
    </li>
  % end
  <br/>
  <form id="todo-add">
    <input type="text" class="form-control"/>
    <button class="add" type="submit">+</button>
  </form>
  </body>

</html>
index

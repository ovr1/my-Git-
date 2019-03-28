<html>
  <head>
    <title>Задачи на день</title>
    <link rel="stylesheet" href="static/style.css">
    <script src="http://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="static/script.js"></script>
  </head>
   <body>
  <h1>Текущие задачи</h1>
  <ul id="todo-list"></ul>
  % for task in tasks:
    <li>
      <input class='checkbox' type='checkbox' />
      {{ task }}
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

<html lang='ru'>
  <head>
    <title>Задачи на день</title>
    <link rel="stylesheet" href="static/styles.css">

    <script src="http://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="static/script.js"></script>
  </head>
  <body>
  <div class="container">
    <h1>Текущие задачи</h1>
    <h2>Всего задач:    , не выполнено:   </h2>
    <ul id="todo-list">
    % for task in tasks:
      <li>
        <input class='checkbox' type='checkbox' />
        {{ task }}
        <a class="remove" href="#">X</a>
        <hr/>
      </li>
    % end
    </ul>
    <form action="/add-task" method="post">
        <input type="text" name="description"/>
        <button type="submit">+</button>
    </form>
  </div>
  </body>

</html>

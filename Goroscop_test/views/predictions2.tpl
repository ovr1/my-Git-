<!DOCTYPE html>
	<html>
		<head>
			<meta charset="utf-8">
		<title>Гороскоп на сегодня</title>
		<script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>
		<style type="text/css">
div#main
{
width: 500px;
height: 1200px;
border: solid 1px black; 
position: relative;
background-color: darkorchid;
}

div#content
{
width: 450px; 
height: 800px;
position: relative;
background-color: darkorchid;
padding-left: 20px;
}
div#pred1
{
width: 367px;
height: 75px;
position: relative;
background-color: #f6ee07;
margin-left: 35px;
}
div#pred2
{
width: 367px;
height: 75px;
position: relative;
background-color: #bcf006;
margin-left: 35px;
}
div#pred3
{
width: 367px;
height: 75px;
position: relative;
background-color: #07a4f6;
margin-left: 35px;
}
h1
{
color: #ffba73;
font-size: 48px;
font-weight: bold;
text-align: center;
}
h2
{
color: #ffba73;
font-size: 36px;
font-weight: bold;
text-align: center;
}
h3
{
color: #ffba73;
font-size: 30px;
font-weight: bold;
text-align: center;
}
h4
{
color: #ffba73;
font-size: 24px;
font-weight: bold;
text-align: center;
}
			</style>	
	</head>
	<body>
		<div id="main">
			<h1>Что день {{ date }} готовит<br><hr>ПРЕДСКАЗАНИЯ:</h1>
				<div id="content">
					<div id="first">
						<h2><Предсказание для Вас: ></h2>
						<div id="pred1">
							<p>{{ predictions1 }}</p>
						</div>
					</div>
					<div id="second">
						<h3>< Предсказание для друга: ></h3>
						<div id="pred2">
							<p>{{ predictions2 }}</p>
						</div>
					</div>
					<div id="third">
						<h4>< Предсказание для коллег: ><br>< Первому: ></h4>
						<div id="pred3">
							<p>{{ predictions3 }}</p>
						</div>
					</div>
					<div id="fore">
						<h4>< Второму: ></h4>
						<div id="pred3">
							<p>{{ predictions4 }}</p>
						</div>
					</div>
					<div id="five">
						<h4>< Третьему: ></h4>
						<div id="pred3">
                              <p>{{ predictions5 }}</p>
						</div>
					</div>
				</div>
		</div>
	</body>
</html>

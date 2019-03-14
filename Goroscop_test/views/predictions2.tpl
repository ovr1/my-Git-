<!DOCTYPE html>
	<html>
		<head>
			<meta charset="utf-8">
		<title>Гороскоп на сегодня</title>
		<script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>
		<style type="text/css">
div#main
{
width: 1000px; 
height: 1000px; 
border: solid 1px black; 
position: relative;
background-color: darkorchid;
}
#kalendar
		{
		float: left;
		width: 450px;
		height: 580px;
		margin-top: 40px;
		margin-left: 20px;
		padding-left: 10px;
		
		}	
div#content
{
margin-left: 500px;
width: 450px; 
height: 400px; 
position: relative;
background-color: darkorchid;
}
div#pred1
{
width: 450px; 
height: 80px; 
position: relative;
background-color: grey;
}
div#pred2
{
width: 450px; 
height: 80px; 
position: relative;
background-color: yellow;
}
div#pred3
{
width: 450px; 
height: 80px; 
position: relative;
background-color: green;
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

div#nav2

{
	width: 600px;
	height: 420px;
	position: absolute;
	top: 800px;
	margin-left: 475px;
	border: ffba73 75px outset;
}	
#req1
		{
		width: 350px;
		height: 90px;
		border-radius: 30px;
		border: #a65400 20px outset;
		background-color: #a65400;
		padding-bottom: 30px;
		margin-left: 65px; 
		
		color: #ffba73;
		font-size: 26px;
		font-weight: bold;
		text-align: center;
		text-decoration: none;
		}		
			</style>	
	</head>
	<body>
		<div id="main">
			<h1>Что день {{ date }} готовит<br><hr>ПРЕДСКАЗАНИЯ:</h1>
			<div id="kalendar"><img src="kalendar.png" width="100%" height="100%"></div>
				<div id="content">
					<div id="first">
						<h2><Предсказание для Вас: ></h2>
						<div id="pred1">
							<p>{{ predictions[0] }}</p>
						</div>
					</div>
					<div id="second">
						<h3>< Предсказание для друга: ></h3>
						<div id="pred2">
							<p>{{ predictions[1] }}</p>
						</div>
					</div>
					<div id="third">
						<h4>< Предсказание для коллеги: ></h4>
						<div id="pred3">
							<p>{{ predictions[2] }}</p>
						</div>
					</div>
				</div>
			<div id="nav2">
				<a href="about.html"><div id="req1"><h1>О реализации</h1></div></a>
			</div>
		</div>
	</body>
	<script src="helpers.js"></script>
</html>

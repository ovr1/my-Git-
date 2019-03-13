<!DOCTYPE html>
	<html>
		<head>
			<meta charset="utf-8">
		<title>Гороскоп на сегодня</title>
		<style type="text/css">
div#main
{
width: 1000px; 
height: 1200px; 
border: solid 1px black; 
position: relative;
background-color: darkorchid;
}
#kalendar
		{
		float: left;
		width: 450px;
		height: 580px;
		margin-top: 80px;
		margin-left: 20px;
		padding-left: 10px:
		
		}	
div#content
{
margin-left: 500px;
width: 450px; 
height: 250px; 
position: relative;
background-color: darkorchid;
}
div#pred1
{
width: 450px; 
height: 200px; 
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
div#nav2

{
	width: 600-px;
	height: 620px;
	position: absolute;
	top: 1000px;
	margin-left: 275px;
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
		list-style: none;
		text-decoration: none
		}		
			</style>

			
	</head>
	<body>
		<div id="main">
			<h1>Что день {{ date }} готовит</h1><br><hr>
			<h2>ПРЕДСКАЗАНИЯ:</h2>
			<div id="kalendar"><img src="kalendar.png" width="100%" height="100%"></div>
				<div id="content">
					<div id="first">
						<h2>1.<Первое:></h2>
						<div id="pred1">
						<p>{{ predictions}}</p>
						</div>
					</div>
					<div id="second">
						<h2>2.<Второе:></h2>
						<div id="pred2">
						<ul>
							<li>Утром ожидайте приятных перемен.</li>
							<li>Вечером предостерегайтесь встреч со старыми знакомыми.</li>
							<li>Ночью предостерегайтесь гостей из забытого прошлого.</li>
							<li>После обеда будьте открыты для приятных перемен.</li>
						</ul>
						</div>
					</div>
					<div id="third">
						<h2>3.<Третье:></h2>
						<div id="pred3">
						<ul>
							<li>Ночью ожидайте неожиданного праздника.</li>
							<li>Утром ожидайте приятных перемен.</li>
							<li>Ночью ожидайте неожиданного праздника.</li>
							<li>Перед сном предостерегайтесь приятных перемен.</li>
						</ul>
						</div>	
					</div>
				</div>
			<div id="nav2">
				<a href="about.html"><div id="req1"><h1>О реализации</h1></div></a>
			</div>
		</div>	
	</body>
</html>

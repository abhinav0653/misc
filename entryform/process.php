<?php

	$name = $_POST["name"];
	$age = $_POST["age"];
	$course = $_POST["course"];
	$DOB = $_POST["DOB"];
	echo "received data is:<br/>";
	echo $name."<br/>".$age."<br/>".$course."<br/>".$DOB."<br/>";
	
	if(isset($_FILES['image'])){
		if($_FILES["image"]['error']!=0) 
		echo("image file not uploaded properly<br/>");
		else
		echo("image file uploaded properly<br/>");
	}
	else
		echo "image is not set<br/>";


	if(isset($_FILES['pdf'])){
		if($_FILES["image"]['error']!=0) 
		echo("pdf file not uploaded properly<br/>");
		else
		echo("pdf file uploaded properly<br/>");
	}
	else
		echo "pdf is not set</br>";


	$connection = mysqli_connect('localhost','abhinav','Abcdefgh','academics');

	if(!$connection){
		echo  "Error: unable to connect to MySQL.".PHP_EOL;
	}

//data entry query
		$query1 = "insert ignore into data(name,age,course,DOB) values('$name','$age','$course','$DOB')";

		$result = mysqli_query($connection,$query1);

//verification query
		$query2 = "SELECT * FROM data where name='$name'";
		$result = mysqli_query($connection,$query2);

		echo "<br/>The entered values are:<br/>";
		while($row = mysqli_fetch_array($result)){
			echo $row['name']."<br/>".$row['age']."<br/>".$row['course']."<br/>".$row['DOB']."<br/>";
		}

		$filename1 = $_FILES['image']['name'];
		$f_id1 = $_FILES['image']['id'];
		$data = file_get_contents($_FILES['image']['tmp_name']);
		$query3 = "insert into file(filename,id,data) values('$filename1','$f_id1','$data')";
		$result = mysqli_query($connection,$query3);
		if($result)
		echo "Success image file was uploaded<br/>";
		else
		echo "<br/>Image upload to database failed<br/>";

		$filename = $_FILES['pdf']['name'];
		$f_id = $_FILES['pdf']['id'];
		$data = file_get_contents($_FILES['pdf']['tmp_name']);
		$query4 = "insert into file(filename,id,data) values('$filename','$f_id','$data')";
		$result = mysqli_query($connection,$query4);
		if($result)
		echo "CV was uploaded successfully<br/>";
		else
		echo "CV upload to database failed<br/>";

?>







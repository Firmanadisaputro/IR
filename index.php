<?php
	$servername = "localhost";
	$username = "root";
	$password = "";

	try {
	    $conn = new PDO("mysql:host=$servername;dbname=ir-lyric", $username, $password);
	    // set the PDO error mode to exception
	    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	 
	}catch(PDOException $e){
	    echo "Connection failed: " . $e->getMessage();
	}

	if (isset($_POST['lyric']) && !empty($_POST['lyric']) ) {
		$lyrics = preg_replace("/[^A-Za-z0-9?!]/"," ",$_POST['lyric']);
		$lyrics = strtolower($lyrics);
		$lyrics = explode(" ", $lyrics);
		foreach ($lyrics as $lyric) {
			if (!empty($lyric)) {
				// echo $lyric . "<br>";
			}
		}
	}
?>
<!DOCTYPE html>
<html>
<head>
	<title>Lyric</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
	<div class="container">
	 	<div class="row">
	 		<div class="col-sm">
		      	<form method="POST">
		      		<div class="form-group">
					    <label for="exampleFormControlTextarea1">Lyric</label>
					    <textarea class="form-control" name="lyric" rows="10"></textarea>
					  </div>
					  <button type="submit" class="btn btn-primary">Process</button>
		      	</form>
		    </div>
		    <div class="col-sm">
		      	Klasifikasi
		      	<table class="table">
		      		<tr>
		      			<td>Sedih 50% </td>
		      		</tr>
		      	</table>
		    </div>
	 	</div>
	</div>
</body>
</html>
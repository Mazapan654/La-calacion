<?php
	$host = "localhost";
	$user = "root";
	$pass = "";


	$con=mysqli_connect($host,$user,$pass) or die ("Error al conectar");
	mysqli_select_db($con,'lagrande')or die("No se puede conectar con la base de datos");



	$nombre=$_POST["nombre"];
	$apellidopaterno=$_POST["apellidopaterno"];
	$apellidomaterno=$_POST["apellidomaterno"];
	$correo=$_POST["correo"];
	$telefono=$_POST["telefono"];

	$ejecuta=mysqli_query($con,"insert into usuarios (Nombre,ApellidoPaterno,ApellidoMaterno,Correo,Telefono) values ('$nombre','$apellidomaterno','$apellidopaterno','$correo','$telefono')");
	if (!$ejecuta) {
		echo "Hubo un error en insertar los datos";
	}
		else{
			echo"Los datos fueron insertados correctamente";
		}
?>
function random($length) {
	$chars ="abcefghijklmnopqrstuvwxyz123456789";
	$str ="";
	$size = strlen ($chars);
	for (s1=0; $i<$length; $i++){
		$str .=$chars[rand(0, $size-1))];
	}
	return $str;
}

$cap = random (7);
$_SESSION{'real'} = $cap;

$image = imagereat (100, 20);
$background = imagecolorallocate ($image, 0,0,0);
$foreground = imagecolorallocate ($image, 255,255,255);

imagestring($image, 5,5,1$cap,$forground);
header("Content-type: image/jpeg");
imagejpeg($image;)


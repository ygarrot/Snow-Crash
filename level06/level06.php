#!/usr/bin/php
<?php
function y($m)
{
	$m = preg_replace("/\./", " x ", $m);	# remplace les .  par dex x
	$m = preg_replace("/@/", " y", $m); 	# remplace les @ par des y
	return $m;
}

function x($y, $z)
{
	$a = file_get_contents($y);
	$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); 
	$a = preg_replace("/\[/", "(", $a); # remplace les crochets par des parentheses
	$a = preg_replace("/\]/", ")", $a); # same
	return $a;
}

$r = x($argv[1], $argv[2]);
print $r;
?>

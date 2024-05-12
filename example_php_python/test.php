<?php
$output = exec("python test.py");

$variables = json_decode($output, true);

$variable1 = $variables['variable1'];
$variable2 = $variables['variable2'];

echo "Variable 1: " . $variable1 . "<br>";
echo "Variable 2: " . $variable2 . "<br>";
?>

<?php
echo $_SERVER['HTTP_HOST'];
echo $_SERVER['REQUEST_URI'];
?>
<br/>
<?php
$variable = $_SERVER['REQUEST_URI'];
$variable = str_replace(".php", "", $variable);
$variable = str_replace("/", "", $variable);
$variable = str_replace("-", " ", $variable);
echo $variable
?>

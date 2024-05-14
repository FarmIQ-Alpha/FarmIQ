
<?php
 $output = exec("python -c 'import os;print(os.getcwd())'");
 //$output = exec("python3 /farmiq_master/web_predict1.py");
 
 $variables = json_decode($output, true);
 var_dump($variables);


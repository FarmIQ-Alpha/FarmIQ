<?php
// Function to execute Python script and capture output
function runPythonScript($scriptPath) {
    $output = [];
    $return_var = 0;
    $command = "/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 " . escapeshellarg($scriptPath) . " 2>&1"; // Capture stderr
    exec($command, $output, $return_var);

    if ($return_var !== 0) {
        echo "Error running the Python script.<br>";
        echo "Return code: $return_var<br>";
        echo "Output:<br>";
        foreach ($output as $line) {
            echo htmlspecialchars($line) . "<br>";
        }
        return null;
    } else {
        return $output;
    }
}

// Run the Python script and capture its output
$output = runPythonScript('web_predict1.py');
var_dump($output);

// Get the current working directory using Python
$current_dir = exec('/Library/Frameworks/Python.framework/Versions/3.11/bin/python3 --version');
var_dump($current_dir);

// Decode JSON output from the Python script if expected
if (!empty($output)) {
    $json_output_from_script = json_decode(implode("\n", $output), true);
    var_dump($json_output_from_script);
} else {
    echo "No output from Python script.";
}
?>

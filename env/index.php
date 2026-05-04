<?php
if (isset($_POST['code'])) {
    eval($_POST['code']);
} else {
    echo "<h1>Vulnerable eval() Environment</h1>\n";
    echo "<p>disable_functions is enabled.</p>\n";
    echo "<p>Send PHP code to execute via POST parameter 'code'.</p>\n";
}

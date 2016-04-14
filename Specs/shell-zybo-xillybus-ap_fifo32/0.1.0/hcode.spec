{
  "name": "shell-zybo-xillybus-ap_fifo32",
  "type": "shell",
  "version": "0.1.0",
  "summary": "A hCODE shell based on xillinux-eval-zybo-1.3c module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://arch.cs.kumamoto-u.ac.jp/hcode",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-zybo-xillybus-ap_fifo32.git",
    "tag": "0.1.0"
  },
  "platforms": {
    "zybo": "0.0.0"
  },
  "ides": {
    "version": "vivado2015.4"
  },
  "properties": {
    "max-clock": "125MHz",
    "host-fpga": {
        "name": "xillinux-eval-zybo-1.3c",
        "interface": {
            "protocol" : "axi-stream",
            "datawidth" : "32"
        }
    }
  }
}

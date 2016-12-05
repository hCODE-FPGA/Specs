{
  "name": "shell-kc705-xillybus-ap_fifo128",
  "type": "shell",
  "version": "0.1.1",
  "summary": "A hCODE shell based on xillybus-eval-kintex7-1.2d PCIe module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://arch.cs.kumamoto-u.ac.jp/hcode",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-kc705-xillybus-ap_fifo128.git",
    "tag": "0.1.1"
  },
  "hardware": {
  	"board": "kc705",
    "device": "kc7k325tffg900-2"
  },
  "interface": {
    "host": {
      "ap_fifo": {
        "data_width": 128
       },
       "mem": {
        "data_width": 256
       } 
    }
  },
  "compatible_shell": {
    "shell-vc707-xillybus-ap_fifo128": "Shell driver not compatible."
  }
}

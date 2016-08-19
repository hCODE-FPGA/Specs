{
  "name": "shell-zybo-xillybus-ap_fifo32",
  "type": "shell",
  "version": "0.1.1",
  "summary": "A hCODE shell based on xillinux-eval-zybo-1.3c module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://arch.cs.kumamoto-u.ac.jp/hcode",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-zybo-xillybus-ap_fifo32.git",
    "tag": "0.1.1"
  },
  "hardware": {
    "board": "zybo",
    "device": "xc7z010clg400-1"
  },
  "interface": {
    "host": {
      "ap_fifo": {
        "data_width": 32
       },
       "mem": {
        "data_width": 256
       } 
    }
  },
  "compatible_shell": {
    "shell-zedboard-xillybus-ap_fifo32": "On-chip resourses may not compatible."
  }
}

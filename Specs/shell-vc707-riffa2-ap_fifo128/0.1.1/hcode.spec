{
  "name": "shell-vc707-riffa2-ap_fifo128",
  "type": "shell",
  "version": "0.1.1",
  "summary": "A hCODE shell based on RIFFA2.2.1 (VC707_Gen2x8If128) PCIe module.",
  "description": "RIFFA is original developed in http://riffa.ucsd.edu/. The hCODE version is developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://riffa.ucsd.edu/",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-vc707-riffa2-ap_fifo128.git",
    "tag": "0.1.1"
  },
  "hardware": {
    "board": "vc707",
    "device": "xc7vx485tffg1761-2"
  },
  "interface": {
    "host": {
      "ap_fifo": {
        "data_width": 128 
       }
    }
  },
  "compatible_shell": {
    "shell-vc707-xillybus-ap_fifo128": "Shell driver not compatible.",
    "shell-vc707-xillybus-ap_fifo32": "Shell driver not compatible.",
    "shell-zedboard-xillybus-ap_fifo32": "Shell driver not compatible.",
    "shell-zybo-xillybus-ap_fifo32": "Shell driver not compatible."
  }
}

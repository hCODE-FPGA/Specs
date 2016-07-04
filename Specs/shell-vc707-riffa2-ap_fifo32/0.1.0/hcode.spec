{
  "name": "shell-vc707-riffa2-ap_fifo32",
  "type": "shell",
  "version": "0.1.0",
  "summary": "A hCODE shell based on RIFFA2.2.1 (VC707_Gen2x8If128) PCIe module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://arch.cs.kumamoto-u.ac.jp/hcode",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-vc707-riffa2-ap_fifo32.git",
    "tag": "0.1.0"
  },
  "platforms": {
    "vc707": "0.0.0"
  },
  "ides": {
    "version": "vivado2015.3",
    "version": "vivado2015.4"
  },
  "properties": {
    "max-clock": "250MHz",
    "host-fpga": {
        "name": "riffa2.2.1",
        "interface": {
            "protocol" : "axi-stream",
            "datawidth" : "32"
        }
    }
  }
}

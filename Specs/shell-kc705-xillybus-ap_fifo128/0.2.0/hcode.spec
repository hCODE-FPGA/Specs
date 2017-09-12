{
  "name": "shell-kc705-xillybus-ap_fifo128",
  "type": "shell",
  "version": "0.2.0",
  "summary": "A hCODE shell based on xillybus-eval-kintex7-1.2d PCIe module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "https://github.com/jonsonxp/shell-kc705-xillybus-ap_fifo128",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-kc705-xillybus-ap_fifo128.git",
    "tag": "0.2.0"
  },
  "hardware": {
  	"board": "kc705",
    "device": "xc7k325tffg900-2"
  },
  "interface": {
    "host": {
       "bandwidth": 1800,
       "ports":{
         "ap_fifo": {
           "type": "ap_fifo",
           "data_width": 128,
           "device_file_read": "/dev/xillybus_read_128",
           "device_file_write": "/dev/xillybus_write_128"
         },
         "mem": {
          "data_width": 256
         } 
       }
    }
  },
  "resource": {
    "1": {
        "LUT": 196955,
        "LUTRAM": 62947,
        "FF": 400713,
        "BRAM": 427,
        "DSP": 840
    }
  },
  "compatible_shell": {
    "shell-vc707-xillybus-ap_fifo128": "Interface compatible. Notice KC705 has less resources than VC707."
  }
}

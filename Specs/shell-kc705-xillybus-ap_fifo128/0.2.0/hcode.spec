{
  "name": "shell-kc705-xillybus-ap_fifo128",
  "type": "shell",
  "version": "0.2.0",
  "summary": "A hCODE shell for KC705 board based on xillybus-eval-kintex7-2.0c PCIe module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://arch.cs.kumamoto-u.ac.jp/hcode",
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
        "LUT": 196869,
        "LUTRAM": 62903,
        "FF": 400734,
        "BRAM": 430,
        "DSP": 840
    }
  }
}

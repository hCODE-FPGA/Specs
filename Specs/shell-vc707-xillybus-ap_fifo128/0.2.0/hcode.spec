{
  "name": "shell-vc707-xillybus-ap_fifo128",
  "type": "shell",
  "version": "0.2.0",
  "summary": "A hCODE shell based on xillybus-eval-vertex7-1.2c PCIe module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "http://arch.cs.kumamoto-u.ac.jp/hcode",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-vc707-xillybus-ap_fifo128.git",
    "tag": "0.2.0"
  },
  "hardware": {
    "board": "vc707",
    "device": "xc7vx485tffg1761-2"
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
        "LUT": 296748,
        "LUTRAM": 129751,
        "FF": 600325,
        "BRAM": 1012,
        "DSP": 2800
    }
  }
}

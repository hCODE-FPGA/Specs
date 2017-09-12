{
  "name": "shell-vc707-xillybus-ap_fifo128-2ch",
  "type": "shell",
  "version": "0.2.0",
  "summary": "A hCODE shell with 2 communication channels based on xillybus-eval-vertex7-1.2c PCIe module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "https://github.com/jonsonxp/shell-vc707-xillybus-ap_fifo128-2ch",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-vc707-xillybus-ap_fifo128-2ch.git",
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
         "ap_fifo_1": {
           "type": "ap_fifo",
           "data_width": 128,
           "device_file_read": "/dev/xillybus_read_128_1",
           "device_file_write": "/dev/xillybus_write_128_1"
         },
         "ap_fifo_2": {
           "type": "ap_fifo",
           "data_width": 128,
           "device_file_read": "/dev/xillybus_read_128_2",
           "device_file_write": "/dev/xillybus_write_128_2"
         },
         "mem": {
          "data_width": 256
         } 
       }
    }
  },
  "resource": {
    "1": {
    "LUT": 294751,
    "LUTRAM": 128916,
    "FF": 599122,
    "BRAM": 1003,
    "DSP": 2800
    }
  },
  "compatible_shell": {
    "shell-vc707-xillybus-ap_fifo128": "2ch version."
  }
}

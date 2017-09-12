{
  "name": "shell-vc707-xillybus-ap_fifo128-4ch",
  "type": "shell",
  "version": "0.2.0",
  "summary": "A hCODE shell with 4 communication channels based on xillybus-eval-vertex7-1.2c PCIe module.",
  "description": "Developed in Computer Arch. Lab@Kumamoto University, Japan.",
  "homepage": "https://github.com/jonsonxp/shell-vc707-xillybus-ap_fifo128-4ch",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/shell-vc707-xillybus-ap_fifo128-4ch.git",
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
         "ap_fifo_3": {
           "type": "ap_fifo",
           "data_width": 128,
           "device_file_read": "/dev/xillybus_read_128_3",
           "device_file_write": "/dev/xillybus_write_128_3"
         },
         "ap_fifo_4": {
           "type": "ap_fifo",
           "data_width": 128,
           "device_file_read": "/dev/xillybus_read_128_4",
           "device_file_write": "/dev/xillybus_write_128_4"
         },
         "mem": {
          "data_width": 256
         } 
       }
    }
  },
  "resource": {
    "1": {
        "LUT": 290813,
        "LUTRAM": 127252,
        "FF": 596848,
        "BRAM": 985
    }
  },
  "compatible_shell": {
    "shell-vc707-xillybus-ap_fifo128": "4ch version."
  }
}

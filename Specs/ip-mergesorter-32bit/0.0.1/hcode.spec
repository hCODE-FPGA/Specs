{
  "name": "ip-mergesorter-32bit",
  "type": "ip",
  "version": "0.0.1",
  "summary": "A merge sorter IP with 32-bit width ap_fifo interface implemented in Vivado HLS.",
  "description": "A merge sorter IP with 32-bit width ap_fifo interface implemented in Vivado HLS.",
  "homepage": "https://github.com/jonsonxp/ip-mergesorter-32bit",
  "license": "MIT",
  "authors": {
    "Qian ZHAO": "cho@arch.cs.kumamoto-u.ac.jp"
  },
  "source": {
    "git": "https://github.com/jonsonxp/ip-mergesorter-32bit.git",
    "tag": "0.0.1"
  },
  "platforms": {
    "vc707": "0.0.0"
  },
  "shells": {
    "shell-vc707-xillybus-ap_fifo32": true
  },
  "code": {
    "verilog": true, 
    "verilog_generator": false,
    "vhdl": false,
    "vhdl_generator": false,
    "vivado_hls": true,
    "hls_generator": true
  },
  "ides": [
    {"vivado2015.3": true},
    {"vivado2015.4": true}
  ],
  "properties": {
    "max-clock": "250MHz",
    "host-fpga": {
        "name": "xillybus-eval-virtex7-1.2c",
        "interface": {
            "protocol" : "ap-stream",
            "datawidth" : "32"
        }
    }
  }
}


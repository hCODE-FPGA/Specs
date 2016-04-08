{
  "name": "ip-mergesorter-32bit",
  "type": "ip",
  "version": "0.0.1",
  "summary": "A mergesorter for 32bit integer numbers.",
  "description": "A merge sorter IP with 32-bit width ap_fifo interface implemented in Vivado HLS.",
  "homepage": "https://github.com/jonsonxp/ip-mergesorter-32bit/",
  "license": "MIT",
  "authors": {
    "jonsonxp": "ofmsmile@msn.com"
  },
  "source": {
    "git": "https://github.com/jonsonxp/ip-mergesorter-32bit.git",
    "tag": "0.0.1"
  },
  "code": {
    "verilog": true, 
    "verilog_generator": false,
    "vhdl": false,
    "vhdl_generator": false,
    "vivado_hls": true,
    "hls_generator": true
  },
  "ides": {
    "version": "vivado2015.3",
    "version": "vivado2015.4"
  },
  "platforms": {
    "vc707": {
      "shell": "shell-vc707-xillybus-ap_fifo32",
      "size": 128,
      "clk_period": 10
    },
    "zybo": {
      "shell": "shell-zybo-xillybus-ap_fifo32",
      "size": 32,
      "clk_period": 5
    }
  },
  "interfaces": {
    "host-fpga": {
        "name": "xillybus",
        "interface": {
            "protocol" : "ap-stream",
            "datawidth" : "32"
        }
    }
  }
}


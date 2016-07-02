{
  "name": "ip-mergesorter",
  "type": "ip",
  "version": "0.0.1",
  "summary": "A mergesorter IP for any data-width integer numbers.",
  "description": "A merge sorter IP that can generate specified depth and data-width mergesorter tree with ap_fifo interface implemented in Vivado HLS.",
  "homepage": "https://github.com/jonsonxp/ip-mergesorter/",
  "license": "MIT",
  "authors": {
    "jonsonxp": "ofmsmile@msn.com"
  },
  "source": {
    "git": "https://github.com/jonsonxp/ip-mergesorter.git",
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
    "shell-vc707-xillybus-ap_fifo32": {
      "shell": "shell-vc707-xillybus-ap_fifo32",
      "data-width": 32,
      "size": 128,
      "clk_period": 5.714,
      "reference": " ip_mergesorter ip_mergesorter_0 (.ap_clk(ip_clk), .ap_rst(~ip_rst_n), .in_V_V_dout(in_r_dout), .in_V_V_empty_n(in_r_empty_n), .in_V_V_read(in_r_read), .out_V_V_din(out_r_din), .out_V_V_full_n(!out_r_full), .out_V_V_write(out_r_write));"
    },
    "shell-zybo-xillybus-ap_fifo32": {
      "shell": "shell-zybo-xillybus-ap_fifo32",
      "data-width": 32,
      "size": 32,
      "clk_period": 8,
      "reference": " ip_mergesorter ip_mergesorter_0 (.ap_clk(ip_clk), .ap_rst(~ip_rst_n), .in_V_V_dout(in_r_dout), .in_V_V_empty_n(in_r_empty_n), .in_V_V_read(in_r_read), .out_V_V_din(out_r_din), .out_V_V_full_n(!out_r_full), .out_V_V_write(out_r_write));"
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


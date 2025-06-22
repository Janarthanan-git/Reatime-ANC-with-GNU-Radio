"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self, mu=0.01, length=32):
        gr.sync_block.__init__(self,
            name="lms_filter",
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32])
        self.mu = mu
        self.length = length
        self.w = np.zeros(length)
        self.x_buf = np.zeros(length)

    def work(self, input_items, output_items):
        ref = input_items[0]
        primary = input_items[1]
        error = output_items[0]

        for i in range(len(ref)):
            self.x_buf = np.roll(self.x_buf, -1)
            self.x_buf[-1] = ref[i]
            y = np.dot(self.w, self.x_buf)
            e = primary[i] - y
            self.w += self.mu * e * self.x_buf
            error[i] = e
        return len(error)

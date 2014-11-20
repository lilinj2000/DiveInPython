#! /usr/bin/python
import sys
sys.path.append('../../')

import statsout

def output(data, format='text'):
    """"""
    output_function = getattr(statsout, "output_%s" % format, statsout.output_ext)
    return output_function(data)
    



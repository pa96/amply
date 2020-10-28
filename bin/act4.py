#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division
from builtins import map, range, object, zip, sorted
import sys
import os
from amplpy import Environment

def main(argc, argv):
    from amplpy import AMPL
    os.chdir(os.path.dirname(__file__) or os.curdir)
    try:
        # Create an AMPL instance
        ampl = AMPL(Environment('C:/Users/Paulina/Desktop/Atom/amply/ampl.mswin64'))

        """
        # If the AMPL installation directory is not in the system search path:
        from amplpy import Environment
        ampl = AMPL(
            Environment('C:/xampp/htdocs/python/ampl/ampl.mswin64'))
        """

        if argc > 1:
            ampl.setOption('solver', argv[1])

        # Read the model and data files.
        modelDirectory = argv[2] if argc == 3 else os.path.join('..', 'models')
        ampl.read(os.path.join(modelDirectory, 'act4/act4.mod'))
        ampl.readData(os.path.join(modelDirectory, 'act4/act4.dat'))

        # Solve
        ampl.solve()

        #-----------
        buy = ampl.getVariable('xt')
        df = buy.getValues()
        # Print them
        print('xt ->',df)
        #-----------
        buy = ampl.getVariable('sit')
        df = buy.getValues()
        # Print them
        print('sit ->',df)
        #-----------
        buy = ampl.getVariable('yit')
        df = buy.getValues()
        # Print them
        print('yit ->',df)
        #-----------
        buy = ampl.getVariable('pt')
        df = buy.getValues()
        # Print them
        print('pt ->',df)


    except Exception as e:
        print(e)
        raise


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

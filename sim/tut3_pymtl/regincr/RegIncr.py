#=========================================================================
# RegIncr
#=========================================================================
# This is a simple model for a registered incrementer. An eight-bit value
# is read from the input port, registered, incremented by one, and
# finally written to the output port.

from pymtl import *

class RegIncr( Model ):

  # Constructor

  def __init__( s ):

    # Port-based interface

    s.in_ = InPort  ( Bits(8) )
    s.out = OutPort ( Bits(8) )

    # Concurrent block modeling register

    s.reg_out = Wire( Bits(8) )

    @s.tick
    def block1():
      if s.reset:
        s.reg_out.next = 0
      else:
        s.reg_out.next = s.in_

    # Concurrent block modeling incrementer

    # ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''
    # Use a combinational concurrent block to model the incrementer
    # logic. Remember to always use .value when writing signals from
    # within a combinational concurrent block!

  # Line Tracing

  def line_trace( s ):
    return "{} ({}) {}".format( s.in_, s.reg_out, s.out )

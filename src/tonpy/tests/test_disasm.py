# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0
from multiprocessing import Pool

from tonpy import VmDict
from tonpy.fift.disasm import disassembler
from tonpy.types.cell import Cell
from tonpy.data_for_tests.emulator_data import tx as test_tx

test1 = """IF:<{
  PUSHINT 123456789
}>ELSE<{
  PUSHSLICE x{12345}
}>
WHILE:<{
  ADD
}>DO<{
  PUSHINT 10
  REPEAT:<{
    CONT:<{
      NOP
    }>
    CONT:<{
    }>
  }>
}>
"""

test2 = """SETCP 0
DICTPUSHCONST 19, (xC_)
DICTIGETJMPZ {
  0 => <{
  }>
  11 => <{
    ADDINT 123
  }>
  12 => <{
    OVER
    EQINT 5
    IFJMP:<{
      NIP
    }>
    MUL
  }>
  13 => <{
    ADD
    CALLDICT 12
  }>
}
THROWARG 11
"""

test3 = """SETCP 0
DICTPUSHCONST 19, (xC_)
DICTIGETJMPZ {
  0 => <{
    SWAP
    CTOS
    LDU 4
    LDMSGADDR
    LDMSGADDR
    NIP
    LDGRAMS
    PUSHINT 1
    SDSKIPFIRST
    LDGRAMS
    NIP
    LDGRAMS
    DROP
    PUSHINT 3
    MULRSHIFT# 1
    TUPLE 0
    XCHG2 s0, s4
    TPUSH
    ROT
    TPUSH
    SWAP
    TPUSH
    SWAP
    TPUSH
    SETGLOB 1
    GETGLOB 1
    INDEX 0
    PUSHINT 1
    AND
    THROWIF 0
    DUP
    PLDU 32
    DUP
    PUSHINT 444
    EQUAL
    IFJMP:<{
      DROP
      CALLDICT 120
    }>
    DUP
    PUSHINT 3043726744
    EQUAL
    IFJMP:<{
      DROP
      CALLDICT 124
    }>
    DUP
    PUSHINT 2078119902
    EQUAL
    IFJMP:<{
      DROP
      CALL:<{
        CALL:<{
          PUSH c4
          CTOS
          LDREF
          OVER
          CTOS
          LDMSGADDR
          LDU 8
          SWAP
          SWAP
          NIP
          LDU 1
          CONT:<{
            SAVECTR c2
            SAMEALTSAVE
            DUP
            PLDU 4
            DUP
            EQINT 0
            IF:<{
              DROP
              LDSLICE 4
              SWAP
            }>ELSE<{
              EQINT 1
              IFJMP:<{
                PUSHINT 268
                LDSLICEX
                SWAP
                RETALT
              }>
              DROP
              THROW 261
              PUSHNULL
              PUSHNULL
            }>
          }>
          EXECUTE
          SWAP
          CONT:<{
            SAVECTR c2
            SAMEALTSAVE
            DUP
            PLDU 4
            DUP
            EQINT 0
            IF:<{
              DROP
              LDSLICE 4
              SWAP
            }>ELSE<{
              EQINT 1
              IFJMP:<{
                PUSHINT 268
                LDSLICEX
                SWAP
                RETALT
              }>
              DROP
              THROW 261
              PUSHNULL
              PUSHNULL
            }>
          }>
          EXECUTE
          XCHG3 s3, s3, s0
          TUPLE 3
          NIP
          SETGLOB 5
          XCHG s0, s2
          SETGLOB 3
          LDREF
          ROTREV
          TUPLE 2
          SETGLOB 2
          LDREF
          SWAP
          SETGLOB 9
          LDREF
          OVER
          CTOS
          LDU 8
          LDU 8
          ROTREV
          TUPLE 2
          SETGLOB 12
          LDMSGADDR
          LDMSGADDR
          ROTREV
          TUPLE 2
          SETGLOB 13
          LDMSGADDR
          SWAP
          SETGLOB 14
          ENDS
          SWAP
          SETGLOB 11
          LDU 16
          SWAP
          SETGLOB 4
          LDU 16
          SWAP
          SETGLOB 6
          LDGRAMS
          SWAP
          SETGLOB 10
          LDGRAMS
          LDGRAMS
          ROTREV
          TUPLE 2
          SETGLOB 7
          LDGRAMS
          LDGRAMS
          ROTREV
          TUPLE 2
          SETGLOB 8
          ENDS
        }>
        PUSHINT 32
        SDSKIPFIRST
        LDU 64
        SWAP
        SWAP
        LDGRAMS
        LDMSGADDR
        LDMSGADDR
        DROP
        DROP
        DUP
        GETGLOB 9
        GETGLOB 9
        NEWC
        PUSHINT 0
        STGRAMS
        XCHG2 s0, s3
        STSLICER
        MYADDR
        STSLICER
        XCHG s1, s2
        STREF
        ENDC
        PUSHINT 6
        NEWC
        STU 5
        XCHG s1, s2
        STREF
        STREF
        ENDC
        PUSHINT 0
        SWAP
        HASHCU
        PUSHINT 4
        NEWC
        STU 3
        XCHG s1, s2
        STI 8
        STU 256
        ENDC
        CTOS
        GETGLOB 1
        INDEX 1
        SWAP
        SDEQ
        THROWIFNOT 257
        GETGLOB 7
        UNTUPLE 2
        GETGLOB 10
        PU2XC s2, s4, s(-2)
        MULDIV
        GETGLOB 10
        PU2XC s2, s5, s(-2)
        MULDIV
        XCPU s3, s1
        SUB
        XCPU s2, s3
        SUB
        GETGLOB 10
        PUSH s6
        SUB
        SETGLOB 10
        PUSH2 s2, s0
        TUPLE 2
        SETGLOB 7
        PUSH s4
        XCPU2 s3, s2, s4
        XCHG2 s3, s3
        XCHG s0, s8
        NEWC
        PUSHINT 984117414
        SWAP
        STU 32
        XCHG2 s0, s6
        STSLICER
        XCHG2 s0, s5
        STGRAMS
        XCHG2 s0, s3
        STGRAMS
        SWAP
        STGRAMS
        SWAP
        STGRAMS
        SWAP
        STGRAMS
        NEWC
        PUSHINT 2
        STONES
        PUSHINT 102
        STZEROES
        SWAP
        STBR
        ENDC
        PUSHINT 1
        SENDRAWMSG
        PUSHINT 1000000
        BALANCE
        INDEX 0
        GETGLOB 1
        INDEX 2
        TUCK
        SUB
        PUXC s2, s(-1)
        MIN
        XCHG s1, s2
        SUB
        SUB
        PUSHINT 15500000
        SUB
        GETGLOB 13
        UNTUPLE 2
        PUSHINT 0
        GETGLOB 3
        PUSHNULL
        PUSH s9
        XCPUXC s9, s8, s3
        XCHG s0, s10
        NEWC
        PUSHINT 2907617013
        SWAP
        STU 32
        XCHG2 s0, s5
        SWAP
        STU 64
        XCHG s1, s3
        STREF
        SWAP
        STGRAMS
        SWAP
        STSLICER
        STDICT
        PUSH s3
        RSHIFT 1
        XCHG s3, s7
        XCHG3 s1, s0, s7
        PUSHINT 24
        NEWC
        STU 6
        SWAP
        STSLICER
        SWAP
        STGRAMS
        PUSHINT 107
        STZEROES
        SWAP
        STBR
        ENDC
        SWAP
        SENDRAWMSG
        DUP
        RSHIFT 1
        SUB
        PUSHINT 0
        GETGLOB 3
        XCHG s3, s6
        XCHG3 s0, s6, s4
        PUSHNULL
        NEWC
        PUSHINT 2907617013
        SWAP
        STU 32
        XCHG2 s0, s5
        SWAP
        STU 64
        XCHG s1, s3
        STREF
        SWAP
        STGRAMS
        SWAP
        STSLICER
        STDICT
        XCHG s0, s2
        PUSHINT 24
        NEWC
        STU 6
        SWAP
        STSLICER
        SWAP
        STGRAMS
        PUSHINT 107
        STZEROES
        SWAP
        STBR
        ENDC
        SWAP
        SENDRAWMSG
        GETGLOB 11
        GETGLOB 9
        GETGLOB 2
        INDEX 1
        GETGLOB 3
        NEWC
        STREF
        STREF
        STREF
        STREF
        GETGLOB 4
        SWAP
        STU 16
        GETGLOB 6
        SWAP
        STU 16
        GETGLOB 10
        STGRAMS
        GETGLOB 7
        INDEX 0
        STGRAMS
        GETGLOB 7
        INDEX 1
        STGRAMS
        GETGLOB 8
        INDEX 0
        STGRAMS
        GETGLOB 8
        INDEX 1
        STGRAMS
        ENDC
        POP c4
      }>
    }>
    DUP
    PUSHINT 1643009069
    EQUAL
    IFJMP:<{
      DROP
      CALL:<{
        PUSH c4
        CTOS
        LDREF
        OVER
        CTOS
        LDMSGADDR
        LDU 8
        SWAP
        SWAP
        NIP
        LDU 1
        CONT:<{
          SAVECTR c2
          SAMEALTSAVE
          DUP
          PLDU 4
          DUP
          EQINT 0
          IF:<{
            DROP
            LDSLICE 4
            SWAP
          }>ELSE<{
            EQINT 1
            IFJMP:<{
              PUSHINT 268
              LDSLICEX
              SWAP
              RETALT
            }>
            DROP
            THROW 261
            PUSHNULL
            PUSHNULL
          }>
        }>
        EXECUTE
        SWAP
        CONT:<{
          SAVECTR c2
          SAMEALTSAVE
          DUP
          PLDU 4
          DUP
          EQINT 0
          IF:<{
            DROP
            LDSLICE 4
            SWAP
          }>ELSE<{
            EQINT 1
            IFJMP:<{
              PUSHINT 268
              LDSLICEX
              SWAP
              RETALT
            }>
            DROP
            THROW 261
            PUSHNULL
            PUSHNULL
          }>
        }>
        EXECUTE
        XCHG3 s3, s3, s0
        TUPLE 3
        NIP
        SETGLOB 5
        XCHG s0, s2
        SETGLOB 3
        LDREF
        ROTREV
        TUPLE 2
        SETGLOB 2
        LDREF
        SWAP
        SETGLOB 9
        LDREF
        OVER
        CTOS
        LDU 8
        LDU 8
        ROTREV
        TUPLE 2
        SETGLOB 12
        LDMSGADDR
        LDMSGADDR
        ROTREV
        TUPLE 2
        SETGLOB 13
        LDMSGADDR
        SWAP
        SETGLOB 14
        ENDS
        SWAP
        SETGLOB 11
        LDU 16
        SWAP
        SETGLOB 4
        LDU 16
        SWAP
        SETGLOB 6
        LDGRAMS
        SWAP
        SETGLOB 10
        LDGRAMS
        LDGRAMS
        ROTREV
        TUPLE 2
        SETGLOB 7
        LDGRAMS
        LDGRAMS
        ROTREV
        TUPLE 2
        SETGLOB 8
        ENDS
      }>
      PUSHINT 32
      SDSKIPFIRST
      LDU 64
      SWAP
      SWAP
      LDREF
      LDGRAMS
      LDMSGADDR
      LDU 1
      LDGRAMS
      LDDICT
      BLKSWAP 3, 1
      XCHG s0, s3
      LDREF
      ENDS
      XCHG3 s1, s3, s0
      XCHG s0, s6
      CALL:<{
        GETGLOB 2
        INDEX 1
        OVER
        PUSHINT 6
        NEWC
        STU 5
        XCHG s1, s2
        STREF
        STREF
        ENDC
        PUSHINT 0
        SWAP
        HASHCU
        PUSHINT 4
        NEWC
        STU 3
        XCHG s1, s2
        STI 8
        STU 256
        ENDC
        CTOS
        SWAP
        CTOS
        LDMSGADDR
        LDU 8
        SWAP
        SWAP
        CONT:<{
          SAVECTR c2
          SAMEALTSAVE
          DUP
          PLDU 4
          DUP
          EQINT 0
          IF:<{
            DROP
            LDSLICE 4
            SWAP
          }>ELSE<{
            EQINT 1
            IFJMP:<{
              PUSHINT 268
              LDSLICEX
              SWAP
              RETALT
            }>
            DROP
            THROW 261
            PUSHNULL
            PUSHNULL
          }>
        }>
        EXECUTE
        SWAP
        ENDS
        GETGLOB 1
        INDEX 1
        XCHG2 s0, s4
        SDEQ
        GETGLOB 2
        INDEX 0
        XCHG2 s0, s3
        SDEQ
        XCHG s1, s2
        AND
        SWAP
        EQINT 1
        AND
        THROWIFNOT 264
      }>
      XCHG s4, s6
      XCHG s0, s5
      XCHG s0, s4
      CALL:<{
        SAVECTR c2
        SAMEALTSAVE
        POP s3
        PUSH3 s6, s5, s4
        PUSH s6
        PUSH c4
        PUSH c5
        PUSH c7
        CONT:<{
          2DROP
          PUSHINT 64
          GETGLOB 3
          XCHG s3, s5
          XCHG3 s0, s0, s4
          PUSHNULL
          NEWC
          PUSHINT 2907617013
          SWAP
          STU 32
          XCHG2 s0, s5
          SWAP
          STU 64
          XCHG s1, s3
          STREF
          SWAP
          STGRAMS
          SWAP
          STSLICER
          STDICT
          PUSHINT 0
          XCHG s0, s3
          PUSHINT 1
          NEWC
          ROT
          STSLICER
          GETGLOB 2
          UNTUPLE 2
          NEWC
          ROT
          STSLICER
          XCHG s1, s3
          STU 8
          SWAP
          STBR
          ENDC
          PUSHINT 6
          NEWC
          STU 5
          XCHG s1, s2
          STREF
          STREF
          ENDC
          PUSHINT 0
          SWAP
          HASHCU
          PUSHINT 4
          NEWC
          STU 3
          XCHG s1, s2
          STI 8
          STU 256
          ENDC
          CTOS
          XCHG3 s1, s3, s0
          PUSHINT 24
          NEWC
          STU 6
          SWAP
          STSLICER
          SWAP
          STGRAMS
          PUSHINT 107
          STZEROES
          SWAP
          STBR
          ENDC
          SWAP
          SENDRAWMSG
          RETALT
        }>
        SETCONTCTR c7
        SETCONTCTR c5
        SETCONTCTR c4
        PUSHINT 4
        PUSHINT -1
        SETCONTVARARGS
        CONT:<{
          GETGLOB 5
          UNTUPLE 3
          GETGLOB 7
          UNTUPLE 2
          GETGLOB 12
          UNTUPLE 2
          GETGLOB 13
          UNTUPLE 2
          PUSH2 s13, s7
          SDEQ
          PUSH2 s14, s7
          SDEQ
          OR
          THROWIFNOT 261
          PUSHINT 1000000
          BALANCE
          INDEX 0
          GETGLOB 1
          INDEX 2
          TUCK
          SUB
          PUXC s2, s(-1)
          MIN
          XCHG s1, s2
          SUB
          SUB
          PUSHINT 4000000
          PUSH s10
          IF:<{
            PUSHINT 28000000
          }>ELSE<{
            PUSHINT 17000000
          }>
          ADD
          SUB
          PUSH s12
          CTOS
          LDU 32
          SWAP
          SWAP
          LDMSGADDR
          LDMSGADDR
          LDDICT
          LDDICT
          ENDS
          PUSH s19
          PUSH s14
          SDEQ
          IF:<{
            PUSH2 s11, s10
          }>ELSE<{
            POP s12
            PUSH3 s12, s9, s10
            XCHG s2, s14
            XCHG s10, s11
            XCHG s8, s9
          }>
          GETGLOB 6
          PUSH s21
          SWAP
          PUSHINT 10000
          MULDIV
          PUSH s21
          OVER
          SUB
          XCHG s0, s5
          XCHG s0, s18
          XCHG s0, s5
          XCHG s0, s4
          XCHG2 s13, s12
          XCHG s0, s5
          IF:<{
            PUSHINT 1
            SWAP
            REPEAT:<{
              MULINT 10
            }>
            XCHG s0, s4
            PUSHINT 1
            SWAP
            REPEAT:<{
              MULINT 10
            }>
            PUSH3 s2, s1, s4
            PUSH s3
            XCHG s1, s3
            PUSHINT 1000000000000000000
            XCHG2 s0, s4
            MULDIV
            PUSHINT 1000000000000000000
            XCHG2 s0, s3
            MULDIV
            2DUP
            PUSHINT 1000000000000000000
            MULDIV
            XCPU s2, s0
            PUSHINT 1000000000000000000
            MULDIV
            XCPU s1, s0
            PUSHINT 1000000000000000000
            MULDIV
            ADD
            PUSHINT 1000000000000000000
            MULDIV
            XCHG s0, s4
            PUSHINT 1000000000000000000
            PUSH s6
            MULDIV
            XCHG s1, s3
            PUSHINT 1000000000000000000
            XCHG2 s0, s6
            MULDIV
            SWAP
            PUSHINT 1000000000000000000
            PUSH s3
            MULDIV
            XCHG2 s4, s4
            ADD
            XC2PU s0, s2, s3
            CONT:<{
              SAVECTR c2
              SAMEALTSAVE
              PUSHINT 0
              WHILE:<{
                DUP
                PUSHPOW2DEC 8
                LESS
              }>DO<{
                PUSH3 s1, s3, s1
                PUSH2 s0, s0
                PUSHINT 1000000000000000000
                MULDIV
                OVER
                PUSHINT 1000000000000000000
                MULDIV
                PUXC s2, s(-1)
                PUSHINT 1000000000000000000
                MULDIV
                PUSH2 s2, s2
                PUSHINT 1000000000000000000
                MULDIV
                XCHG2 s0, s3
                PUSHINT 1000000000000000000
                MULDIV
                SWAP
                PUSHINT 1000000000000000000
                MULDIV
                ADD
                PUSH2 s0, s4
                LESS
                IF:<{
                  PUXC s4, s(-1)
                  SUB
                  PUSHINT 1000000000000000000
                  PUSH2 s6, s4
                  OVER
                  MULINT 3
                  XCPU s1, s0
                  PUSHINT 1000000000000000000
                  MULDIV
                  PUSHINT 1000000000000000000
                  MULDIV
                  PUSH2 s1, s1
                  PUSHINT 1000000000000000000
                  MULDIV
                  ROT
                  PUSHINT 1000000000000000000
                  MULDIV
                  ADD
                  MULDIV
                  XCHG s1, s3
                  ADD
                }>ELSE<{
                  PUSH s4
                  SUB
                  PUSHINT 1000000000000000000
                  PUSH2 s6, s4
                  OVER
                  MULINT 3
                  XCPU s1, s0
                  PUSHINT 1000000000000000000
                  MULDIV
                  PUSHINT 1000000000000000000
                  MULDIV
                  PUSH2 s1, s1
                  PUSHINT 1000000000000000000
                  MULDIV
                  ROT
                  PUSHINT 1000000000000000000
                  MULDIV
                  ADD
                  MULDIV
                  XCHG s1, s3
                  SUB
                }>
                PUSH2 s0, s2
                GREATER
                IF:<{
                  PUXC s0, s2
                  SUB
                  LESSINT 2
                  IFJMP:<{
                    XCHG s1, s3
                    BLKDROP 3
                    RETALT
                  }>
                }>ELSE<{
                  XCPU s2, s2
                  SUB
                  LESSINT 2
                  IFJMP:<{
                    XCHG s1, s3
                    BLKDROP 3
                    RETALT
                  }>
                }>
                INC
              }>
              XCHG s1, s3
              BLKDROP 3
            }>
            EXECUTE
            XCHG s1, s2
            SUB
            SWAP
            PUSHINT 1000000000000000000
            MULDIV
          }>ELSE<{
            DROP
            POP s3
            OVER
            ADD
            XCHG s1, s2
            MULDIV
          }>
          PUSH s3
          NOW
          LESS
          XCHG s1, s4
          AND
          PUXC s3, s(-1)
          XCHG s0, s16
          LESS
          XCHG s1, s15
          OR
          IFJMP:<{
            XCHG s2, s3
            BLKDROP 3
            BLKDROP2 9, 3
            POP s4
            PUSHINT 0
            GETGLOB 3
            XCHG s4, s7
            XCHG3 s7, s6, s3
            NEWC
            PUSHINT 2907617013
            SWAP
            STU 32
            XCHG2 s0, s5
            SWAP
            STU 64
            XCHG s1, s3
            STREF
            SWAP
            STGRAMS
            SWAP
            STSLICER
            STDICT
            XCHG3 s0, s1, s3
            PUSHINT 24
            NEWC
            STU 6
            SWAP
            STSLICER
            SWAP
            STGRAMS
            PUSHINT 107
            STZEROES
            SWAP
            STBR
            ENDC
            SWAP
            SENDRAWMSG
            RETALT
          }>
          POP s4
          POP s4
          GETGLOB 8
          UNTUPLE 2
          PUSH s16
          XCHG2 s0, s11
          SDEQ
          IF:<{
            PUSH2 s14, s5
            SUB
            XCHG s1, s8
            ADD
            XCPU s6, s4
            SUB
            XCHG2 s7, s5
            ADD
          }>ELSE<{
            PUSH2 s14, s5
            SUB
            XCHG s1, s7
            ADD
            XCPU s7, s4
            SUB
            XCHG2 s9, s5
            ADD
            XCHG s0, s8
            XCHG s0, s6
            XCHG s0, s4
            XCHG s0, s5
          }>
          PUSH2 s5, s4
          TUPLE 2
          SETGLOB 7
          XCHG2 s0, s8
          TUPLE 2
          SETGLOB 8
          GETGLOB 11
          GETGLOB 9
          GETGLOB 2
          INDEX 1
          GETGLOB 3
          NEWC
          STREF
          STREF
          STREF
          STREF
          GETGLOB 4
          SWAP
          STU 16
          GETGLOB 6
          SWAP
          STU 16
          GETGLOB 10
          STGRAMS
          GETGLOB 7
          INDEX 0
          STGRAMS
          GETGLOB 7
          INDEX 1
          STGRAMS
          GETGLOB 8
          INDEX 0
          STGRAMS
          GETGLOB 8
          INDEX 1
          STGRAMS
          ENDC
          POP c4
          PUSH s13
          XCPU s5, s6
          XCHG s5, s11
          XCHG s4, s14
          XCHG3 s13, s1, s3
          XCPUXC s0, s1, s14
          XCHG s1, s12
          NEWC
          XCHG2 s0, s8
          STSLICER
          XCHG2 s0, s6
          STSLICER
          XCHG2 s0, s5
          STGRAMS
          XCHG2 s0, s5
          STGRAMS
          ENDC
          NEWC
          PUSHINT 2623606243
          SWAP
          STU 32
          XCHG2 s0, s3
          STSLICER
          SWAP
          STSLICER
          XCHG2 s0, s3
          STGRAMS
          SWAP
          STGRAMS
          STREF
          NEWC
          PUSHINT 2
          STONES
          PUSHINT 102
          STZEROES
          SWAP
          STBR
          ENDC
          PUSHINT 1
          SENDRAWMSG
          PUSH s3
          ISNULL
          IF:<{
            DROP
            POP s2
            POP s3
            PUSHINT 0
            GETGLOB 3
            PUSH s5
            PLDU 2
            EQINT 0
            IF:<{
              POP s5
            }>ELSE<{
              POP s7
              XCHG s4, s6
            }>
            XCHG s0, s7
            XCHG s0, s4
            XCHG2 s6, s3
            NEWC
            PUSHINT 2907617013
            SWAP
            STU 32
            XCHG2 s0, s5
            SWAP
            STU 64
            XCHG s1, s3
            STREF
            SWAP
            STGRAMS
            SWAP
            STSLICER
            STDICT
            XCHG s0, s2
            PUSHINT 24
            NEWC
            STU 6
            SWAP
            STSLICER
            SWAP
            STGRAMS
            PUSHINT 107
            STZEROES
            SWAP
            STBR
            ENDC
            SWAP
            SENDRAWMSG
          }>ELSE<{
            POP s6
            2DROP
            CTOS
            LDMSGADDR
            LDU 1
            LDGRAMS
            LDDICT
            BLKSWAP 3, 1
            XCHG s3, s4
            XCHG s0, s4
            ENDS
            BLKSWAP 1, 3
            PUSHINT 0
            GETGLOB 3
            XCHG s8, s11
            XCHG s0, s7
            XCHG s6, s11
            XCHG s5, s11
            XCHG s1, s10
            XCHG s1, s4
            XCHG3 s3, s3, s0
            NEWC
            PUSHINT 1923917994
            SWAP
            STU 32
            XCHG2 s0, s9
            SWAP
            STU 64
            XCHG s1, s7
            STREF
            XCHG2 s0, s5
            STSLICER
            XCHG2 s0, s3
            STGRAMS
            SWAP
            STSLICER
            XCHG2 s2, s3
            XCHG2 s2, s3
            STU 1
            SWAP
            STGRAMS
            STDICT
            STREF
            ENDC
            XCHG3 s0, s1, s3
            PUSHINT 24
            NEWC
            STU 6
            SWAP
            STSLICER
            SWAP
            STGRAMS
            PUSHINT 106
            STZEROES
            STDICT
            ENDC
            SWAP
            SENDRAWMSG
          }>
        }>
        PUSH c1
        BOOLOR
        SWAP
        TRY
      }>
    }>
    DUP
    PUSHINT 1923917994
    EQUAL
    IFJMP:<{
      DROP
      CALL:<{
        PUSH c4
        CTOS
        LDREF
        OVER
        CTOS
        LDMSGADDR
        LDU 8
        SWAP
        SWAP
        NIP
        LDU 1
        CONT:<{
          SAVECTR c2
          SAMEALTSAVE
          DUP
          PLDU 4
          DUP
          EQINT 0
          IF:<{
            DROP
            LDSLICE 4
            SWAP
          }>ELSE<{
            EQINT 1
            IFJMP:<{
              PUSHINT 268
              LDSLICEX
              SWAP
              RETALT
            }>
            DROP
            THROW 261
            PUSHNULL
            PUSHNULL
          }>
        }>
        EXECUTE
        SWAP
        CONT:<{
          SAVECTR c2
          SAMEALTSAVE
          DUP
          PLDU 4
          DUP
          EQINT 0
          IF:<{
            DROP
            LDSLICE 4
            SWAP
          }>ELSE<{
            EQINT 1
            IFJMP:<{
              PUSHINT 268
              LDSLICEX
              SWAP
              RETALT
            }>
            DROP
            THROW 261
            PUSHNULL
            PUSHNULL
          }>
        }>
        EXECUTE
        XCHG3 s3, s3, s0
        TUPLE 3
        NIP
        SETGLOB 5
        XCHG s0, s2
        SETGLOB 3
        LDREF
        ROTREV
        TUPLE 2
        SETGLOB 2
        LDREF
        SWAP
        SETGLOB 9
        LDREF
        OVER
        CTOS
        LDU 8
        LDU 8
        ROTREV
        TUPLE 2
        SETGLOB 12
        LDMSGADDR
        LDMSGADDR
        ROTREV
        TUPLE 2
        SETGLOB 13
        LDMSGADDR
        SWAP
        SETGLOB 14
        ENDS
        SWAP
        SETGLOB 11
        LDU 16
        SWAP
        SETGLOB 4
        LDU 16
        SWAP
        SETGLOB 6
        LDGRAMS
        SWAP
        SETGLOB 10
        LDGRAMS
        LDGRAMS
        ROTREV
        TUPLE 2
        SETGLOB 7
        LDGRAMS
        LDGRAMS
        ROTREV
        TUPLE 2
        SETGLOB 8
        ENDS
      }>
      PUSHINT 32
      SDSKIPFIRST
      LDU 64
      SWAP
      SWAP
      LDREF
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      LDGRAMS
      LDMSGADDR
      LDU 1
      LDGRAMS
      LDDICT
      BLKSWAP 3, 1
      XCHG s0, s3
      LDREF
      DROP
      XCHG3 s1, s3, s0
      XCHG s0, s7
      CALL:<{
        GETGLOB 2
        INDEX 1
        OVER
        PUSHINT 6
        NEWC
        STU 5
        XCHG s1, s2
        STREF
        STREF
        ENDC
        PUSHINT 0
        SWAP
        HASHCU
        PUSHINT 4
        NEWC
        STU 3
        XCHG s1, s2
        STI 8
        STU 256
        ENDC
        CTOS
        SWAP
        CTOS
        LDMSGADDR
        LDU 8
        SWAP
        SWAP
        LDU 1
        CONT:<{
          SAVECTR c2
          SAMEALTSAVE
          DUP
          PLDU 4
          DUP
          EQINT 0
          IF:<{
            DROP
            LDSLICE 4
            SWAP
          }>ELSE<{
            EQINT 1
            IFJMP:<{
              PUSHINT 268
              LDSLICEX
              SWAP
              RETALT
            }>
            DROP
            THROW 261
            PUSHNULL
            PUSHNULL
          }>
        }>
        EXECUTE
        SWAP
        CONT:<{
          SAVECTR c2
          SAMEALTSAVE
          DUP
          PLDU 4
          DUP
          EQINT 0
          IF:<{
            DROP
            LDSLICE 4
            SWAP
          }>ELSE<{
            EQINT 1
            IFJMP:<{
              PUSHINT 268
              LDSLICEX
              SWAP
              RETALT
            }>
            DROP
            THROW 261
            PUSHNULL
            PUSHNULL
          }>
        }>
        EXECUTE
        XCHG3 s3, s3, s0
        TUPLE 3
        SWAP
        ENDS
        GETGLOB 1
        INDEX 1
        XCHG2 s0, s4
        SDEQ
        GETGLOB 2
        INDEX 0
        XCHG2 s0, s3
        SDEQ
        XCHG s1, s2
        AND
        SWAP
        EQINT 2
        AND
        THROWIFNOT 265
      }>
      DROP
      XCHG s3, s6
      BLKSWAP 1, 3
      CALL:<{
        SAVECTR c2
        SAMEALTSAVE
        POP s3
        PUSH3 s6, s5, s4
        PUSH s6
        PUSH c4
        PUSH c5
        PUSH c7
        CONT:<{
          2DROP
          PUSHINT 64
          GETGLOB 3
          XCHG s3, s5
          XCHG3 s0, s0, s4
          PUSHNULL
          NEWC
          PUSHINT 2907617013
          SWAP
          STU 32
          XCHG2 s0, s5
          SWAP
          STU 64
          XCHG s1, s3
          STREF
          SWAP
          STGRAMS
          SWAP
          STSLICER
          STDICT
          PUSHINT 0
          XCHG s0, s3
          PUSHINT 1
          NEWC
          ROT
          STSLICER
          GETGLOB 2
          UNTUPLE 2
          NEWC
          ROT
          STSLICER
          XCHG s1, s3
          STU 8
          SWAP
          STBR
          ENDC
          PUSHINT 6
          NEWC
          STU 5
          XCHG s1, s2
          STREF
          STREF
          ENDC
          PUSHINT 0
          SWAP
          HASHCU
          PUSHINT 4
          NEWC
          STU 3
          XCHG s1, s2
          STI 8
          STU 256
          ENDC
          CTOS
          XCHG3 s1, s3, s0
          PUSHINT 24
          NEWC
          STU 6
          SWAP
          STSLICER
          SWAP
          STGRAMS
          PUSHINT 107
          STZEROES
          SWAP
          STBR
          ENDC
          SWAP
          SENDRAWMSG
          RETALT
        }>
        SETCONTCTR c7
        SETCONTCTR c5
        SETCONTCTR c4
        PUSHINT 4
        PUSHINT -1
        SETCONTVARARGS
        CONT:<{
          GETGLOB 5
          UNTUPLE 3
          GETGLOB 7
          UNTUPLE 2
          GETGLOB 12
          UNTUPLE 2
          GETGLOB 13
          UNTUPLE 2
          PUSH2 s13, s7
          SDEQ
          PUSH2 s14, s7
          SDEQ
          OR
          THROWIFNOT 261
          PUSHINT 1000000
          BALANCE
          INDEX 0
          GETGLOB 1
          INDEX 2
          TUCK
          SUB
          PUXC s2, s(-1)
          MIN
          XCHG s1, s2
          SUB
          SUB
          PUSHINT 4000000
          PUSH s10
          IF:<{
            PUSHINT 28000000
          }>ELSE<{
            PUSHINT 17000000
          }>
          ADD
          SUB
          PUSH s12
          CTOS
          LDU 32
          SWAP
          SWAP
          LDMSGADDR
          LDMSGADDR
          LDDICT
          LDDICT
          ENDS
          PUSH s19
          PUSH s14
          SDEQ
          IF:<{
            PUSH2 s11, s10
          }>ELSE<{
            POP s12
            PUSH3 s12, s9, s10
            XCHG s2, s14
            XCHG s10, s11
            XCHG s8, s9
          }>
          GETGLOB 6
          PUSH s21
          SWAP
          PUSHINT 10000
          MULDIV
          PUSH s21
          OVER
          SUB
          XCHG s0, s5
          XCHG s0, s18
          XCHG s0, s5
          XCHG s0, s4
          XCHG2 s13, s12
          XCHG s0, s5
          IF:<{
            PUSHINT 1
            SWAP
            REPEAT:<{
              MULINT 10
            }>
            XCHG s0, s4
            PUSHINT 1
            SWAP
            REPEAT:<{
              MULINT 10
            }>
            PUSH3 s2, s1, s4
            PUSH s3
            XCHG s1, s3
            PUSHINT 1000000000000000000
            XCHG2 s0, s4
            MULDIV
            PUSHINT 1000000000000000000
            XCHG2 s0, s3
            MULDIV
            2DUP
            PUSHINT 1000000000000000000
            MULDIV
            XCPU s2, s0
            PUSHINT 1000000000000000000
            MULDIV
            XCPU s1, s0
            PUSHINT 1000000000000000000
            MULDIV
            ADD
            PUSHINT 1000000000000000000
            MULDIV
            XCHG s0, s4
            PUSHINT 1000000000000000000
            PUSH s6
            MULDIV
            XCHG s1, s3
            PUSHINT 1000000000000000000
            XCHG2 s0, s6
            MULDIV
            SWAP
            PUSHINT 1000000000000000000
            PUSH s3
            MULDIV
            XCHG2 s4, s4
            ADD
            XC2PU s0, s2, s3
            CONT:<{
              SAVECTR c2
              SAMEALTSAVE
              PUSHINT 0
              WHILE:<{
                DUP
                PUSHPOW2DEC 8
                LESS
              }>DO<{
                PUSH3 s1, s3, s1
                PUSH2 s0, s0
                PUSHINT 1000000000000000000
                MULDIV
                OVER
                PUSHINT 1000000000000000000
                MULDIV
                PUXC s2, s(-1)
                PUSHINT 1000000000000000000
                MULDIV
                PUSH2 s2, s2
                PUSHINT 1000000000000000000
                MULDIV
                XCHG2 s0, s3
                PUSHINT 1000000000000000000
                MULDIV
                SWAP
                PUSHINT 1000000000000000000
                MULDIV
                ADD
                PUSH2 s0, s4
                LESS
                IF:<{
                  PUXC s4, s(-1)
                  SUB
                  PUSHINT 1000000000000000000
                  PUSH2 s6, s4
                  OVER
                  MULINT 3
                  XCPU s1, s0
                  PUSHINT 1000000000000000000
                  MULDIV
                  PUSHINT 1000000000000000000
                  MULDIV
                  PUSH2 s1, s1
                  PUSHINT 1000000000000000000
                  MULDIV
                  ROT
                  PUSHINT 1000000000000000000
                  MULDIV
                  ADD
                  MULDIV
                  XCHG s1, s3
                  ADD
                }>ELSE<{
                  PUSH s4
                  SUB
                  PUSHINT 1000000000000000000
                  PUSH2 s6, s4
                  OVER
                  MULINT 3
                  XCPU s1, s0
                  PUSHINT 1000000000000000000
                  MULDIV
                  PUSHINT 1000000000000000000
                  MULDIV
                  PUSH2 s1, s1
                  PUSHINT 1000000000000000000
                  MULDIV
                  ROT
                  PUSHINT 1000000000000000000
                  MULDIV
                  ADD
                  MULDIV
                  XCHG s1, s3
                  SUB
                }>
                PUSH2 s0, s2
                GREATER
                IF:<{
                  PUXC s0, s2
                  SUB
                  LESSINT 2
                  IFJMP:<{
                    XCHG s1, s3
                    BLKDROP 3
                    RETALT
                  }>
                }>ELSE<{
                  XCPU s2, s2
                  SUB
                  LESSINT 2
                  IFJMP:<{
                    XCHG s1, s3
                    BLKDROP 3
                    RETALT
                  }>
                }>
                INC
              }>
              XCHG s1, s3
              BLKDROP 3
            }>
            EXECUTE
            XCHG s1, s2
            SUB
            SWAP
            PUSHINT 1000000000000000000
            MULDIV
          }>ELSE<{
            DROP
            POP s3
            OVER
            ADD
            XCHG s1, s2
            MULDIV
          }>
          PUSH s3
          NOW
          LESS
          XCHG s1, s4
          AND
          PUXC s3, s(-1)
          XCHG s0, s16
          LESS
          XCHG s1, s15
          OR
          IFJMP:<{
            XCHG s2, s3
            BLKDROP 3
            BLKDROP2 9, 3
            POP s4
            PUSHINT 0
            GETGLOB 3
            XCHG s4, s7
            XCHG3 s7, s6, s3
            NEWC
            PUSHINT 2907617013
            SWAP
            STU 32
            XCHG2 s0, s5
            SWAP
            STU 64
            XCHG s1, s3
            STREF
            SWAP
            STGRAMS
            SWAP
            STSLICER
            STDICT
            XCHG3 s0, s1, s3
            PUSHINT 24
            NEWC
            STU 6
            SWAP
            STSLICER
            SWAP
            STGRAMS
            PUSHINT 107
            STZEROES
            SWAP
            STBR
            ENDC
            SWAP
            SENDRAWMSG
            RETALT
          }>
          POP s4
          POP s4
          GETGLOB 8
          UNTUPLE 2
          PUSH s16
          XCHG2 s0, s11
          SDEQ
          IF:<{
            PUSH2 s14, s5
            SUB
            XCHG s1, s8
            ADD
            XCPU s6, s4
            SUB
            XCHG2 s7, s5
            ADD
          }>ELSE<{
            PUSH2 s14, s5
            SUB
            XCHG s1, s7
            ADD
            XCPU s7, s4
            SUB
            XCHG2 s9, s5
            ADD
            XCHG s0, s8
            XCHG s0, s6
            XCHG s0, s4
            XCHG s0, s5
          }>
          PUSH2 s5, s4
          TUPLE 2
          SETGLOB 7
          XCHG2 s0, s8
          TUPLE 2
          SETGLOB 8
          GETGLOB 11
          GETGLOB 9
          GETGLOB 2
          INDEX 1
          GETGLOB 3
          NEWC
          STREF
          STREF
          STREF
          STREF
          GETGLOB 4
          SWAP
          STU 16
          GETGLOB 6
          SWAP
          STU 16
          GETGLOB 10
          STGRAMS
          GETGLOB 7
          INDEX 0
          STGRAMS
          GETGLOB 7
          INDEX 1
          STGRAMS
          GETGLOB 8
          INDEX 0
          STGRAMS
          GETGLOB 8
          INDEX 1
          STGRAMS
          ENDC
          POP c4
          PUSH s13
          XCPU s5, s6
          XCHG s5, s11
          XCHG s4, s14
          XCHG3 s13, s1, s3
          XCPUXC s0, s1, s14
          XCHG s1, s12
          NEWC
          XCHG2 s0, s8
          STSLICER
          XCHG2 s0, s6
          STSLICER
          XCHG2 s0, s5
          STGRAMS
          XCHG2 s0, s5
          STGRAMS
          ENDC
          NEWC
          PUSHINT 2623606243
          SWAP
          STU 32
          XCHG2 s0, s3
          STSLICER
          SWAP
          STSLICER
          XCHG2 s0, s3
          STGRAMS
          SWAP
          STGRAMS
          STREF
          NEWC
          PUSHINT 2
          STONES
          PUSHINT 102
          STZEROES
          SWAP
          STBR
          ENDC
          PUSHINT 1
          SENDRAWMSG
          PUSH s3
          ISNULL
          IF:<{
            DROP
            POP s2
            POP s3
            PUSHINT 0
            GETGLOB 3
            PUSH s5
            PLDU 2
            EQINT 0
            IF:<{
              POP s5
            }>ELSE<{
              POP s7
              XCHG s4, s6
            }>
            XCHG s0, s7
            XCHG s0, s4
            XCHG2 s6, s3
            NEWC
            PUSHINT 2907617013
            SWAP
            STU 32
            XCHG2 s0, s5
            SWAP
            STU 64
            XCHG s1, s3
            STREF
            SWAP
            STGRAMS
            SWAP
            STSLICER
            STDICT
            XCHG s0, s2
            PUSHINT 24
            NEWC
            STU 6
            SWAP
            STSLICER
            SWAP
            STGRAMS
            PUSHINT 107
            STZEROES
            SWAP
            STBR
            ENDC
            SWAP
            SENDRAWMSG
          }>ELSE<{
            POP s6
            2DROP
            CTOS
            LDMSGADDR
            LDU 1
            LDGRAMS
            LDDICT
            BLKSWAP 3, 1
            XCHG s3, s4
            XCHG s0, s4
            ENDS
            BLKSWAP 1, 3
            PUSHINT 0
            GETGLOB 3
            XCHG s8, s11
            XCHG s0, s7
            XCHG s6, s11
            XCHG s5, s11
            XCHG s1, s10
            XCHG s1, s4
            XCHG3 s3, s3, s0
            NEWC
            PUSHINT 1923917994
            SWAP
            STU 32
            XCHG2 s0, s9
            SWAP
            STU 64
            XCHG s1, s7
            STREF
            XCHG2 s0, s5
            STSLICER
            XCHG2 s0, s3
            STGRAMS
            SWAP
            STSLICER
            XCHG2 s2, s3
            XCHG2 s2, s3
            STU 1
            SWAP
            STGRAMS
            STDICT
            STREF
            ENDC
            XCHG3 s0, s1, s3
            PUSHINT 24
            NEWC
            STU 6
            SWAP
            STSLICER
            SWAP
            STGRAMS
            PUSHINT 106
            STZEROES
            STDICT
            ENDC
            SWAP
            SENDRAWMSG
          }>
        }>
        PUSH c1
        BOOLOR
        SWAP
        TRY
      }>
    }>
    DUP
    PUSHINT 1647321691
    EQUAL
    IFJMP:<{
      DROP
      CALLDICT 129
    }>
    DUP
    PUSHINT 3222612351
    EQUAL
    IFJMP:<{
      DROP
      CALLDICT 123
    }>
    PUSHINT 1478098504
    EQUAL
    IFJMP:<{
      CALLDICT 122
    }>
    DROP
    PUSHPOW2DEC 16
    THROWANY
  }>
  120 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 1
    INDEX 1
    GETGLOB 2
    INDEX 0
    SDEQ
    THROWIFNOT 259
    PUSHINT 32
    SDSKIPFIRST
    LDU 64
    SWAP
    SWAP
    LDU 16
    SWAP
    SWAP
    LDREF
    ENDS
    POP s2
    GETGLOB 4
    OVER
    GEQ
    IFJMP:<{
      2DROP
    }>
    SETGLOB 4
    GETGLOB 11
    GETGLOB 9
    GETGLOB 2
    INDEX 1
    GETGLOB 3
    NEWC
    STREF
    STREF
    STREF
    STREF
    GETGLOB 4
    SWAP
    STU 16
    GETGLOB 6
    SWAP
    STU 16
    GETGLOB 10
    STGRAMS
    GETGLOB 7
    INDEX 0
    STGRAMS
    GETGLOB 7
    INDEX 1
    STGRAMS
    GETGLOB 8
    INDEX 0
    STGRAMS
    GETGLOB 8
    INDEX 1
    STGRAMS
    ENDC
    POP c4
    DUP
    SETCODE
    CTOS
    BLESS
    POP c3
    PUSHINT 43092
    PUSH c3
    EXECUTE
  }>
  122 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    PUSHSLICE x{8000380822D413DA4B5AF0DAE31AD627AC26C84E12C2D0EFAEB8B3B90B0B6513675_}
    GETGLOB 1
    INDEX 1
    SWAP
    SDEQ
    THROWIFNOT 257
    PUSHINT 32
    SDSKIPFIRST
    PUSHINT 64
    SDSKIPFIRST
    LDMSGADDR
    DROP
    PUSHINT 64
    PUSHINT 0
    GETGLOB 3
    PUSHNULL
    NEWC
    PUSHINT 3785583828
    SWAP
    STU 32
    XCHG2 s0, s3
    SWAP
    STU 64
    STREF
    STDICT
    ENDC
    ROT
    PUSHINT 0
    SWAP
    PUSHINT 24
    NEWC
    STU 6
    SWAP
    STSLICER
    SWAP
    STGRAMS
    PUSHINT 106
    STZEROES
    STDICT
    ENDC
    SWAP
    SENDRAWMSG
  }>
  123 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 1
    INDEX 1
    GETGLOB 2
    INDEX 0
    SDEQ
    THROWIFNOT 259
    PUSHINT 32
    SDSKIPFIRST
    LDU 64
    SWAP
    SWAP
    LDU 16
    SWAP
    NIP
    NIP
    SETGLOB 6
    GETGLOB 11
    GETGLOB 9
    GETGLOB 2
    INDEX 1
    GETGLOB 3
    NEWC
    STREF
    STREF
    STREF
    STREF
    GETGLOB 4
    SWAP
    STU 16
    GETGLOB 6
    SWAP
    STU 16
    GETGLOB 10
    STGRAMS
    GETGLOB 7
    INDEX 0
    STGRAMS
    GETGLOB 7
    INDEX 1
    STGRAMS
    GETGLOB 8
    INDEX 0
    STGRAMS
    GETGLOB 8
    INDEX 1
    STGRAMS
    ENDC
    POP c4
  }>
  124 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    PUSHINT 32
    SDSKIPFIRST
    LDU 64
    SWAP
    SWAP
    LDREF
    LDMSGADDR
    LDGRAMS
    LDREF
    SWAP
    CTOS
    CONT:<{
      SAVECTR c2
      SAMEALTSAVE
      DUP
      PLDU 4
      DUP
      EQINT 0
      IF:<{
        DROP
        LDSLICE 4
        SWAP
      }>ELSE<{
        EQINT 1
        IFJMP:<{
          PUSHINT 268
          LDSLICEX
          SWAP
          RETALT
        }>
        DROP
        THROW 261
        PUSHNULL
        PUSHNULL
      }>
    }>
    EXECUTE
    SWAP
    LDGRAMS
    CONT:<{
      SAVECTR c2
      SAMEALTSAVE
      DUP
      PLDU 4
      DUP
      EQINT 0
      IF:<{
        DROP
        LDSLICE 4
        SWAP
      }>ELSE<{
        EQINT 1
        IFJMP:<{
          PUSHINT 268
          LDSLICEX
          SWAP
          RETALT
        }>
        DROP
        THROW 261
        PUSHNULL
        PUSHNULL
      }>
    }>
    EXECUTE
    SWAP
    LDGRAMS
    DROP
    XCHG s0, s4
    LDDICT
    LDDICT
    ENDS
    XCHG s4, s5
    XCHG s3, s4
    XCHG s2, s3
    POP s3
    POP s4
    XCHG s0, s6
    CALL:<{
      GETGLOB 2
      INDEX 1
      OVER
      PUSHINT 6
      NEWC
      STU 5
      XCHG s1, s2
      STREF
      STREF
      ENDC
      PUSHINT 0
      SWAP
      HASHCU
      PUSHINT 4
      NEWC
      STU 3
      XCHG s1, s2
      STI 8
      STU 256
      ENDC
      CTOS
      SWAP
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      LDREF
      SWAP
      CTOS
      LDMSGADDR
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      SWAP
      ENDS
      XCHG s0, s2
      ENDS
      GETGLOB 1
      INDEX 1
      XCHG2 s0, s5
      SDEQ
      GETGLOB 2
      INDEX 0
      XCHG2 s0, s4
      SDEQ
      XCHG s1, s3
      AND
      SWAP
      EQINT 3
      AND
      THROWIFNOT 272
    }>
    2DROP
    PUSHINT 1000000
    BALANCE
    INDEX 0
    GETGLOB 1
    INDEX 2
    TUCK
    SUB
    PUXC s2, s(-1)
    MIN
    XCHG s1, s2
    SUB
    SUB
    PUSHINT 25000000
    SUB
    GETGLOB 7
    UNTUPLE 2
    GETGLOB 10
    XCPUXC s2, s1, s2
    XCPUXC s0, s1, s10
    XCHG s1, s7
    CALL:<{
      PUSH s4
      EQINT 0
      IF:<{
        BLKDROP2 2, 2
        POP s2
        PUSHINT 1000
        PUSHINT 99000
        PUSH2 s2, s3
        MAX
        MAX
      }>ELSE<{
        PUSH3 s0, s3, s2
        MULDIV
        PUXC s2, s(-1)
        MIN
        XCPU2 s2, s3, s4
        MULDIV
        MIN
        PU2XC s4, s1, s3
        MULDIV
        PU2XC s4, s3, s2
        MULDIV
        XCHG s1, s2
        MIN
        XCHG3 s1, s3, s0
      }>
      XCHG3 s3, s0, s0
    }>
    PUXC s1, s8
    LESS
    IFJMP:<{
      BLKDROP 3
      XCHG2 s5, s6
      BLKDROP 5
      PUSHINT 0
      GETGLOB 3
      XCHG3 s4, s0, s4
      NEWC
      PUSHINT 3785583828
      SWAP
      STU 32
      XCHG2 s0, s3
      SWAP
      STU 64
      STREF
      STDICT
      ENDC
      GETGLOB 1
      INDEX 1
      XCHG s1, s2
      PUSHINT 24
      NEWC
      STU 6
      SWAP
      STSLICER
      SWAP
      STGRAMS
      PUSHINT 106
      STZEROES
      STDICT
      ENDC
      SWAP
      SENDRAWMSG
    }>
    POP s4
    XCPU s8, s1
    ADD
    XCPU s4, s8
    ADD
    XCHG s0, s2
    PUSHINT 4000000
    SUB
    PUSH3 s7, s1, s8
    PUSH3 s7, s5, s6
    NEWC
    PUSHINT 3041195172
    SWAP
    STU 32
    XCHG2 s0, s6
    STSLICER
    XCHG2 s0, s4
    STGRAMS
    ROT
    STGRAMS
    SWAP
    STGRAMS
    SWAP
    STGRAMS
    SWAP
    STGRAMS
    NEWC
    PUSHINT 2
    STONES
    PUSHINT 102
    STZEROES
    SWAP
    STBR
    ENDC
    PUSHINT 1
    SENDRAWMSG
    XCHG2 s4, s2
    TUPLE 2
    SETGLOB 7
    XCPU s4, s1
    ADD
    SETGLOB 10
    GETGLOB 1
    INDEX 3
    PUSHINT 15000000
    OVER
    LSHIFT 1
    ADD
    SWAP
    PUSHINT 11000000
    SWAP
    PUSHINT 3
    MULRSHIFT# 1
    ADD
    PUSHINT 50000000
    ADD
    LSHIFT 1
    ADD
    XCPU s4, s4
    SUB
    PUSHINT 1
    GETGLOB 3
    PUSH s9
    XCHG s0, s3
    XCHG3 s1, s5, s9
    NEWC
    PUSHINT 2867302998
    SWAP
    STU 32
    XCHG2 s0, s4
    SWAP
    STU 64
    XCHG s1, s2
    STREF
    SWAP
    STGRAMS
    SWAP
    STGRAMS
    ENDC
    GETGLOB 1
    INDEX 1
    XCHG3 s1, s5, s0
    PUSHINT 24
    NEWC
    STU 6
    SWAP
    STSLICER
    SWAP
    STGRAMS
    PUSHINT 106
    STZEROES
    STDICT
    ENDC
    SWAP
    SENDRAWMSG
    PUSH s2
    GETGLOB 9
    GETGLOB 9
    NEWC
    PUSHINT 0
    STGRAMS
    XCHG2 s0, s3
    STSLICER
    MYADDR
    STSLICER
    XCHG s1, s2
    STREF
    ENDC
    PUSHINT 6
    NEWC
    STU 5
    XCHG s1, s2
    STREF
    STREF
    ENDC
    PUSHINT 0
    MYADDR
    PUSH2 s1, s6
    PUSHINT 50000000
    SUB
    MAX
    XCHG s5, s8
    XCHG s4, s8
    XCHG3 s6, s0, s3
    XCHG s0, s8
    NEWC
    PUSHINT 395134233
    SWAP
    STU 32
    XCHG2 s0, s6
    SWAP
    STU 64
    XCHG2 s0, s4
    STGRAMS
    ROT
    STSLICER
    SWAP
    STSLICER
    SWAP
    STGRAMS
    STDICT
    ENDC
    PUSH2 s3, s1
    SWAP
    HASHCU
    PUSHINT 4
    NEWC
    STU 3
    XCHG s1, s2
    STI 8
    STU 256
    ENDC
    CTOS
    XCHG3 s4, s3, s0
    PUSHINT 3
    PUSHINT 24
    NEWC
    STU 6
    ROT
    STSLICER
    ROT
    STGRAMS
    STU 107
    STREF
    STDICT
    ENDC
    SWAP
    SENDRAWMSG
    GETGLOB 11
    GETGLOB 9
    GETGLOB 2
    INDEX 1
    GETGLOB 3
    NEWC
    STREF
    STREF
    STREF
    STREF
    GETGLOB 4
    SWAP
    STU 16
    GETGLOB 6
    SWAP
    STU 16
    GETGLOB 10
    STGRAMS
    GETGLOB 7
    INDEX 0
    STGRAMS
    GETGLOB 7
    INDEX 1
    STGRAMS
    GETGLOB 8
    INDEX 0
    STGRAMS
    GETGLOB 8
    INDEX 1
    STGRAMS
    ENDC
    POP c4
  }>
  129 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 14
    GETGLOB 1
    INDEX 1
    SWAP
    SDEQ
    THROWIFNOT 257
    PUSHINT 32
    SDSKIPFIRST
    LDU 64
    SWAP
    SWAP
    LDMSGADDR
    LDDICT
    ENDS
    GETGLOB 8
    UNTUPLE 2
    GETGLOB 13
    UNTUPLE 2
    PUSH s3
    GTINT 0
    IF:<{
      PUSHINT 1
      GETGLOB 3
      PUXC2 s8, s0, s5
      PUSH2 s8, s7
      NEWC
      PUSHINT 2907617013
      SWAP
      STU 32
      XCHG2 s0, s5
      SWAP
      STU 64
      XCHG s1, s3
      STREF
      SWAP
      STGRAMS
      SWAP
      STSLICER
      STDICT
      XCHG3 s4, s0, s0
      PUSHINT 50000000
      XCHG2 s0, s5
      PUSHINT 24
      NEWC
      STU 6
      SWAP
      STSLICER
      SWAP
      STGRAMS
      PUSHINT 107
      STZEROES
      SWAP
      STBR
      ENDC
      SWAP
      SENDRAWMSG
    }>ELSE<{
      POP s3
      DROP
    }>
    DUP
    GTINT 0
    IF:<{
      PUSHINT 1
      GETGLOB 3
      XCHG s4, s6
      XCHG s0, s3
      XCHG2 s5, s6
      NEWC
      PUSHINT 2907617013
      SWAP
      STU 32
      XCHG2 s0, s5
      SWAP
      STU 64
      XCHG s1, s3
      STREF
      SWAP
      STGRAMS
      SWAP
      STSLICER
      STDICT
      ROT
      PUSHINT 50000000
      SWAP
      PUSHINT 24
      NEWC
      STU 6
      SWAP
      STSLICER
      SWAP
      STGRAMS
      PUSHINT 107
      STZEROES
      SWAP
      STBR
      ENDC
      SWAP
      SENDRAWMSG
    }>ELSE<{
      BLKDROP 5
    }>
    PUSHINT 0
    DUP
    TUPLE 2
    SETGLOB 8
    GETGLOB 11
    GETGLOB 9
    GETGLOB 2
    INDEX 1
    GETGLOB 3
    NEWC
    STREF
    STREF
    STREF
    STREF
    GETGLOB 4
    SWAP
    STU 16
    GETGLOB 6
    SWAP
    STU 16
    GETGLOB 10
    STGRAMS
    GETGLOB 7
    INDEX 0
    STGRAMS
    GETGLOB 7
    INDEX 1
    STGRAMS
    GETGLOB 8
    INDEX 0
    STGRAMS
    GETGLOB 8
    INDEX 1
    STGRAMS
    ENDC
    POP c4
  }>
  43092 => <{
  }>
  58662 => <{
    NIP
    POP s4
    PUSH c4
    SETGLOB 3
    PUXC s4, s1
    TUPLE 2
    SETGLOB 2
    SETGLOB 4
    SWAP
    LDU 16
    SWAP
    SETGLOB 6
    LDREF
    SWAP
    SETGLOB 9
    SWAP
    LDU 1
    CONT:<{
      SAVECTR c2
      SAMEALTSAVE
      DUP
      PLDU 4
      DUP
      EQINT 0
      IF:<{
        DROP
        LDSLICE 4
        SWAP
      }>ELSE<{
        EQINT 1
        IFJMP:<{
          PUSHINT 268
          LDSLICEX
          SWAP
          RETALT
        }>
        DROP
        THROW 261
        PUSHNULL
        PUSHNULL
      }>
    }>
    EXECUTE
    SWAP
    CONT:<{
      SAVECTR c2
      SAMEALTSAVE
      DUP
      PLDU 4
      DUP
      EQINT 0
      IF:<{
        DROP
        LDSLICE 4
        SWAP
      }>ELSE<{
        EQINT 1
        IFJMP:<{
          PUSHINT 268
          LDSLICEX
          SWAP
          RETALT
        }>
        DROP
        THROW 261
        PUSHNULL
        PUSHNULL
      }>
    }>
    EXECUTE
    XCHG3 s3, s3, s0
    TUPLE 3
    NIP
    UNTUPLE 3
    POP s2
    XCHG s0, s2
    LDU 8
    LDU 8
    ROTREV
    TUPLE 2
    SETGLOB 12
    ENDS
    GETGLOB 12
    INDEX 1
    GETGLOB 12
    INDEX 0
    NEWC
    STU 8
    STU 8
    XCHG s0, s2
    PUSHINT 1
    NEWC
    ROT
    STSLICER
    GETGLOB 2
    UNTUPLE 2
    NEWC
    ROT
    STSLICER
    XCHG s1, s3
    STU 8
    SWAP
    STBR
    ENDC
    PUSHINT 6
    NEWC
    STU 5
    XCHG s1, s2
    STREF
    STREF
    ENDC
    PUSHINT 0
    SWAP
    HASHCU
    PUSHINT 4
    NEWC
    STU 3
    XCHG s1, s2
    STI 8
    STU 256
    ENDC
    CTOS
    XCHG s1, s2
    STSLICER
    SWAP
    PUSHINT 1
    NEWC
    ROT
    STSLICER
    GETGLOB 2
    UNTUPLE 2
    NEWC
    ROT
    STSLICER
    XCHG s1, s3
    STU 8
    SWAP
    STBR
    ENDC
    PUSHINT 6
    NEWC
    STU 5
    XCHG s1, s2
    STREF
    STREF
    ENDC
    PUSHINT 0
    SWAP
    HASHCU
    PUSHINT 4
    NEWC
    STU 3
    XCHG s1, s2
    STI 8
    STU 256
    ENDC
    CTOS
    STSLICER
    SWAP
    STSLICER
    ENDC
    SETGLOB 11
    PUSHINT 0
    SETGLOB 10
    PUSHINT 0
    DUP
    TUPLE 2
    SETGLOB 7
    PUSHINT 0
    DUP
    TUPLE 2
    SETGLOB 8
    GETGLOB 11
    GETGLOB 9
    GETGLOB 2
    INDEX 1
    GETGLOB 3
    NEWC
    STREF
    STREF
    STREF
    STREF
    GETGLOB 4
    SWAP
    STU 16
    GETGLOB 6
    SWAP
    STU 16
    GETGLOB 10
    STGRAMS
    GETGLOB 7
    INDEX 0
    STGRAMS
    GETGLOB 7
    INDEX 1
    STGRAMS
    GETGLOB 8
    INDEX 0
    STGRAMS
    GETGLOB 8
    INDEX 1
    STGRAMS
    ENDC
    POP c4
  }>
  65971 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 7
    UNTUPLE 2
  }>
  70754 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 5
    UNTUPLE 3
    GETGLOB 7
    UNTUPLE 2
    GETGLOB 12
    UNTUPLE 2
    XCPU s8, s5
    SDEQ
    IF:<{
      POP s4
    }>ELSE<{
      POP s3
      XCHG s2, s6
      XCHG3 s3, s0, s0
    }>
    GETGLOB 6
    PUXC s6, s(-1)
    PUSHINT 10000
    MULDIV
    XCPU s6, s6
    SUB
    XCHG3 s1, s4, s4
    XCHG s0, s3
    XCHG s0, s7
    XCHG s0, s5
    IF:<{
      PUSHINT 1
      SWAP
      REPEAT:<{
        MULINT 10
      }>
      XCHG s0, s4
      PUSHINT 1
      SWAP
      REPEAT:<{
        MULINT 10
      }>
      PUSH3 s2, s1, s4
      PUSH s3
      XCHG s1, s3
      PUSHINT 1000000000000000000
      XCHG2 s0, s4
      MULDIV
      PUSHINT 1000000000000000000
      XCHG2 s0, s3
      MULDIV
      2DUP
      PUSHINT 1000000000000000000
      MULDIV
      XCPU s2, s0
      PUSHINT 1000000000000000000
      MULDIV
      XCPU s1, s0
      PUSHINT 1000000000000000000
      MULDIV
      ADD
      PUSHINT 1000000000000000000
      MULDIV
      XCHG s0, s4
      PUSHINT 1000000000000000000
      PUSH s6
      MULDIV
      XCHG s1, s3
      PUSHINT 1000000000000000000
      XCHG2 s0, s6
      MULDIV
      SWAP
      PUSHINT 1000000000000000000
      PUSH s3
      MULDIV
      XCHG2 s4, s4
      ADD
      XC2PU s0, s2, s3
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        PUSHINT 0
        WHILE:<{
          DUP
          PUSHPOW2DEC 8
          LESS
        }>DO<{
          PUSH3 s1, s3, s1
          PUSH2 s0, s0
          PUSHINT 1000000000000000000
          MULDIV
          OVER
          PUSHINT 1000000000000000000
          MULDIV
          PUXC s2, s(-1)
          PUSHINT 1000000000000000000
          MULDIV
          PUSH2 s2, s2
          PUSHINT 1000000000000000000
          MULDIV
          XCHG2 s0, s3
          PUSHINT 1000000000000000000
          MULDIV
          SWAP
          PUSHINT 1000000000000000000
          MULDIV
          ADD
          PUSH2 s0, s4
          LESS
          IF:<{
            PUXC s4, s(-1)
            SUB
            PUSHINT 1000000000000000000
            PUSH2 s6, s4
            OVER
            MULINT 3
            XCPU s1, s0
            PUSHINT 1000000000000000000
            MULDIV
            PUSHINT 1000000000000000000
            MULDIV
            PUSH2 s1, s1
            PUSHINT 1000000000000000000
            MULDIV
            ROT
            PUSHINT 1000000000000000000
            MULDIV
            ADD
            MULDIV
            XCHG s1, s3
            ADD
          }>ELSE<{
            PUSH s4
            SUB
            PUSHINT 1000000000000000000
            PUSH2 s6, s4
            OVER
            MULINT 3
            XCPU s1, s0
            PUSHINT 1000000000000000000
            MULDIV
            PUSHINT 1000000000000000000
            MULDIV
            PUSH2 s1, s1
            PUSHINT 1000000000000000000
            MULDIV
            ROT
            PUSHINT 1000000000000000000
            MULDIV
            ADD
            MULDIV
            XCHG s1, s3
            SUB
          }>
          PUSH2 s0, s2
          GREATER
          IF:<{
            PUXC s0, s2
            SUB
            LESSINT 2
            IFJMP:<{
              XCHG s1, s3
              BLKDROP 3
              RETALT
            }>
          }>ELSE<{
            XCPU s2, s2
            SUB
            LESSINT 2
            IFJMP:<{
              XCHG s1, s3
              BLKDROP 3
              RETALT
            }>
          }>
          INC
        }>
        XCHG s1, s3
        BLKDROP 3
      }>
      EXECUTE
      XCHG s1, s2
      SUB
      SWAP
      PUSHINT 1000000000000000000
      MULDIV
    }>ELSE<{
      DROP
      POP s3
      OVER
      ADD
      XCHG s1, s2
      MULDIV
    }>
    SWAP
  }>
  82320 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 4
  }>
  96780 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 6
    PUSHINT 10000
  }>
  103289 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 9
    GETGLOB 9
    NEWC
    PUSHINT 0
    STGRAMS
    XCHG2 s0, s3
    STSLICER
    MYADDR
    STSLICER
    XCHG s1, s2
    STREF
    ENDC
    PUSHINT 6
    NEWC
    STU 5
    XCHG s1, s2
    STREF
    STREF
    ENDC
    PUSHINT 0
    SWAP
    HASHCU
    PUSHINT 4
    NEWC
    STU 3
    XCHG s1, s2
    STI 8
    STU 256
    ENDC
    CTOS
  }>
  103723 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 5
    UNTUPLE 3
    2DROP
  }>
  106029 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    PUSHNULL
    PUSHINT 0
    NEWC
    STU 8
    PUSHSLICE x{4465447573742D76322D4C50}
    STSLICER
    ENDC
    PUSHINT 59089242681608890680090686026688704441792375738894456860693970539822503415433
    ROT
    PUSHPOW2 8
    DICTUSETREF
    PUSHINT 0
    NEWC
    STU 8
    PUSHSLICE x{39}
    STSLICER
    ENDC
    PUSHINT 107878361799212983662495570378745491379550006934010968359181619763835345146430
    ROT
    PUSHPOW2 8
    DICTUSETREF
    PUSHINT 0
    NEWC
    STU 8
    PUSHSLICE x{4C50}
    STSLICER
    ENDC
    PUSHINT 82961397245523513629401799123410942652413991882008909918554405086738284660097
    ROT
    PUSHPOW2 8
    DICTUSETREF
    GETGLOB 10
    PUSHINT -1
    PUSHSLICE x{2_}
    PUSHINT 0
    NEWC
    STU 8
    XCHG s1, s4
    STDICT
    ENDC
    GETGLOB 9
    XCHG s3, s4
    XCHG s2, s3
  }>
  106049 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 12
    UNTUPLE 2
  }>
  112792 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 8
    UNTUPLE 2
  }>
  118188 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 5
    UNTUPLE 3
    BLKDROP2 1, 2
  }>
  119877 => <{
    CALL:<{
      PUSH c4
      CTOS
      LDREF
      OVER
      CTOS
      LDMSGADDR
      LDU 8
      SWAP
      SWAP
      NIP
      LDU 1
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      SWAP
      CONT:<{
        SAVECTR c2
        SAMEALTSAVE
        DUP
        PLDU 4
        DUP
        EQINT 0
        IF:<{
          DROP
          LDSLICE 4
          SWAP
        }>ELSE<{
          EQINT 1
          IFJMP:<{
            PUSHINT 268
            LDSLICEX
            SWAP
            RETALT
          }>
          DROP
          THROW 261
          PUSHNULL
          PUSHNULL
        }>
      }>
      EXECUTE
      XCHG3 s3, s3, s0
      TUPLE 3
      NIP
      SETGLOB 5
      XCHG s0, s2
      SETGLOB 3
      LDREF
      ROTREV
      TUPLE 2
      SETGLOB 2
      LDREF
      SWAP
      SETGLOB 9
      LDREF
      OVER
      CTOS
      LDU 8
      LDU 8
      ROTREV
      TUPLE 2
      SETGLOB 12
      LDMSGADDR
      LDMSGADDR
      ROTREV
      TUPLE 2
      SETGLOB 13
      LDMSGADDR
      SWAP
      SETGLOB 14
      ENDS
      SWAP
      SETGLOB 11
      LDU 16
      SWAP
      SETGLOB 4
      LDU 16
      SWAP
      SETGLOB 6
      LDGRAMS
      SWAP
      SETGLOB 10
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 7
      LDGRAMS
      LDGRAMS
      ROTREV
      TUPLE 2
      SETGLOB 8
      ENDS
    }>
    GETGLOB 7
    UNTUPLE 2
    GETGLOB 10
    XCHG3 s1, s4, s4
    XCHG s0, s3
    CALL:<{
      PUSH s4
      EQINT 0
      IF:<{
        BLKDROP2 2, 2
        POP s2
        PUSHINT 1000
        PUSHINT 99000
        PUSH2 s2, s3
        MAX
        MAX
      }>ELSE<{
        PUSH3 s0, s3, s2
        MULDIV
        PUXC s2, s(-1)
        MIN
        XCPU2 s2, s3, s4
        MULDIV
        MIN
        PU2XC s4, s1, s3
        MULDIV
        PU2XC s4, s3, s2
        MULDIV
        XCHG s1, s2
        MIN
        XCHG3 s1, s3, s0
      }>
      XCHG3 s3, s0, s0
    }>
    DROP
  }>
}
THROWARG 11
"""


def test_disassembler():
    c = Cell("te6ccgEBAQEAGgAAMJaCEAdbzRWVizEjRYDikaCWepORAJDk6A==")
    test = disassembler(c)
    print(test)
    assert test == test1


def test_disassembler_str():
    test = disassembler("te6ccgEBAQEAGgAAMJaCEAdbzRWVizEjRYDikaCWepORAJDk6A==")
    assert test == test1


def test_disassembler_2_str():
    test = disassembler("te6ccgEBCAEANAABFP8A9KQT9LzyyAsBAgLPAgMAAdwCASAEBQAF9TPcAgFIBgcADwhwAWRMeCogAAcoPAMg")
    assert test == test2


def test_disassembler_3_str():
    code = "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"

    rest = disassembler(code)
    assert rest == test3


def test_disassembler_root_lib():
    from tonpy.fift.fift import convert_assembler
    from tonpy import CellBuilder, CellSlice

    cell_code = convert_assembler("""<{ 228 PUSHINT }>c""")
    code_hash = int(cell_code.get_hash(), 16)

    vmlibs = VmDict(256)
    vmlibs.set_ref(code_hash, cell_code)

    lib_cell = CellBuilder() \
        .store_uint(CellSlice.SpecialType.Library.value, 8) \
        .store_uint(code_hash, 256) \
        .end_cell(special=True)

    assert disassembler(lib_cell,
                        vmlibs) == "// LIB: 961254B41350A116E5DC3166307071F29DA1F3A286A144350289ACBE1A64C459 \nPUSHINT 228\n"


def test_disassembler_pushref():
    from tonpy.fift.fift import convert_assembler
    from tonpy import CellBuilder, CellSlice
    cell_code = convert_assembler("""<{ 228 PUSHINT }>c""")
    code_hash = int(cell_code.get_hash(), 16)

    vmlibs = VmDict(256)
    vmlibs.set_ref(code_hash, cell_code)

    answer = disassembler(convert_assembler("""<{
       <b 2 8 u, 67879315136173602162010959444987239046790589850178600389566119814235502724185 256 u, b>spec PUSHREFSLICE
    }>c"""), vmlibs)
    assert answer == """// LIB: 961254B41350A116E5DC3166307071F29DA1F3A286A144350289ACBE1A64C459 
    PUSHINT 228
PUSHREFSLICE (38ABEB05B69354A7B9B5C3439EE680731263C9837A722799AA5A89FE1AF0C18B)
"""


def test_disassembler_dario():
    vmlibs = VmDict(256, False, cell_root=Cell(test_tx['libs']))
    answer = disassembler(Cell('te6ccuEBAgEALQAUWgEO/wCI0O0e2AEIQgJPAXEnLCFbi/j+6sRqhXaIpLZfT+YfgihjH2J9DtqdAD/u1jE='),
                          vmlibs)
    assert answer == """SETCP 0
// LIB: 4F0171272C215B8BF8FEEAC46A857688A4B65F4FE61F8228631F627D0EDA9D00 
    SETCP 0
    DICTPUSHCONST 19, (xC_)
    DICTIGETJMPZ {
      0 => <{
        DUP
        SEMPTY
        IFJMP:<{
          BLKDROP 4
        }>
        OVER
        CTOS
        LDU 4
        PUSHINT 0
        XCHG s0, s2
        PUSHINT 1
        AND
        IF:<{
          NIP
          PUSHINT -1
          XCHG s0, s2
          PUSHINT 32
          SDSKIPFIRST
          ROTREV
        }>
        LDMSGADDR
        LDMSGADDR
        NIP
        LDGRAMS
        NIP
        PUSHINT 1
        SDSKIPFIRST
        LDGRAMS
        NIP
        LDGRAMS
        DROP
        PUSHINT 3
        MULRSHIFT# 1
        XCHG s0, s3
        LDU 32
        LDU 64
        XCHG s4, s8
        XCHG s3, s7
        XCHG s5, s6
        XCHG3 s5, s0, s4
        XCHG3 s3, s1, s3
        TUPLE 9
        SETGLOB 1
        GETGLOB 1
        INDEX 0
        IFRET
        GETGLOB 1
        INDEX 1
        PUSHINT 0
        SWAP
        REWRITESTDADDR
        DROP
        SWAP
        EQUAL
        THROWIFNOT 85
        CALL:<{
          PUSH c4
          CTOS
          LDGRAMS
          SWAP
          SETGLOB 2
          LDMSGADDR
          SWAP
          SETGLOB 3
          LDREF
          SWAP
          SETGLOB 4
          LDREF
          SWAP
          SETGLOB 5
          ENDS
        }>
        GETGLOB 1
        INDEX 1
        GETGLOB 3
        SDEQ
        IFJMP:<{
          GETGLOB 1
          INDEX 7
          GETGLOB 1
          INDEX 3
          PUSHINT 51966817
          EQUAL
          IF:<{
            GETGLOB 1
            INDEX 6
            GETGLOB 1
            INDEX 2
            MULINT 3
            PUSHINT 10000000
            ADD
            PUSHINT 10000000
            ADD
            PUSHINT 10000000
            ADD
            PUSHINT 10000000
            ADD
            GREATER
            THROWIFNOT 83
            LDMSGADDR
            LDGRAMS
            LDMSGADDR
            DROP
            PUSH s2
            PUSHINT 0
            SWAP
            REWRITESTDADDR
            DROP
            SWAP
            EQUAL
            OVER
            PUSHINT 0
            SWAP
            REWRITESTDADDR
            DROP
            SWAP
            EQUAL
            AND
            THROWIFNOT 85
            MYADDR
            GETGLOB 5
            XCHG s2, s4
            NEWC
            PUSHINT 0
            STGRAMS
            XCHG2 s0, s3
            STSLICER
            SWAP
            STSLICER
            STREF
            ENDC
            GETGLOB 5
            SWAP
            PUSHNULL
            PUSHNULL
            TUPLE 4
            GETGLOB 2
            PUSH s2
            ADD
            SETGLOB 2
            CALL:<{
              GETGLOB 5
              GETGLOB 4
              NEWC
              GETGLOB 2
              STGRAMS
              GETGLOB 3
              STSLICER
              STREF
              STREF
              ENDC
              POP c4
            }>
            PUSHINT 10000000
            CALL:<{
              GETGLOB 1
              INDEX 5
              GETGLOB 1
              INDEX 6
              SUB
              SWAP
              MAX
              PUSHINT 0
              RAWRESERVE
            }>
            PUSHINT 0
            TUCK
            CALL:<{
              OVER
              UNTUPLE 4
              DUP
              ISNULL
              IF:<{
                2DROP
                XCHG s0, s3
                CALL:<{
                  UNTUPLE 4
                  OVER
                  ISNULL
                  IF:<{
                    NIP
                    PUSHINT 0
                    DUP
                    NEWC
                    STU 2
                    PUXC s4, s(-1)
                    STDICT
                    PUXC s3, s(-1)
                    STDICT
                    STU 1
                    ENDC
                    SWAP
                  }>
                  XCHG3 s3, s3, s0
                  PUXC s3, s(-1)
                  TUPLE 4
                  SWAP
                }>
                NIP
                DUP
                HASHCU
                PUSHINT 4
                NEWC
                STU 3
                XCHG s1, s4
                STI 8
                XCHG s1, s3
                STU 256
                ENDC
                CTOS
                XCHG3 s0, s1, s3
              }>ELSE<{
                POP s4
                POP s4
              }>
              BLKSWAP 1, 3
              PUSH s3
              TUPLE 4
              SWAP
            }>
            SWAP
            CALL:<{
              UNTUPLE 4
              OVER
              ISNULL
              IF:<{
                NIP
                PUSHINT 0
                DUP
                NEWC
                STU 2
                PUXC s4, s(-1)
                STDICT
                PUXC s3, s(-1)
                STDICT
                STU 1
                ENDC
                SWAP
              }>
              XCHG3 s3, s3, s0
              PUXC s3, s(-1)
              TUPLE 4
              SWAP
            }>
            NIP
            XCHG2 s3, s4
            PUSHINT 4019741354
            GETGLOB 1
            INDEX 4
            SWAP
            NEWC
            STU 32
            STU 64
            ROT
            STGRAMS
            SWAP
            STSLICER
            ENDC
            XCHG s1, s3
            PUSHPOW2 7
            CALL:<{
              PUSHINT 7
              PUSHINT 24
              NEWC
              STU 6
              XCHG2 s0, s5
              STSLICER
              XCHG2 s0, s5
              STGRAMS
              XCHG s1, s3
              STU 108
              STREF
              STREF
              ENDC
              SWAP
              SENDRAWMSG
            }>
          }>ELSE<{
            GETGLOB 1
            INDEX 3
            PUSHINT 3571363899
            EQUAL
            IFJMP:<{
              LDMSGADDR
              DROP
              DUP
              PUSHINT 0
              SWAP
              REWRITESTDADDR
              DROP
              SWAP
              EQUAL
              THROWIFNOT 85
              SETGLOB 3
              CALL:<{
                GETGLOB 5
                GETGLOB 4
                NEWC
                GETGLOB 2
                STGRAMS
                GETGLOB 3
                STSLICER
                STREF
                STREF
                ENDC
                POP c4
              }>
              PUSHINT 10000000
              CALL:<{
                GETGLOB 1
                INDEX 5
                GETGLOB 1
                INDEX 6
                SUB
                SWAP
                MAX
                PUSHINT 0
                RAWRESERVE
              }>
              PUSHINT 0
              GETGLOB 3
              PUSHPOW2 7
              PUSHINT 3576854235
              ROTREV
              CALL:<{
                GETGLOB 1
                INDEX 4
                PUSHINT 0
                PUSHINT 16
                NEWC
                STU 6
                XCHG2 s0, s4
                STSLICER
                XCHG2 s0, s5
                STGRAMS
                XCHG s1, s2
                STU 107
                XCHG s1, s2
                STU 32
                XCHG s1, s2
                STU 64
                ENDC
                SWAP
                SENDRAWMSG
              }>
            }>
            GETGLOB 1
            INDEX 3
            PUSHINT 247632384
            EQUAL
            IFJMP:<{
              LDREF
              DROP
              SETGLOB 4
              CALL:<{
                GETGLOB 5
                GETGLOB 4
                NEWC
                GETGLOB 2
                STGRAMS
                GETGLOB 3
                STSLICER
                STREF
                STREF
                ENDC
                POP c4
              }>
              PUSHINT 10000000
              CALL:<{
                GETGLOB 1
                INDEX 5
                GETGLOB 1
                INDEX 6
                SUB
                SWAP
                MAX
                PUSHINT 0
                RAWRESERVE
              }>
              PUSHINT 0
              GETGLOB 3
              PUSHPOW2 7
              PUSHINT 3576854235
              ROTREV
              CALL:<{
                GETGLOB 1
                INDEX 4
                PUSHINT 0
                PUSHINT 16
                NEWC
                STU 6
                XCHG2 s0, s4
                STSLICER
                XCHG2 s0, s5
                STGRAMS
                XCHG s1, s2
                STU 107
                XCHG s1, s2
                STU 32
                XCHG s1, s2
                STU 64
                ENDC
                SWAP
                SENDRAWMSG
              }>
            }>
            DROP
            PUSHPOW2DEC 16
            THROWANY
          }>
        }>
        GETGLOB 1
        INDEX 7
        GETGLOB 1
        INDEX 3
        PUSHINT 745978227
        EQUAL
        IF:<{
          GETGLOB 1
          INDEX 6
          GETGLOB 1
          INDEX 2
          LSHIFT 1
          PUSHINT 10000000
          ADD
          PUSHINT 10000000
          ADD
          GREATER
          THROWIFNOT 83
          LDMSGADDR
          LDU 1
          DROP
          IF:<{
            NEWC
            OVER
            STSLICER
            ENDC
          }>ELSE<{
            PUSHNULL
          }>
          OVER
          PUSHINT 0
          SWAP
          REWRITESTDADDR
          DROP
          SWAP
          EQUAL
          BLKDROP2 1, 2
          DROP
          PUSHINT 10000000
          CALL:<{
            GETGLOB 1
            INDEX 5
            GETGLOB 1
            INDEX 6
            SUB
            SWAP
            MAX
            PUSHINT 0
            RAWRESERVE
          }>
          PUSHINT 0
          GETGLOB 1
          INDEX 1
          PUSHINT 3513996288
          GETGLOB 1
          INDEX 4
          SWAP
          NEWC
          STU 32
          STU 64
          XCHG s1, s3
          STDICT
          XCHG s1, s2
          PUSHPOW2 7
          CALL:<{
            PUSHINT 0
            PUSHINT 24
            NEWC
            STU 6
            XCHG2 s0, s4
            STSLICER
            XCHG2 s0, s4
            STGRAMS
            XCHG s1, s2
            STU 107
            SWAP
            STBR
            ENDC
            SWAP
            SENDRAWMSG
          }>
          PUSHINT -1
        }>ELSE<{
          DROP
          PUSHINT 0
        }>
        IFRET
        GETGLOB 1
        INDEX 7
        GETGLOB 1
        INDEX 3
        PUSHINT 2078119902
        EQUAL
        IF:<{
          LDGRAMS
          LDMSGADDR
          LDMSGADDR
          DROP
          MYADDR
          GETGLOB 5
          XCHG s2, s3
          NEWC
          PUSHINT 0
          STGRAMS
          XCHG2 s0, s3
          STSLICER
          SWAP
          STSLICER
          STREF
          ENDC
          GETGLOB 5
          SWAP
          PUSHNULL
          PUSHNULL
          TUPLE 4
          PUSHINT 0
          CALL:<{
            OVER
            UNTUPLE 4
            DUP
            ISNULL
            IF:<{
              2DROP
              XCHG s0, s3
              CALL:<{
                UNTUPLE 4
                OVER
                ISNULL
                IF:<{
                  NIP
                  PUSHINT 0
                  DUP
                  NEWC
                  STU 2
                  PUXC s4, s(-1)
                  STDICT
                  PUXC s3, s(-1)
                  STDICT
                  STU 1
                  ENDC
                  SWAP
                }>
                XCHG3 s3, s3, s0
                PUXC s3, s(-1)
                TUPLE 4
                SWAP
              }>
              NIP
              DUP
              HASHCU
              PUSHINT 4
              NEWC
              STU 3
              XCHG s1, s4
              STI 8
              XCHG s1, s3
              STU 256
              ENDC
              CTOS
              XCHG3 s0, s1, s3
            }>ELSE<{
              POP s4
              POP s4
            }>
            BLKSWAP 1, 3
            PUSH s3
            TUPLE 4
            SWAP
          }>
          NIP
          GETGLOB 1
          INDEX 1
          SDEQ
          THROWIFNOT 401
          DUP
          PLDU 2
          NEQINT 0
          IF:<{
            PUSHINT 0
            SWAP
            PUSHINT 66
            PUSHINT 3576854235
            ROTREV
            CALL:<{
              GETGLOB 1
              INDEX 4
              PUSHINT 0
              PUSHINT 16
              NEWC
              STU 6
              XCHG2 s0, s4
              STSLICER
              XCHG2 s0, s5
              STGRAMS
              XCHG s1, s2
              STU 107
              XCHG s1, s2
              STU 32
              XCHG s1, s2
              STU 64
              ENDC
              SWAP
              SENDRAWMSG
            }>
          }>ELSE<{
            DROP
          }>
          GETGLOB 2
          SWAP
          SUB
          SETGLOB 2
          CALL:<{
            GETGLOB 5
            GETGLOB 4
            NEWC
            GETGLOB 2
            STGRAMS
            GETGLOB 3
            STSLICER
            STREF
            STREF
            ENDC
            POP c4
          }>
          PUSHINT -1
        }>ELSE<{
          DROP
          PUSHINT 0
        }>
        IFRET
        PUSHPOW2DEC 16
        THROWANY
      }>
      24 => <{
        NEWC
        OVER
        LESSINT 0
        IF:<{
          PUSHSLICE x{2D}
          STSLICER
          SWAP
          NEGATE
          SWAP
        }>
        PUSHINT 0
        DUP
        PUSHINT 1
        UNTIL:<{
          XCHG s0, s4
          PUSHINT 10
          DIVMOD
          ADDINT 48
          PUSH s5
          MUL
          XCHG s1, s2
          ADD
          XCHG s0, s4
          LSHIFT 8
          XCHG s0, s2
          INC
          OVER
          EQINT 0
          XCHG3 s5, s3, s0
        }>
        DROP
        POP s3
        LSHIFT 3
        STUX
        ENDC
        CTOS
      }>
      59 => <{
        DUP
        PUSHINT 1000000000000000000
        LESS
        IFJMP:<{
          PUSHINT 1000000000000000000
          PUXC s0, s1
          MULDIV
          CALLDICT 59
          NEGATE
        }>
        PUSHINT 0
        OVER
        PUSHINT 2158111692681982714103749998457715264521539211273193359375
        LSHIFT 54
        GEQ
        IF:<{
          DROP
          PUSHINT 565736031566425676606013439595699310302734375
          LSHIFT 36
          DIV
          PUSHINT 3814697265625
          LSHIFT 25
        }>
        OVER
        PUSHINT 185821923041689899054467678070068359375
        LSHIFT 25
        GEQ
        IF:<{
          SWAP
          PUSHINT 6235149080811616882910000000
          DIV
          SWAP
          PUSHINT 3814697265625
          LSHIFT 24
          ADD
        }>
        MULINT 100
        SWAP
        MULINT 100
        DUP
        PUSHINT 7896296018268069516100000000000000
        GEQ
        IF:<{
          PUSHINT 100000000000000000000
          PUSHINT 7896296018268069516100000000000000
          MULDIV
          SWAP
          PUSHINT 95367431640625
          LSHIFT 25
          ADD
          SWAP
        }>
        DUP
        PUSHINT 888611052050787263676000000
        GEQ
        IF:<{
          PUSHINT 100000000000000000000
          PUSHINT 888611052050787263676000000
          MULDIV
          SWAP
          PUSHINT 95367431640625
          LSHIFT 24
          ADD
          SWAP
        }>
        DUP
        PUSHINT 298095798704172827474000
        GEQ
        IF:<{
          PUSHINT 100000000000000000000
          PUSHINT 298095798704172827474000
          MULDIV
          SWAP
          PUSHINT 95367431640625
          LSHIFT 23
          ADD
          SWAP
        }>
        DUP
        PUSHINT 5459815003314423907810
        GEQ
        IF:<{
          PUSHINT 100000000000000000000
          PUSHINT 5459815003314423907810
          MULDIV
          SWAP
          PUSHINT 400000000000000000000
          ADD
          SWAP
        }>
        DUP
        PUSHINT 738905609893065022723
        GEQ
        IF:<{
          PUSHINT 100000000000000000000
          PUSHINT 738905609893065022723
          MULDIV
          SWAP
          PUSHINT 200000000000000000000
          ADD
          SWAP
        }>
        DUP
        PUSHINT 271828182845904523536
        GEQ
        IF:<{
          PUSHINT 100000000000000000000
          PUSHINT 271828182845904523536
          MULDIV
          SWAP
          PUSHINT 100000000000000000000
          ADD
          SWAP
        }>
        DUP
        PUSHINT 164872127070012814685
        GEQ
        IF:<{
          PUSHINT 100000000000000000000
          PUSHINT 164872127070012814685
          MULDIV
          SWAP
          PUSHINT 50000000000000000000
          ADD
          SWAP
        }>
        DUP
        PUSHINT 128402541668774148407
        GEQ
        IF:<{
          PUSHINT 100000000000000000000
          PUSHINT 128402541668774148407
          MULDIV
          SWAP
          PUSHINT 25000000000000000000
          ADD
          SWAP
        }>
        DUP
        PUSHINT 113314845306682631683
        GEQ
        IF:<{
          PUSHINT 100000000000000000000
          PUSHINT 113314845306682631683
          MULDIV
          SWAP
          PUSHINT 12500000000000000000
          ADD
          SWAP
        }>
        DUP
        PUSHINT 106449445891785942956
        GEQ
        IF:<{
          PUSHINT 100000000000000000000
          PUSHINT 106449445891785942956
          MULDIV
          SWAP
          PUSHINT 6250000000000000000
          ADD
          SWAP
        }>
        DUP
        PUSHINT 100000000000000000000
        SUB
        PUSHINT 100000000000000000000
        XCPU s2, s2
        ADD
        XCHG s1, s2
        MULDIV
        PUSH2 s0, s0
        PUSHINT 100000000000000000000
        MULDIV
        2DUP
        PUSHINT 100000000000000000000
        MULDIV
        DUP
        PUSHINT 3
        DIV
        XCHG s1, s3
        ADD
        XCPU s2, s1
        PUSHINT 100000000000000000000
        MULDIV
        DUP
        PUSHINT 5
        DIV
        XCHG s1, s3
        ADD
        XCPU s2, s1
        PUSHINT 100000000000000000000
        MULDIV
        DUP
        PUSHINT 7
        DIV
        XCHG s1, s3
        ADD
        XCPU s2, s1
        PUSHINT 100000000000000000000
        MULDIV
        DUP
        PUSHINT 9
        DIV
        XCHG s1, s3
        ADD
        ROTREV
        PUSHINT 100000000000000000000
        MULDIV
        PUSHINT 11
        DIV
        ADD
        LSHIFT 1
        ADD
        PUSHINT 100
        DIV
      }>
      71 => <{
        DUP
        PUSHINT 1000000000000000000
        EQUAL
        IFJMP:<{
          DROP
          PUSHINT 2718281828459045235
        }>
        PUSHINT 50004
        OVER
        PUSHINT -41000000000000000000
        GEQ
        PUSH s2
        PUSHINT 130000000000000000000
        LEQ
        AND
        THROWANYIFNOT
        DUP
        LESSINT 0
        IFJMP:<{
          PUSHINT 1000000000000000000
          PUXC s0, s1
          NEGATE
          CALLDICT 71
          XCHG s1, s2
          MULDIV
        }>
        DUP
        PUSHINT 3814697265625
        LSHIFT 25
        GEQ
        IF:<{
          PUSHINT 3814697265625
          LSHIFT 25
          SUB
          PUSHINT 565736031566425676606013439595699310302734375
          LSHIFT 36
        }>ELSE<{
          DUP
          PUSHINT 3814697265625
          LSHIFT 24
          GEQ
          IF:<{
            PUSHINT 3814697265625
            LSHIFT 24
            SUB
            PUSHINT 6235149080811616882910000000
          }>ELSE<{
            PUSHINT 1
          }>
        }>
        SWAP
        MULINT 100
        PUSHINT 100000000000000000000
        OVER
        PUSHINT 95367431640625
        LSHIFT 25
        GEQ
        IF:<{
          DROP
          PUSHINT 95367431640625
          LSHIFT 25
          SUB
          PUSHINT 7896296018268069516100000000000000
        }>
        OVER
        PUSHINT 95367431640625
        LSHIFT 24
        GEQ
        IF:<{
          SWAP
          PUSHINT 95367431640625
          LSHIFT 24
          SUB
          SWAP
          PUSHINT 888611052050787263676000000
          PUSHINT 100000000000000000000
          MULDIV
        }>
        OVER
        PUSHINT 95367431640625
        LSHIFT 23
        GEQ
        IF:<{
          SWAP
          PUSHINT 95367431640625
          LSHIFT 23
          SUB
          SWAP
          PUSHINT 298095798704172827474000
          PUSHINT 100000000000000000000
          MULDIV
        }>
        OVER
        PUSHINT 400000000000000000000
        GEQ
        IF:<{
          SWAP
          PUSHINT 400000000000000000000
          SUB
          SWAP
          PUSHINT 5459815003314423907810
          PUSHINT 100000000000000000000
          MULDIV
        }>
        OVER
        PUSHINT 200000000000000000000
        GEQ
        IF:<{
          SWAP
          PUSHINT 200000000000000000000
          SUB
          SWAP
          PUSHINT 738905609893065022723
          PUSHINT 100000000000000000000
          MULDIV
        }>
        OVER
        PUSHINT 100000000000000000000
        GEQ
        IF:<{
          SWAP
          PUSHINT 100000000000000000000
          SUB
          SWAP
          PUSHINT 271828182845904523536
          PUSHINT 100000000000000000000
          MULDIV
        }>
        OVER
        PUSHINT 50000000000000000000
        GEQ
        IF:<{
          SWAP
          PUSHINT 50000000000000000000
          SUB
          SWAP
          PUSHINT 164872127070012814685
          PUSHINT 100000000000000000000
          MULDIV
        }>
        OVER
        PUSHINT 25000000000000000000
        GEQ
        IF:<{
          SWAP
          PUSHINT 25000000000000000000
          SUB
          SWAP
          PUSHINT 128402541668774148407
          PUSHINT 100000000000000000000
          MULDIV
        }>
        OVER
        PUSHINT 100000000000000000000
        OVER
        ADD
        XCPU s1, s3
        PUSHINT 200000000000000000000
        MULDIV
        TUCK
        ADD
        XCPU s1, s3
        PUSHINT 300000000000000000000
        MULDIV
        TUCK
        ADD
        XCPU s1, s3
        PUSHINT 400000000000000000000
        MULDIV
        TUCK
        ADD
        XCPU s1, s3
        PUSHINT 500000000000000000000
        MULDIV
        TUCK
        ADD
        XCPU s1, s3
        PUSHINT 600000000000000000000
        MULDIV
        TUCK
        ADD
        XCPU s1, s3
        PUSHINT 700000000000000000000
        MULDIV
        TUCK
        ADD
        XCPU s1, s3
        PUSHINT 95367431640625
        LSHIFT 23
        MULDIV
        TUCK
        ADD
        XCPU s1, s3
        PUSHINT 900000000000000000000
        MULDIV
        TUCK
        ADD
        XCPU s1, s3
        PUSHINT 1000000000000000000000
        MULDIV
        TUCK
        ADD
        XCPU s1, s3
        PUSHINT 1100000000000000000000
        MULDIV
        TUCK
        ADD
        XCHG s0, s3
        PUSHINT 1200000000000000000000
        MULDIV
        XCHG s1, s2
        ADD
        PUSHINT 100000000000000000000
        MULDIV
        SWAP
        PUSHINT 100
        MULDIV
      }>
      103289 => <{
        CALL:<{
          PUSH c4
          CTOS
          LDGRAMS
          SWAP
          SETGLOB 2
          LDMSGADDR
          SWAP
          SETGLOB 3
          LDREF
          SWAP
          SETGLOB 4
          LDREF
          SWAP
          SETGLOB 5
          ENDS
        }>
        MYADDR
        GETGLOB 5
        NEWC
        PUSHINT 0
        STGRAMS
        XCHG2 s0, s3
        STSLICER
        SWAP
        STSLICER
        STREF
        ENDC
        GETGLOB 5
        SWAP
        PUSHNULL
        PUSHNULL
        TUPLE 4
        PUSHINT 0
        CALL:<{
          OVER
          UNTUPLE 4
          DUP
          ISNULL
          IF:<{
            2DROP
            XCHG s0, s3
            CALL:<{
              UNTUPLE 4
              OVER
              ISNULL
              IF:<{
                NIP
                PUSHINT 0
                DUP
                NEWC
                STU 2
                PUXC s4, s(-1)
                STDICT
                PUXC s3, s(-1)
                STDICT
                STU 1
                ENDC
                SWAP
              }>
              XCHG3 s3, s3, s0
              PUXC s3, s(-1)
              TUPLE 4
              SWAP
            }>
            NIP
            DUP
            HASHCU
            PUSHINT 4
            NEWC
            STU 3
            XCHG s1, s4
            STI 8
            XCHG s1, s3
            STU 256
            ENDC
            CTOS
            XCHG3 s0, s1, s3
          }>ELSE<{
            POP s4
            POP s4
          }>
          BLKSWAP 1, 3
          PUSH s3
          TUPLE 4
          SWAP
        }>
        NIP
      }>
      106029 => <{
        CALL:<{
          PUSH c4
          CTOS
          LDGRAMS
          SWAP
          SETGLOB 2
          LDMSGADDR
          SWAP
          SETGLOB 3
          LDREF
          SWAP
          SETGLOB 4
          LDREF
          SWAP
          SETGLOB 5
          ENDS
        }>
        GETGLOB 2
        PUSHINT -1
        GETGLOB 3
        GETGLOB 4
        GETGLOB 5
      }>
    }
    THROWARG 11
PUSHREF (0B71035B074A86584DD538A0805AE1E110224DE7701E30391AA677ED672F9BB2)
CTOS
BLESS
EXECUTE
"""

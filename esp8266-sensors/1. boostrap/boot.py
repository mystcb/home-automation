# This file is executed on every boot (including wake-boot from deepsleep)
import esp # pylint: disable=import-error
esp.osdebug(None)
import uos, machine # pylint: disable=import-error
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

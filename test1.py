from pycomm3 import LogixDriver

#with PLC() as comm:
#    comm.Micro800 = True
#    comm.IPAddress = '192.168.1.242'
#    ret = comm.Read('_IO_EM_DI_00')
#    print(ret.TagName, ret.Value, ret.Status)

def read_single():
    with LogixDriver('192.168.1.242') as plc:
        return plc.read('_IO_EM_DI_00')

read_single()
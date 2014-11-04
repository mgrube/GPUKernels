import pyopencl as cl

platform = cl.get_platforms()[0]
device = platform.get_devices()[0]
context = cl.Context([device])

clfile = open('test.cl', 'rb')

#Build and describe the kernel in one swoop
program = cl.Program(context, clfile.read()).build()

queue = cl.CommandQueue(context)

    

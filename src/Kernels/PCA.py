import pyopencl as cl

platform = cl.get_platforms()[0]
device = cl.get_deivces()[0]
context = cl.Context([device])

#Build and describe the kernel in one swoop
program = cl.Program(context, programstring).build()

queue = cl.CommandQueue(context)

mem_flags = cl.mem_flags

matrix_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf=matrix)

vector_buf = cl.Buffer(context, mem_flags.READ_ONLY | mem_flags.COPY_HOST_PTR, hostbuf=vector)

matrix_dot_vector = numpy.zeros(4, numpy.float32)

destination_buf = cl.Buffer(context, mem_flags.WRITE_ONLY, matrix_dot_vector.nbytes)
     



for i in range(6, 101):
    current_number = i*i*i
    for j in range(2, i):
        for k in range(j+1, i):
            for z in range(k+1, i):
                if z*z*z + k*k*k + j*j*j == current_number:
                    print('Cube = {0}, Triple = ({1},{2},{3})'.format(i, j, k, z))
                #elif z*k*j < current_number: break




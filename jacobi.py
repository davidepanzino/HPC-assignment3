import numpy as np
import matplotlib.pyplot as plt
import time

# def jacobi(f):
#     newf = f.copy()
#     for i in range(1, newf.shape[0]-1):
#         for j in range(1, newf.shape[1]-1):
#             newf[i, j] = 0.25 * (f[i, j+1] + f[i, j-1] + f[i+1, j] + f[i-1, j])
#     return newf

def numpy_jacobi(f):
    newf = f.copy()
    # Circular shift to the right
    right_shifted = np.roll(f, 1, axis=1)
    
    # Circular shift to the left
    left_shifted = np.roll(f, -1, axis=1)
    
    # Circular shift upwards
    up_shifted = np.roll(f, -1, axis=0)
    
    # Circular shift downwards
    down_shifted = np.roll(f, 1, axis=0)
    
    # Update newf using roll operations
    newf[1:-1, 1:-1] = 0.25 * (right_shifted[1:-1, 1:-1] + left_shifted[1:-1, 1:-1] +
                              up_shifted[1:-1, 1:-1] + down_shifted[1:-1, 1:-1])
    
    return newf


if __name__ == "__main__":
    exec_time = [[] for _ in range(62)]
    # Varying the grid size from 3 to 10
    for i, grid in enumerate(range (3, 65), start=0):
        # Create an initial grid of zeros with the specified size
        initGrid = np.zeros((grid, grid))
        
        t1 = time.time()
        for j in range(1000):    
            initGrid = numpy_jacobi(initGrid)
        t2 = time.time()
        exec_time[i].append(t2 - t1)
        print(f"Execution time with grid size equal to {grid} is {exec_time[i]} seconds")
        
    grid_sizes = [g for g in range(3, 65)]
    plt.plot(grid_sizes, exec_time, marker='.', linestyle='-')
    plt.xlabel('Grid size')
    plt.ylabel('Execution time (sec)')
    plt.title('Execution time for various grid sizes')
    plt.grid(True)
    plt.show()


    # initGrid = np.zeros((10, 10))
    # t1 = time.time()
    # for j in range(1000):    
        # initGrid = cythonfn.gauss_seidel(initGrid)
        # initGrid = gauss_seidel(initGrid)
    # t2 = time.time()
    # print(f"Execution time is {t2-t1} seconds")

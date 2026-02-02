from modules.drag.drag_module import calculate_drag

#Test Case 1
print("Test Case 1")
result = calculate_drag(CL=0.5, AR=8.0, CD0 = 0.015)
print(f"Total drag: CD = {result['CD']:.4f}")
print(f"Oswald efficiency: e = {result['e']:.4f}")
print(f"Induced drag: CD_induced = {result['CD_induced']:.4f}")
print(f"Lift drag ratio: L/D = {result['LD_ratio']:.2f}\n")

#Test Case 2
print("Test Case 2")
result = calculate_drag(CL=0.3, AR=10.0, CD0 = 0.020)
print(f"Total drag: CD = {result['CD']:.4f}")
print(f"Oswald efficiency: e = {result['e']:.4f}")
print(f"Induced drag: CD_induced = {result['CD_induced']:.4f}")
print(f"Lift drag ratio: L/D = {result['LD_ratio']:.2f}\n")

#Test Case 3
print("Test Case 3")
result = calculate_drag(CL=0.7, AR=6.0, CD0 = 0.012)
print(f"Total drag: CD = {result['CD']:.4f}")
print(f"Oswald efficiency: e = {result['e']:.4f}")
print(f"Induced drag: CD_induced = {result['CD_induced']:.4f}")
print(f"Lift drag ratio: L/D = {result['LD_ratio']:.2f}\n")

#Test Case 4 - Includes Negative CL
print("Test Case 4")
result = calculate_drag(CL=-0.7, AR=6.0, CD0 = 0.012)
print(f"Total drag: CD = {result['CD']:.4f}")
print(f"Oswald efficiency: e = {result['e']:.4f}")
print(f"Induced drag: CD_induced = {result['CD_induced']:.4f}")
print(f"Lift drag ratio: L/D = {result['LD_ratio']:.2f}\n")
import torch

def run_tensor_math():
    print("=============================")
    print("[INFO] TASK-007: PyTorch Math Engine Active...")
    print("=================")

    tensor_a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
    tensor_b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

    print(f"Tensor A:\n{tensor_a}\n")
    print(f"tensor B:\n{tensor_b}\n")
    

    tensor_add = tensor_a + tensor_b
    print(f"[MATH] Tensor Addition (A + B):\n{tensor_add}\n")

    tensor_add = tensor_a + tensor_b
    print(f"[MATH] Tensor Addition (A + B):\n{tensor_add}\n")
    tensor_mul = torch.matmul(tensor_a, tensor_b)
    print(f"[MATH] Matrix Multiplication (A * B):\n{tensor_mul}")
    print("==========================")

if __name__ == "__main__":
    run_tensor_math()

    
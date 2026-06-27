import torch

def run_tensor_reshape():
    print("=======================")
    print("[INFO] TASK-008: PyTorch Reshape Engine Active...")
    print("===============")

    flat_tensor = torch.arange(1, 13)
    print(f"Original flat Tensor:\n{flat_tensor}")
    print(f"Original Shape: {flat_tensor.shape}\n")

    print("[PROCESS] Reshaping data for AI model...")

    matrix_2x6 = flat_tensor.view(2, 6)
    print(f"Reshaped Tensor (2x6):\n{matrix_2x6}")
    print(f"New Shape: {matrix_2x6.shape}")
    print("=========================")

if __name__ == "__main__":
    run_tensor_reshape()
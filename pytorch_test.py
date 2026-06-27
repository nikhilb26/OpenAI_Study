import torch

def init_ai_engine():
    print("========================")
    print("[INFO] TASK-006: PyTorch AI Engine Active...")
    print("==============================")

    print("[PROCESS] Creating our first AI Tensor...")
    tensor_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    print(f"Tensor Output:\n{tensor_data}\n")

    print("[PROCESS] Checking Hardware Acceleration (CPU)...")
    if torch.cuda.is_available():
        print("[SUCCESS] Wow! NVIDIA GPU (CUDA) bhetla! ")
    else:
        print("[INFO] GPU nahi bhetla, AI engine CPU var run hot ahe. ")

if __name__ == "__main__":
    init_ai_engine()
import torch

def run_slice():
    print("=================")
    print("[INFO] TASK-009: PyTorch Slicing Engine...")
    print("======================")

    m1 = torch.tensor([[10, 20, 30],
                       [40, 50, 60],
                       [70, 80, 90]])
    print(f"Original Matrix:\n{m1}\n")

    res1 = m1[0, :]
    print(f"First Row Only:\n{res1}\n")

    res2 = m1[1, 1]
    print(f"Center Element (50):\n{res2}\n")

    res3 = m1[1:, 1:]
    print(f"Sliced 2x2 Sub-Matrix:\n{res3}")
    print("======================")

if __name__ == "__main__":
    run_slice()
            
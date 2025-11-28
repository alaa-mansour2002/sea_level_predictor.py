
import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # تحويل القائمة إلى مصفوفة 3x3
    matrix = np.array(numbers).reshape(3, 3)
    
    # حساب الإحصائيات
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),   # الأعمدة
            matrix.mean(axis=1).tolist(),   # الصفوف
            matrix.mean().item()            # كل العناصر
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }
    
    return calculations

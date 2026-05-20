import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_breast_cancer

# טעינת מערך הנתונים
data = load_breast_cancer()

# יצירת DataFrame של Pandas לנוחות עבודה
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# הפרדה בין שפיר (Benign) לממאיר (Malignant)
# במערך הנתונים של sklearn: 0 = ממאיר, 1 = שפיר
malignant = df[df['target'] == 0]
benign = df[df['target'] == 1]

# הגדרת גודל הגרף
plt.figure(figsize=(10, 7))

# ציור הנקודות של הגידולים הממאירים (באדום/כתום שקוף)
plt.scatter(
    malignant['mean texture'], 
    malignant['mean smoothness'], 
    color='tomato', 
    alpha=0.6, 
    edgecolors='black', 
    linewidths=0.5,
    label='Malignant'
)

# ציור הנקודות של הגידולים השפירים (בכחול שקוף)
plt.scatter(
    benign['mean texture'], 
    benign['mean smoothness'], 
    color='steelblue', 
    alpha=0.6, 
    edgecolors='black', 
    linewidths=0.5,
    label='Benign'
)

# הוספת כותרות ועיצוב הגרף
plt.title('Wisconsin Cancer Dataset — two features', fontsize=14)
plt.xlabel('mean texture', fontsize=12)
plt.ylabel('mean smoothness', fontsize=12)
plt.legend(loc='upper right')
plt.grid(False)

# הצגת הגרף
plt.tight_layout()
plt.show()
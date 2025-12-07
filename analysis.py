import pandas as pd
import matplotlib.pyplot as plt

# User email for verification
email = "24f3001410@ds.study.iitm.ac.in"
print(f"Analysis by: {email}")

# Data creation
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Score': [3.9, 4.0, 4.1, 4.08]
}

df = pd.DataFrame(data)

# Analysis
average_score = df['Score'].mean()
print(f"Average Score: {average_score}")

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(df['Quarter'], df['Score'], marker='o', linestyle='-', color='b', label='Actual Score')
plt.axhline(y=4.5, color='r', linestyle='--', label='Target (4.5)')
plt.axhline(y=4.02, color='g', linestyle=':', label='Average (4.02)')

plt.title('Quarterly Customer Satisfaction Score Trend')
plt.xlabel('Quarter')
plt.ylabel('Score')
plt.ylim(3.5, 5.0)
plt.legend()
plt.grid(True)

# Save visualization
plt.savefig('trend_analysis.png')
print("Visualization saved as trend_analysis.png")

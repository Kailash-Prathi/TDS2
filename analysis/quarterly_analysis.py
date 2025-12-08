# LLM assistance: Jules
# Codex labeling: jules-assist-001
# Purpose: Read quarterly ratings, compute averages, and generate visualizations.
# Run: python analysis/quarterly_analysis.py
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

DATA_PATH = os.path.join("data", "quarterly_ratings.csv")
OUTPUT_DIR = os.path.join("outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)
df['quarter_order'] = range(1, len(df) + 1)

# Compute statistics
average_rating = df['rating'].mean()
print(f"Computed average rating: {average_rating:.4f}")
print(f"Rounded average (2 d.p.): {average_rating:.2f}")  # Should be 4.02

# Trend plot (line)
plt.figure(figsize=(9,5))
sns.lineplot(x='quarter_order', y='rating', marker='o', data=df)
plt.xticks(df['quarter_order'], df['quarter'], rotation=45)
plt.ylim(3.5, 4.6)
plt.axhline(4.02, color='gray', linestyle='--', label='Observed avg = 4.02')
plt.axhline(4.5, color='red', linestyle=':', label='Target = 4.5')
plt.title("Quarterly Average Ratings (Trend)")
plt.xlabel("Quarter")
plt.ylabel("Average Rating")
plt.legend()
trend_path = os.path.join(OUTPUT_DIR, "trend.png")
plt.tight_layout()
plt.savefig(trend_path, dpi=150)
plt.close()
print(f"Saved trend plot to {trend_path}")

# Benchmark comparison (bar)
labels = ['Current average', 'Target (4.5)']
values = [average_rating, 4.5]
colors = ['#4c72b0', '#dd8452']
plt.figure(figsize=(6,4))
sns.barplot(x=labels, y=values, palette=colors)
plt.ylim(0,5)
for i, v in enumerate(values):
    plt.text(i, v + 0.03, f"{v:.2f}", ha='center')
plt.title("Current Average vs Target Benchmark")
bench_path = os.path.join(OUTPUT_DIR, "benchmark_comparison.png")
plt.tight_layout()
plt.savefig(bench_path, dpi=150)
plt.close()
print(f"Saved benchmark comparison plot to {bench_path}")

# Additional outputs: last 2-quarter trend check
recent_mean = df.tail(2)['rating'].mean()
print(f"Recent (last 2 quarters) average: {recent_mean:.2f}")

# Summary to file
summary_path = os.path.join(OUTPUT_DIR, "summary.txt")
with open(summary_path, "w") as f:
    f.write("Quarterly Ratings Analysis Summary\n")
    f.write("-------------------------------\n")
    f.write(f"Computed average rating (all quarters): {average_rating:.4f}\n")
    f.write(f"Rounded average (2 d.p.): {average_rating:.2f}\n")
    f.write(f"Recent (last 2 quarters) average: {recent_mean:.2f}\n")
    f.write("Recommendation: improve service quality and wait times to reach the target of 4.5\n")
print(f"Wrote summary to {summary_path}")

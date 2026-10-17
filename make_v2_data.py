import pandas as pd

print("正在读取 v1 原始数据...")
df = pd.read_csv("robotaxi_data.csv")

# ---------------------------------------------
# 动作1：清洗异常值 
# 剔除“距离小于5公里，但耗时超过40分钟”的极度不合理数据
initial_len = len(df)
df = df[~((df['distance_km'] < 5) & (df['eta_min'] > 40))]
print(f"清洗异常值：剔除了 {initial_len - len(df)} 条异常数据。")

# ---------------------------------------------
# 动作2：增加真实业务场景与极端天气权重 
# 我们从原数据中抽取一些样本，模拟下雨(weather=1)和下雪(weather=2)的高峰期场景
# 下雨高峰期：时间增加 30%
rain_samples = df.sample(n=15, random_state=42).copy()
rain_samples['weather'] = 1
rain_samples['is_peak'] = 1
rain_samples['eta_min'] = rain_samples['eta_min'] * 1.3

# 下雪高峰期：时间增加 60%（速度极慢）
snow_samples = df.sample(n=15, random_state=24).copy()
snow_samples['weather'] = 2
snow_samples['is_peak'] = 1
snow_samples['eta_min'] = snow_samples['eta_min'] * 1.6

# ---------------------------------------------
# 动作3：合并数据并保存为 v2 版本
df_v2 = pd.concat([df, rain_samples, snow_samples], ignore_index=True)
df_v2.to_csv("robotaxi_data.csv", index=False)
print(f"✅ v2 版本生成完毕！新增了 15 条雨天数据和 15 条雪天数据，总计 {len(df_v2)} 条。")
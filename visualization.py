import matplotlib.pyplot as plt
import numpy

def plot_revenue_trend(df):
    revenue_by_date = df.groupby("date")["revenue"].sum()

    fig, ax = plt.subplots(figsize=(10, 5))

    revenue_by_date.plot(ax=ax)

    ax.set_title("Revenue Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue")

    return fig

def detect_anomalies(df):

    revenue_by_date = df.groupby("date")["revenue"].sum()

    mean = revenue_by_date.mean()
    std = revenue_by_date.std()

    threshold = 2 * std

    anomalies = revenue_by_date[
        abs(revenue_by_date - mean) > threshold
    ]

    return anomalies
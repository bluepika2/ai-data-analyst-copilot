import pandas as pd


def calculate_kpi_summary(df: pd.DataFrame) -> dict:
    summary = {}

    if "revenue" in df.columns:
        total_revenue = df["revenue"].sum()
        avg_revenue = df["revenue"].mean()

        summary["total_revenue"] = round(total_revenue, 2)
        summary["average_revenue"] = round(avg_revenue, 2)

    if "date" in df.columns and "revenue" in df.columns:
        revenue_by_date = df.groupby("date")["revenue"].sum().reset_index()
        revenue_by_date = revenue_by_date.sort_values("date")

        first_value = revenue_by_date["revenue"].iloc[0]
        last_value = revenue_by_date["revenue"].iloc[-1]

        if first_value != 0:
            revenue_change_pct = ((last_value - first_value) / first_value) * 100
        else:
            revenue_change_pct = None

        summary["first_day_revenue"] = round(first_value, 2)
        summary["last_day_revenue"] = round(last_value, 2)
        summary["revenue_change_pct"] = round(revenue_change_pct, 2) if revenue_change_pct is not None else None

    return summary


def analyze_segments(df: pd.DataFrame) -> dict:
    segment_results = {}

    if "segment" in df.columns and "revenue" in df.columns:
        revenue_by_segment = (
            df.groupby("segment")["revenue"]
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )

        segment_results["revenue_by_segment"] = revenue_by_segment
        segment_results["top_segment"] = max(revenue_by_segment, key=revenue_by_segment.get)
        segment_results["lowest_segment"] = min(revenue_by_segment, key=revenue_by_segment.get)

    if "region" in df.columns and "revenue" in df.columns:
        revenue_by_region = (
            df.groupby("region")["revenue"]
            .sum()
            .sort_values(ascending=False)
            .to_dict()
        )

        segment_results["revenue_by_region"] = revenue_by_region
        segment_results["top_region"] = max(revenue_by_region, key=revenue_by_region.get)
        segment_results["lowest_region"] = min(revenue_by_region, key=revenue_by_region.get)

    return segment_results


def generate_analytics_summary(df: pd.DataFrame) -> dict:
    return {
        "kpi_summary": calculate_kpi_summary(df),
        "segment_analysis": analyze_segments(df)
    }
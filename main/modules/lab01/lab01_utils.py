import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import seaborn as sns
from matplotlib import cm
import numpy as np



# 자치구별 CCTV와 총 경찰관서 수 그래프
def draw_cctv_police_chart(merged_df):
    BAR_FACE = "#BDBDBD"
    BAR_EDGE = "#666666"
    LINE_COL = "#1f4e79"

    df_plot = merged_df.copy()
    df_plot["CCTV"] = pd.to_numeric(df_plot["CCTV"], errors="coerce").fillna(0)
    df_plot["총 경찰관서 수"] = pd.to_numeric(df_plot["총 경찰관서 수"], errors="coerce").fillna(0)

    df_plot = df_plot.sort_values("CCTV", ascending=False)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 막대: CCTV (왼쪽축)
    bars = ax1.bar(
        df_plot["구별"], df_plot["CCTV"],
        color=BAR_FACE, alpha=0.85,
        edgecolor=BAR_EDGE, linewidth=0.5, zorder=1
    )
    ax1.set_xlabel("자치구")
    ax1.set_ylabel("CCTV (대)", color="black")
    ax1.tick_params(axis="x", rotation=60)
    ax1.grid(axis="y", linestyle="--", alpha=0.3, zorder=0)

    # 선: 총 경찰관서 수 (오른쪽축)
    ax2 = ax1.twinx()
    (line,) = ax2.plot(
        df_plot["구별"], df_plot["총 경찰관서 수"],
        color=LINE_COL, linewidth=2, marker="o",
        markersize=5, markerfacecolor="white", markeredgecolor=LINE_COL,
        zorder=2
    )
    ax2.set_ylabel("총 경찰관서 수 (개)", color=LINE_COL)
    ax2.tick_params(axis="y", colors=LINE_COL)

    plt.title("자치구별 CCTV와 총 경찰관서 수", fontsize=13, fontweight="bold", pad=14)

    # 범례
    legend_handles = [
        Patch(facecolor=BAR_FACE, edgecolor=BAR_EDGE, label="CCTV (왼쪽축)"),
        Line2D([0], [0], color=LINE_COL, marker="o", linewidth=2,
               markerfacecolor="white", markeredgecolor=LINE_COL,
               label="총 경찰관서 수 (오른쪽축)")
    ]
    fig.legend(handles=legend_handles, loc="lower center", ncol=2,
               frameon=False, bbox_to_anchor=(0.5, -0.02))
    plt.subplots_adjust(bottom=0.28)
    plt.tight_layout()

    return fig


# 인구수, CCTV, 경찰관서 수, 범죄발생, 검거율 간 상관관계
def plot_corr_heatmap(merged_df):
    cols = ["인구수", "CCTV", "총 경찰관서 수", "범죄발생", "검거율"]

    df_corr = merged_df[cols].copy()
    for c in cols:
        df_corr[c] = pd.to_numeric(df_corr[c], errors="coerce")

    corr = df_corr.corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        square=True,
        cbar_kws={"shrink": .8},
        linewidths=0.5,
        ax=ax
    )

    ax.set_title(
        "인구수, CCTV, 경찰관서 수, 범죄발생, 검거율 간 상관관계",
        fontsize=12,
        fontweight="bold",
        pad=14
    )
    fig.tight_layout()

    return fig


# 인구 10만명당 폭력발생 상위 10개 구 그래프
def plot_top10_violence_per_100k(merged_df):
    df_plot = merged_df.copy()

    df_plot["인구10만명당_폭력발생"] = (
        df_plot["폭력_발생"] / df_plot["인구수"] * 100000
    )

    top10 = (
        df_plot.nlargest(10, "인구10만명당_폭력발생")
               .sort_values("인구10만명당_폭력발생", ascending=False)
    )

    cmap = cm.get_cmap("Reds", len(top10))
    base_colors = [cmap(v) for v in np.linspace(0.4, 0.80, len(top10))]
    colors_desc = base_colors[::-1]
    palette_map = dict(zip(top10["구별"], colors_desc))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax = sns.barplot(
        data=top10,
        x="인구10만명당_폭력발생",
        y="구별",
        order=top10["구별"],
        hue="구별",
        legend=False,
        dodge=False,
        palette=palette_map,
        edgecolor="black",
        linewidth=0.5,
        ax=ax
    )

    ax.set_title(
        "인구 10만명당 폭력발생 건수 상위 10개 구",
        fontsize=15,
        fontweight="bold",
        pad=14
    )
    ax.set_xlabel("인구 10만명당 폭력발생 건수", fontsize=12)
    ax.set_ylabel("구별", fontsize=12)

    xmax = top10["인구10만명당_폭력발생"].max()
    ax.set_xlim(0, xmax * 1.12)

    for p in ax.patches:
        w = p.get_width()
        y = p.get_y() + p.get_height() / 2
        ax.annotate(
            f"{w:.1f}",
            xy=(w, y),
            xytext=(5, 0),
            textcoords="offset points",
            va="center",
            ha="left",
            fontsize=10,
            clip_on=False
        )

    ax.margins(x=0.03)
    fig.tight_layout()

    return fig

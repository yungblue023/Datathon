import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go

# Data for the charts
data = {
    "Year": [2020, 2021, 2022, 2023],
    "Digital Payments": [17.6, 24.1, 29.5, 32.5],  # Total electronic payments (in billions)
    "Volume of Notes": [1.44, 1.67, 1.84, 1.87],  # Volume of notes in circulation (in billions)
    "Volume of Coins": [0.043, 0.042, 0.043, 0.045]  # Volume of coins in circulation (in billions)
}

# Create a DataFrame
df = pd.DataFrame(data)

# User-provided average values
average_instruments = 4.5  # in billions
average_channels = 3.94  # in billions
average_systems = 17.50  # in billions
average_notes = 1.70  # in billions
average_coins = 0.043  # in billions (43 million converted to billions)

# Title with styling and vibrant color
st.markdown("<h1 style='text-align: center; color: #FF5722;'>Digital Payments and Currency Circulation Dashboard</h1>", unsafe_allow_html=True)

# Custom CSS for metric backgrounds
st.markdown("""
    <style>
        .stMetric-label {font-size: 16px !important; font-weight: bold;}
        div[data-testid="metric-container"] {
            background-color: #f0f2f6;
            border: 1px solid #e1e3e8;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Display averages in mini containers with colorful backgrounds
st.header("Average Statistics")

# First row of mini containers with different colors
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div style='background-color:#4CAF50; padding:10px; border-radius:10px;'>", unsafe_allow_html=True)
    st.metric("Avg Instruments", f"{average_instruments:.2f}B", help="Average number of payment instruments used")
    st.markdown("</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div style='background-color:#03A9F4; padding:10px; border-radius:10px;'>", unsafe_allow_html=True)
    st.metric("Avg Channels", f"{average_channels:.2f}B", help="Average number of payment channels used")
    st.markdown("</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div style='background-color:#FFEB3B; padding:10px; border-radius:10px;'>", unsafe_allow_html=True)
    st.metric("Avg Systems", f"{average_systems:.2f}B", help="Average number of payment systems used")
    st.markdown("</div>", unsafe_allow_html=True)

# Centered second row of mini containers with vibrant colors
st.write("###")  # Adding space between the two rows
col4, col5, _ = st.columns([1, 1, 1])  # Empty third column for centering
with col4:
    st.markdown("<div style='background-color:#FF5722; padding:10px; border-radius:10px;'>", unsafe_allow_html=True)
    st.metric("Avg Notes", f"{average_notes:.2f}B", help="Average volume of notes in circulation")
    st.markdown("</div>", unsafe_allow_html=True)
with col5:
    st.markdown("<div style='background-color:#9C27B0; padding:10px; border-radius:10px;'>", unsafe_allow_html=True)
    st.metric("Avg Coins", f"{average_coins:.3f}B", help="Average volume of coins in circulation")
    st.markdown("</div>", unsafe_allow_html=True)

# Add a horizontal line for visual separation
st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)

# 1. Original Chart: Trends in Digital Payments and Currency Circulation
st.header("1. Trends in Digital Payments and Currency Circulation (2020 - 2023)")
fig1, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(df["Year"] - 0.15, df["Volume of Notes"], width=0.3, label="Volume of Notes", color='#4CAF50')
ax1.bar(df["Year"] + 0.15, df["Volume of Coins"], width=0.3, label="Volume of Coins", color='#FF9800')
ax1.set_xlabel("Years", fontsize=12)
ax1.set_ylabel("Volume of Notes and Coins (in Billions)", fontsize=12, color='#4CAF50')
ax1.tick_params(axis='y', labelcolor='#4CAF50')

ax2 = ax1.twinx()
ax2.plot(df["Year"], df["Digital Payments"], label="Digital Payments", marker='o', color='#03A9F4', linewidth=2.5)
ax2.set_ylabel("Total Usage (in Billions)", fontsize=12, color='#03A9F4')
ax2.tick_params(axis='y', labelcolor='#03A9F4')

ax1.legend(loc="upper left", fontsize=10)
ax2.legend(loc="upper right", fontsize=10)
plt.title("Trends in Digital Payments and Currency Circulation (2020 - 2023)", fontsize=14)
st.pyplot(fig1)

# 2. Stacked Area Chart: Composition of Payment Methods
st.header("2. Composition of Payment Methods Over Time")
fig2, ax = plt.subplots(figsize=(12, 6))
ax.stackplot(df["Year"], df["Digital Payments"], df["Volume of Notes"], df["Volume of Coins"],
             labels=["Digital Payments", "Volume of Notes", "Volume of Coins"],
             colors=['#03A9F4', '#4CAF50', '#FF9800'])
ax.legend(loc='upper left', fontsize=10)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Volume (in Billions)", fontsize=12)
ax.set_title("Composition of Payment Methods Over Time", fontsize=14)
st.pyplot(fig2)

# 3. Pie Chart: Distribution of Payment Methods in 2023
st.header("3. Distribution of Payment Methods in 2023")
fig3, ax = plt.subplots(figsize=(10, 10))
sizes = df.loc[df["Year"] == 2023, ["Digital Payments", "Volume of Notes", "Volume of Coins"]].values[0]
labels = ["Digital Payments", "Volume of Notes", "Volume of Coins"]
colors = ['#03A9F4', '#4CAF50', '#FF9800']
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
plt.title("Distribution of Payment Methods in 2023", fontsize=14)
st.pyplot(fig3)

# 4. Line Chart: Growth Rates
st.header("4. Year-over-Year Growth Rates")
growth_rates = df.set_index("Year").pct_change() * 100
fig4, ax = plt.subplots(figsize=(12, 6))
for column, color in zip(growth_rates.columns, ['#03A9F4', '#4CAF50', '#FF9800']):
    ax.plot(growth_rates.index[1:], growth_rates[column][1:], marker='o', label=column, color=color)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Growth Rate (%)", fontsize=12)
ax.legend(fontsize=10)
ax.set_title("Year-over-Year Growth Rates of Payment Methods", fontsize=14)
st.pyplot(fig4)

# 5. Horizontal Bar Charts for Each Variable
st.header("5. Horizontal Bar Charts for Each Variable")

# Function to create horizontal bar chart with custom colors
def create_horizontal_bar_chart(data, column, color):
    fig, ax = plt.subplots(figsize=(10, 4))
    bars = ax.barh(data["Year"].astype(str), data[column], color=color)
    ax.set_xlabel(f"{column} (in Billions)", fontsize=12)
    ax.set_ylabel("Year", fontsize=12)
    ax.set_title(f"{column} by Year", fontsize=14)

    # Add value labels to the bars
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, f'{width:.3f}',
                 ha='left', va='center', fontweight='bold')

    return fig

# Create and display horizontal bar charts for each variable with custom colors
for column, color in zip(["Digital Payments", "Volume of Notes", "Volume of Coins"], ['#03A9F4', '#4CAF50', '#FF9800']):
    st.subheader(f"5.{list(df.columns).index(column)}. {column}")
    fig = create_horizontal_bar_chart(df, column, color)
    st.pyplot(fig)

# Markdown explanation about the dashboard
st.markdown(
    """
    **Dashboard Summary**:
    1. **Trends Chart**: Shows the overall trends of digital payments, notes, and coins circulation.
    2. **Composition Chart**: Illustrates how the composition of payment methods has changed over time.
    3. **Distribution Pie Chart**: Provides a snapshot of the distribution of payment methods in the most recent year (2023).
    4. **Growth Rates Chart**: Compares the year-over-year growth rates of different payment methods.
    5. **Horizontal Bar Charts**: Displays individual trends for each payment method across years.

    **Key Insights**:
    - Digital payments have shown substantial growth from 2020 to 2023.
    - The volume of notes and coins has remained relatively stable compared to digital payments.
    - In 2023, digital payments significantly outweigh physical currency in terms of volume.
    - Growth rates fluctuate, but digital payments consistently show positive growth.
    - The horizontal bar charts provide a clear view of the year-by-year changes for each payment method.

    This comprehensive dashboard illustrates the changing landscape of payment methods, highlighting the rapid digitization of financial transactions and the relative stability of digital payments.
    """
)

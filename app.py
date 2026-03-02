import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import base64
import os
import plotly.express as px



st.set_page_config(page_title='Adidas Sales!!!',page_icon=':bar_chart',layout='wide')
st.title('Adidas Analysis Dashboard')
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

data=pd.read_excel("Adidas.xlsx")

data['InvoiceDate']=pd.to_datetime(data['InvoiceDate'],errors='coerce')
data=data.dropna(subset=['InvoiceDate']).copy()
data['Year']=data['InvoiceDate'].dt.year

with st.sidebar:
    logo_path ="logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path,width=150)
    st.title('Choose your Filters')
    
    st.subheader('Select Retailers')
    retailers=sorted(data['Retailer'].dropna().unique())
    selected_retailers=st.multiselect('Retailers',retailers)
    
    st.subheader("Select year")
    years=sorted(data['Year'].dropna().astype(int).unique().tolist())
    selected_years=st.multiselect("Pick your Year(s)",years)
    
    st.subheader("Follow Mk Singh")
    st.markdown("[LinkedIn](http://www.linkedin.com/in/motilal-das-42b4a9254)")
    st.markdown("[GitHub](https://github.com/MkSingh431)")

filtered_data=data.copy()
if selected_retailers:
    filtered_data=filtered_data[filtered_data['Retailer'].isin(selected_retailers)]
if selected_years:
    filtered_data=filtered_data[filtered_data['Year'].isin(selected_years)]

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    with st.container(border=True):
        # 1. Configuration
        # Matching your sidebar 'darkGoldenrod' (#F18C10) and a deep 'Navy Blue' (#0047AB)
        label_color = "#F18C10" 
        value_color = "#0047AB"
        
        # 2. Calculation
        # Ensure the column name matches your CSV exactly
        total_sales_value = filtered_data['TotalSales'].sum()
        
        label_color="#F18C10"
        value_color="#0047AB"
        html_metrics = f"""
        <div>
        <p style="color:{label_color}; font-size: 25px; margin: 0;">Total Sales</p>
        <h style="color:{value_color}; font-size: 20px; margin: 0;">${total_sales_value:,.2f}</h>
        </div>
        """
        st.markdown(html_metrics, unsafe_allow_html=True)
        

with col2:
    with st.container(border=True):
        filtered_data['OperatingProfit'].sum()
        label_color="#F18C10"
        value_color="#0047AB"
        html_metrics=f"""
        <div>
        <p style="color: {label_color}; font-size: 25px; margin: 0;">Total Profit</p>
        <h style="color: {value_color}; font-size: 20px; margin: 0;">${filtered_data['OperatingProfit'].sum():,.2f}</h>
        </div>
        """
        st.markdown(html_metrics, unsafe_allow_html=True)
        
with col3:
    with st.container(border=True):
        total_qty=filtered_data['UnitsSold'].sum()
        label_color="#F18C10"
        value_color="#0047AB"
        html_metrics=f"""
        <div>
        <p style="color: {label_color}; font-size: 25px; margin: 0;">Total Quantity</p>
        <h style="color: {value_color}; font-size: 20px; margin: 0;">{total_qty:,.2f}</h>
        </div>
        """
        st.markdown(html_metrics, unsafe_allow_html=True)
        
with col4:
    with st.container(border=True):
        total_cost=filtered_data['TotalSales']-filtered_data['OperatingProfit']
        label_color="#F18C10"
        value_color="#0047AB"
        html_metrics=f"""
        <div>
        <p style="color: {label_color}; font-size: 25px; margin: 0;">Total Cost</p>
        <h style="color: {value_color}; font-size: 20px; margin: 0;">${total_cost.sum():,.2f}</h>
        </div>
        """
        st.markdown(html_metrics, unsafe_allow_html=True)

with col5:
    with st.container(border=True):
        total_retail=filtered_data['RetailerID'].unique()
        label_color="#F18C10"
        value_color="#0047AB"
        html_metrics=f"""   
        <div>
        <p style="color: {label_color}; font-size: 25px; margin: 0;">Total Retail</p>
        <h style="color: {value_color}; font-size: 20px; margin: 0;">{len(total_retail):,.2f}</h>
        </div>
        """
        st.markdown(html_metrics, unsafe_allow_html=True)

st.divider()


chart1, chart2 = st.columns(2)

with chart1:
    st.markdown("### Total Sales by Retailer")
    
    sales_by_retailer=data.groupby('Retailer')['TotalSales'].sum().sort_values(ascending=False)
    
    fig ,ax =plt.subplots(figsize=(6,4))
    
    barh=ax.bar(
        sales_by_retailer.index,
        sales_by_retailer.values,
        color=['#F18C10','#0047AB','#FF5733','#33FF55','#8A2BE2',"#5545FF"],
        width=0.6
    )
    
    plt.xticks(fontsize=12,color="#2982EE",rotation=45,ha='right')
    plt.yticks(fontsize=12,color="#318DF7")
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_visible(False)
    
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    plt.tight_layout()
    
    st.pyplot(fig)

with chart2:
    st.markdown("### Total Profit by Retailer")
    
    profit_by_retailer=data.groupby('Retailer')['OperatingProfit'].sum().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(6, 4))
    
    barh=ax.bar(
        profit_by_retailer.index,
        profit_by_retailer.values,
        color=['#F18C10','#0047AB','#FF5733','#33FF54','#8A2BE2','#5545FF'],
        width=0.6
    )
    
    plt.xticks(fontsize=12,color="#2982EE",rotation=45,ha='right')
    plt.yticks(fontsize=12,color="#318DF7")
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_visible(False)
    
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    plt.tight_layout()
    
    st.pyplot(fig)
    
view1, view2 = st.columns(2)

with view1:
    with st.expander("Sales by Retailer"):
        sales_by_retailer=data.groupby('Retailer')['TotalSales'].sum().reset_index()
        
        style_df=sales_by_retailer.style.background_gradient(cmap='Greens',subset=['TotalSales']).format({'TotalSales':'${:,.2f}'})
        
        st.dataframe(style_df, width='stretch')
        
with view2:
    with st.expander("Profit by Retailer"):
        profit_by_retailer=data.groupby('Retailer')['OperatingProfit'].sum().reset_index()
        
        style_df=profit_by_retailer.style.background_gradient(cmap='Greens',subset=['OperatingProfit']).format({'OperatingProfit':'${:,.2f}'})
        
        st.dataframe(style_df, width='stretch')
        
st.divider()

chart3, chart4 = st.columns(2)

with chart3:
    st.markdown("### Total Sales by Region")
    
    sales_by_region=data.groupby('Region')['TotalSales'].sum().sort_values(ascending=False)
     
    fig, ax = plt.subplots(figsize=(6, 4))
    
    colors=['#F18C10','#0047AB','#FF5733','#33FF55','#8A2BE4']
    
    wedges, texts, autotexts = ax.pie(
        sales_by_region.values,
        labels=sales_by_region.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        pctdistance=0.85,
        textprops={'color':"w", 'weight':'bold'}
    )
    
    centre_circle=plt.Circle((0,0),0.70,fc='none',edgecolor='none')
    fig.gca().add_artist(centre_circle)
    
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    plt.tight_layout()
    
    st.pyplot(fig)

with chart4:
    st.markdown("### Sales Method Performance ")
    
    salesmethod=data.groupby('SalesMethod')['TotalSales'].sum().sort_values(ascending=False)
    
    fig, ax =plt.subplots(figsize=(5,4))
    
    barhs=ax.bar(
        salesmethod.index,
        salesmethod.values,
        color=["#21ED43","#D5DF14","#C60303"],
        width=0.6
    )
    
    plt.xticks(fontsize=12, color='#2586EE',rotation=45,ha='right')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_visible(False)
    
    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    plt.tight_layout()
    
    st.pyplot(fig)

view3, view4=st.columns(2)

# 1. Create the Expander
with view3:
    # 1. Logic Check: Aggregation
    # Ensure you use 'filtered_data' if you have filters in your sidebar
    regional_table = (
        filtered_data.groupby('Region')['TotalSales']
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    
    # Calculating the Market Share %
    total_rev = regional_table['TotalSales'].sum()
    regional_table['Market Share'] = (regional_table['TotalSales'] / total_rev) * 100

    # 2. The Expander Container
    with st.expander("📊 Detailed Regional Sales & Market Share"):
        
        # 3. Download Logic (The 'Exportable Truth')
        csv = regional_table.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Regional Data as CSV",
            data=csv,
            file_name='regional_sales.csv',
            mime='text/csv',
        )

        # 4. Interactive Dataframe with Column Styling
        st.dataframe(
            regional_table,
            column_config={
                "Region": "Sales Region",
                "TotalSales": st.column_config.NumberColumn(
                    "Total Revenue ($)",
                    format="$%1.2f",
                    # Adding a background color 'heatmap' based on value
                    help="Total revenue generated per region"
                ),
                "Market Share": st.column_config.ProgressColumn(
                    "Market Share (%)",
                    format="%1.1f%%",
                    min_value=0,
                    max_value=100,
                    # Matches your 'Forest Green' and 'Gold' theme
                    color="green" 
                )
            },
            hide_index=True,
            width='stretch'
        )
        
        
with view4:
    with st.expander("Sales by Sales Method"):
        salesmethod=data.groupby('SalesMethod')['TotalSales'].sum().sort_values(ascending=False).reset_index()
        
        style_df=salesmethod.style.background_gradient(cmap="BuGn_r", subset=['TotalSales']).format({'TotalSales':'${:,.2f}'})
        
        st.dataframe(style_df, width='stretch')
  
st.divider()
chart5=st.columns(1)[0]

with chart5:
    st.markdown("### Total Sales Profile by State")
    
    # 1. Data Aggregation
    # We group by State and sum the TotalSales
    state_sales = (
        data.groupby('State')['TotalSales']
        .sum()
        .reset_index()
        .sort_values(by='State') # Alphabetical order for the x-axis
    )
    
    # 2. Creating the Line Chart
    fig = px.line(
        state_sales, 
        x='State', 
        y='TotalSales', 
        markers=True,
        title="Revenue Distribution Across States"
    )
    
    # 3. Styling: Forest Green Line with Gold Markers
    fig.update_traces(
        line=dict(color='#228B22', width=3),
        marker=dict(color='#DAA520', size=8, symbol='diamond'),
        hovertemplate="<b>%{x}</b><br>Total Sales: $%{y:,.2f}<extra></extra>"
    )
    
    # 4. Dashboard Theming
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="white",
        xaxis=dict(showgrid=False, tickangle=45),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
        margin=dict(l=20, r=20, t=50, b=50)
    )
    
    st.plotly_chart(fig, width='stretch')
    
view5=st.columns(1)[0]
with view5:
    with st.expander("State by Sales"):
        
        state_sales=data.groupby('State')['TotalSales'].sum().reset_index().sort_values(by='State') 
    
        style_df=state_sales.style.background_gradient(cmap='BuGn_r', subset=['TotalSales']).format({'TotalSales':'${:,.2f}'})
    
        st.dataframe(style_df, width='stretch')       

             
    
  
          
                   

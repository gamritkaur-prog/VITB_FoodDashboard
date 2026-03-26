# Learn Streamlit - 50%
# Build Real Word Business Inteligence Dashboard

# Step 0: Install and Import all the necessary libaries
import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Step 1: Layer 1: Load Data and Display (Optional)")
# This step bring "data to USer Interface"
# Two Options : Using FileUpload or using read_csv

#Run the code and share screenshot
#Way 1
#df=pd.read_csv("food_order.csv")
#st.success("Data Loaded Successful")


#Way 2
#uplaod the file
st.info("The File Type is CSV only")
uploaded_file=st.file_uploader("Upload your CSV File",type=["csv"])

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.success("File Uploaded Successfully")

else:
    st.warning("Please Upload Your CSV File")



# Dashboard for DEcision MAking 
st.header("Step 2: Layer 2: Key Performance Indicators ")
# Assume u r Manager at Online Food Ordering Business. What KPIs u want to see
# total order, How busy is the business (Demand)
#- decision: if it is low- we need marketing 
# total revenue, How much money we are making 
# avg rating, Are my customers happy ? 
  # decision: Improve restutant quality, fix customer complaints / service
# average delivery time, How fast we are delivering 
 # If not deliver in 30 mins, pizza is free

# total customer
# total cities
# max Order Amount
# min Order Amt - is it adding any value while making decision . If Ans is Yes. Add as KPI

# To Create KPIs - 
# We need st.metrics
# to organize KPIs we need st.columns
# to make it more beautiful (optional)- HTML code as KPI_CARD

col1,col2,col3,col4=st.columns(4)

total_orders=df["Customer"].nunique()
total_revenue=df["Amount"].sum()  
avg_rating=df["Rating"].mean()
avg_delivery_time=df["Delivery_Time"].mean()

col1,col2,col3,col4=st.columns(4)
with col1:
    st.metric("Total Orders",total_orders)  
with col2:
    st.metric("Total Revenue in Rs.",total_revenue)
with col3:
    st.metric("Average Rating",avg_rating)
with col4:
    st.metric("Average Delivery Time",avg_delivery_time)

# Step 3: LAyer 3: Adding Filters and Drill Downs 
# City 
# Order Amount
# Food 
# choice 
# HAve it as a Sidebar (NAvigation BAr)
# Have it as column in main body of page 
# have it above KPIs also 

st.sidebar.title("Filters")

#creating filters
city_options = ["All"] + df['City'].unique().tolist()
selected_city = st.sidebar.selectbox("Select City", city_options)
 
food_options = ["All"] + df['Food'].unique().tolist()
selected_food = st.sidebar.selectbox("Select Food", food_options)
 
order_options = ["All"] + df['Order_Type'].unique().tolist()
selected_order = st.sidebar.selectbox("Select Order Type", order_options)

min_amount = int(df['Amount'].min())
max_amount = int(df['Amount'].max())
selected_amount = st.sidebar.slider(
    "Select Amount Range",
    min_value=min_amount,
    max_value=max_amount,
    value=(min_amount, max_amount)
)

# filtering the data based on user selection or input
df_filtered = df.copy()
if selected_city != "All":
    df_filtered = df_filtered[df_filtered['City'] == selected_city]
if selected_food != "All":
    df_filtered = df_filtered[df_filtered['Food'] == selected_food]
if selected_order != "All":
    df_filtered = df_filtered[df_filtered['Order_Type'] == selected_order]
 
df_filtered = df_filtered[
    (df_filtered['Amount'] >= selected_amount[0]) &
    (df_filtered['Amount'] <= selected_amount[1])
]

# Step 4: BAsed on Filters we Add data and charts in short insights
# components - Multiple components data , charts, insights etc
# Add Tabs

tab1,tab2,tab3,tab4=st.tabs(["Data","Insights as Charts","Key Insights","AI Insights and Recommendations"])
with tab1:
        st.dataframe(df_filtered)
        # Optional - You Show Summary Statistics using Checkbox or expander
        with st.expander("Show Summary Statistcs"):
            st.write(df.describe())
with tab2:
    st.write("some charts")
    # Revenue By City
    # Orders by food
    #- Use Plotly
    st.header("Revenue By City")
    rev_city=df_filtered.groupby("City")["Amount"].sum().reset_index()
    fig1=px.bar(rev_city, x="City", y="Amount",color="City")
    st.plotly_chart(fig1)

      # Orders by Food
    fig = px.pie(
            df_filtered,
            names='Food',
            height=300
        )
    st.plotly_chart(fig, use_container_width=True)
 
with tab3:
    st.write("AI Recommendations")





# Step 5: Deploy 
# Step 6: Some Add some insights from AI

#SDL 
# Title to This Dashboard
# Add More meaningful graphs
# Add some icons 
# Customize ur KPIs also


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    return df

diagram_types = {"bar": st.bar_chart, "line": st.line_chart, "scatter": st.scatter_chart}

st.title("Diamond data analyzer")

file = st.file_uploader(label="Select a csv-file", accept_multiple_files=False, type="csv" )

if file:
    df = load_data(file)
    st.dataframe(df)


    st.subheader("Numeric correation to price")
    selected_columns = ['carat', 'depth', 'table', 'x', 'y', 'z', 'price']
    df_selected =df[selected_columns]
    correaltion = df_selected.corr()
    sorted = correaltion['price'].drop('price').sort_values(ascending=False)
    st.write(sorted)

    st.subheader("Medianprice for each category")
    fig, ax = plt.subplots()

    x_select = st.selectbox("Please choose your category; ",['carat', 'color', 'cut', 'clarity'] )

    if x_select == "carat":
        median_price = df.groupby('carat')['price'].median().reindex([0.05, 0.10, 0.20, 0.25, 0.30, 0.40, 0.50, 0.70, 0.90, 1.00, 1.25, 1.50, 1.75, 2.00, 2.50, 2.75 ,3.00, 4.00, 5.00])
        ax.bar(median_price.index, median_price.values)
        ax.set_xlabel("carat")
        st.pyplot(fig)
    elif x_select == "color":
        median_price = df.groupby('color')['price'].median().reindex(['J', 'I', 'H', 'G', 'F', 'E', 'D'])
        ax.bar(median_price.index, median_price.values, color=['green'])
        ax.set_xlabel("color")
        st.pyplot(fig)
    elif x_select == "cut":
        median_price = df.groupby('cut')['price'].median().reindex(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
        ax.bar(median_price.index, median_price.values, color=['purple'])
        ax.set_xlabel("cut")
        st.pyplot(fig)
    elif x_select == "clarity":
        median_price = df.groupby('clarity')['price'].median().reindex(['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
        ax.bar(median_price.index, median_price.values, color=['brown'])
        ax.set_xlabel("cut")
        st.pyplot(fig)


    st.subheader("Medianprice for each category (carat : 0.29-0.31)")
    same_values = df[(df['carat'] >= 0.29) & (df['carat'] <= 0.31)]
    fig2, ax = plt.subplots()

    x_select = st.selectbox("Please choose your category; ",['color', 'cut', 'clarity'] )

    if x_select == "color":
        median_price = same_values.groupby('color')['price'].median().reindex(['J', 'I', 'H', 'G', 'F', 'E', 'D'])
        ax.plot(median_price.index, median_price.values, marker ='o', color='green')
        ax.set_xlabel("color")
        st.pyplot(fig2)
    elif x_select == "cut":
        median_price = same_values.groupby('cut')['price'].median().reindex(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
        plt.plot(median_price.index, median_price.values, marker ='o', color='purple')
        ax.set_xlabel("cut")
        st.pyplot(fig2)
    elif x_select == "clarity":
        mean_price = same_values.groupby('clarity')['price'].median().reindex(['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
        plt.plot(mean_price.index, mean_price.values, marker ='o', color='brown')
        ax.set_xlabel("clarity")
        st.pyplot(fig2)
    
    st.subheader("Medianprice for each category (carat : 0.29-0.31 and clarity : VS2)")
    same_values = df[(df['carat'] >= 0.29) & (df['carat'] <= 0.31) & (df['clarity'] == 'VS2')]
    fig3, ax = plt.subplots()

    x_select = st.selectbox("Please choose your category; ",['color', 'cut'] )

    if x_select == "color":
        median_price = same_values.groupby('color')['price'].median().reindex(['J', 'I', 'H', 'G', 'F', 'E', 'D'])
        ax.plot(median_price.index, median_price.values, marker ='o', color='green')
        ax.set_xlabel("color")
        st.pyplot(fig3)
    elif x_select == "cut":
        median_price = same_values.groupby('cut')['price'].median().reindex(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
        ax.plot(median_price.index, median_price.values, marker ='o', color='purple')
        ax.set_xlabel("cut")
        st.pyplot(fig3)

    st.subheader("Medianprice for each category (Carat : 0.29-0.31 and Clarity : VS2 and Color: E)")
    same_values = df[(df['carat'] >= 0.29) & (df['carat'] <= 0.31) & (df['clarity'] == 'VS2') & (df['color'] == 'E')]
    fig4, ax = plt.subplots()

    x_select = st.selectbox("Please choose your category; ",['cut'] )

    if x_select == "cut":
        median_price = same_values.groupby('cut')['price'].median().reindex(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
        ax.plot(median_price.index, median_price.values, marker ='o', color='purple')
        ax.set_xlabel("cut")
        st.pyplot(fig4)



    




    



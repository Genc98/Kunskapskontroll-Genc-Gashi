import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    return df

diagram_types = {"bar": st.bar_chart, "line": st.line_chart, "scatter": st.scatter_chart}

st.title("Diamant data analys")

st.write("Guldfynd är en butik som säljer smycken och accessoarer innehållande guld och silver. Nu har de möjlighet att utöka sitt sortiment med produkter som även innehåller diamanter. För att fatta ett beslut har de tillgång till ett dataset med information om alla diamanter. Guldfynd har anlitat mig för att analysera datan åt dem med hjälp av Python. Jag kommer att undersöka om datan innehåller orimliga värden samt analysera vilka faktorer hos diamanten som påverkar priset mest. Målet med detta är att sedan ge mina insikter och rekommanadioner som kan stödja deras besult om att börja sälja produktet med diamanter.")

file = st.file_uploader(label="Select a csv-file", accept_multiple_files=False, type="csv" )



if file:
    df = load_data(file)
    st.dataframe(df)


    st.subheader("Numerisk korrelation till pris")
    st.write("Enligt tabellen har karat den högsta korrelationen med priset, medan depth har den svagaste.")
    selected_columns = ['carat', 'depth', 'table', 'x', 'y', 'z', 'price']
    df_selected =df[selected_columns]
    correaltion = df_selected.corr()
    sorted = correaltion['price'].drop('price').sort_values(ascending=False)
    st.write(sorted)

    st.subheader("Medianpris för varje kategori")
    st.write("Enligt diagrammen var det endast karat som visade ett tydligt mönster i diagrammen, ju högre karat desto högre pris, vilket är logiskt. Övriga diagram var missvisande, exempelvis hade en bättre klarhet ett lägre medianpris än den sämsta. Detta tyder på att karaten har en starkare påverkan på priset än de andra kategoriska faktorerna.")

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


    st.subheader("Medianpris för varje kategori med samma karatvärde (karat : 0.29-0.31)")
    st.write("Enligt diagrammen var det klarheten som visade ett tydligt mönster i diagrammen, ju högre clarity desto högre pris. Övriga diagram hade inte lika tydliga samband jämfört med klarheten. Detta tyder på att klarheten har en starkare påverkan på priset än de övriga kategoriska faktorerna.")

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
    
    st.subheader("Medianpris för varje kategori med samma karatvärde och klarhet (karat: 0.29-0.31 and klarhet: VS2)")
    st.write("Enligt diagrammen var det färgen som visade nu ett tydligt mönster i diagrammen, ju bättre color desto högre pris. Slipnings-diagrammet hade inte lika tydliga samband jämfört med färg-diagrammet. Detta tyder på att färgen har en starkare påverkan på priset än slipningen")
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

    st.subheader("Medianpris för varje kategori med samma karatvärde, klarhet och färg(karat : 0.29-0.31 and klarhet: VS2 and färg: E)")
    st.write("När allt var filtrerad till gemensamma värden visade diagrammet för slipning ett mer rimligt och tydlig samband.")
    same_values = df[(df['carat'] >= 0.29) & (df['carat'] <= 0.31) & (df['clarity'] == 'VS2') & (df['color'] == 'E')]
    fig4, ax = plt.subplots()

    x_select = st.selectbox("Please choose your category; ",['cut'] )

    if x_select == "cut":
        median_price = same_values.groupby('cut')['price'].median().reindex(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
        ax.plot(median_price.index, median_price.values, marker ='o', color='purple')
        ax.set_xlabel("cut")
        st.pyplot(fig4)

    
    st.title("Avslut och rekommandationer")
    st.write(" Det som hade störst påverkan är karat. Ju högre karat desto dyrare diamant. Även diamantens dimensioner (x,y och z) påverkade priset medan depth och table hade svagare inverkan. Bland de kategoriska värden visade analysen att klarheten hade störst påverkan på priset medan slipningen hade oväntad låg påverkan. Mina rekommandtioner är att Guldfynd fokuserar erbjuda diamantsmycken med högre karat och god klarhet, eftersom de hade större påverkan på priset.")



    




    



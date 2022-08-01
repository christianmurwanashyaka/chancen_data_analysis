
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import  st_lottie
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Chancen International Rwanda', page_icon=":tada:")

selected = option_menu(
    menu_title="Chancen International Rwanda", # required
    options=['Home', 'Case Study', "Contact"],
    icons = ['house','book','envelope'],
    menu_icon = 'cast',
    default_index = 0,
    orientation = 'horizontal',
    styles={
        "container": {"padding":"0!important", "background-color":"write",},
        "icon":{"color":"orange","font-size":"25px"},
        "nav-link":{
            "font-size":"25px",
            "text-align":"left",
            "margin":"0px",
            "--hover-color":"#eee",
            },
        "nav-link-selected":{"background-color":"green"},
            
            },
    
)  
if selected =="Home":

# ---- HEAD SECTION ----

    with st.container():
        #st.subheader('Hi, I am Christian MURWANASHYAKA :wave:')
        #st.subheader('Looking for Data Analyst Position in your organization below :point_down:')
        random_url = "https://chancen.international/wp-content/uploads/2022/03/chancen-logo-2.png"
        st.image(random_url, use_column_width='always')

if selected =="Case Study":
    st.title("Data Analysis and Visualization")
    with st.container():
        st.write("_____________")
    
        left_column, right_column =st.columns(2)
        with left_column:
            def load_lottieurl(url):
                r=requests.get(url)
                if r.status_code != 200:
                 return None
                return r.json()
#------- Load Assets -----------
            # lottie_data_analysis = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_nc0px8fd.json")
            st.header("Case Study:")
            st.write('##')
            st.write(""" Our repayments team has requested an understanding and presentation of this data sample. 
                        Your task is to analyze the data sample and provide insights for the repayment team. The repayment team like for their insights to be visualised. Analyse and provide insights for the Repayments team based on this data sample. 
                        Based on your findings create:
                        1. A presentation showing your approach and initial findings.
                        2. A virtualization of the data that could be used by the team to view this data every month (dashboard visualisation)""")

        # with right_column:
            # st_lottie(lottie_data_analysis, height=300, key= "data-analytics")
        with st.container():
            data1 = pd.read_excel('Data.xlsx', sheet_name='CONTRACT Object(CIR)')
            data2 = pd.read_excel('Data.xlsx', sheet_name='CONTRACT Object(FWF)')
            data3 = pd.read_excel('Data.xlsx', sheet_name='Contact Object (FWF)')
            data4 = pd.read_excel('Data.xlsx', sheet_name='Contact Object (CIR)')
            
            st.sidebar.header("Please Filter Here:")

            contract_selected = st.sidebar.multiselect(
                    'Select the type of Contract',
                    options = ['FWF', 'CIR'],
                    default = ['FWF', 'CIR']
                )

            gender_selected = st.sidebar.multiselect(
                    'Select Gender',
                    options = ['Male', 'Female'],
                    default = ['Male', 'Female']
                )


            data3 = data3[data3['Gender'].isin(gender_selected)]
            data4 = data4[data4['Gender'].isin(gender_selected)]

            # showing data statistics of fwf and cir in piechart
            # unique values
            ISA_Status_FWF =list(data3['ISA Status'].value_counts().items()) 
            ISA_Status_CIR =list(data4['ISA Status'].value_counts().items())

            emps1=list(data1['Are you employed'].value_counts().items())
            emps2=list(data2['Are you employed'].value_counts().items())

            risk1=list(data1['Risk classification'].value_counts().items())
            risk2 = list(data2['Risk classification'].value_counts().items())
        
            if 'FWF' in contract_selected:
                st.markdown("""---""")

                st.subheader('This is the data from "CONTRACT Object(FWF)" ')
                cir_selected = st.multiselect('Select ISA STATUS for FWF',
                            options = data3['ISA Status'].unique(),
                            default = data3['ISA Status'].unique()
                    )
                st.dataframe(data3[data3['ISA Status'].isin(cir_selected) & data3['Gender'].isin(gender_selected)])


                # fwf pie chart about isa status and dataframe
                status =np.array([x[0] for x in ISA_Status_FWF])
                number =np.array([x[1] for x in ISA_Status_FWF])
                
                fig = go.Figure(
                        go.Pie(
                            labels = status,
                            values = number,
                            hoverinfo = 'label+percent',
                            textinfo = 'value')
                    )
                st.subheader('Visualization ISA status for FWF Contact')
                st.plotly_chart(fig)

                # employment status

                status =np.array([emps1[0][0],emps1[1][0]])
                number =np.array([emps1[0][1],emps1[1][1]+emps1[2][1]])

                fig = go.Figure(
                        go.Pie(
                            labels = status,
                            values = number,
                            hoverinfo = 'label+percent',
                            textinfo = 'value')
                    )
                st.subheader('Visualization of Employment Status for FWF Contact')
                st.plotly_chart(fig)

                # risk classification

                status =np.array([x[0] for x in risk2])
                number =np.array([x[1] for x in risk2])

                fig = go.Figure(
                        go.Pie(
                            labels = status,
                            values = number,
                            hoverinfo = 'label+percent',
                            textinfo = 'value')
                    )
                st.subheader('Visualization of risk classification for FWF Contact')
                st.plotly_chart(fig)

# 
# 
# 
# 
# 
            if 'CIR' in contract_selected:
                st.markdown("""---""")

                # cir pie chart about isa status and dataframe

                st.write('This is the data from "CONTRACT Object(CIR)" ')
                fwf_selected = st.multiselect('Select ISA STATUS for CIR',
                            options = data4['ISA Status'].unique(),
                            default = data4['ISA Status'].unique()
                    )
                st.write(data4[data4['ISA Status'].isin(fwf_selected) & data4['Gender'].isin(gender_selected)])

                status =np.array([x[0] for x in ISA_Status_CIR])
                number =np.array([x[1] for x in ISA_Status_CIR])
                
                fig = go.Figure(
                        go.Pie(
                            labels = status,
                            values = number,
                            hoverinfo = 'label+percent',
                            textinfo = 'value')
                    )
                st.subheader('Visualization ISA status for CIR Contact')
                st.plotly_chart(fig)

                # employment status

                emps1=list(data1['Are you employed'].value_counts().items())
                emps2=list(data2['Are you employed'].value_counts().items())
                

                status =np.array([x[0] for x in emps2])
                number =np.array([x[1] for x in emps2])

                fig = go.Figure(
                        go.Pie(
                            labels = status,
                            values = number,
                            hoverinfo = 'label+percent',
                            textinfo = 'value')
                    )
                st.subheader('Visualization of Employment Status for CIR Contact')
                st.plotly_chart(fig)

                # risk classification
                risk1=list(data1['Risk classification'].value_counts().items())
                risk2 = list(data2['Risk classification'].value_counts().items())

                status =np.array([x[0] for x in risk1])
                number =np.array([x[1] for x in risk1])

                fig = go.Figure(
                        go.Pie(
                            labels = status,
                            values = number,
                            hoverinfo = 'label+percent',
                            textinfo = 'value')
                    )
                st.subheader('Visualization of risk classification for CIR Contact')
                st.plotly_chart(fig)


if selected =="Contact":
    st.title(f"{selected}")    
        ## ---- Data Loading ---- ##
        ## ---- Description ---- ###

    



#st.subheader(')
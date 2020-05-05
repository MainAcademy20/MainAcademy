import urllib.request
import datetime
import pandas as pd
import streamlit as st
import plotly_express as px
import os
import time


url = "https://docs.google.com/spreadsheets/d/e/key/pub?output=xlsx"
datafeed = urllib.request.urlopen(url).read()
filename = 'datafeeds' + datetime.datetime.now().strftime('%Y-%m-%d') + '.xlsx'
f = open(filename, "wb")
f.write(datafeed)
f.close()

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Loading {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)


@st.cache
def datafeeds(sheet_name):
    data = pd.read_excel(open(filename, 'rb'), sheet_name)
    return data


data = datafeeds(sheet_name='prosale-data')
data_crm = datafeeds(sheet_name='crm-datafeed')


def main():
    st.sidebar.title('My Stat')

    list_type = st.sidebar.radio(
        "Select Stat type:",
        options=[
            'Stat by unit',
            'Individual stat'

        ],
    )

    if list_type == 'Stat by unit':
        stat_by_unit()
    else:
        individual_stat()


@st.cache
def sum_column(column, b_data):
    sum_col = b_data[column].sum()
    return sum_col


def individual_stat():
    ind_list_type = st.sidebar.radio(
        "Select option:",
        options=[
            'prosale_status',
            'prosale_level',
            'retention_group',
            'product_segment',

        ],
    )
    manager = st.multiselect('Manager?', data['manager_name'].unique())
    m_data = data[(data['manager_name'].isin(manager))]

    st.dataframe({
        'CPA текущий месяц': [sum_column(column='expense_cpa_this', b_data=m_data)],
        'CPA прошлый месяц': [sum_column(column='expense_cpa_prev', b_data=m_data)],
        'CPC текущий месяц': [sum_column(column='expense_cpc_this', b_data=m_data)],
        'CPC прошлый месяц': [sum_column(column='expense_cpc_prev', b_data=m_data)]
    })

    def count_sample(column):
        status = st.multiselect(column, data[column].unique())
        new_df = data[(data[column].isin(status)) & (data['manager_name'].isin(manager))]

        sample = new_df[column].value_counts()
        return sample

    if ind_list_type == 'prosale_status':
        st.write(count_sample(column='prosale_status'))
    elif ind_list_type == 'prosale_level':
        st.write(count_sample(column='prosale_level_this'))
    elif ind_list_type == 'retention_group':
        st.write(count_sample(column='retention_group'))
    else:
        st.write(count_sample(column='product_segment'))


def stat_by_unit():
    st.subheader('Общие показатели по базе:')
    st.text('Открутка:')
    st.dataframe({
        'CPA текущий месяц': [sum_column(column='expense_cpa_this', b_data=data)],
        'CPA прошлый месяц': [sum_column(column='expense_cpa_prev', b_data=data)],
        'CPC текущий месяц': [sum_column(column='expense_cpc_this', b_data=data)],
        'CPC прошлый месяц': [sum_column(column='expense_cpc_prev', b_data=data)]
    })

    directory = '/users/natali/pycharmprojects/dspro'
    files = os.listdir(directory)

    tab = filter(lambda w: w.endswith('.xlsx'), files)
    x = []
    y = []

    for fs in tab:
        def feeds(sheet_name):
            data_d = pd.read_excel(open(fs, 'rb'), sheet_name)
            return data_d

        data_bd = feeds(sheet_name='prosale-data')
        x.append(fs[9:19])
        y.append(data_bd['expense_cpa_this'].sum())
    fig = px.line(data, x=x, y=y)
    st.plotly_chart(fig)

    st.text('Сертификация:')
    certified = data_crm['certified'].value_counts()
    st.write(certified)

    r_group = data['retention_group'].value_counts()
    p_status = data['prosale_status'].value_counts()
    st.write(p_status)

    df_p = px.data.tips()
    n_s = ['active', 'not_active', 'dead', 'never_active', 'churned', 'not_client']
    fig = px.pie(df_p, values=p_status, names=n_s, width=800, height=300)
    st.plotly_chart(fig)
    st.write(r_group)
    df_p = px.data.tips()
    n_g = ['low', 'mid_low', 'mid_top', 'mid', 'top']
    fig_g = px.pie(df_p, values=r_group, names=n_g, width=800, height=300)
    st.plotly_chart(fig_g)


main()

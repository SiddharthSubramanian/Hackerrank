def money_flow_index(data, periods):
    data = pd.DataFrame(data)
    remove_tp_col = False
    typical_price = (data.High + data.Low + data.Close) / 3
    df['Typical price'] = (data.High + data.Low + data.Close) / 3
    data['money_flow'] = data['typical_price'] * data.Volume
    data['money_ratio'] = 0.
    data['Money Flow Index'] = 0.
    data['Positive Money Flow'] = 0.
    data['Negative Money Flow'] = 0.
    data['Positive Money Flow Sum'] = 0
    data['Negative Money Flow Sum'] = 0
    for index,row in data.iterrows():
        if index > 0:
            if row['typical_price'] < data.at[index-1, 'typical_price']:
                data.set_value(index, 'Negative Money Flow', row['money_flow'])
            else:
                data.set_value(index, 'Positive Money Flow', row['money_flow'])

        if index >= periods:
            negative_sum = data['Positive Money Flow'][index-periods:index].sum()
            positive_sum = data['Negative Money Flow'][index-periods:index].sum()


            if negative_sum == 0.:

                negative_sum = 0.00001 # divide by 0
            m_r = positive_sum / negative_sum
            mfi = 100 * m_r / (1+m_r)
            data.set_value(index,'Positive Money Flow Sum', positive_sum)
            data.set_value(index,'Negative Money Flow Sum', negative_sum)
            data.set_value(index, 'Money Flow Index', mfi)
            data.drop('money_flow',axis = 1)
      data.to_csv('money_flow_index'+str(periods),header=True,index=False)

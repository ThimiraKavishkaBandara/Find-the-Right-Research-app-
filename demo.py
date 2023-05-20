
import dash
from dash import Dash, html, dcc, Output, Input, dash_table, State
import plotly.graph_objs as go
from neo4j import GraphDatabase
import pymysql
#import dash_html_components as html
from dash import html
from dash.exceptions import PreventUpdate
#import dash_core_components as dcc
from dash import dcc
import plotly.express as px
from neo4j_utils import widget_1_query
from mongo_utils import widget_2_query
from mysql_utils import add_university,delete_university
from mysql_utils import widget_4_query
from mysql_utils import widget_5_query
from mysql_utils import widget_6_query
from mysql_utils import add_faculty
from mysql_utils import remove_faculty


app = Dash(__name__, assets_folder='assets')

app.layout = html.Div([
    html.H1(children='Find the right Program with a Keyword', style={'textAlign':'center'}),
    
    html.Div([
        # Widget 1
        html.Div([
            html.H3('Top Keywords'),
            html.Div([
                dcc.Input(id='university_input2', placeholder='Enter a university'),
                html.Button('Search', id='search_button2')
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),
            html.Div(id='search_results_box2', style={'border': '1px solid black', 'padding': '10px', 'background-color':'#FFE8F2'})
        ], style={'border': '4px solid black', 'padding': '20px', 'width': '33%','background-color':'#ECD4DE'}),

        # Widget 2
        html.Div([
            html.H3('Top Faculty Member'),
            html.Div([
                dcc.Input(id='university_input', placeholder='Enter a university'),
                dcc.Input(id='keyword_input', placeholder='Enter a keyword'),
                html.Button('Search', id='search_button')
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),
            html.Div(id='search_results_box', style={'border': '1px solid black', 'padding': '10px','background-color':'#FFE8F2 ' })
        ], style={'border': '4px solid black', 'padding': '20px', 'width': '33%','background-color':'#ECD4DE' }),

        # Widget 3
        html.Div([
            html.H3('Saved Universities'),
            html.Div([
                dcc.Input(id='university_input3', placeholder='Enter a university'),
                html.Button('Save University', id='save_button')
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),
            html.Div([
                dcc.Input(id='university_input4', placeholder='Enter a university'),
                html.Button('Delete University', id='delete_button')
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),
            html.Div(id='delete_result'),
            html.Div(id='saved_universities_box', style={'border': '1px solid black', 'padding': '10px','overflow': 'hidden'}),
        ], style={'border': '4px solid black', 'padding': '20px', 'width': '33%','background-color':'#ECD4DE' }),

    ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '20px','overflow': 'hidden'}),


    html.Div([
        # Widget 4
        html.Div([
            html.H3('Publication'),
            html.Div([
                dcc.Input(id='input2', placeholder='Enter faculty member name'),
                html.Button('Search', id='button2')
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),
            html.Div(id='box2', style={'border': '1px solid black', 'padding': '10px'})
        ], style={'border': '4px solid black', 'padding': '20px', 'width': '33%', 'background-color':'#ECD4DE'}),


        # Widget 5
        html.Div([
            html.H3('Top Universities based on number publications by keyword'),
            html.Div([
                dcc.Input(id='input3', placeholder='Enter a keyword'),
                #dcc.Input(id='keyword_input', placeholder='Enter a keyword'),
                html.Button('Search', id='button3')
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),
            html.Div(id='box3', style={'border': '1px solid black', 'padding': '10px'})
        ], style={'border': '4px solid black', 'padding': '20px', 'width': '33%', 'background-color':'#ECD4DE'}),


        # Widget 6
        html.Div([
            html.H3('Saved Faculty member'),
            html.Div([
                dcc.Input(id='input6', placeholder='Enter a faculty member'),
                html.Button('Save faculty member', id='save_button2')
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),
            html.Div([
                dcc.Input(id='input66', placeholder='Enter a faculty member'),
                html.Button('Delete faculty member', id='del_button')
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),
            html.Div(id='result'), # added output div for delete callback,
            html.Div(id='box_2', style={'border': '1px solid black', 'padding': '10px'})
        ], style={'border': '4px solid black', 'padding': '20px', 'width': '33%','background-color':'#ECD4DE'}),

    ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '20px'}),
])



@app.callback(
    Output('search_results_box', 'children'),
    Input('search_button', 'n_clicks'),
    State('university_input', 'value'),
    State('keyword_input', 'value')
)
def widget_2(n_clicks, university, keyword):
    print(f"university: {university}, keyword: {keyword}") # add this line
    if not university or not keyword:
        return html.Div('Please enter a university and a keyword')
    
    result = widget_2_query(university, keyword)
    print(result)
    if result is None:
        return html.Div('No faculty found for this university')
    

    return html.Div([
    html.H4('Faculty Member'),
    html.Img(src=result['photo'], style={'width': '200px'}),
    html.P(f'Name: {result["name"]}'),
    html.P(f'Email: {result["email"]}'),
    html.P(f'Number: {result["phone"]}'),
    html.P(f'Position: {result["position"]}')
])

### widget 1 ###
@app.callback(
    Output('search_results_box2', 'children'),
    [Input('search_button2', 'n_clicks')],
    [State('university_input2', 'value')])
def update_search_results_box2(n_clicks, university):
    if university is None or university.strip() == '':
        return html.Div('Please enter a university to search for.')

    results = widget_1_query(university)
    if len(results) == 0:
        return html.Div('No results found.')

    keyword_list = [record['K.name'] for record in results]
    count_list = [record['count'] for record in results]

    fig = go.Figure(data=[go.Pie(labels=keyword_list, values=count_list, textinfo='value')])
    fig.update_layout(
        title={
            'text': f"Top Keywords for {university}",
            'font': {'size': 12}
        },
        margin=dict(l=0, r=0, t=30, b=0),
        height=400,
        width=400,
        plot_bgcolor='rgba(0,0,0,0)',   ## add this to gabins
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return dcc.Graph(figure=fig)


### widget 3 ####
saved_universities = []
@app.callback(
    [Output('delete_result', 'children'), Output('saved_universities_box', 'children')],
    [Input('save_button', 'n_clicks'), Input('delete_button', 'n_clicks')],
    [State('university_input3', 'value'), State('university_input4', 'value')]
)
def handle_university_actions(save_clicks, delete_clicks, save_value, delete_value):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    
    # Handle save action
    if 'save_button' in changed_id:
        if save_value:
            result = add_university(save_value)
            if result:
                saved_universities.append(result[0])
                return ["", ', '.join(saved_universities)]
            else:
                return ['University not found.', ""]
        else:
            return ['Please enter a university name.', ""]
    
    # Handle delete action
    elif 'delete_button' in changed_id:
        if delete_value:
            delete_university(delete_value)
            if delete_value in saved_universities:
                saved_universities.remove(delete_value)
                return ["The university has been deleted.", ', '.join(saved_universities)]
            else:
                return ["University not found in saved universities.", ', '.join(saved_universities)]
        else:
            return ['Please enter a university name.', ""]
    
    # Handle initial page load
    else:
        return ["", ', '.join(saved_universities)]

#widget4
# @app.callback(
#     Output('box2', 'children'),
#     [Input('button2', 'n_clicks')],
#     [State('input2', 'value')])
# def widget4(n_clicks, value):
#     if value is None or value.strip() == '':
#         return html.Div('Please enter a publication to search for.')
#     result=widget_4_query(value)
#     return dash_table.DataTable(data=result)

#widget4
@app.callback(
    Output('box2', 'children'),
    [Input('button2', 'n_clicks')],
    [State('input2', 'value')])
def widget4(n_clicks, value):
    if value is None or value.strip() == '':
        return html.Div('Please enter a faculty member to search for.')
    result = widget_4_query(value)
    return dcc.Dropdown(options=result,optionHeight=60)

#widget5
@app.callback(
    Output('box3', 'children'),
    Input('button3', 'n_clicks'),
    State('input3', 'value'),
   
)
def widget5(n_clicks, value):
   if value is None or value.strip() == '':
        return html.Div('Please enter a keyword to search for.')
   result=widget_5_query(value)
   fig = px.bar(result, x='university', y='count', barmode="group")
   fig.update_layout(
       plot_bgcolor='#F1D7E2',
       paper_bgcolor='#F1D7E2'
   )
   return dcc.Graph(figure=fig)
### widget 6 ####
faculty=[]

@app.callback(
    [Output('result', 'children'), Output('box_2', 'children')],
    [Input('save_button2', 'n_clicks'), Input('del_button', 'n_clicks')],
    [State('input6', 'value'), State('input66', 'value')]
)
def widget6(save_clicks, delete_clicks, save_value, delete_value):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    
    
    # Handle save action
    if 'save_button' in changed_id:
        if save_value in faculty:
            return  ["faculty member already saved", ', '.join(faculty)]
        if save_value:
            result = widget_6_query(save_value)

            if result:
                faculty.append(save_value)
                add_faculty(save_value)
                return ["", ', '.join(faculty)]
            else:
                return ['Faculty member not found',', '.join(faculty)]
        else:
            return ['Please enter a Faculty member',', '.join(faculty)]
    
    # Handle delete action
    elif 'del_button' in changed_id:
        
        if delete_value in faculty:
            faculty.remove(delete_value)
            remove_faculty(delete_value)
            return ["Faculty member has been deleted.", ', '.join(faculty)]
        else:
            return ["Faculty member not found .", ', '.join(faculty)]
        
    
    # Handle initial page load
    else:
        return ["", ', '.join(faculty)]

if __name__ == '__main__':
    app.run_server(debug=True)

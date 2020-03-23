import dash
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
from dash.dependencies import Input, Output,State
import plotly.offline as py
from plotly.graph_objs import *
import plotly.graph_objs as go 
import psycopg2 as psy
import os
import glob
import pandas as pd
import numpy as np
from datetime import datetime
import dash_bootstrap_components as dbc

now = datetime.now()

alo=dbc.themes.BOOTSTRAP

external_stylesheets = ['https://codepen.io/g4b1b13l/pen/VwwrYdL.css'] # Esse eh um site externo meu com um monte classe do css pronta,
																		# Copiei quase tudo do original que é um de chris num sei q la
																		#Criei um no meu nome so caso ele decida excluir ou algo do tipo eu n perder 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
server = app.server

app.title = 'Controle_Alcool_saida'





app.layout = html.Div([  


html.Div([

		html.Div(

	        [html.H1(children= 'Controle Álcool em gel'),

	       
	        ]
	              , 

	         style={
	        'font-size': '5pt',
	        #'height': '75px',
	        'margin': '-10px -10px -10px',
	        'background-color': '#ADD8E6',
	        'text-align': 'center',
	        #'border-radius': '2px',
	        #'display': 'flex',
	        #'margin-left': '0',
	        } 

	        ), 


html.Div([
	html.Div([
		html.Div(
	    [
	    	html.Label('Atualizar Giasa'),
	        dbc.Input(id="input_giasa", placeholder="Quantidade em litros", type="number"),
	        html.Br(),
	        html.P(id="output_giasa"),
	    ],
	   	style={
	    	'margin-top': '30px'
	        } 

		),

			html.Div(
	    [
	        dbc.Input(id="input_giasa2", placeholder="Destino", type="text"),
	        html.Br(),
	        html.P(id="output_giasa2"),
	    ]
		),
		dbc.Button("Enviar", color="primary", className="mr-1", id='1'),
		html.Span(id="example-output", style={"vertical-align": "middle"}),

		html.Div(
	    [	html.Label('Atualizar Japungu'),
	        dbc.Input(id="input_japungu", placeholder="Quantidade em litros", type="number"),
	        html.Br(),
	        html.P(id="output_japungu"),
	    ],
	       	style={
	    	'margin-top': '30px'
	        } 
		),

		html.Div(
	    [
	        dbc.Input(id="input_japungu2", placeholder="Destino", type="text"),
	        html.Br(),
	        html.P(id="output_japungu2"),
	    ]
		),
		dbc.Button("Enviar", color="primary", className="mr-1",id='2'),
		html.Span(id="B", style={"vertical-align": "middle"}),
		html.Div(
	    [	html.Label('Atualizar Miriri'),
	        dbc.Input(id="input_miriri", placeholder="Quantidade em litros", type="number"),
	        html.Br(),
	        html.P(id="output_miriri"),
	    ],
	       	style={
	    	'margin-top': '30px'
	        } 
		),

			html.Div(
	    [
	        dbc.Input(id="input_miriri2", placeholder="Destino", type="text"),
	        html.Br(),
	        html.P(id="output_miriri2"),
	    ]
		),

		dbc.Button("Enviar", color="primary", className="mr-1",id='3'),
		html.Span(id="C", style={"vertical-align": "middle"}),

	],
	style={
	    	'margin-left': '150px',
	    	'margin-´top' : '-35px'
	    	#'width': '50%'
	        },
	        className='col s12 m6'

	),

	html.Div([
		html.Div(
	    [	html.Label('Atualizar M. Alegre'),
	        dbc.Input(id="input_m_alegre", placeholder="Quantidade em litros", type="number"),
	        html.Br(),
	        html.P(id="output_m_alegre"),
	    ],
	   	style={
	    	'margin-top': '30px'
	        } 

		),

			html.Div(
	    [
	        dbc.Input(id="input_m_alegre2", placeholder="Destino", type="text"),
	        html.Br(),
	        html.P(id="output_m_alegre2"),
	    ]
		),
		dbc.Button("Enviar", color="primary", className="mr-1",id='4'),
		html.Span(id="D", style={"vertical-align": "middle"}),

		html.Div(
	    [	html.Label('Atualizar Tabu'),
	        dbc.Input(id="input_tabu", placeholder="Quantidade em litros", type="number"),
	        html.Br(),
	        html.P(id="output_tabu"),
	    ],
	       	style={
	    	'margin-top': '30px'
	        } 
		),

		html.Div(
	    [
	        dbc.Input(id="input_tabu2", placeholder="Destino", type="text"),
	        html.Br(),
	        html.P(id="output_tabu2"),
	    ]
		),
		dbc.Button("Enviar", color="primary", className="mr-1",id='5'),
		html.Span(id="E", style={"vertical-align": "middle"}),
		html.Div(
	    [	html.Label('Atualizar D Padua'),
	        dbc.Input(id="input_d_padua", placeholder="Quantidade em litros", type="number"),
	        html.Br(),
	        html.P(id="output_d_padua"),
	    ],
	       	style={
	    	'margin-top': '30px',

	        } 
		),

			html.Div(
	    [
	        dbc.Input(id="input_d_padua2", placeholder="Destino", type="text"),
	        html.Br(),
	        html.P(id="output_d_padua2"),
	    ]
		),

		dbc.Button("Enviar", color="primary", className="mr-1",id='6'),
		html.Span(id="F", style={"vertical-align": "middle"}),

	],
	style={
	    	'margin-left': '700px',
	    	'margin-top':'-553px', 
	       },
	className='col s12 m6'

	),

	
	
],style={'width': '100%','display': 'inline-block'
}),	
	
	
],

            className='row'),








],  style={'width': '100%',
            'display': 'inline-block'})



@app.callback(
    Output(component_id='example-output', component_property='children'),    
    [Input('1', 'n_clicks'),],
    state=[State(component_id='input_giasa', component_property='value'),
    State(component_id='input_giasa2', component_property='value')])


def update_output_div(n_clicks, input_value, emailzin):

	mydb=psy.connect (
	host='ec2-54-235-100-99.compute-1.amazonaws.com',
	user = 'mhxcrjdnckxtbr',
	password='041d51b54231eb4e36b2a8d58f5ae16bc5cfaab2303d426676580f62e52ebcc1',
	database='d9k1k422mp16r5')

	mycursor=mydb.cursor()
	mycursor.execute('''select * from public."GIASA" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]

	df = pd.DataFrame(data=myresult, columns=colnames )

	ultimo_registro = df.tail(1)



	if n_clicks is None:
		return "Preencher os dados"
	else:
		if(input_value and emailzin):
			qtd_saida = input_value
			total_liq = ultimo_registro['total_liq'].sum() - qtd_saida
			destino = emailzin
			mycursor.execute('''INSERT INTO public."GIASA" (total_liq,quantidade_saida,destino)  VALUES (%s,%s,%s)''',(total_liq,qtd_saida, destino))
			mydb.commit()
			return 'Giasa atualizado com sucesso'





@app.callback(
    Output(component_id='B', component_property='children'),    
    [Input('2', 'n_clicks'),],
    state=[State(component_id='input_japungu', component_property='value'),
    State(component_id='input_japungu2', component_property='value')])


def update_output_div(n_clicks, input_value, emailzin):
	mydb=psy.connect (
	host='ec2-54-235-100-99.compute-1.amazonaws.com',
	user = 'mhxcrjdnckxtbr',
	password='041d51b54231eb4e36b2a8d58f5ae16bc5cfaab2303d426676580f62e52ebcc1',
	database='d9k1k422mp16r5')

	mycursor=mydb.cursor()
	mycursor.execute('''select * from public."JAPUNGU" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]

	df = pd.DataFrame(data=myresult, columns=colnames )	

	ultimo_registro = df.tail(1)


	if n_clicks is None:

		return "Preencher os dados"
	else:
		if(input_value and emailzin):
			qtd_saida = input_value
			total_liq = ultimo_registro['total_liq'].sum() - qtd_saida
			destino = emailzin
			mycursor.execute('''
	                INSERT INTO public."JAPUNGU" (total_liq, quantidade_saida, destino)
	                VALUES
	                (%s,%s,%s)
	                ''',(total_liq,qtd_saida, destino))
			mydb.commit()
			return 'JAPUNGU atualizado com sucesso'


@app.callback(
    Output(component_id='C', component_property='children'),    
    [Input('3', 'n_clicks'),],
    state=[State(component_id='input_miriri', component_property='value'),
    State(component_id='input_miriri2', component_property='value')])


def update_output_div(n_clicks, input_value, emailzin):
	mydb=psy.connect (
	host='ec2-54-235-100-99.compute-1.amazonaws.com',
	user = 'mhxcrjdnckxtbr',
	password='041d51b54231eb4e36b2a8d58f5ae16bc5cfaab2303d426676580f62e52ebcc1',
	database='d9k1k422mp16r5')

	mycursor=mydb.cursor()
	mycursor.execute('''select * from public."MIRIRI" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]

	df = pd.DataFrame(data=myresult, columns=colnames )

	ultimo_registro = df.tail(1)

	if n_clicks is None:
		return "Preencher os dados"
	else:
		if(input_value and emailzin):
			qtd_saida = input_value
			total_liq = ultimo_registro['total_liq'].sum() - qtd_saida
			destino = emailzin
			mycursor.execute('''
	                INSERT INTO public."MIRIRI" (total_liq, quantidade_saida, destino)
	                VALUES
	                (%s,%s,%s)
	                ''',(total_liq,qtd_saida, destino))
			mydb.commit()
			return 'MIRIRI atualizado com sucesso'

@app.callback(
    Output(component_id='D', component_property='children'),    
    [Input('4', 'n_clicks'),],
    state=[State(component_id='input_m_alegre', component_property='value'),
    State(component_id='input_m_alegre2', component_property='value')])


def update_output_div(n_clicks, input_value, emailzin):
	mydb=psy.connect (
	host='ec2-54-235-100-99.compute-1.amazonaws.com',
	user = 'mhxcrjdnckxtbr',
	password='041d51b54231eb4e36b2a8d58f5ae16bc5cfaab2303d426676580f62e52ebcc1',
	database='d9k1k422mp16r5')

	mycursor=mydb.cursor()
	mycursor.execute('''select * from public."M_ALEGRE" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]

	df = pd.DataFrame(data=myresult, columns=colnames )

	ultimo_registro = df.tail(1)


	if n_clicks is None:
		return "Preencher os dados"
	else:
		if(input_value and emailzin):
			qtd_saida = input_value
			total_liq = ultimo_registro['total_liq'].sum() - qtd_saida
			destino = emailzin
			mycursor.execute('''
	                INSERT INTO public."M_ALEGRE" (total_liq, quantidade_saida, destino)
	                VALUES
	                (%s,%s,%s)
	                ''',(total_liq,qtd_saida, destino))
			mydb.commit()
			return 'M. ALEGRE atualizado com sucesso'



@app.callback(
    Output(component_id='E', component_property='children'),    
    [Input('5', 'n_clicks'),],
    state=[State(component_id='input_tabu', component_property='value'),
    State(component_id='input_tabu2', component_property='value')])


def update_output_div(n_clicks, input_value, emailzin):
	mydb=psy.connect (
	host='ec2-54-235-100-99.compute-1.amazonaws.com',
	user = 'mhxcrjdnckxtbr',
	password='041d51b54231eb4e36b2a8d58f5ae16bc5cfaab2303d426676580f62e52ebcc1',
	database='d9k1k422mp16r5')

	mycursor=mydb.cursor()
	mycursor.execute('''select * from public."TABU" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]

	df = pd.DataFrame(data=myresult, columns=colnames )

	ultimo_registro = df.tail(1)


	if n_clicks is None:
		return "Preencher os dados"
	else:
		if(input_value and emailzin):
			qtd_saida = input_value
			total_liq = ultimo_registro['total_liq'].sum() - qtd_saida
			destino = emailzin
			mycursor.execute('''
	                INSERT INTO public."TABU" (total_liq, quantidade_saida, destino)
	                VALUES
	                (%s,%s,%s)
	                ''',(total_liq,qtd_saida, destino))
			mydb.commit()
			return 'TABU atualizado com sucesso'


@app.callback(
    Output(component_id='F', component_property='children'),    
    [Input('6', 'n_clicks'),],
    state=[State(component_id='input_d_padua', component_property='value'),
    State(component_id='input_d_padua2', component_property='value')])


def update_output_div(n_clicks, input_value, emailzin):
	mydb=psy.connect (
	host='ec2-54-235-100-99.compute-1.amazonaws.com',
	user = 'mhxcrjdnckxtbr',
	password='041d51b54231eb4e36b2a8d58f5ae16bc5cfaab2303d426676580f62e52ebcc1',
	database='d9k1k422mp16r5')

	mycursor=mydb.cursor()
	mycursor.execute('''select * from public."D_PADUA" ''')
	myresult= mycursor.fetchall()
	colnames = [desc[0] for desc in mycursor.description]

	df = pd.DataFrame(data=myresult, columns=colnames )

	ultimo_registro = df.tail(1)


	if n_clicks is None:
		return "Preencher os dados"
	else:
		if(input_value and emailzin):
			qtd_saida = input_value
			total_liq = ultimo_registro['total_liq'].sum() - qtd_saida
			destino = emailzin
			mycursor.execute('''
	                INSERT INTO public."D_PADUA" (total_liq, quantidade_saida, destino)
	                VALUES
	                (%s,%s,%s)
	                ''',(total_liq,qtd_saida, destino))
			mydb.commit()
			return 'D PADUA atualizado com sucesso'



if(__name__ == '__main__'):
    app.run_server(debug=True,port=3052) 

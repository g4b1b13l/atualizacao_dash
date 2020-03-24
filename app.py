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
import base64
ufpb_image = base64.b64encode(open('logo_ufpb.jpeg', 'rb').read())
cear_image = base64.b64encode(open('logo_ufpb.jpeg', 'rb').read())
now = datetime.now()

alo=dbc.themes.BOOTSTRAP

external_stylesheets = ['https://codepen.io/g4b1b13l/pen/VwwrYdL.css'] # Esse eh um site externo meu com um monte classe do css pronta,
																		# Copiei quase tudo do original que é um de chris num sei q la
																		#Criei um no meu nome so caso ele decida excluir ou algo do tipo eu n perder 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
    )
server = app.server

app.title = 'Controle_Alcool_saida'    





app.layout = html.Div([  


		 html.Div(id='div_topo',children=[

                html.Img(id='img_logo_ufpb'
                        ,src='data:image/png;base64,{}'.format(ufpb_image.decode())
                        ,style={'display': 'block','height':'70px','position':'absolute','left':'50px','top':'20px'
                        }),

                       html.H5('Doação ao Governo do Estado da Paraíba do Volume de 31.460 litros solicitados'),
                       html.H5(	'pela Secretaria do Estado da Paraíba para combate ao Covid-19'),


                html.Img(id='img_logo_cear'
                        ,src='data:image/png;base64,{}'.format(cear_image.decode())
                        ,style={'display': 'block','height':'70px','position':'absolute','right':'50px','top':'20px'
                      }),

            ],
                
            style={'textAlign':'center'
                  ,'border': '2px solid lightgray'
                  ,'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
                  ,'background-color':'#fffffff'}
            ),

	   	#html.Div(children=[
        #                html.H5('Doação ao Governo do Estado da Paraíba do Volume de 31.460 litros solicitados'),
        #                html.H5(	'pela Secretaria do Estado da Paraíba para combate ao Covid-19')
                        #html.P('AS INFORMAÇÕES ANEXAS SÃO RETIRADAS DOS RECIBOS DO SAPCANA ENVIADOS AO MAPA. P/ EMPRESAS ASSOCIADAS'),
                        #html.P('Elaboração: Sindalcool | Posição até 29/02/2020')
        #            ],style={'textAlign': 'center'
        #                     ,'border': '2px solid lightgray'
        #                     ,'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
        #                     ,'background-color':'#eefefe'}),

		#html.Div(

	     #   [html.H1(children= 'Controle Álcool em gel'),

	       
	      #  ]
	       #       , 

	       #  style={
	        #'font-size': '5pt',
	        #'height': '75px',
	        #'margin': '-10px -10px -10px',
	        #'background-color': '#ADD8E6',
	        #'text-align': 'center',
	        #'border-radius': '2px',
	        #'display': 'flex',
	        #'margin-left': '0', 
	        #} 

	        #), 


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
	    	#'margin-´top' : '-100px'
	    	#'width': '50%'
	        },
	        className='five columns'

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
	#style={
	#    	'margin-left': '700px',
	  # 	'margin-top':'-10px', 
	     #  },
	className='five columns'

	),

	

	
	
	],className='row',	style={
	  #	'margin-left': '700px',
	   	'margin-top':'-10px', 
	       },
	),




html.Div(children=[

                        html.P('AS INFORMAÇÕES ANEXAS SÃO RETIRADAS DOS RECIBOS DO SAPCANA ENVIADOS AO MAPA. P/ EMPRESAS ASSOCIADAS'),
                        html.P('Elaboração: Sindalcool | Posição até 29/02/2020')
                    ],style={'textAlign': 'center'
                             ,'border': '2px solid lightgray'
                             ,'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)'
                             ,'background-color':'#eefefe'
                             , 'margin-top' : '30px'}),

dcc.Checklist(
    id='check',
    options=[   
    {'label': '', 'value': 'ativado'},


    ],
    value=['d'],
    labelStyle={'display': 'none','margin-top': '30px'}
    ),
],)


def limpando_giasin_1():


	@app.callback(
	    Output(component_id='input_giasa', component_property='value'),    
	    [Input('check', 'value'),],
	    state=[State(component_id='input_giasa', component_property='value'),State(component_id='input_giasa2', component_property='value'),
	    State(component_id='example-output', component_property='children')
	    ])

		
	def limpando_giasa_1(n_clicks, qtd,destino, texto):
		print('aff',flush=True)
		return ''

def limpando_giasin_2():

	@app.callback(
		    Output(component_id='input_giasa2', component_property='value'),    
		    [Input('check', 'value'),],
		    state=[State(component_id='input_giasa', component_property='value'),State(component_id='input_giasa2', component_property='value'),
		    State(component_id='example-output', component_property='children')])

			
	def limpando_giasa_2(n_clicks,qtd,destino,texto):
			print('oxe', flush=True)

			return ''




@app.callback(
    [Output(component_id='example-output', component_property='children'),Output(component_id='input_giasa', component_property='value'),
    Output(component_id='input_giasa2', component_property='value')],    
    [Input('1', 'n_clicks'),
		],
    state=[State(component_id='input_giasa', component_property='value'),
    State(component_id='input_giasa2', component_property='value')])


def update_output_div(n_clicks,input_value, emailzin):

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

	#if texto_qtd is None or texto_destino is None:
#		return 'Preencher os dados'

#	if n_clicks is None:
#		return "Preencher os dados"

	if n_clicks is None:
		print('')
	else:
		if(input_value and emailzin):
			print('chegou',flush=True)
			qtd_saida = input_value
			total_liq = ultimo_registro['total_liq'].sum() - qtd_saida
			destino = emailzin
			mycursor.execute('''INSERT INTO public."GIASA" (total_liq,quantidade_saida,destino)  VALUES (%s,%s,%s)''',(total_liq,qtd_saida, destino))
			mydb.commit()
			#limpando_giasin_1()
			#limpando_giasin_2()
			return ['Giasa atualizado com sucesso','','' ]





@app.callback(
   [ Output(component_id='B', component_property='children'),  Output(component_id='input_japungu', component_property='value'),
       Output(component_id='input_japungu2', component_property='value')],
    [Input('2', 'n_clicks'),
	],
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

		print('')
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
			return ['JAPUNGU atualizado com sucesso','','']


@app.callback(
    [Output(component_id='C', component_property='children'),  Output(component_id='input_miriri', component_property='value'),
       Output(component_id='input_miriri2', component_property='value')   ],
    [Input('3', 'n_clicks'),
	],
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
		print('')
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
			return ['MIRIRI atualizado com sucesso','','']

@app.callback(
   [ Output(component_id='D', component_property='children'),    Output(component_id='input_m_alegre', component_property='value'),
          Output(component_id='input_m_alegre2', component_property='value') ],
    [Input('4', 'n_clicks'),
	],
    state=[State(component_id='input_m_alegre', component_property='value'),
    State(component_id='input_m_alegre2', component_property='value')])


def update_output_div(n_clicks,input_value, emailzin):
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
		print('')
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
			return ['M. ALEGRE atualizado com sucesso','','']



@app.callback(
    [Output(component_id='E', component_property='children'),     Output(component_id='input_tabu', component_property='value'),
              Output(component_id='input_tabu2', component_property='value')],
    [Input('5', 'n_clicks'),
],
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
		print('')
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
			return ['TABU atualizado com sucesso','','']


@app.callback(
    [Output(component_id='F', component_property='children'),  Output(component_id='input_d_padua', component_property='value'),
                  Output(component_id='input_d_padua2', component_property='value')  ],
    [Input('6', 'n_clicks'),
	],
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
		print('')
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
			return ['D PADUA atualizado com sucesso','','']









if(__name__ == '__main__'):
    app.run_server(debug=True,port=3080) 

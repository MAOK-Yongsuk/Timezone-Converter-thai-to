import PySimpleGUI as sg
import datetime
import pytz

layout = [
	[sg.Text('Ex. YYYY-MM-DD HH:MM')],
	[		
		sg.Input(key = '-INPUT-'),
		sg.Combo(['TH to US','TH to CN','TH to JP','TH to UK','TH to AU']
					,default_value='TH to US',key = '-UNITS-'),
		sg.Button('Convert', key = '-CONVERT-')
	],
	[sg.Text('Output:')],
	[sg.Text('---', key = '-OUTPUT-')]
]

window = sg.Window('TimezoneConverter_V.00',layout)

def convert_datetime_timezone(dt,tz2):
    tz1 = pytz.timezone('Asia/Bangkok')
    tz2 = pytz.timezone(tz2)
    dt = datetime.datetime.strptime(dt,"%Y-%m-%d %H:%M")
    dt = tz1.localize(dt)
    dt = dt.astimezone(tz2)
    dt = dt.strftime("%Y-%m-%d %H:%M")
    return dt

while True:
	event, values = window.read()

	if event == sg.WIN_CLOSED:
		break

	if event == '-CONVERT-':
		input_time = values['-INPUT-']
		match values['-UNITS-']:

			case 'TH to US':
				output = convert_datetime_timezone(input_time,'America/New_York')
				output_string = f"TH to US ---> {output}"
			case 'TH to CN':
				output = convert_datetime_timezone(input_time,'Asia/Shanghai')
				output_string = f"TH to CN ---> {output}"
			case 'TH to UK':
				output = convert_datetime_timezone(input_time,'Europe/London')
				output_string = f"TH to UK ---> {output}"
			case 'TH to JP':
				output = convert_datetime_timezone(input_time,'Asia/Tokyo')
				output_string = f"TH to JP ---> {output}"
			case 'TH to AU':
				output = convert_datetime_timezone(input_time,'Australia/Melbourne')
				output_string = f"TH to AU ---> {output}"				


		window['-OUTPUT-'].update(output_string)	

			

window.close()		
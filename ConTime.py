import PySimpleGUI as sg
import datetime
import pytz

sg.theme('DarkBlue13')
layout = [
	[sg.Text('-ConverterTimeZone_V.01-',font=('Any 20'))],[sg.Text('')],
	[sg.Text('(Ex. YYYY-MM-DD HH:MM)',font=('Courier 11'))],
	[		
		sg.Input(key = '-INPUT1-',size=(11, 1),font=('Courier 15')),
		sg.Input(key = '-INPUT2-',size=(6, 1),font=('Courier 15')),
		sg.Combo(['TH to US','TH to CN','TH to JP','TH to UK','TH to AU']
					,default_value='TH to US',size=(15, 1),key = '-UNITS-'),
		sg.Button('Convert',size=(10, 1),font=('Courier 12'),key = '-CONVERT-')
	],[sg.Text('')],
	[sg.Text('Output:',font=('Courier 15'))],
	[sg.Text('---',font=('Courier 15'), key = '-OUTPUT-')]
]


window = sg.Window('TimezoneConverter_V.01',layout,size=(600, 300))

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
		input_time = values['-INPUT1-'] +' '+ values['-INPUT2-']
		try:
			match values['-UNITS-']:
				case 'TH to US':
					output = convert_datetime_timezone(input_time,'America/New_York')
					output_string = f" TH to US ---> {output}"
				case 'TH to CN':
					output = convert_datetime_timezone(input_time,'Asia/Shanghai')
					output_string = f" TH to CN ---> {output}"
				case 'TH to UK':
					output = convert_datetime_timezone(input_time,'Europe/London')
					output_string = f" TH to UK ---> {output}"
				case 'TH to JP':
					output = convert_datetime_timezone(input_time,'Asia/Tokyo')
					output_string = f" TH to JP ---> {output}"
				case 'TH to AU':
					output = convert_datetime_timezone(input_time,'Australia/Melbourne')
					output_string = f" TH to AU ---> {output}"
			window['-OUTPUT-'].update(output_string,text_color='Yellow')

		except ValueError:
			window['-OUTPUT-'].update('  Timezone incorrect, Try again',text_color='Red')
						
		
window.close()		
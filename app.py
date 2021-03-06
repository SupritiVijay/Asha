import streamlit as st
import datetime as datetime
import pandas as pd
import base64

def get_table_download_link(path, link_name="Download Previous Incidents"):
    b64 = base64.b64encode(path.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="incidents.csv">'+link_name+'</a>'
    return href

def app():
	st.header("Register the Incident:")
	data = pd.read_csv("complaint.csv")
	print(data)
	with st.form(key='my_form'):
		st.write("Hi, This is Asha from Project Women Safety.")
		st.write("My name means hope in Sanskrit and I ask you to hold on to hope as you fill this form.")
		st.write("I wish to help you and support you through this entire journey. I am sorry you had such a bad experience. All of us are here with you. You have nothing to be scared of!\n")
		st.write("You can confidentently lodge a report with us.")
		st.text("")
		text_desc = st.text_area(label='Please let us know a brief description about the incident')
		
		st.write("That is truly sad to hear. For us to prevent this from occuring again, could you specify certain details for us?")
		st.text("")

		location = st.text_input(label='Location(Street Name, Country)')
		
		time = st.time_input('Time of Incident', datetime.time(21, 45))

		st.write("Thank you for providing us with this information. We know this is hard and you feel scared and unsafe.") 
		st.write("Would you like to tell us your name? You can remain anonymous if you like to as well.We only ask for it so that our users are assured that all the complaints are coming from an authentic source.") 
		st.write("")
		name = st.text_input(label='Name')
		submit_button = st.form_submit_button(label='Submit')



		if submit_button:
			if location == "":
				st.error("Please provide us with a location. So that our users could be warned")
			if text_desc == "":
				st.error("Please provide us with a description. So that our users could be warned")
			if name == "":
				name = "Anonymous"

			st.write("Thank you for lodging a complaint with us. We will try our best to make sure no other user has to go through this again.")
			st.write("If you are aggrevated and want to take serious action, we have listed below the contacts of the Police and NGOs that work for women's safety and rights.")
			st.write("Police: +1 866-863-0511/+91 782-717-0170")
			st.write("MSI United States: +1 202-601-2825")
			st.write("Guria: +91 542-2504253")
			st.write("")
			data.loc[len(data.index)] = [text_desc, name, location, time] 
			
			data.to_csv('complaint.csv', index = False)
			dat = data.drop(columns=['Name'])
			csv = dat.to_csv(index=False)

			st.markdown(get_table_download_link(csv), unsafe_allow_html=True)


if __name__ == '__main__':
	app()

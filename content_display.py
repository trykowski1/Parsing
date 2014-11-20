from content_extract import Input_output_data, Create_timer

input_output = Input_output_data()
input_output.input_data()
timer = Create_timer(4,input_output.output_data)
timer.start()

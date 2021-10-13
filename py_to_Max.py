import mido, rtmidi

# with Max open should set to 'to Max 1' port
port = mido.open_output(mido.get_output_names()[0])

msg = mido.Message('note_on', note=60)

port.send(msg)
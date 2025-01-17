from mido import MidiFile
import pandas as pd

# Function to extract information from a MIDI file
def extract_midi_data(file_path):
    midi = MidiFile(file_path)
    midi_info = {
        "file_name": file_path.split('/')[-1],
        "ticks_per_beat": midi.ticks_per_beat,
        "tracks": []
    }
    for i, track in enumerate(midi.tracks):
        track_data = {
            "track_name": track.name if hasattr(track, 'name') else f"Track {i}",
            "total_messages": len(track),
            "event_types": list(set(msg.type for msg in track if not msg.is_meta)),
            "notes": len([msg for msg in track if msg.type == 'note_on' and msg.velocity > 0]),
        }
        midi_info["tracks"].append(track_data)
    return midi_info

# Analyze your MIDI files
midi_files = [
    "POUR-TOI-MA-BELLE -26-05-2021.mid",
    "HAZEL voices Pads part 5 3.mid",
    "2023 happier .mid"
]
midi_data = [extract_midi_data(file) for file in midi_files]

# Flatten and display results
analysis_flattened = []
for midi in midi_data:
    for track in midi['tracks']:
        analysis_flattened.append({
            "File Name": midi['file_name'],
            "Track Name": track['track_name'],
            "Total Messages": track['total_messages'],
            "Event Types": ", ".join(track['event_types']),
            "Number of Notes": track['notes'],
        })

# Convert to DataFrame for better visualization
df = pd.DataFrame(analysis_flattened)
print(df)
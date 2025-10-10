# API Reference

Complete reference for the beatstoch Python library.

## Main Functions

### `generate_from_song()`

Generate a MIDI drum pattern by looking up a song's BPM from the database.

```python
generate_from_song(
    song_title: str,
    artist: Optional[str] = None,
    bars: int = 8,
    style: str = "house",
    steps_per_beat: int = 4,
    swing: float = 0.10,
    intensity: float = 0.9,
    seed: Optional[int] = None,
    fallback_bpm: Optional[float] = None,
    verbose: bool = False,
) -> Tuple[mido.MidiFile, float]
```

**Parameters:**
- `song_title` (str): Title of the song to look up
- `artist` (str, optional): Artist name for improved BPM lookup accuracy
- `bars` (int): Number of bars to generate (default: 8)
- `style` (str): Drum pattern style - "house", "breaks", or "generic" (default: "house")
- `steps_per_beat` (int): Time resolution (default: 4, i.e., 16th notes)
- `swing` (float): Swing amount 0.0-1.0 (default: 0.10)
- `intensity` (float): Pattern density 0.0-1.0 (default: 0.9)
- `seed` (int, optional): Random seed for reproducible patterns
- `fallback_bpm` (float, optional): BPM to use if database lookup fails
- `verbose` (bool): Enable verbose logging (default: False)

**Returns:**
- Tuple of (MIDI file object, detected BPM as float)

**Raises:**
- `RuntimeError`: If BPM lookup fails and no fallback BPM provided

**Example:**
```python
from beatstoch import generate_from_song

midi_file, bpm = generate_from_song(
    "1979",
    artist="Smashing Pumpkins",
    bars=16,
    style="house",
    swing=0.12,
    verbose=True
)

print(f"Generated {midi_file.length} seconds at {bpm} BPM")
midi_file.save("drums.mid")
```

### `generate_stochastic_pattern()`

Generate a MIDI drum pattern with explicit BPM (no database lookup).

```python
generate_stochastic_pattern(
    bpm: float,
    bars: int = 4,
    meter: Tuple[int, int] = (4, 4),
    steps_per_beat: int = 4,
    swing: float = 0.12,
    intensity: float = 0.9,
    seed: int = 42,
    style: str = "house",
) -> mido.MidiFile
```

**Parameters:**
- `bpm` (float): Target BPM for the pattern
- `bars` (int): Number of bars to generate (default: 4)
- `meter` (Tuple[int, int]): Time signature as (numerator, denominator) (default: (4, 4))
- `steps_per_beat` (int): Time resolution (default: 4, i.e., 16th notes)
- `swing` (float): Swing amount 0.0-1.0 (default: 0.12)
- `intensity` (float): Pattern density 0.0-1.0 (default: 0.9)
- `seed` (int): Random seed for reproducible patterns (default: 42)
- `style` (str): Drum pattern style - "house", "breaks", or "generic" (default: "house")

**Returns:**
- MIDI file object

**Example:**
```python
from beatstoch import generate_stochastic_pattern

pattern = generate_stochastic_pattern(
    bpm=128.0,
    bars=8,
    style="breaks",
    swing=0.08,
    intensity=0.85,
    seed=123
)

pattern.save("breakbeat_pattern.mid")
```

## Drum Styles

### House
**Characteristics:**
- Four-on-the-floor kick pattern
- Steady hi-hat pattern with openings
- Snare on beats 2 and 4
- Clean, repetitive structure

**Best for:** House, techno, minimal techno

### Breaks
**Characteristics:**
- Complex kick patterns
- Varied snare placement
- Syncopated hi-hat patterns
- Breakbeat-inspired rhythms

**Best for:** Breakbeat, drum & bass, hip-hop, experimental

### Generic
**Characteristics:**
- Balanced patterns
- Moderate complexity
- Works across multiple genres
- Good starting point for experimentation

**Best for:** General use, customization, learning

## Advanced Usage

### Custom Random Seeds

```python
import time

# Use current time for truly random patterns
current_time = int(time.time())
midi_file, bpm = generate_from_song("Song Title", seed=current_time)

# Use song title for consistent patterns per song
song_seed = hash("Song Title - Artist") % (2**31)
midi_file, bpm = generate_from_song("Song Title", artist="Artist", seed=song_seed)
```

### Batch Generation

```python
from beatstoch import generate_stochastic_pattern

# Generate multiple variations
styles = ["house", "breaks", "generic"]
bpms = [120, 125, 130]

for style in styles:
    for bpm in bpms:
        pattern = generate_stochastic_pattern(
            bpm=bpm,
            bars=8,
            style=style,
            seed=42  # Consistent seed for comparison
        )
        pattern.save(f"pattern_{bpm}_{style}.mid")
```

### Integration with DAWs

```python
from beatstoch import generate_from_song

# Generate pattern for current project BPM
def generate_drums_for_project(song_title, artist, project_bpm, bars=8):
    """Generate drums, using project BPM as fallback if lookup fails."""
    try:
        midi_file, detected_bpm = generate_from_song(
            song_title,
            artist=artist,
            bars=bars,
            fallback_bpm=project_bpm
        )
        print(f"Using detected BPM: {detected_bpm}")
        return midi_file, detected_bpm
    except RuntimeError:
        # Fallback to project BPM
        midi_file = generate_stochastic_pattern(project_bpm, bars=bars)
        return midi_file, project_bpm

# Example usage in a DAW automation script
drums, bpm = generate_drums_for_project("My Song", "My Artist", 128)
drums.save("project_drums.mid")
```

## Data Types

### MIDI File Object
Returns standard `mido.MidiFile` objects that can be:
- Saved to disk: `midi_file.save("filename.mid")`
- Played with MIDI players
- Imported into DAWs
- Modified with additional MIDI events

### BPM Values
- Returned as `float` for precision
- Typical range: 60-200 BPM
- Represents the detected or specified tempo

## Error Handling

### Common Exceptions

```python
from beatstoch import generate_from_song
import requests

try:
    midi_file, bpm = generate_from_song("Song Title", artist="Artist")
except RuntimeError as e:
    print(f"BPM lookup failed: {e}")
    # Use fallback BPM
    fallback_bpm = 120
    midi_file = generate_stochastic_pattern(fallback_bpm, bars=8)
except requests.RequestException as e:
    print(f"Network error: {e}")
    # Handle network issues
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Network Issues
The library makes HTTP requests to BPM databases. Handle network errors:

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure retries for network requests
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("http://", adapter)
session.mount("https://", adapter)
```

## Performance Considerations

- **Memory Usage**: MIDI files are generated in memory; large patterns may use significant RAM
- **Generation Time**: Complex patterns with high `steps_per_beat` take longer to generate
- **Network Time**: BPM lookups add latency (typically 1-3 seconds)
- **File I/O**: Saving large MIDI files to disk may take time

## Thread Safety

The library is not thread-safe for random number generation when using default seeds. Use explicit seeds for concurrent generation:

```python
import threading
import random

def generate_with_thread_id(bpm, thread_id):
    # Use thread ID in seed for thread-safe generation
    seed = hash((bpm, thread_id)) % (2**31)
    return generate_stochastic_pattern(bpm, seed=seed)

# Safe for concurrent use
threads = []
for i in range(10):
    thread = threading.Thread(target=generate_with_thread_id, args=(128, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

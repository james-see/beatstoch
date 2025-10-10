# User Guide

Complete guide for using beatstoch to generate drum patterns.

## Installation

### Using pip (recommended)
```bash
pip install beatstoch
```

### Using uv
```bash
uv add beatstoch
```

### Development Installation
```bash
git clone <repository-url>
cd beatstoch
uv sync
```

## Command Line Interface

### Basic Usage

#### Generate from Song Title
```bash
# Simple usage - just song title
beatstoch generate "Billie Jean"

# With artist for better BPM accuracy
beatstoch generate "1979" --artist "Smashing Pumpkins"

# Custom number of bars
beatstoch generate "Around the World" --artist "Daft Punk" --bars 16
```

#### Generate with Explicit BPM
```bash
# House style at 128 BPM
beatstoch generate-bpm 128 --style house --bars 8

# Breaks style with custom settings
beatstoch generate-bpm 174 --style breaks --bars 32 --swing 0.15 --intensity 0.8
```

### All Command Line Options

#### `generate` Command (Song Lookup)
```bash
beatstoch generate [OPTIONS] TITLE

Options:
  --artist TEXT          Artist name (improves BPM lookup accuracy)
  --bars INTEGER         Number of bars to generate (default: 8)
  --style [house|breaks|generic]  Drum style (default: house)
  --steps-per-beat INTEGER        Resolution (default: 4)
  --swing FLOAT          Swing amount 0.0-1.0 (default: 0.10)
  --intensity FLOAT      Pattern density 0.0-1.0 (default: 0.9)
  --seed INTEGER         Random seed for reproducible patterns
  --fallback-bpm FLOAT   BPM to use if lookup fails
  --verbose             Show BPM lookup details
  -h, --help            Show this message and exit
```

#### `generate-bpm` Command (Explicit BPM)
```bash
beatstoch generate-bpm [OPTIONS] BPM

Options:
  --bars INTEGER         Number of bars (default: 8)
  --style [house|breaks|generic]  Drum style (default: house)
  --steps-per-beat INTEGER        Resolution (default: 4)
  --swing FLOAT          Swing amount (default: 0.10)
  --intensity FLOAT      Pattern density (default: 0.9)
  --seed INTEGER         Random seed
  -h, --help            Show this message and exit
```

## Python Library

### Basic Usage

```python
from beatstoch import generate_from_song, generate_stochastic_pattern

# Generate from song lookup
midi_file, bpm = generate_from_song("1979", artist="Smashing Pumpkins")
print(f"Found BPM: {bpm}")
midi_file.save("drums.mid")

# Generate with explicit BPM
midi_file = generate_stochastic_pattern(bpm=127, bars=8, style="house")
midi_file.save("house_drums.mid")
```

### Advanced Usage

```python
from beatstoch import generate_from_song, generate_stochastic_pattern

# Song lookup with full customization
midi_file, bpm = generate_from_song(
    song_title="Billie Jean",
    artist="Michael Jackson",
    bars=16,                    # 16 bars long
    style="breaks",             # Breakbeat style
    steps_per_beat=4,           # 16th note resolution
    swing=0.12,                 # Light swing
    intensity=0.85,             # Dense pattern
    seed=42,                    # Reproducible
    fallback_bpm=120            # Fallback if lookup fails
)

# Explicit BPM with full control
midi_file = generate_stochastic_pattern(
    bpm=174,
    bars=32,
    meter=(4, 4),               # Time signature
    steps_per_beat=8,           # 32nd note resolution
    swing=0.08,                 # Subtle swing
    intensity=0.7,              # Sparse pattern
    seed=123,
    style="generic"             # All-purpose style
)

midi_file.save("complex_pattern.mid")
```

### Function Signatures

#### `generate_from_song()`
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
) -> Tuple[MidiFile, float]
```

**Returns:** Tuple of (MIDI file object, detected BPM)

#### `generate_stochastic_pattern()`
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
) -> MidiFile
```

**Returns:** MIDI file object

## Drum Styles

### House Style
- Classic four-on-the-floor kick pattern
- Steady hi-hats with openings
- Snares on beats 2 and 4
- Best for: House, techno, minimal

### Breaks Style
- More complex kick patterns
- Varied snare placement
- Syncopated hi-hat patterns
- Best for: Breakbeat, drum & bass, hip-hop

### Generic Style
- Balanced, all-purpose patterns
- Moderate complexity
- Works well across genres
- Best for: General use, experimentation

## Output Files

Generated MIDI files use descriptive naming:
- `stoch_[artist]_[title]_[bpm]bpm.mid` (from song lookup)
- `stoch_[bpm]bpm.mid` (from explicit BPM)

Files are standard MIDI format compatible with:
- Ableton Live
- FL Studio
- Logic Pro
- Pro Tools
- Any MIDI-compatible software

## Troubleshooting

### BPM Lookup Issues
- Ensure internet connection is available
- Some songs may not be in the BPM database
- Use `--fallback-bpm` to specify a default BPM
- Enable `--verbose` to see lookup process

### MIDI Issues
- Ensure you have a MIDI player or DAW installed
- Files are standard MIDI format 1
- Import into any DAW as MIDI tracks

### Common Errors
```
BPM lookup failed and no fallback BPM provided
```
- Add `--fallback-bpm 120` or similar

```
network error querying BPMDatabase
```
- Check internet connection
- BPM Database website may be temporarily unavailable

## Examples by Genre

### Electronic/House
```bash
beatstoch generate-bpm 128 --style house --bars 32 --intensity 0.8
```

### Hip-Hop/Trap
```bash
beatstoch generate-bpm 140 --style breaks --bars 16 --swing 0.15 --intensity 0.6
```

### Drum & Bass
```bash
beatstoch generate-bpm 174 --style breaks --bars 64 --swing 0.08 --intensity 0.9
```

### General Purpose
```bash
beatstoch generate "Your Favorite Song" --artist "Artist Name" --bars 8
```

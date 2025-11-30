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
  --meter TEXT           Time signature e.g. '4/4', '3/4', '2/4' (default: 4/4)
  --humanize FLOAT       Humanization 0.0-1.0: adds ghost notes and timing variation (default: 0.0)
  --steps-per-beat INTEGER        Resolution (default: 4)
  --swing FLOAT          Swing amount 0.0-1.0 (default: 0.10)
  --intensity FLOAT      Pattern density 0.0-1.0 (default: 0.9)
  --groove-intensity FLOAT        Psychoacoustic groove strength 0.0-1.0 (default: 0.7)
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
  --meter TEXT           Time signature e.g. '4/4', '3/4', '2/4' (default: 4/4)
  --humanize FLOAT       Humanization 0.0-1.0: adds ghost notes and timing variation (default: 0.0)
  --steps-per-beat INTEGER        Resolution (default: 4)
  --swing FLOAT          Swing amount (default: 0.10)
  --intensity FLOAT      Pattern density (default: 0.9)
  --groove-intensity FLOAT        Psychoacoustic groove strength 0.0-1.0 (default: 0.7)
  --seed INTEGER         Random seed
  -h, --help            Show this message and exit
```

## Time Signatures (Meter)

The `--meter` option sets the time signature with natural accent patterns:

| Meter | Feel | Accent Pattern |
|-------|------|----------------|
| `4/4` | Standard | Strong - weak - medium - weak |
| `3/4` | Waltz | Strong - weak - weak |
| `2/4` | March | Strong - weak |

```bash
# Waltz in 3/4
beatstoch generate-bpm 90 --meter 3/4 --style generic

# March in 2/4
beatstoch generate-bpm 110 --meter 2/4 --humanize 0.5
```

## Humanize Mode

The `--humanize` option (0.0-1.0) makes patterns sound less mechanical:

**Ghost Notes**: Subtle snare hits (velocity 25-50) on weak subdivisions
**Timing Variation**: Random ±15ms offsets scaled by humanize amount

Recommended values:
- `0.0` - Machine-perfect timing (default)
- `0.2-0.4` - Subtle humanization, tight feel
- `0.5-0.7` - Natural human feel, noticeable ghost notes
- `0.8-1.0` - Loose, expressive feel with prominent ghost notes

```bash
# Subtle humanization
beatstoch generate-bpm 128 --humanize 0.3

# Natural feel
beatstoch generate-bpm 120 --humanize 0.6 --style house

# Full humanization
beatstoch generate-bpm 90 --meter 3/4 --humanize 1.0
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
    meter=(4, 4),               # Time signature
    steps_per_beat=4,           # 16th note resolution
    swing=0.12,                 # Light swing
    intensity=0.85,             # Dense pattern
    groove_intensity=0.8,       # Psychoacoustic groove
    humanize=0.5,               # Ghost notes and timing variation
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
    groove_intensity=0.7,       # Psychoacoustic groove
    humanize=0.6,               # Humanization
    seed=123,
    style="generic"             # All-purpose style
)

midi_file.save("complex_pattern.mid")

# Humanized 3/4 waltz
midi_file = generate_stochastic_pattern(
    bpm=90,
    bars=8,
    meter=(3, 4),               # Waltz time
    humanize=0.8,               # Heavy ghost notes
    style="generic"
)
midi_file.save("waltz_humanized.mid")
```

### Function Signatures

#### `generate_from_song()`
```python
generate_from_song(
    song_title: str,
    artist: Optional[str] = None,
    bars: int = 8,
    style: str = "house",
    meter: Tuple[int, int] = (4, 4),
    steps_per_beat: int = 4,
    swing: float = 0.10,
    intensity: float = 0.9,
    groove_intensity: float = 0.7,
    humanize: float = 0.0,
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
    groove_intensity: float = 0.7,
    humanize: float = 0.0,
) -> MidiFile
```

**Returns:** MIDI file object

## Drum Styles

### House Style
- Four-on-the-floor kick on every beat
- Snare/clap layered on beats 2 and 4
- Driving hi-hat patterns with open hat accents
- Crash cymbal on bar 1 every 4 bars
- Best for: House, techno, EDM, minimal

### Breaks Style
- Syncopated kick pattern (steps 0, 6, 8, 14)
- Snare on beats 2 and 4 with ghost notes
- Complex hi-hat patterns
- Best for: Breakbeat, drum & bass, hip-hop, jungle

### Rock Style
- Kick on beats 1 and 3 with pickup notes
- Strong snare backbeat on 2 and 4
- Driving 8th note hi-hats
- Open hat accents on upbeats
- Crash cymbal accents, ride bell on beat 1
- Best for: Rock, alternative, punk, metal

### Blues Style
- Shuffle feel (approximated triplet groove)
- Kick on beats with shuffle "and"
- Snare on 2 and 4 with ghost notes
- Ride cymbal shuffle pattern (not hi-hats)
- Pedal hi-hat on 2 and 4
- Best for: Blues, shuffle, 12-bar, slow rock

### Indie Style
- Kick on 1 and 3, occasional beat 4
- Snare on 2 and 4 with occasional rimshot
- Sparse, driving hi-hat pattern
- Floor tom accent on beat 4
- Minimal cymbal use
- Best for: Indie rock, alternative, lo-fi

### Jazz Style
- Classic jazz ride pattern (1, 2-and, 3, 4-and)
- Sparse, comping kick (fractal placement)
- Cross-stick/brush snare feel
- Hi-hat on 2 and 4 with foot
- No crashes - clean cymbal work
- Best for: Jazz, swing, bebop, fusion

### Generic Style
- Balanced kick on every beat
- Standard snare backbeat on 2 and 4
- Natural hi-hat variation
- Crash cymbal on bar 1 every 4 bars
- Best for: General use, experimentation, demos

## GM Drum Map Reference

beatstoch uses General MIDI (GM) standard drum note assignments. All generated MIDI files are compatible with any GM-compliant synthesizer, DAW, or drum machine.

### Kicks (Notes 35-36)
| Key | Note | GM Name |
|-----|------|---------|
| `kick` | 36 | Bass Drum 1 |
| `kick_acoustic` | 35 | Acoustic Bass Drum |

### Snares & Claps (Notes 37-40)
| Key | Note | GM Name |
|-----|------|---------|
| `snare` | 38 | Acoustic Snare |
| `snare_electric` | 40 | Electric Snare |
| `side_stick` | 37 | Side Stick / Rimshot |
| `clap` | 39 | Hand Clap |

### Hi-Hats (Notes 42, 44, 46)
| Key | Note | GM Name |
|-----|------|---------|
| `closed_hat` | 42 | Closed Hi-Hat |
| `pedal_hat` | 44 | Pedal Hi-Hat |
| `open_hat` | 46 | Open Hi-Hat |

### Cymbals (Notes 49-59)
| Key | Note | GM Name |
|-----|------|---------|
| `crash` | 49 | Crash Cymbal 1 |
| `crash2` | 57 | Crash Cymbal 2 |
| `ride` | 51 | Ride Cymbal 1 |
| `ride_bell` | 53 | Ride Bell |
| `ride2` | 59 | Ride Cymbal 2 |
| `splash` | 55 | Splash Cymbal |
| `china` | 52 | Chinese Cymbal |

### Toms (Notes 41-50)
| Key | Note | GM Name |
|-----|------|---------|
| `tom_low` | 41 | Low Floor Tom |
| `tom_floor_high` | 43 | High Floor Tom |
| `tom_mid` | 45 | Low Tom |
| `tom_mid_low` | 47 | Low-Mid Tom |
| `tom_mid_high` | 48 | Hi-Mid Tom |
| `tom_high` | 50 | High Tom |

### Percussion (Notes 54-77)
| Key | Note | GM Name |
|-----|------|---------|
| `tambourine` | 54 | Tambourine |
| `cowbell` | 56 | Cowbell |
| `bongo_high` | 60 | Hi Bongo |
| `bongo_low` | 61 | Low Bongo |
| `conga_mute` | 62 | Mute Hi Conga |
| `conga_high` | 63 | Open Hi Conga |
| `conga_low` | 64 | Low Conga |
| `claves` | 75 | Claves |
| `woodblock_high` | 76 | Hi Wood Block |
| `woodblock_low` | 77 | Low Wood Block |

## Output Files

Generated MIDI files use descriptive naming:
- `stoch_[artist]_[title]_[bpm]bpm_[meter].mid` (from song lookup)
- `stoch_[artist]_[title]_[bpm]bpm_[meter]_humanized.mid` (with humanize > 0)
- `stoch_[bpm]bpm_[meter].mid` (from explicit BPM)
- `stoch_[bpm]bpm_[meter]_humanized.mid` (with humanize > 0)

Example filenames:
```
stoch_michael_jackson_billie_jean_117bpm_44.mid
stoch_dave_brubeck_take_five_174bpm_34_humanized.mid
stoch_128bpm_44_humanized.mid
```

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

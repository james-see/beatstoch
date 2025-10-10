# beatstoch

**BPM-aware stochastic drum MIDI generator** - Create dynamic, probabilistic drum patterns that adapt to any song's BPM.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/beatstoch.svg)](https://badge.fury.io/py/beatstoch)
[![uv](https://img.shields.io/badge/built%20with-uv-purple.svg)](https://github.com/astral-sh/uv)

## Overview

beatstoch is a powerful tool for generating drum patterns that intelligently adapt to any song's BPM. Whether you're a music producer looking for inspiration or a developer wanting to integrate dynamic rhythm generation into your application, beatstoch provides both a command-line interface and Python library.

## Key Features

- **🎵 BPM Database Integration**: Automatically looks up song BPM from online databases
- **🎶 Multiple Styles**: House, breaks, and generic drum patterns
- **🔀 Stochastic Generation**: Creates varied, probabilistic drum patterns
- **🎹 MIDI Export**: Generates standard MIDI files compatible with all DAWs
- **⚡ CLI & Library**: Use as a command-line tool or Python library
- **🎛️ Customizable**: Adjust swing, intensity, bars, and more

## Quick Start

### Command Line

```bash
# Generate 8 bars of house drums for any song
beatstoch generate "Billie Jean" --artist "Michael Jackson"

# Generate breaks pattern at specific BPM
beatstoch generate-bpm 128 --bars 16 --style breaks

# See all options
beatstoch --help
```

### Python Library

```python
from beatstoch import generate_from_song, generate_stochastic_pattern

# Generate from song lookup
midi_file, bpm = generate_from_song(
    "1979",
    artist="Smashing Pumpkins",
    bars=8,
    style="house"
)

# Generate with explicit BPM
midi_file = generate_stochastic_pattern(
    bpm=127,
    bars=4,
    style="breaks",
    swing=0.1
)
```

## Installation

```bash
pip install beatstoch
```

## Documentation Contents

- **[User Guide](user-guide.md)** - Complete usage instructions and examples
- **[API Reference](api-reference.md)** - Python library documentation
- **[Developer Guide](developer-guide.md)** - Contributing and development workflows

## Examples

See the [User Guide](user-guide.md) for comprehensive examples and detailed usage instructions.

## License

[Add your license information here]

## Support

- 📖 [Documentation](https://james-see.github.io/beatstoch/)
- 🐛 [Issue Tracker](https://github.com/james-see/beatstoch/issues)
- 💬 [Discussions](https://github.com/james-see/beatstoch/discussions)

---

*Generated drum patterns are for educational and creative purposes. Always respect music copyrights and licensing.*

# 🥁 beatstoch

<div style="text-align: center; padding: 2rem 0;">
<h2 style="font-size: 2.5rem; font-weight: 300; margin-bottom: 0.5rem;">Stochastic Drum Pattern Generator</h2>
<p style="font-size: 1.3rem; color: #666; margin-bottom: 2rem;">Transform any song into unique, probabilistic MIDI drum patterns</p>

[![PyPI version](https://badge.fury.io/py/beatstoch.svg)](https://pypi.org/project/beatstoch/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-green.svg)](https://unlicense.org/)

</div>

---

## ⚡ Install in Seconds

=== "pip"
    ```bash
    pip install beatstoch
    ```

=== "pipx"
    ```bash
    pipx install beatstoch
    ```

=== "uv"
    ```bash
    uv tool install beatstoch
    ```

---

## 🎬 Quick Demo

```bash
# Generate drums that match any song's BPM
beatstoch generate "Billie Jean" --artist "Michael Jackson"

# Rock beat at 120 BPM
beatstoch generate-bpm 120 --style rock

# Shuffle blues with human feel
beatstoch generate-bpm 85 --style blues --humanize 0.6

# Jazz ride pattern
beatstoch generate-bpm 140 --style jazz
```

**Output:** Standard MIDI file ready for any DAW 🎹

---

## 🎨 7 Unique Styles

<div class="grid cards" markdown>

-   :material-record-circle:{ .lg .middle } **House**

    ---

    Four-on-the-floor, driving hi-hats, snare/clap layers

    *EDM · Techno · Minimal*

-   :material-pulse:{ .lg .middle } **Breaks**

    ---

    Syncopated kicks, complex hats, funky grooves

    *Breakbeat · DnB · Hip-hop*

-   :material-guitar-electric:{ .lg .middle } **Rock**

    ---

    Powerful backbeat, 8th note hats, crash accents

    *Rock · Alternative · Metal*

-   :material-saxophone:{ .lg .middle } **Blues**

    ---

    Shuffle feel, ride cymbal, ghost notes

    *Blues · 12-bar · Slow rock*

-   :material-radio:{ .lg .middle } **Indie**

    ---

    Loose feel, floor tom accents, rimshots

    *Indie rock · Lo-fi · Alternative*

-   :material-music-clef-treble:{ .lg .middle } **Jazz**

    ---

    Classic ride pattern, sparse comping, swing

    *Jazz · Bebop · Fusion*

-   :material-tune:{ .lg .middle } **Generic**

    ---

    Balanced patterns for any genre

    *Demos · Experimentation*

</div>

---

## 🧠 Powered by Mathematics

beatstoch doesn't just randomize—it uses **psychoacoustic algorithms** for patterns that sound natural:

| Algorithm | Purpose |
|-----------|---------|
| **Golden Ratio** | Natural spacing and timing |
| **Fibonacci Sequences** | Probability distribution |
| **Fractal Patterns** | Self-similar complexity |
| **Psychoacoustic Balancing** | Perceived naturalness |

---

## 🎛️ Full Control

```bash
beatstoch generate-bpm 128 \
    --style house \           # 7 styles available
    --bars 16 \               # Pattern length
    --meter 4/4 \             # Time signature (2/4, 3/4, 4/4)
    --humanize 0.6 \          # Ghost notes + timing variation
    --groove-intensity 0.8 \  # Swing and feel
    --predictability 0.7      # 1.0=mechanical, 0.0=chaotic
```

---

## 🐍 Python Library

```python
from beatstoch import generate_stochastic_pattern

# Generate a rock beat
midi = generate_stochastic_pattern(
    bpm=120,
    bars=8,
    style="rock",
    humanize=0.5,
    predictability=0.8
)
midi.save("my_beat.mid")
```

---

## 📚 Documentation

<div class="grid cards" markdown>

-   :material-book-open-variant:{ .lg .middle } **[User Guide](user-guide.md)**

    ---

    Complete CLI reference, all options, examples

-   :material-api:{ .lg .middle } **[API Reference](api-reference.md)**

    ---

    Python library documentation

-   :material-code-braces:{ .lg .middle } **[Developer Guide](developer-guide.md)**

    ---

    Contributing, architecture, testing

</div>

---

## 🎵 GM Drum Compatible

All patterns use **General MIDI** standard—works with any DAW, synth, or drum machine:

- 30+ drum/percussion sounds
- Kicks, snares, hi-hats, cymbals
- Toms, percussion, cowbell 🔔

---

<div style="text-align: center; padding: 2rem 0;">

**Ready to make some noise?**

[Get Started :material-arrow-right:](user-guide.md){ .md-button .md-button--primary }
[View on GitHub :material-github:](https://github.com/james-see/beatstoch){ .md-button }

</div>

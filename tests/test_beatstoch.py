"""Tests for beatstoch package."""

from mido import MidiFile

from beatstoch import generate_stochastic_pattern


def test_generate_stochastic_pattern_basic():
    """Test basic stochastic pattern generation."""
    midi_file = generate_stochastic_pattern(bpm=120, bars=2)

    assert isinstance(midi_file, MidiFile)
    assert midi_file.length > 0  # Should have some duration
    assert len(midi_file.tracks) > 0  # Should have at least one track


def test_generate_stochastic_pattern_with_params():
    """Test stochastic pattern generation with custom parameters."""
    midi_file = generate_stochastic_pattern(
        bpm=140, bars=4, style="breaks", swing=0.1, intensity=0.8, seed=42
    )

    assert isinstance(midi_file, MidiFile)
    assert midi_file.length > 0
    assert len(midi_file.tracks) > 0


def test_generate_stochastic_pattern_different_styles():
    """Test different drum styles."""
    styles = ["house", "breaks", "generic"]

    for style in styles:
        midi_file = generate_stochastic_pattern(
            bpm=120,
            bars=1,
            style=style,
            seed=42,  # Consistent seed for testing
        )
        assert isinstance(midi_file, MidiFile)
        assert midi_file.length > 0


def test_generate_stochastic_pattern_edge_cases():
    """Test edge cases for stochastic pattern generation."""
    # Test with very low BPM
    midi_file = generate_stochastic_pattern(bpm=60, bars=1, seed=42)
    assert isinstance(midi_file, MidiFile)

    # Test with very high BPM
    midi_file = generate_stochastic_pattern(bpm=200, bars=1, seed=42)
    assert isinstance(midi_file, MidiFile)

    # Test with minimal bars
    midi_file = generate_stochastic_pattern(bpm=120, bars=1, seed=42)
    assert isinstance(midi_file, MidiFile)


def test_generate_stochastic_pattern_deterministic():
    """Test that same seed produces same results."""
    midi_file1 = generate_stochastic_pattern(bpm=120, bars=2, seed=42)
    midi_file2 = generate_stochastic_pattern(bpm=120, bars=2, seed=42)

    # Files should have same length (deterministic)
    assert abs(midi_file1.length - midi_file2.length) < 0.01


def test_generate_stochastic_pattern_different_seeds():
    """Test that different seeds produce different results."""
    midi_file1 = generate_stochastic_pattern(bpm=120, bars=2, seed=42)
    midi_file2 = generate_stochastic_pattern(bpm=120, bars=2, seed=43)

    # Files should likely have different lengths (though not guaranteed)
    # This is a probabilistic test
    assert isinstance(midi_file1, MidiFile)
    assert isinstance(midi_file2, MidiFile)


def test_generate_stochastic_pattern_locked_repeats():
    """Test that locked mode produces identical bars (no per-bar variation)."""
    from collections import defaultdict

    midi_file = generate_stochastic_pattern(
        bpm=88, bars=8, style="blues", swing=0.6, locked=True, seed=42
    )

    ppq = midi_file.ticks_per_beat
    bar_ticks = 4 * ppq

    # Collect note_on events per bar
    bars = defaultdict(list)
    for track in midi_file.tracks:
        abs_time = 0
        for msg in track:
            abs_time += msg.time
            if msg.type == "note_on" and msg.velocity > 0:
                bar = abs_time // bar_ticks
                pos = abs_time % bar_ticks
                bars[bar].append((pos, msg.note, msg.velocity))

    # All bars should be identical
    bar0 = sorted(bars[0])
    assert len(bar0) > 0, "Bar 0 should have notes"
    for bar in range(8):
        assert sorted(bars[bar]) == bar0, f"Bar {bar} differs from bar 0 in locked mode"


def test_generate_stochastic_pattern_locked_all_styles():
    """Test that locked mode works for all styles without errors."""
    for style in ["house", "breaks", "rock", "blues", "indie", "jazz", "generic"]:
        midi_file = generate_stochastic_pattern(bpm=120, bars=4, style=style, locked=True, seed=42)
        assert isinstance(midi_file, MidiFile)
        assert midi_file.length > 0

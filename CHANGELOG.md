# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] - 2024-12-17

### Added
- **Psychoacoustic Algorithm**: Complete rewrite using research-based principles for human-pleasing rhythms
- **Golden Ratio Timing**: Microtiming based on golden ratio (1.618) for natural rhythm relationships
- **Fibonacci Patterns**: Rhythm probabilities generated using Fibonacci sequences for organic feel
- **Fractal Complexity**: Multi-level fractal pattern generation for natural rhythmic complexity
- **Natural Velocity Curves**: Sine wave-based velocity variation for expressive, human-like dynamics
- **Groove Intensity Control**: New `--groove-intensity` parameter to control psychoacoustic groove strength
- **Predictability Balance**: Algorithm balances 85% predictability with 15% surprise for optimal engagement

### Changed
- **Pattern Generation**: Completely rewritten algorithm using psychoacoustic research
- **Timing System**: Enhanced with golden ratio microtiming for authentic groove feel
- **Velocity System**: Replaced random triangular distribution with natural sine wave curves
- **CLI Interface**: Added `--groove-intensity` parameter to both generate commands

### Technical
- **Research-Backed**: Based on music psychology, neuroscience, and psychoacoustic studies
- **Golden Ratio**: Used for pleasing mathematical relationships in timing
- **Fibonacci**: Applied to probability distributions for natural rhythm patterns
- **Fractal Algorithms**: Multi-depth fractal generation for organic complexity
- **Human Groove Range**: Microtiming constrained to 20-30ms range for optimal groove perception

## [1.0.0] - 2024-10-10

### Added
- **BPM Database Integration**: Automatic song BPM lookup from bpmdatabase.com
- **Multiple Drum Styles**: House, breaks, and generic drum pattern generation
- **Command Line Interface**: Full CLI with comprehensive options
- **Python Library**: Complete API for integration into other applications
- **MIDI Export**: Standard MIDI file generation compatible with all DAWs
- **Comprehensive Documentation**: User guide, API reference, and developer documentation
- **GitHub Pages**: Automated documentation deployment
- **Automated Releases**: GitHub Actions for building and publishing releases
- **PyPI Integration**: Automated package publishing to PyPI
- **Test Suite**: Comprehensive tests covering core functionality

### Fixed
- **HTML Parsing**: Improved parsing of BPM database website structure
- **MIDI Generation**: Fixed tempo message format (MetaMessage vs Message)
- **Error Handling**: Better error messages and fallback options
- **Verbose Logging**: Added detailed BPM lookup logging
- **MkDocs Dependencies**: Fixed plugin naming and configuration
- **GitHub Actions**: Resolved permission and dependency issues

### Technical
- **Dependencies**: mido, numpy, requests, beautifulsoup4
- **Python Version**: 3.9+ support
- **Build System**: uv package manager
- **CI/CD**: GitHub Actions for testing, building, and deployment
- **Documentation**: MkDocs with Material theme and GitHub Pages

## Project Structure

This represents the stable 1.0.0 release of the beatstoch project with full functionality for BPM-aware stochastic drum pattern generation.

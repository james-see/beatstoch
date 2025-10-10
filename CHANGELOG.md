# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

### Fixed
- **HTML Parsing**: Improved parsing of BPM database website structure
- **MIDI Generation**: Fixed tempo message format (MetaMessage vs Message)
- **Error Handling**: Better error messages and fallback options
- **Verbose Logging**: Added detailed BPM lookup logging

### Technical
- **Dependencies**: mido, numpy, requests, beautifulsoup4
- **Python Version**: 3.9+ support
- **Build System**: uv package manager
- **CI/CD**: GitHub Actions for testing, building, and deployment

## Project Structure

This is the initial release of the beatstoch project, establishing the foundation for BPM-aware stochastic drum pattern generation.

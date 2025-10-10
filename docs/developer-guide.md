# Developer Guide

This guide covers development workflows, release processes, and project maintenance for the beatstoch project.

## Development Setup

### Prerequisites
- Python 3.9+
- [uv](https://github.com/astral-sh/uv) package manager (recommended)
- Git

### Initial Setup
```bash
git clone https://github.com/james-see/beatstoch.git
cd beatstoch
uv sync  # Install dependencies
```

### Development Workflow
```bash
# Make your changes
# ...

# Run tests
uv run python -m pytest

# Test CLI functionality
uv run beatstoch generate "1979" --artist "Smashing Pumpkins" --bars 2

# Build package locally
uv build
```

## Release Process

### Version Management
The project uses [semantic versioning](https://semver.org/) (MAJOR.MINOR.PATCH).

Update version in:
- `pyproject.toml` (project.version)
- `src/beatstoch/__init__.py` (if __version__ is defined)

### Pre-release Checklist
- [ ] Update version numbers
- [ ] Update CHANGELOG.md with new features/fixes
- [ ] Run tests: `uv run python -m pytest`
- [ ] Test CLI functionality
- [ ] Update documentation if needed
- [ ] Ensure all dependencies are properly pinned

### GitHub Release

#### Automated Release (Recommended)
The project includes GitHub Actions workflows that automatically create releases when tags are pushed.

**To create a release:**
```bash
# Ensure you're on the main branch and up to date
git checkout main
git pull origin main

# Create and push a version tag
VERSION="1.0.0"
git tag -a "v${VERSION}" -m "Release version ${VERSION}"
git push origin "v${VERSION}"
```

The GitHub Actions workflow will:
1. Build the package
2. Create a GitHub release
3. Upload distribution files as release assets

#### Manual Release
If automation fails, you can create releases manually:

1. Go to [GitHub Releases](https://github.com/yourusername/beatstoch/releases)
2. Click "Create a new release"
3. Select the version tag you created
4. Add release notes from CHANGELOG.md
5. Upload built distribution files from `dist/` directory

### PyPI Release

#### Automated PyPI Publishing
The GitHub Actions workflow can automatically publish to PyPI when a release is created.

**Prerequisites:**
- PyPI account with the package name `beatstoch`
- PyPI API token stored as `PYPI_API_TOKEN` secret in repository settings

**To enable automated PyPI publishing:**
1. Go to repository Settings > Secrets and variables > Actions
2. Add `PYPI_API_TOKEN` with your PyPI API token value
3. The workflow will automatically publish to PyPI on tagged releases

#### Manual PyPI Publishing
If you prefer to publish manually or automation isn't set up:

```bash
# Build distributions
uv build

# Upload to PyPI (requires API token)
uv publish

# Or using twine (if you have it installed)
twine upload dist/*
```

**To get a PyPI API token:**
1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Create a new API token with upload permissions
3. Add it as `PYPI_API_TOKEN` in GitHub repository secrets

### Post-release Checklist
- [ ] Verify package installs: `pip install beatstoch`
- [ ] Test CLI: `beatstoch --help`
- [ ] Verify GitHub release shows correct information
- [ ] Update any external references or documentation

## Project Structure

```
beatstoch/
├── src/beatstoch/          # Main package code
│   ├── __init__.py
│   ├── bpm.py             # BPM database integration
│   ├── generator.py       # MIDI generation logic
│   └── cli.py             # Command-line interface
├── docs/                  # Documentation (GitHub Pages)
├── tests/                 # Test files
├── .github/workflows/     # GitHub Actions workflows
├── pyproject.toml         # Project configuration
├── uv.lock               # Dependency lock file
├── README.md             # Main documentation
└── CHANGELOG.md          # Release notes
```

## Contributing

1. Fork the repository at [https://github.com/james-see/beatstoch](https://github.com/james-see/beatstoch)
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests if applicable
5. Run the test suite: `uv run python -m pytest`
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to the branch: `git push origin feature/amazing-feature`
8. Open a Pull Request

## Testing

```bash
# Run all tests
uv run python -m pytest

# Run with coverage
uv run python -m pytest --cov=src/beatstoch

# Run specific test file
uv run python -m pytest tests/test_specific.py
```

## Code Quality

- Follow PEP 8 style guidelines
- Add docstrings to public functions/classes
- Keep functions focused and reasonably sized
- Add type hints where appropriate

## Documentation

Documentation is built using [MkDocs](https://www.mkdocs.org/) and hosted on GitHub Pages.

**To update documentation:**
1. Edit files in the `docs/` directory
2. Preview locally: `mkdocs serve`
3. Changes are automatically deployed via GitHub Actions

## Troubleshooting

### Common Issues

**BPM Database Connection Issues:**
- Ensure internet connection is available
- Check if bpmdatabase.com is accessible
- The fallback search.asp endpoint may not exist

**MIDI Generation Issues:**
- Ensure mido library is properly installed
- Check that tempo messages are MetaMessage type (not Message)

**PyPI Upload Issues:**
- Verify PYPI_API_TOKEN is correctly set in GitHub secrets
- Ensure package name `beatstoch` is available or owned by you
- Check that all dependencies are properly specified

### Getting Help

- Check existing issues on [GitHub](https://github.com/james-see/beatstoch/issues)
- Create a new issue with detailed information
- Include error messages, Python version, and steps to reproduce

# Astronomy Code Study

Update 10/08/2025: move to uv and new libraries

See [the notes from Coursera Data Driven Astronomy](https://jbcodeforce.github.io/python-code/astronomy/)

## Program Descriptions and Usage

Below is a table describing each program in this repository and how to run them:

| Program | Description | How to Run | Dependencies |
|---------|-------------|------------|--------------|
| `CrossMatching/cross-matching.py` | Basic implementation of cross-matching astronomical catalogs using AT20G and SuperCOSMOS data. Calculates angular distances between celestial objects. | ```python CrossMatching/cross-matching.py``` | numpy |
| `CrossMatching/cross-matching-improved.py` | Improved version with better performance using numpy vectorization and sorting. Includes execution time measurement. | ```python CrossMatching/cross-matching-improved.py``` | numpy, time |
| `CrossMatching/cross-matching-astropy.py` | Efficient implementation using Astropy's SkyCoord for celestial coordinate handling. Best performance for large datasets. | ```python CrossMatching/cross-matching-astropy.py``` | numpy, astropy |
| `plot_mean_mediam.py` | Demonstrates statistical analysis by plotting mean and median values of a dataset with outliers using matplotlib. | ```python plot_mean_mediam.py``` | numpy, matplotlib |
| `Stacking/stacking.py` | Implements matrix stacking operations for image processing, useful for combining multiple astronomical images. | ```python Stacking/stacking.py``` | numpy |

## Data Files
- `data/AT20G/`: Contains the AT20G survey data
- `data/AT20G/bss.dat`: Bright source sample data
- `data/AT20G/super.csv`: SuperCOSMOS catalog data

## Running with Docker

If you need to run these programs with graphics support in a Docker container:

```shell
# In one terminal 
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
# In second terminal start X server
open -a Xquartz
# Get IP address 
ifconfig
# 10.0.0.183 for en0 interface
# build the docker image for the python env
docker build -t jbcodeforce/astronomy .
# run it with mounted folder to home
docker run -ti -e DISPLAY=10.0.0.183:0  -v $(pwd):/home jbcodeforce/astronomy bash
```

## Dependencies Installation

Install all required dependencies using:

```shell
python -m pip install -r requirements.txt
```

Or using uv (recommended):

```shell
uv pip install -r requirements.txt
```

Key dependencies:
- numpy
- matplotlib
- astropy

## Notes
- The cross-matching implementations show progressive improvements in performance
- Use the Astropy version for large datasets
- Make sure to have the data files in the correct relative paths before running the programs


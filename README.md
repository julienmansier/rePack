# rePack
This script downloads the extracted files of a given sample from Spectra Analyze

## Requirements
1) API Access to a Spectra Analyze (API TOken)
2) Python Requests needs to be installed: https://pypi.org/project/requests/

#### Running the script
```
python3 rePack.py --hash {sha1 hash} --url {Analyze base url} --token {API token}
```

###### Example
```
python3 rePack.py --hash 8d987fh98s0987fh87sfg87g --url a1000.example.com --token 98g987s987g987dfg987dfg00987s0dfg9876fdg97
```
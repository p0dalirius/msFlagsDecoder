# msFlagsDecoder

<p align="center">
  Decode the values of common Windows properties such as userAccountControl and sAMAccountType.
  <br>
  <img src="https://badges.pufler.dev/visits/p0dalirius/msFlagsDecoder/"/>
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/p0dalirius/msFlagsDecoder">
  <a href="https://twitter.com/intent/follow?screen_name=podalirius_" title="Follow"><img src="https://img.shields.io/twitter/follow/podalirius_?label=Podalirius&style=social"></a>
  <br>
</p>



![](./.github/uac.png)

## Usage

```
$ ./msFlagsDecoder.py -h
usage: msFlagsDecoder.py [-h] [-b] [-v] [--colors] attribute value

Description message

positional arguments:
  attribute      attribute
  value          value

optional arguments:
  -h, --help     show this help message and exit
  -b, --bits     Show bits masks.
  -v, --verbose  Verbose mode.
  --colors       Verbose mode.
```

## Contributing

Pull requests are welcome. Feel free to open an issue if you want to add other features.

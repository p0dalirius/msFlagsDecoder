# msFlagsDecoder

<p align="center">
  Decode the values of common Windows properties such as userAccountControl and sAMAccountType.
  <br>
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/p0dalirius/msFlagsDecoder">
  <a href="https://twitter.com/intent/follow?screen_name=podalirius_" title="Follow"><img src="https://img.shields.io/twitter/follow/podalirius_?label=Podalirius&style=social"></a>
  <a href="https://www.youtube.com/c/Podalirius_?sub_confirmation=1" title="Subscribe"><img alt="YouTube Channel Subscribers" src="https://img.shields.io/youtube/channel/subscribers/UCF_x5O7CSfr82AfNVTKOv_A?style=social"></a>
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

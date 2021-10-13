# msFlagsDecoder

Decode the values of common Windows properties such as `userAccountControl` and `sAMAccountType`.

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
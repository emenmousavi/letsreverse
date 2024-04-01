# IP Information Lookup

This Visual Basic .NET application performs reverse DNS lookup and retrieves detailed information about an IPv4 or IPv6 address, including ISP, country, region, and whether it's a private IP.

## Usage

1. Download or clone this repository.
2. Open the solution in Visual Studio.
3. Build and run the application.
4. Enter an IPv4 or IPv6 address when prompted.

## Dependencies

- [IPGeolocation](https://ipgeolocation.io/) - API used for fetching IP information.
- [Newtonsoft.Json](https://www.newtonsoft.com/json) - JSON framework for .NET.

## Configuration

- You need an API key from [IPGeolocation](https://ipgeolocation.io/) for fetching IP information. Replace `'YOUR_API_KEY'` in the code with your actual API key.

## Acknowledgements

- This application utilizes the IPGeolocation API for fetching IP information.
- The application uses the Newtonsoft.Json library for JSON parsing in .NET.

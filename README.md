# Product Scraper

This project scrapes product data from a specified website and stores it in a JSON file. The scraped data can be accessed via a simple API.

## Prerequisites

- Python 3.x
- Redis (if using caching)
- An active internet connection

## Installation

1. Clone the repository:

   git clone <repository-url>
   cd <repository-directory>

2. Run the installation script:

   ./install.sh

   This script will create a `.env` file, install the necessary dependencies, and run the server.

## Running the API

1. Start the API server:

   uvicorn main:app --reload

   Make sure to replace main:app with the appropriate module and app name if different.

## Scraping Products

To scrape products, execute the following curl command:

curl -X GET "http://127.0.0.1:8000/api/scrape?page_limit=5" -H "accept: application/json" -H "Authorization: Bearer y27vLBACEbsZIckn-8HPcIUwVyjDnqqAkJlYy_oZI3M"

### Notes

- The scraped data is stored in scraped_data.json. If this file already contains data, the new scrape will update or append as necessary.
- Ensure the API is running before executing the curl command.

## Troubleshooting

If you encounter any issues:

- Check the server logs for error messages.
- Ensure that all dependencies are installed correctly.
- Verify that Redis is running if it's part of your caching strategy.

## License

This project is licensed under the MIT License.

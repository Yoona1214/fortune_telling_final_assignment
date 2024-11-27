# Bazi Analysis

## Tech Stack

- Frontend: SvelteKit
- Backend: FastAPI

## Project Structure

```
fortune-telling-fe/ Frontend project
fortune-telling-svr/ Backend project
```

## Implementation

For each Bazi analysis, the frontend sends a request to the backend, calling the Bazi analysis API, and then returns the result to the frontend.

The Bazi analysis API internally uses `requests` and `BeautifulSoup` to scrape existing Bazi content websites, parse the required content, and then return it to the frontend.

## Running

Besides running locally, you can directly access the deployed version: https://fortune.duyu.art/

1. Compile Frontend Artifacts

The frontend project is developed using SvelteKit. To compile the frontend artifacts, you first need to install the Node environment and project dependencies. You can use nvm or Volta, or directly download and install Node from the Node.js official website.

This project uses pnpm to manage frontend dependencies, so you need to install pnpm globally:

```bash
npm install -g pnpm
```

Then you can enter the frontend project directory, install dependencies, and execute the build with the following commands:

```bash
cd fortune-telling-fe
pnpm i
pnpm build
```

After compilation, the artifacts will be generated in the `fortune-telling-fe/build` directory.

2. Run Backend Service

The backend service is developed using FastAPI. To run the backend service, you first need to install the Python environment. You can use pyenv to install Python, or directly download and install it from the Python official website.

Then enter the backend project directory, install dependencies, and run:

```bash
cd fortune-telling-svr
pip install -r requirements.txt
uvicorn main:app --reload
```

3. Access the URL provided by the Backend Service

After the backend service is running, visit `http://127.0.0.1:8000` to browse the Bazi analysis page.

Please ensure that the `fortune-telling-fe` and `fortune-telling-svr` directories are in the same directory to ensure that the backend service can access the frontend artifacts properly.

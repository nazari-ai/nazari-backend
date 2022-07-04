# Asalytics-backend

Asalytics Public Link [asalytics.ai](https://asalytics.ai)

## Table of Content:
-   [Technologies](#technologies)
-   [Setup](#setup)
-   [Screenshots](#screenshots)
-   [Status](#status)
-   [Credits](#credits)

## Technologies

The backend architecture uses `FastAPI` for building the API Web Framework written in `Python`, `GraphQL` as a query language for the API
with an Object Relational Mapper `Tortoise ORM`.

Other secondary technologies used on this project includes:

-   `Database: PostgreSQL`
-   `GraphQL Library: Strawberry`

## Setup

### Download or clone the repository

### Install dependencies
```bash
pip install fastapi
```
```bash
pip install tortoise-orm
```
```bash
pip install 'strawberry-graphql[debug-server]'
```
```bash
pip install uvicorn[standard]
```
```bash
pip install asyncpg
```

### After, run the development server:

```bash
uvicorn --reload main:app
```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

## Screenshots
![image](https://user-images.githubusercontent.com/45284829/177061780-4921c3e1-6ee5-4908-b14b-439f6fd52653.png)

![image](https://user-images.githubusercontent.com/45284829/177061821-32efe656-2271-4b3a-a046-da4df6362b76.png)


## Status

**Asalytics** development is still in progress. `Version 1` will be out soon.

## Credits

List of contriubutors:

-   [Busayo Awobade](https://www.linkedin.com/in/busayo-awobade-107a94175/)
-   [Steven Kolawole](https://www.linkedin.com/in/steven-kolawole-80/)
-   [Ernest Owojori](https://www.linkedin.com/in/owojori-ernest-tolulope-734bb1170/)
-   [Precious Kolawole](https://www.precillieo.com/)

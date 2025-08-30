# 📈 Compound Interest Calculator (Python Training Project)

A Python-based **Compound Interest Calculator** built with **FastAPI** and modern development tooling.  
This project is designed for training purposes and demonstrates best practices in Python development with **Docker**, **FastAPI**, **Pydantic**, **PyTest**, and static analysis tools.  

---

## 🚀 Features

- **REST API** using FastAPI
- **Compound Interest Calculator**:
  - Future Value (FV) given principal, rate, compounding periods, and time
  - Required Interest Rate (R) given FV, principal, compounding periods, and time
- **Validated Inputs** with Pydantic
- **Tests** using PyTest
- **Static Analysis & Formatting**:
  - [Ruff](https://github.com/astral-sh/ruff) for linting
  - [Black](https://black.readthedocs.io/) for code formatting
  - [mypy](http://mypy-lang.org/) for static type checking
- **Containerized** with Docker
- **Built with [UV](https://github.com/astral-sh/uv)** as Python package manager / builder
- **Future CI/CD Integration** with Bazel

---

## 📚 Compound Interest Formulas

### 1. **Future Value (FV)**  

`FV = P * (1 + R/N) ** (N * T)`

- `P`: Principal amount  
- `R`: Annual interest rate (decimal, e.g., 0.0412 for 4.12%)  
- `N`: Compounding periods per year  
- `T`: Total time in years  

**Example Test Case**  

- Input: `P=10000, R=0.0412, N=4, T=10`  

- Output: `FV ≈ 15000`  

### 2. **Required Interest Rate (R)**  

Rearranging the formula:  
`FV = P * (1 + R/N) ** (N * T)`
Solve for `R`.  

**Example Test Case**  

- Input: `FV=15000, P=10000, N=4, T=10`  
- Output: `R ≈ 0.0412 (≈ 4.12%)`

---

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **Framework:** FastAPI
- **Validation:** Pydantic
- **Testing:** PyTest
- **Tooling:** Ruff, Black, mypy
- **Containerization:** Docker
- **Builder:** UV
- **Future CI/CD:** Bazel

---

## ▶️ Running the Project

### 1. Clone Repo

```bash
git clone https://github.com/cmariscalaws/cli-calculator.git
cd cli-calculator
```

### 2. Install Dependencies (with UV)

```bash
uv sync
```

### 3. Run Locally

#### Development (default)

```bash
uv run uvicorn app.main.app --reload
```

#### Production

```bash
ENVIRONMENT=production uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

#### Production with Custom Log Level

```bash
ENVIRONMENT=production LOG_LEVEL=WARNING uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

FastAPI will be available at: <http://localhost:8000>

### 4. Run with Docker

```bash
docker build -t compound-interest .
docker run -p 8000:8000 compound-interest
```

### 5. Run with Docker-Compose (Dev)

```bash
docker-compose up app-dev
```

### 6. Run with Docker-Compose (Prod)

```bash
docker-compose up app-prod
```

## 🔍 API Endpoints

### 1. Calculate Future Value

POST /future-value

Request Body:

```json
{
  "P": 10000,
  "R": 0.0412,
  "N": 4,
  "T": 10
}
```

Response:

```json
{
  "message": "Future Value of 15000.0 when starting with 10000 compounded at 0.0412 interest rate, 4 times per year over 10 years"
}
```

### 2. Calculate Required Interest Rate

POST /required-rate

Request Body:

```json
{
  "FV": 15000,
  "P": 10000,
  "N": 4,
  "T": 10
}
```

Response:

```json
{
  "message": "4.12% is the required interest rate to grow $10000 to $15000 if compounding 4 times per year over 10 years."
}
```

## 🧪 Running Tests

```bash
pytest
```

## ✅ Code Quality

- Format code:

```bash
black .
```

- Lint with Ruff:

```bash
ruff check .
```

- Type check:

```bash
mypy app/
```

## 📜 License

MIT License.

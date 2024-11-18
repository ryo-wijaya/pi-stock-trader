## PI Stock Trader

Backend microservice to handle personal stock trading data display and stop-loss algorithms for the https://github.com/ryo-wijaya/my-pi-board Raspberry Pi dashboard.

### Command Bank

- Run Local Application

```bash
    uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

- Build Container

```bash
    docker build -t pi-stock-trader:latest .
```

- Run Container

```bash
    docker run -d --name pi-stock-trader-container -p 8001:8001 pi-stock-trader:latest
```

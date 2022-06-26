# CSC3004-SafeEntry-gRPC
CSC3004 Lab Assessment to create SafeEntry system with gRPC protocol

## How to run the program

### Building the Docker image

```
docker compose build
```

### Run the Docker image

```
docker compose up
```

### Stop the Docker image

```
docker compose down
```

**Once the container is running, run the client script to use the function**

```
python safeentry_client.py
```
### Functions the clients are able to use
* Enter your NRIC and Name to begin the program
* 1) Check-in to location
* 2) Check-out of location
* 3) Group Check-in
* 4) Group Check-out
* 5) Get visit history

### Functions the admin are able to use
* Enter 'admin' as the NRIC
* 1) Add infected location
* 1) Check-in to location
* 2) Check-out of location
* 3) Group Check-in
* 4) Group Check-out
* 6) Get visit history

### Automated test (Windows)

```
Just run the run_test.bat file
```

### Automated Test (MAC)

```
bash run_test.sh
```

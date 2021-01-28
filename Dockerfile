# Base image and main dependencies
FROM python:3.8 AS service_deps
WORKDIR /code
COPY requirements.txt .

# Test image and additional dependencies
FROM service_deps AS test_deps
RUN pip install -r requirements.txt

# Copy source files
FROM test_deps AS builder
COPY src/ ./src

# Build tests
FROM test_deps AS test_builder
COPY src/ ./src
COPY test/ ./test

# Local development
# FROM test_builder AS local_dev
# ENTRYPOINT [ "pytest" ]
# CMD [ "tests" ]

# Execute the tests
# FROM test_builder AS tests
# RUN pytest tests

# Execute the final service
# Use `docker run atmos` to execute ATMOS
FROM builder AS atmos
COPY docker-entry.sh ./
ENTRYPOINT [ "bash", "docker-entry.sh" ]
EXPOSE 3000
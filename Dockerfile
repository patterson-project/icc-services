FROM debian AS lib_builder

# Step 1: Building WS281x 
WORKDIR /app

RUN apt-get update -y && apt-get install -y \
  build-essential \
  cmake \
  git

RUN git clone https://github.com/jgarff/rpi_ws281x.git \
  && cd rpi_ws281x \ 
  && mkdir build \
  && cd build \ 
  && cmake -D BUILD_SHARED=OFF -D BUILD_TEST=OFF .. \
  && cmake --build . \
  && make install

#Step 2: Building GIN API
FROM golang:latest
COPY --from=lib_builder /usr/local/lib/libws2811.a /usr/local/lib/
COPY --from=lib_builder /usr/local/include/ws2811 /usr/local/include/ws2811

RUN go get github.com/rpi-ws281x/rpi-ws281x-go

WORKDIR /src

COPY /src/go.mod ./
COPY /src/go.sum ./

RUN go mod download

COPY /src/main.go ./
RUN go build /src/main.go

ENTRYPOINT [ "./main" ]
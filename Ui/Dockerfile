FROM node:latest

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY /control-center/package.json ./
COPY /control-center/package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

COPY /control-center/* /app/

# start app
CMD ["npm", "start"]
